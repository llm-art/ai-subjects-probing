#!/usr/bin/env python3
"""Run the locked probe battery (probes/probes.json) against vision-language models.

Methodology constraints enforced here (do not weaken):
  - Each probe variant runs in a SEPARATE stateless session per image per model.
  - Probe C checklist questions are asked individually and sequentially as turns
    of one session, never as a single list.
  - Probe A is recorded verbatim and never scored.
  - B_enriched runs only if B_plain has already completed for that image+model,
    and only when every subject description for the image's category is written
    (no "TODO" entries).
  - Every session carries probes.json's global_system_instruction as the system
    message (forbids web search / external tools).
  - All prompts are read from probes/probes.json (the locked battery), never
    hardcoded here.

Execution model: a thread pool (--workers, default 4) over work units of
(model, image); each worker runs all selected probes for its unit in canonical
order. Calls to the same provider are spaced by --delay across all threads.

Providers:
  gemini   - Google Generative Language API. Env: GEMINI_API_KEY.
  harvard  - Harvard HUIT "AIS OpenAI Direct" gateway (OpenAI chat-completions
             format, Azure-style `api-key` header). Env: HARVARD_API_KEY,
             optionally HARVARD_API_BASE (default
             https://go.apis.huit.harvard.edu/ais-openai-direct/v1).

Keys are read from a `.env` file in the project root (see .env.example) or
from the environment; real environment variables take precedence.

Usage:
  .venv/bin/python run_probes.py \
      --models gemini:gemini-2.5-pro harvard:gpt-4o \
      --probes A B_plain B_framed B_forced C \
      [--images aeneas-anchises-troy ...] [--workers 4] [--dry-run] [--force]
  .venv/bin/python run_probes.py --reports-only   # rebuild reports, no API calls

Outputs:
  results/raw/<model_slug>/<image_id>/<probe>.json  - raw sessions (gitignored)
  results/reports/<image_id>.md                     - per-image report (tracked),
      regenerated from the raw JSONs each time a unit for that image finishes.
Existing raw files are skipped (resume by default); --force re-runs.
"""

import argparse
import base64
import csv
import hashlib
import io
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv
from PIL import Image

load_dotenv()  # reads .env in the project root; real env vars take precedence

ROOT = Path(__file__).resolve().parent
PROBES_PATH = ROOT / "probes" / "probes.json"
MANIFEST_PATH = ROOT / "data" / "images.tsv"
IMAGES_DIR = ROOT / "data" / "images"
RESULTS_DIR = ROOT / "results" / "raw"
REPORTS_DIR = ROOT / "results" / "reports"

# Canonical execution order: A and the B family before C, B_enriched after B_plain.
PROBE_ORDER = ["A", "B_plain", "B_framed", "B_forced", "B_enriched", "C"]

PROBE_TITLES = {
    "A": "Probe A — Recognition (logged covariate — record only, do not score)",
    "B_plain": "Probe B-plain — Open identification, no context",
    "B_framed": "Probe B-framed — Open identification, cultural framing",
    "B_forced": "Probe B-forced-choice — Closed identification",
    "B_enriched": "Probe B-enriched — Intervention test (after B-plain)",
    "C": "Probe C — Closed verification checklist (expert-scored, semantic match)",
}

GEN_PARAMS = {"temperature": 0.0, "max_tokens": 2048}

RETRY_STATUSES = {429, 500, 502, 503, 504, 529}
MAX_RETRIES = 5

PRINT_LOCK = threading.Lock()
REPORT_LOCK = threading.Lock()


def say(msg, err=False):
    with PRINT_LOCK:
        print(msg, file=sys.stderr if err else sys.stdout, flush=True)


def utcnow():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_probes():
    with open(PROBES_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_manifest():
    with open(MANIFEST_PATH, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def prepare_image(path, max_edge=2048, quality=90):
    """Downscale to fit the vision-model input budget; return JPEG bytes + provenance."""
    img = Image.open(path)
    img.load()
    native = img.size
    if img.mode != "RGB":
        img = img.convert("RGB")
    if max(native) > max_edge:
        scale = max_edge / max(native)
        img = img.resize(
            (round(native[0] * scale), round(native[1] * scale)), Image.LANCZOS
        )
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=quality)
    data = buf.getvalue()
    meta = {
        "file": str(path.relative_to(ROOT)),
        "sha256_original_file": hashlib.sha256(path.read_bytes()).hexdigest(),
        "native_size": list(native),
        "sent_size": list(img.size),
        "sent_bytes": len(data),
        "jpeg_quality": quality,
    }
    return data, meta


def post_with_retry(url, headers, payload):
    last = None
    for attempt in range(MAX_RETRIES):
        resp = requests.post(url, headers=headers, json=payload, timeout=300)
        if resp.status_code == 200:
            return resp
        last = resp
        if resp.status_code in RETRY_STATUSES:
            wait = min(2 ** attempt * 5, 120)
            say(f"    HTTP {resp.status_code}, retrying in {wait}s "
                f"({attempt + 1}/{MAX_RETRIES})", err=True)
            time.sleep(wait)
            continue
        break
    raise RuntimeError(f"API error {last.status_code}: {last.text[:500]}")


class RateLimiter:
    """Space calls to one provider by `delay` seconds across all threads."""

    def __init__(self, delay):
        self.delay = delay
        self.lock = threading.Lock()
        self.next_at = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            slot = max(now, self.next_at)
            self.next_at = slot + self.delay
        pause = slot - now
        if pause > 0:
            time.sleep(pause)


class GeminiProvider:
    name = "gemini"

    def __init__(self, model, system_instruction, limiter):
        self.model = model
        self.system_instruction = system_instruction
        self.limiter = limiter
        self.key = os.environ.get("GEMINI_API_KEY")
        if not self.key:
            raise SystemExit("GEMINI_API_KEY is not set (env or .env)")
        self.url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent"
        )

    def chat(self, turns, image_b64):
        """turns: [{'role': 'user'|'assistant', 'text': ...}]. Image attaches to the
        first user turn. Stateless: full history is resent each call."""
        contents = []
        image_attached = False
        for t in turns:
            role = "user" if t["role"] == "user" else "model"
            parts = []
            if role == "user" and not image_attached:
                parts.append({"inline_data": {"mime_type": "image/jpeg",
                                              "data": image_b64}})
                image_attached = True
            parts.append({"text": t["text"]})
            contents.append({"role": role, "parts": parts})
        payload = {
            "systemInstruction": {"parts": [{"text": self.system_instruction}]},
            "contents": contents,
            "generationConfig": {
                "temperature": GEN_PARAMS["temperature"],
                "maxOutputTokens": GEN_PARAMS["max_tokens"],
            },
        }
        self.limiter.wait()
        resp = post_with_retry(
            self.url,
            {"x-goog-api-key": self.key, "Content-Type": "application/json"},
            payload,
        )
        data = resp.json()
        try:
            parts = data["candidates"][0]["content"]["parts"]
            text = "".join(p.get("text", "") for p in parts).strip()
        except (KeyError, IndexError) as e:
            raise RuntimeError(
                f"Unexpected Gemini response shape: {json.dumps(data)[:500]}") from e
        return text


class HarvardOpenAIProvider:
    name = "harvard"

    def __init__(self, model, system_instruction, limiter):
        self.model = model
        self.system_instruction = system_instruction
        self.limiter = limiter
        self.key = os.environ.get("HARVARD_API_KEY")
        if not self.key:
            raise SystemExit("HARVARD_API_KEY is not set (env or .env)")
        base = os.environ.get(
            "HARVARD_API_BASE",
            "https://go.apis.huit.harvard.edu/ais-openai-direct/v1",
        ).rstrip("/")
        self.url = f"{base}/chat/completions"

    def chat(self, turns, image_b64):
        messages = [{"role": "system", "content": self.system_instruction}]
        image_attached = False
        for t in turns:
            if t["role"] == "user" and not image_attached:
                messages.append({
                    "role": "user",
                    "content": [
                        {"type": "text", "text": t["text"]},
                        {"type": "image_url", "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}"}},
                    ],
                })
                image_attached = True
            else:
                messages.append({"role": t["role"], "content": t["text"]})
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": GEN_PARAMS["temperature"],
            "max_tokens": GEN_PARAMS["max_tokens"],
        }
        self.limiter.wait()
        resp = post_with_retry(
            self.url,
            {"api-key": self.key, "Content-Type": "application/json"},
            payload,
        )
        data = resp.json()
        try:
            return data["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, AttributeError) as e:
            raise RuntimeError(
                f"Unexpected response shape: {json.dumps(data)[:500]}") from e


PROVIDERS = {"gemini": GeminiProvider, "harvard": HarvardOpenAIProvider}


def make_provider(spec, system_instruction, limiters):
    if ":" not in spec:
        raise SystemExit(
            f"Model spec '{spec}' must be provider:model, e.g. gemini:gemini-2.5-pro")
    provider, model = spec.split(":", 1)
    if provider not in PROVIDERS:
        raise SystemExit(f"Unknown provider '{provider}' (known: {list(PROVIDERS)})")
    return PROVIDERS[provider](model, system_instruction, limiters[provider])


def model_slug(spec):
    return spec.replace(":", "_").replace("/", "_")


def result_path(spec, image_id, probe):
    return RESULTS_DIR / model_slug(spec) / image_id / f"{probe}.json"


def base_record(probes, row, spec, probe, image_meta):
    return {
        "probe": probe,
        "probe_battery_version": probes.get("version"),
        "model": spec,
        "image_id": row["id"],
        "category": row["category"],
        "subject_ground_truth": row["subject"],
        "tier": row.get("tier", ""),
        "timestamp_utc": utcnow(),
        "params": dict(GEN_PARAMS),
        "system_instruction": probes["global_system_instruction"],
        "image": image_meta,
    }


def build_enriched_prompt(probes, category):
    """Compose B_enriched from the locked template + per-category descriptions.
    Raises if any description for this category is still TODO."""
    spec = probes["probes"]["B_enriched"]
    subjects = probes["subjects"][category]
    missing = [s for s in subjects
               if spec["subject_descriptions"].get(s, "TODO") == "TODO"]
    if missing:
        raise RuntimeError(
            f"B_enriched blocked: {len(missing)} subject description(s) for "
            f"'{category}' are still TODO in probes.json (expert-lock them first): "
            + "; ".join(missing[:3]) + ("..." if len(missing) > 3 else ""))
    lines = [f"{s}: {spec['subject_descriptions'][s]}" for s in subjects]
    return spec["prompt_template"].replace(
        "{subject_descriptions}", "\n".join(lines))


def run_probe(probes, provider, spec, row, probe, image_b64, image_meta):
    """Run one probe session; return the result record."""
    rec = base_record(probes, row, spec, probe, image_meta)

    if probe == "C":
        checklist = probes["probe_C_checklists"].get(row["id"])
        if not checklist:
            return None  # no expert-locked checklist for this image yet
        turns = []
        answers = []
        for item in checklist:
            turns.append({"role": "user", "text": item["question"]})
            answer = provider.chat(turns, image_b64)
            turns.append({"role": "assistant", "text": answer})
            answers.append({
                "element": item["element"],
                "question": item["question"],
                "model_answer": answer,
                "reference_correct": item["correct"],
                "expert_score": None,
            })
        rec["checklist"] = answers
        rec["transcript"] = turns
        rec["scoring"] = {
            "status": "awaiting_expert",
            "note": "Expert-scored with semantic matching, not exact-match. "
                    "Fill expert_score per element (0/1).",
        }
        return rec

    # single-turn probes
    if probe == "A":
        prompt = probes["probes"]["A_recognition"]["prompt"]
        rec["scoring"] = {
            "status": "logged_covariate_only",
            "note": "Record verbatim, never score. Flag potential contamination "
                    "when interpreting B results.",
        }
    elif probe == "B_plain":
        prompt = probes["probes"]["B_plain"]["prompt"]
    elif probe == "B_framed":
        prompt = probes["probes"]["B_framed"]["prompt"]
    elif probe == "B_forced":
        prompt = probes["probes"][f"B_forced_choice_{row['category']}"]["prompt"]
    elif probe == "B_enriched":
        prompt = build_enriched_prompt(probes, row["category"])
    else:
        raise ValueError(probe)

    answer = provider.chat([{"role": "user", "text": prompt}], image_b64)
    rec["transcript"] = [
        {"role": "user", "text": prompt},
        {"role": "assistant", "text": answer},
    ]
    rec.setdefault("scoring", {"status": "unscored"})
    return rec


# ---------------------------------------------------------------- reports

_DOWNLOAD_LOG = None


def iiif_base(image_id, row):
    """IIIF Image API service base for an image. Prefer the canonical resolved
    URL from download_log.json (handles e.g. RKD's /iiif/ -> /iiif/2/ redirect);
    fall back to the TSV iiif_url minus /info.json."""
    global _DOWNLOAD_LOG
    if _DOWNLOAD_LOG is None:
        log_path = ROOT / "data" / "download_log.json"
        try:
            with open(log_path, encoding="utf-8") as f:
                _DOWNLOAD_LOG = json.load(f)
        except (OSError, json.JSONDecodeError):
            _DOWNLOAD_LOG = {}
    entry = _DOWNLOAD_LOG.get(image_id, {})
    for d in entry.get("downloads", []):
        url = d.get("resolved_url", "")
        m = re.match(r"(.+?)/[^/]+/[^/]+/\d+/default\.\w+$", url)
        if m:
            return m.group(1)
    url = (row.get("iiif_url") or "").strip()
    if url and url != "MANUAL_REQUIRED":
        return re.sub(r"/info\.json$", "", url)
    return None


def block(text):
    """Render verbatim text as a markdown blockquote (keeps reports readable
    even when responses contain markdown of their own)."""
    return "\n".join("> " + line for line in (text or "").splitlines()) or ">"


def write_report(image_id, manifest_by_id):
    """Regenerate results/reports/<image_id>.md from all raw JSONs on disk."""
    records = []
    if RESULTS_DIR.exists():
        for model_dir in sorted(RESULTS_DIR.iterdir()):
            img_dir = model_dir / image_id
            if not img_dir.is_dir():
                continue
            for probe in PROBE_ORDER:
                p = img_dir / f"{probe}.json"
                if p.exists():
                    with open(p, encoding="utf-8") as f:
                        records.append(json.load(f))
    if not records:
        return

    row = manifest_by_id[image_id]
    first = records[0]
    lines = [
        f"# Probe report — `{image_id}`",
        "",
    ]
    base = iiif_base(image_id, row)
    if base:
        lines += [
            f"[![{image_id}]({base}/full/!800,800/0/default.jpg)]"
            f"({base}/full/max/0/default.jpg)",
            "",
            f"_Image served from IIIF (click for full resolution) — "
            f"[info.json]({base}/info.json)_",
            "",
        ]
    lines += [
        f"- **Ground-truth subject:** {row['subject']}",
        f"- **Category:** {row['category']}" + (f" · **Tier:** {row['tier']}" if row.get("tier") else ""),
        f"- **Institution:** {row.get('institution', '')}",
        f"- **Image:** `{first['image']['file']}` — native "
        f"{first['image']['native_size'][0]}×{first['image']['native_size'][1]} px, "
        f"sent {first['image']['sent_size'][0]}×{first['image']['sent_size'][1]} px",
        f"- **SHA-256:** `{first['image']['sha256_original_file']}`",
        f"- **Probe battery version:** {first.get('probe_battery_version', '?')}",
        f"- **System instruction (all sessions):** {first.get('system_instruction', '—')}",
        "",
        "_Each probe ran in a separate stateless session. Probe A is a logged "
        "covariate — record only, never score. Probe C is expert-scored with "
        "semantic matching (e.g. \"a burning building\", \"fire and smoke\" and "
        "\"Troy in flames\" all match a burning-city reference)._",
        "",
    ]

    by_model = {}
    for rec in records:
        by_model.setdefault(rec["model"], []).append(rec)

    for model in sorted(by_model):
        lines += [f"## Model: `{model}`", ""]
        recs = {r["probe"]: r for r in by_model[model]}
        for probe in PROBE_ORDER:
            rec = recs.get(probe)
            if not rec:
                continue
            lines += [f"### {PROBE_TITLES[probe]}",
                      "", f"_Run: {rec['timestamp_utc']}_", ""]
            if probe == "C":
                for i, el in enumerate(rec["checklist"], 1):
                    lines += [
                        f"**Element {i}: {el['element']}**",
                        "",
                        f"Q: {el['question']}",
                        "",
                        block(el["model_answer"]),
                        "",
                        f"_Reference:_ {el['reference_correct']}",
                        "",
                        "- [ ] Expert score (1 = correctly identified, semantic match)",
                        "",
                    ]
            else:
                prompt = rec["transcript"][0]["text"]
                answer = rec["transcript"][1]["text"]
                lines += ["**Prompt:**", "", block(prompt), "",
                          "**Response (verbatim):**", "", block(answer), ""]
    lines.append("")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with REPORT_LOCK:
        with open(REPORTS_DIR / f"{image_id}.md", "w", encoding="utf-8") as f:
            f.write("\n".join(lines))


# ---------------------------------------------------------------- execution

def plan_unit(probes, spec, row, probe_list, force):
    """Return the probes that would actually run for one (model, image) unit.
    Skips are explained on stdout. B_enriched ordering is resolved within the
    unit: it runs if B_plain exists on disk OR runs earlier in this unit."""
    todo = []
    will_have_b_plain = result_path(spec, row["id"], "B_plain").exists()
    for probe in probe_list:
        out = result_path(spec, row["id"], probe)
        if out.exists() and not force:
            continue
        if probe == "C" and row["id"] not in probes["probe_C_checklists"]:
            continue
        if probe == "B_enriched":
            if not will_have_b_plain:
                say(f"[skip] {spec} / {row['id']} / B_enriched: "
                    f"B_plain has not run yet (locked ordering)")
                continue
            try:
                build_enriched_prompt(probes, row["category"])
            except RuntimeError as e:
                say(f"[skip] {spec} / {row['id']} / B_enriched: {e}")
                continue
        if probe == "B_plain":
            will_have_b_plain = True
        todo.append(probe)
    return todo


def run_unit(probes, provider, spec, row, todo, max_edge, manifest_by_id):
    """Worker: run all planned probes for one (model, image) unit, then refresh
    the image's report. Returns a list of (probe, error) failures."""
    failures = []
    img_path = IMAGES_DIR / f"{row['id']}.jpg"
    img_bytes, image_meta = prepare_image(img_path, max_edge)
    image_b64 = base64.b64encode(img_bytes).decode("ascii")
    for probe in todo:
        say(f"[run]  {spec} / {row['id']} / {probe}")
        try:
            rec = run_probe(probes, provider, spec, row, probe,
                            image_b64, image_meta)
        except Exception as e:
            say(f"[FAIL] {spec} / {row['id']} / {probe}: {e}", err=True)
            failures.append((probe, str(e)))
            if probe == "B_plain":
                # locked ordering: without B_plain, B_enriched must not run
                todo = [p for p in todo if p != "B_enriched"]
            continue
        if rec is None:
            continue
        out = result_path(spec, row["id"], probe)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=2, ensure_ascii=False)
    write_report(row["id"], manifest_by_id)
    return failures


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", nargs="+",
                    help="provider:model specs, e.g. gemini:gemini-2.5-pro harvard:gpt-4o")
    ap.add_argument("--probes", nargs="+", default=PROBE_ORDER,
                    choices=PROBE_ORDER, help="probes to run (default: all)")
    ap.add_argument("--images", nargs="+", help="image ids (default: all in TSV)")
    ap.add_argument("--workers", type=int, default=4,
                    help="parallel workers, one (model,image) unit each (default 4)")
    ap.add_argument("--max-edge", type=int, default=2048,
                    help="resize long edge before sending (default 2048)")
    ap.add_argument("--delay", type=float, default=2.0,
                    help="min seconds between calls to the same provider (default 2)")
    ap.add_argument("--force", action="store_true",
                    help="re-run probes even if a result file exists")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the execution plan without calling any API")
    ap.add_argument("--reports-only", action="store_true",
                    help="rebuild results/reports/*.md from existing raw JSONs, no API calls")
    args = ap.parse_args()

    probes = load_probes()
    manifest = load_manifest()
    manifest_by_id = {r["id"]: r for r in manifest}

    if args.reports_only:
        image_ids = args.images or list(manifest_by_id)
        n = 0
        for image_id in image_ids:
            write_report(image_id, manifest_by_id)
            if (REPORTS_DIR / f"{image_id}.md").exists():
                n += 1
        print(f"Reports rebuilt: {n} under {REPORTS_DIR.relative_to(ROOT)}/")
        return

    if not args.models:
        ap.error("--models is required (unless --reports-only)")

    if args.images:
        unknown = set(args.images) - set(manifest_by_id)
        if unknown:
            raise SystemExit(f"Unknown image ids: {sorted(unknown)}")
        manifest = [r for r in manifest if r["id"] in args.images]

    # keep canonical order regardless of CLI order (B_enriched after B_plain)
    probe_list = [p for p in PROBE_ORDER if p in args.probes]

    system_instruction = probes["global_system_instruction"]
    limiters = {name: RateLimiter(args.delay) for name in PROVIDERS}
    providers = ({} if args.dry_run else
                 {s: make_provider(s, system_instruction, limiters)
                  for s in args.models})

    # build (model, image) units
    units = []
    planned = 0
    for spec in args.models:
        for row in manifest:
            if not (IMAGES_DIR / f"{row['id']}.jpg").exists():
                say(f"[skip] {row['id']}: image not downloaded")
                continue
            todo = plan_unit(probes, spec, row, probe_list, args.force)
            if not todo:
                continue
            planned += len(todo)
            if args.dry_run:
                for probe in todo:
                    say(f"[plan] {spec} / {row['id']} / {probe}")
            else:
                units.append((spec, row, todo))

    if args.dry_run:
        print(f"\nDry run: {planned} probe sessions across {len(args.models)} "
              f"model(s); would use {args.workers} workers.")
        return

    failed = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(run_unit, probes, providers[spec], spec, row, todo,
                        args.max_edge, manifest_by_id): (spec, row["id"])
            for spec, row, todo in units
        }
        for fut in as_completed(futures):
            spec, image_id = futures[fut]
            try:
                for probe, err in fut.result():
                    failed.append((spec, image_id, probe, err))
            except Exception as e:
                failed.append((spec, image_id, "<unit>", str(e)))
                say(f"[FAIL] {spec} / {image_id}: {e}", err=True)

    done = planned - len(failed)
    print(f"\nDone: {done}/{planned} probe sessions"
          + (f", {len(failed)} FAILED" if failed else ""))
    for spec, image_id, probe, err in failed:
        print(f"  FAILED {spec} / {image_id} / {probe}: {err[:200]}",
              file=sys.stderr)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
