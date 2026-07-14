#!/usr/bin/env python3
"""Build the static human-evaluation site (docs/) from probe results.

GitHub Pages serves ONLY the static files in docs/ — this script never runs
there. It is a local, offline generator: run it before pushing to refresh the
committed data artifacts the front-end reads.

It aggregates, per image:
  - ground-truth metadata from data/ground_truth_manual.tsv (title/artist/
    date/collection),
  - each model's Probe A structured answers from
    results/raw/<model_slug>/<image_id>/A.json (which is gitignored, hence the
    need to bake it into a committed file),
  - an IIIF thumbnail / full-res URL,

and writes committed artifacts:
  - docs/<image_id>.html                — one self-contained page per image
    (all data inlined, no fetch — works under file:// and on Pages), wired
    together by a header nav bar (prev / next / jump dropdown).
  - docs/index.html                     — contact-sheet landing page.
  - docs/probe_a_verdicts_prefilled.csv — one row per image x model x field,
    every `verdict` prefilled to "correct"; import into a Google Sheet and flip
    only the wrong rows.

Presentation lives in the authored, static docs/style.css (linked relatively).

Scope is Probe A only (title, artist, date, collection) by design.

Usage:
  python build_eval_site.py [--out docs] [--models <slug> ...] [--generated-utc <iso>]
No network calls; stdlib only.
"""

import argparse
import csv
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "data" / "images.tsv"
GROUND_TRUTH_PATH = ROOT / "data" / "ground_truth_manual.tsv"
DOWNLOAD_LOG_PATH = ROOT / "data" / "download_log.json"
RESULTS_DIR = ROOT / "results" / "raw"

FIELDS = ["title", "artist", "date", "collection"]
FIELD_LABELS = {
    "title": "Title / subject",
    "artist": "Artist",
    "date": "Date",
    "collection": "Collection",
}
# mythology before old_testament, then anything else; ids sorted within group.
CATEGORY_ORDER = {"mythology": 0, "old_testament": 1}


def load_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


# --- IIIF thumbnail derivation (mirrors run_probes.iiif_base) -----------------

_DOWNLOAD_LOG = None


_DIRECT_IMAGE_EXT_RE = re.compile(r"\.(jpe?g|png|tiff?|gif|webp)$", re.IGNORECASE)
_IIIF_REQUEST_RE = re.compile(r"/[^/]+/[^/]+/\d+/default\.\w+$")


def direct_image_url(image_id):
    """Return the plain file URL if this image was downloaded directly (no
    IIIF service — e.g. Wikimedia Commons originals), else None. An IIIF
    image-request URL also ends in an image extension, so it must be
    excluded explicitly rather than relying on the extension alone."""
    global _DOWNLOAD_LOG
    if _DOWNLOAD_LOG is None:
        try:
            with open(DOWNLOAD_LOG_PATH, encoding="utf-8") as f:
                _DOWNLOAD_LOG = json.load(f)
        except (OSError, json.JSONDecodeError):
            _DOWNLOAD_LOG = {}
    entry = _DOWNLOAD_LOG.get(image_id, {})
    for d in entry.get("downloads", []):
        url = d.get("resolved_url", "")
        if _DIRECT_IMAGE_EXT_RE.search(url) and not _IIIF_REQUEST_RE.search(url):
            return url
    return None


def iiif_base(image_id, row):
    """IIIF Image API service base. Prefer the canonical resolved URL from
    download_log.json (handles e.g. RKD's /iiif/ -> /iiif/2/ redirect); fall
    back to the TSV iiif_url minus /info.json."""
    global _DOWNLOAD_LOG
    if _DOWNLOAD_LOG is None:
        try:
            with open(DOWNLOAD_LOG_PATH, encoding="utf-8") as f:
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
    if url and url != "MANUAL_REQUIRED" and not _DIRECT_IMAGE_EXT_RE.search(url):
        return re.sub(r"/info\.json$", "", url)
    return None


# --- Probe A field extraction -------------------------------------------------


def _parse_assistant_json(text):
    """Best-effort parse of the assistant's structured answer when scoring is
    absent: strip ```json fences and json.loads."""
    if not text:
        return {}
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    try:
        obj = json.loads(t)
        return obj if isinstance(obj, dict) else {}
    except (json.JSONDecodeError, ValueError):
        return {}


def extract_fields(rec):
    """Return ({field: model_answer_str}, recognized) from a Probe A record.
    Prefer scoring.elements.<field>.model_answer; fall back to parsing the
    assistant transcript turn."""
    fields = {}
    elements = (rec.get("scoring") or {}).get("elements") or {}
    fallback = None
    for field in FIELDS:
        el = elements.get(field) or {}
        val = el.get("model_answer")
        if val is None and "model_answer" not in el:
            if fallback is None:
                turns = rec.get("transcript") or []
                assistant = next(
                    (t.get("text") for t in turns if t.get("role") == "assistant"), ""
                )
                fallback = _parse_assistant_json(assistant)
            val = fallback.get(field)
        fields[field] = "" if val is None else str(val).strip()

    recognized = None
    if "recognized" in (rec.get("scoring") or {}):
        recognized = rec["scoring"]["recognized"]
    elif fallback is not None:
        recognized = fallback.get("recognized")
    return fields, recognized


# --- HTML rendering -----------------------------------------------------------


def esc(value):
    return html.escape("" if value is None else str(value))


def _cell(value, klass):
    v = ("" if value is None else str(value)).strip()
    if not v:
        return f'<div class="{klass}"><span class="empty">— empty —</span></div>'
    return f'<div class="{klass}">{esc(v)}</div>'


def _nav_header(image, prev_id, next_id, position, total, all_images):
    """Sticky nav: prev / jump dropdown / next / counter / index link."""
    options = []
    for im in all_images:
        sel = " selected" if im["id"] == image["id"] else ""
        label = f'{im["id"]} — {im["subject"]}'
        options.append(f'<option value="{esc(im["id"])}.html"{sel}>{esc(label)}</option>')
    prev_html = (
        f'<a class="navbtn" href="{esc(prev_id)}.html">‹ prev</a>'
        if prev_id
        else '<span class="navbtn disabled">‹ prev</span>'
    )
    next_html = (
        f'<a class="navbtn" href="{esc(next_id)}.html">next ›</a>'
        if next_id
        else '<span class="navbtn disabled">next ›</span>'
    )
    return f"""  <header>
    <div class="bar">
      <h1><a href="index.html">Probe&nbsp;A · metadata evaluation</a></h1>
      <div class="controls">
        {prev_html}
        <span class="counter">{position} / {total}</span>
        {next_html}
        <label>Jump
          <select onchange="if(this.value)location.href=this.value;">
            {chr(10).join("            " + o for o in options).strip()}
          </select>
        </label>
        <a class="navbtn" href="index.html">index</a>
      </div>
    </div>
  </header>"""


def render_page(image, prev_id, next_id, position, total, all_images, models):
    gt = image["ground_truth"]
    thumb = ""
    if image["thumb_url"]:
        thumb = (
            f'<a href="{esc(image["full_url"] or image["thumb_url"])}" '
            f'target="_blank" rel="noopener">'
            f'<img class="thumb" src="{esc(image["thumb_url"])}" '
            f'alt="{esc(image["id"])}" loading="lazy"></a>'
        )

    def meta_row(label, val):
        v = (val or "").strip()
        cls = "" if v else ' class="empty"'
        return f"<dt>{label}</dt><dd{cls}>{esc(v) if v else '— empty —'}</dd>"

    tags = "".join(
        f'<span class="tag">{esc(t)}</span>'
        for t in (
            image["category"],
            f'tier {image["tier"]}' if image["tier"] else "",
            image["institution"],
        )
        if t
    )
    source = (
        f'<div class="tags"><a class="tag" href="{esc(image["source_url"])}" '
        f'target="_blank" rel="noopener">source ↗</a></div>'
        if image["source_url"]
        else ""
    )

    cards = []
    for spec in models:
        m = image["models"].get(spec)
        if not m:
            continue
        if m["recognized"] is True:
            rec = '<span class="recognized yes">recognized: yes</span>'
        elif m["recognized"] is False:
            rec = '<span class="recognized no">recognized: no</span>'
        else:
            rec = ""
        ts = (
            f'<span class="meta-min">{esc(m["timestamp_utc"])}</span>'
            if m["timestamp_utc"]
            else ""
        )
        rows = []
        for f in FIELDS:
            rows.append(
                f'<tr class="label-row"><td colspan="2" class="field-label">'
                f"{esc(FIELD_LABELS.get(f, f))}</td></tr>"
                f"<tr><td>{_cell(gt.get(f), 'cell-gt')}</td>"
                f"<td>{_cell(m['fields'].get(f), 'cell-model')}</td></tr>"
            )
        cards.append(
            f"""        <section class="model-card">
          <div class="model-head">
            <span class="name">{esc(spec)}</span>
            {rec}
            {ts}
          </div>
          <table class="fields">
            <thead><tr><th>Ground truth</th><th>Model answer</th></tr></thead>
            <tbody>{''.join(rows)}</tbody>
          </table>
        </section>"""
        )

    header = _nav_header(image, prev_id, next_id, position, total, all_images)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(image["id"])} — Probe A evaluation</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
{header}
  <main>
    <aside class="gt-panel">
      {thumb}
      <h2>Ground truth</h2>
      <dl class="meta">
        {meta_row("Title", gt.get("title"))}
        {meta_row("Artist", gt.get("artist"))}
        {meta_row("Date", gt.get("date"))}
        {meta_row("Collection", gt.get("collection"))}
      </dl>
      <div class="tags">{tags}</div>
      {source}
    </aside>
    <div class="models">
{chr(10).join(cards) if cards else '<p class="loading">No model answers.</p>'}
    </div>
  </main>
</body>
</html>
"""


def render_index(all_images, models, generated_utc):
    # Stats
    by_cat = {}
    for im in all_images:
        by_cat.setdefault(im["category"], []).append(im)
    stat_parts = [
        f'<div class="stat"><span class="stat-n">{len(all_images)}</span><span class="stat-l">images</span></div>',
        f'<div class="stat"><span class="stat-n">{len(models)}</span><span class="stat-l">models</span></div>',
    ]
    for cat, imgs in sorted(by_cat.items()):
        label = cat.replace("_", " ")
        stat_parts.append(
            f'<div class="stat"><span class="stat-n">{len(imgs)}</span>'
            f'<span class="stat-l">{esc(label)}</span></div>'
        )
    stat_parts.append(
        '<div class="stat"><span class="stat-n">4</span>'
        '<span class="stat-l">scored fields</span></div>'
    )

    # Model badges
    model_badges = "".join(
        f'<code class="model-badge">{esc(m)}</code>' for m in models
    )

    # Contact-sheet grid grouped by category
    parts = []
    last_cat = None
    open_grid = False
    for im in all_images:
        if im["category"] != last_cat:
            if open_grid:
                parts.append("</div>")
            last_cat = im["category"]
            label = last_cat.replace("_", " ").title()
            parts.append(f'<h2 class="cat-head">{esc(label)}</h2>')
            parts.append('<div class="grid">')
            open_grid = True
        thumb = (
            f'<img src="{esc(im["thumb_url"])}" alt="{esc(im["id"])}" loading="lazy">'
            if im["thumb_url"]
            else '<div class="noimg"></div>'
        )
        parts.append(
            f'<a class="card" href="{esc(im["id"])}.html">'
            f"{thumb}"
            f'<span class="card-id">{esc(im["id"])}</span>'
            f'<span class="card-sub">{esc(im["subject"])}</span></a>'
        )
    if open_grid:
        parts.append("</div>")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Probe A — VLM metadata evaluation</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="home-header">
    <div class="bar">
      <h1>Probe&nbsp;A · VLM metadata evaluation</h1>
    </div>
  </header>
  <main class="index">
    <section class="hero">
      <p class="hero-desc">
        This tool supports human assessment of <strong>vision-language model (VLM)</strong>
        performance on European paintings. For each image the models were asked to identify
        the artwork by providing structured metadata —
        <em>title, artist, date,</em> and <em>collection</em> — from visual
        inspection alone (no web search).
      </p>
      <p class="hero-desc">
        Ground truth is shown on the left; each model's answer is on the right,
        field by field. Verdicts are recorded in the
        <a href="probe_a_verdicts_prefilled.csv">prefilled CSV</a> →
        imported into a Google Sheet, one row per image × model × field,
        every verdict pre-filled <em>correct</em>.
      </p>
      <div class="stats">{''.join(stat_parts)}</div>
      <p class="hero-models">Models evaluated: {model_badges}</p>
      <ol class="howto">
        <li>Click any painting below to open its evaluation page.</li>
        <li>Compare each model's answer against the ground truth.</li>
        <li>Open the <a href="probe_a_verdicts_prefilled.csv">prefilled CSV</a> in
            Google Sheets and flip <em>correct → incorrect</em> for wrong answers.</li>
        <li>Use the ‹ prev / next › header to move between images without returning here.</li>
      </ol>
    </section>
    {''.join(parts)}
  </main>
  <footer>Generated {esc(generated_utc)} · viewer only — all verdicts in the CSV.</footer>
</body>
</html>
"""


# --- Build --------------------------------------------------------------------


def discover_model_slugs(only=None):
    if not RESULTS_DIR.exists():
        return []
    slugs = sorted(p.name for p in RESULTS_DIR.iterdir() if p.is_dir())
    if only:
        wanted = {s.replace(":", "_").replace("/", "_") for s in only}
        slugs = [s for s in slugs if s in wanted]
    return slugs


def build(out_dir, model_slugs, generated_utc):
    manifest = {r["id"]: r for r in load_tsv(MANIFEST_PATH)}
    ground_truth = {r["id"]: r for r in load_tsv(GROUND_TRUTH_PATH)}

    images = []
    model_specs = set()
    for image_id, row in manifest.items():
        models = {}
        for slug in model_slugs:
            a_path = RESULTS_DIR / slug / image_id / "A.json"
            if not a_path.exists():
                continue
            with open(a_path, encoding="utf-8") as f:
                rec = json.load(f)
            fields, recognized = extract_fields(rec)
            spec = rec.get("model") or slug
            model_specs.add(spec)
            models[spec] = {
                "fields": fields,
                "recognized": recognized,
                "timestamp_utc": rec.get("timestamp_utc", ""),
            }
        if not models:
            continue  # only include images that have at least one Probe A run

        gt_row = ground_truth.get(image_id, {})
        direct_url = direct_image_url(image_id)
        if direct_url:
            thumb_url = full_url = direct_url
        else:
            base = iiif_base(image_id, row)
            thumb_url = f"{base}/full/!800,800/0/default.jpg" if base else ""
            full_url = f"{base}/full/max/0/default.jpg" if base else ""
        images.append(
            {
                "id": image_id,
                "category": row.get("category", ""),
                "subject": row.get("subject", ""),
                "institution": row.get("institution", ""),
                "tier": row.get("tier", ""),
                "source_url": row.get("source_url", ""),
                "thumb_url": thumb_url,
                "full_url": full_url,
                "ground_truth": {f: (gt_row.get(f) or "").strip() for f in FIELDS},
                "models": models,
            }
        )

    images.sort(key=lambda im: (CATEGORY_ORDER.get(im["category"], 99), im["id"]))
    models_sorted = sorted(model_specs)

    out_dir.mkdir(parents=True, exist_ok=True)

    # One self-contained HTML page per image, wired by a nav header.
    total = len(images)
    for i, im in enumerate(images):
        prev_id = images[i - 1]["id"] if i > 0 else None
        next_id = images[i + 1]["id"] if i < total - 1 else None
        page = render_page(im, prev_id, next_id, i + 1, total, images, models_sorted)
        with open(out_dir / f"{im['id']}.html", "w", encoding="utf-8") as f:
            f.write(page)
    with open(out_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(render_index(images, models_sorted, generated_utc))

    # Remove obsolete artifacts from the previous (single-page-app) build.
    for stale in ("data.json", "app.js"):
        p = out_dir / stale
        if p.exists():
            p.unlink()

    csv_path = out_dir / "probe_a_verdicts_prefilled.csv"
    rows = 0
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "image_id",
                "category",
                "subject",
                "model",
                "field",
                "ground_truth",
                "model_answer",
                "verdict",
                "notes",
            ]
        )
        for im in images:
            for spec in models_sorted:
                m = im["models"].get(spec)
                if not m:
                    continue
                for field in FIELDS:
                    w.writerow(
                        [
                            im["id"],
                            im["category"],
                            im["subject"],
                            spec,
                            field,
                            im["ground_truth"].get(field, ""),
                            m["fields"].get(field, ""),
                            "correct",
                            "",
                        ]
                    )
                    rows += 1

    print(
        f"Wrote {total} pages + index.html to {out_dir} "
        f"— {len(images)} images, {len(models_sorted)} models"
    )
    print(f"Wrote {csv_path} — {rows} rows (all verdict=correct)")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="docs", help="output directory (default: docs)")
    ap.add_argument(
        "--models",
        nargs="*",
        default=None,
        help="model specs/slugs to include (default: all discovered under results/raw)",
    )
    ap.add_argument(
        "--generated-utc",
        default=None,
        help="ISO timestamp stamped into data.json (default: now)",
    )
    args = ap.parse_args()

    model_slugs = discover_model_slugs(args.models)
    if not model_slugs:
        print("No model directories found under results/raw/", file=sys.stderr)
        sys.exit(1)

    generated = args.generated_utc or datetime.now(timezone.utc).isoformat(
        timespec="seconds"
    )
    build(ROOT / args.out, model_slugs, generated)


if __name__ == "__main__":
    main()
