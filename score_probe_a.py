#!/usr/bin/env python3
"""
Score Probe A (structured-JSON recognition) per element with an LLM judge.

For every results/raw/<model_slug>/<image_id>/A.json:
  1. parse the model's JSON answer (recognized, artist, title, date, collection),
  2. for each element with ground truth in data/metadata.json, ask a judge model
     whether the model's value matches the institutional ground truth (0/1),
  3. write per-element scores into the A.json `scoring` field,
  4. aggregate to data/probe_a_scores.{md,json}.

The judge defaults to gemini:gemini-2.5-pro and is reused from run_probes.GeminiProvider
(text-only: image_b64=None). The `collection` element is flagged low-confidence because
the institutional keeper is often a historical owner rather than a current museum.

Usage:
  .venv/bin/python score_probe_a.py                       # all models found on disk
  .venv/bin/python score_probe_a.py --judge gemini:gemini-2.5-pro
  .venv/bin/python score_probe_a.py --models gemini:gemini-2.5-pro gemini:gemini-3.5-flash
"""

import argparse
import json
import re
from pathlib import Path

from dotenv import load_dotenv

import run_probes as rp

load_dotenv()

METADATA_PATH = Path("data/metadata.json")
ELEMENTS = ["artist", "title", "date", "collection"]
LOW_CONF = {"collection"}

JUDGE_SYSTEM = (
    "You are a careful art-history grader. You compare a model's answer for one "
    "metadata field of a painting against the institutional ground truth and decide "
    "whether it is correct. Accept translations and name variants (e.g. 'Titian' = "
    "'Tiziano Vecellio'), spelling/diacritic differences, and for dates accept any "
    "value whose range overlaps or is within a few years of the ground truth. "
    "Reply with a SINGLE JSON object: {\"score\": 0 or 1, \"reason\": \"<short>\"}."
)


def parse_model_json(text):
    """Best-effort extraction of a JSON object from a model answer."""
    if not text:
        return None
    t = text.strip()
    # strip ``` fences
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t).strip()
    try:
        return json.loads(t)
    except Exception:
        pass
    # take first balanced {...}
    start = t.find("{")
    if start == -1:
        return None
    depth = 0
    for i in range(start, len(t)):
        if t[i] == "{":
            depth += 1
        elif t[i] == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(t[start:i + 1])
                except Exception:
                    return None
    return None


def ground_truth_for(meta, element):
    """Return ground-truth value(s) for an element, or None if unavailable."""
    if not meta or meta.get("status") in ("no_source", "no_data", None):
        if element == "artist":
            pass  # still may have names below
    if element == "title":
        return meta.get("title")
    if element == "artist":
        names = meta.get("artist_names") or []
        return names or meta.get("artist_ulan")
    if element == "date":
        lbl = meta.get("date_label")
        b, e = meta.get("date_begin"), meta.get("date_end")
        if lbl and b:
            return f"{lbl} (range {b}–{e})"
        return lbl or (f"{b}–{e}" if b else None)
    if element == "collection":
        return meta.get("collection") or meta.get("collection_uri")
    return None


def judge_element(judge, element, model_answer, gt):
    gt_str = " / ".join(str(g) for g in gt) if isinstance(gt, list) else str(gt)
    extra = ""
    if element in LOW_CONF:
        extra = (" Note: the ground-truth keeper may be a historical owner; accept the "
                 "current museum that holds the work as correct too.")
    prompt = (
        f"Field: {element}\n"
        f"Institutional ground truth: {gt_str}\n"
        f"Model's answer: {model_answer!r}\n"
        f"Is the model's answer correct for this field?{extra}"
    )
    try:
        raw = judge.chat([{"role": "user", "text": prompt}], None)
    except Exception as e:
        return None, f"judge call failed: {e}", ""
    parsed = parse_model_json(raw)
    if parsed and "score" in parsed:
        try:
            score = int(parsed["score"])
        except Exception:
            score = 1 if str(parsed["score"]).strip().lower() in ("1", "true", "yes") else 0
        return score, str(parsed.get("reason", "")), raw
    return None, f"unparseable judge reply: {raw[:120]}", raw


def score_one(a_path, metadata, judge, judge_spec):
    rec = json.loads(a_path.read_text(encoding="utf-8"))
    img_id = rec["image_id"]
    answer_text = ""
    for t in rec.get("transcript", []):
        if t["role"] == "assistant":
            answer_text = t["text"]
    parsed = parse_model_json(answer_text)
    meta = metadata.get(img_id, {})

    if parsed is None:
        rec["scoring"] = {
            "status": "parse_error",
            "judge_model": judge_spec,
            "note": "model answer was not parseable JSON",
        }
        a_path.write_text(json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
        return {"image_id": img_id, "status": "parse_error", "elements": {}}

    recognized = parsed.get("recognized")
    elements = {}
    score_sum = 0
    n_scored = 0
    for el in ELEMENTS:
        gt = ground_truth_for(meta, el)
        model_answer = parsed.get(el)
        if gt is None or gt == [] or gt == "":
            continue  # no ground truth → skip
        if model_answer in (None, "", "null"):
            entry = {"model_answer": model_answer, "ground_truth": gt,
                     "score": 0, "reason": "model gave no value"}
        else:
            score, reason, _ = judge_element(judge, el, model_answer, gt)
            if score is None:
                entry = {"model_answer": model_answer, "ground_truth": gt,
                         "score": None, "reason": reason}
            else:
                entry = {"model_answer": model_answer, "ground_truth": gt,
                         "score": score, "reason": reason}
                score_sum += score
                n_scored += 1
        if el in LOW_CONF:
            entry["low_confidence"] = True
        elements[el] = entry

    rec["scoring"] = {
        "status": "scored_llm_judge",
        "judge_model": judge_spec,
        "recognized": recognized,
        "elements": elements,
        "score_sum": score_sum,
        "n_scored": n_scored,
    }
    a_path.write_text(json.dumps(rec, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"image_id": img_id, "status": "scored", "recognized": recognized,
            "elements": elements, "score_sum": score_sum, "n_scored": n_scored}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", default="gemini:gemini-2.5-pro",
                    help="judge model spec (default gemini:gemini-2.5-pro)")
    ap.add_argument("--models", nargs="+",
                    help="model specs to score (default: all on disk)")
    args = ap.parse_args()

    if not METADATA_PATH.exists():
        raise SystemExit("data/metadata.json not found — run fetch_metadata.py first")
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))

    limiters = {name: rp.RateLimiter(2) for name in rp.PROVIDERS}
    judge = rp.make_provider(args.judge, JUDGE_SYSTEM, limiters)

    # discover model dirs
    if args.models:
        model_slugs = [rp.model_slug(m) for m in args.models]
    else:
        model_slugs = [d.name for d in sorted(rp.RESULTS_DIR.iterdir()) if d.is_dir()]

    all_results = {}
    for slug in model_slugs:
        model_dir = rp.RESULTS_DIR / slug
        if not model_dir.is_dir():
            print(f"[skip] {slug}: no results dir")
            continue
        print(f"\n=== scoring {slug} ===")
        per_image = {}
        for img_dir in sorted(model_dir.iterdir()):
            a_path = img_dir / "A.json"
            if not a_path.exists():
                continue
            try:
                res = score_one(a_path, metadata, judge, args.judge)
            except Exception as e:
                print(f"  {img_dir.name:26} ERROR: {e}", flush=True)
                per_image[img_dir.name] = {"image_id": img_dir.name,
                                           "status": f"error: {e}", "elements": {}}
                continue
            per_image[res["image_id"]] = res
            if res["status"] == "scored":
                print(f"  {res['image_id']:26} recognized={res['recognized']!s:5} "
                      f"score {res['score_sum']}/{res['n_scored']}", flush=True)
            else:
                print(f"  {res['image_id']:26} {res['status']}", flush=True)
        all_results[slug] = per_image

    Path("data/probe_a_scores.json").write_text(
        json.dumps(all_results, indent=2, ensure_ascii=False), encoding="utf-8")

    # markdown
    lines = [
        "# Probe A — per-element correctness (LLM-judge)",
        "",
        f"Judge: `{args.judge}`. Ground truth: `data/metadata.json`. "
        "Each element scored 0/1. **collection is low-confidence** (institutional keeper "
        "is often a historical owner, not the current museum).",
        "",
    ]
    for slug, per_image in all_results.items():
        lines += [f"## `{slug}`", "",
                  "| id | recognized | artist | title | date | collection ⚠ | total |",
                  "|---|---|---|---|---|---|---|"]
        tot_sum = tot_n = 0
        for img_id in sorted(per_image):
            r = per_image[img_id]
            if r["status"] != "scored":
                lines.append(f"| {img_id} | — | — | — | — | — | _{r['status']}_ |")
                continue
            els = r["elements"]
            def cell(name):
                e = els.get(name)
                if not e:
                    return "·"
                s = e.get("score")
                return "✓" if s == 1 else ("✗" if s == 0 else "?")
            tot_sum += r["score_sum"]
            tot_n += r["n_scored"]
            lines.append(
                f"| {img_id} | {r['recognized']} | {cell('artist')} | {cell('title')} "
                f"| {cell('date')} | {cell('collection')} | {r['score_sum']}/{r['n_scored']} |")
        lines += ["", f"**Total: {tot_sum}/{tot_n} elements correct**", ""]

    Path("data/probe_a_scores.md").write_text("\n".join(lines), encoding="utf-8")
    print("\nWrote data/probe_a_scores.json and data/probe_a_scores.md")


if __name__ == "__main__":
    main()
