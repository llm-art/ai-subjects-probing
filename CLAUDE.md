# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose

Research harness for probing whether vision-language models identify iconographic subjects in European paintings through visual reasoning or memorisation. Two 15-image sets (classical mythology, Old Testament) are downloaded at full resolution from institutional IIIF endpoints, then presented to multiple models under a locked probe battery.

## Commands

```bash
# Setup
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# Download images (the TSV is the authoritative manifest)
.venv/bin/python download_images.py --input data/images.tsv --skip-existing

# Run the probe battery (keys from .env — see .env.example; --dry-run to preview)
.venv/bin/python run_probes.py --models gemini:gemini-2.5-pro harvard:gpt-4o --dry-run

# Build the static human-evaluation site into docs/ (offline; no API calls)
.venv/bin/python build_eval_site.py
```

Other downloader flags: `--all-canvases` (every canvas of a manifest, not just the first), `--out` (output dir, default `data/images`), `--log` (default `data/download_log.json`).

`run_probes.py` flags: `--probes A B_plain B_framed B_forced B_enriched C`, `--images <id ...>`, `--workers` (default 4, one model×image unit per worker), `--delay` (default 2s, per-provider across all workers), `--max-edge` (default 2048), `--force`, `--reports-only` (rebuild markdown reports, no API calls). Model specs are `provider:model` with providers `gemini` and `harvard` (HUIT OpenAI gateway; base URL overridable via `HARVARD_API_BASE`). Outputs: `results/raw/<model_slug>/<image_id>/<probe>.json` (one stateless session per file, **gitignored**; existing files are skipped so runs resume) and `results/reports/<image_id>.md` (full-transcript per-image report with expert-score checkboxes, **tracked in git**, regenerated from raw JSONs whenever a unit finishes). The runner enforces the probe-battery constraints itself (B_enriched ordering + TODO guard, sequential Probe C turns, `global_system_instruction` no-web-search system message on every session) — do not bypass them.

There are no tests or linters.

## Evaluation site (`docs/`, GitHub Pages)

`build_eval_site.py` aggregates ground truth (`data/ground_truth_manual.tsv`), the manifest, and each model's **Probe A** `A.json` into committed static artifacts under `docs/`: **one self-contained HTML page per image** (`docs/<image_id>.html`, all data inlined — no `fetch`, so it works under `file://` and on Pages), a contact-sheet `docs/index.html`, and `docs/probe_a_verdicts_prefilled.csv` (one row per image×model×field, `verdict` prefilled `correct`). Pages are wired by a sticky nav header (prev / next / jump dropdown). Shared styling is the authored, static `docs/style.css`. The site is a **viewer only**: ground-truth metadata left, each model's parsed Probe A fields (title/artist/date/collection) right; it records nothing — verdicts are edited in a Google Sheet imported from the CSV. Scope is Probe A only by design. The build runs offline (stdlib only, no API/network); rerun it after new probe results (it deletes the obsolete `data.json`/`app.js` from the earlier single-page build). See `docs/README.md` for Pages setup and the CSV→Sheet workflow. Reuses `iiif_base()`'s thumbnail logic (mirrored from `run_probes.py`).

## Data flow

`data/images.tsv` (manifest: id, category, subject, iiif_url, source_url, institution, tier, iiif_note) → `download_images.py` → `data/images/<id>.jpg` + `data/download_log.json` (provenance: resolved URL, native vs downloaded dimensions, `full_resolution` flag).

**`data/images.tsv` is current; `data/images.csv` is a stale earlier version — always use the TSV.**

After a download run, update `data/image_quality_report.md` — stats come from `download_log.json` plus Pillow inspection of the files.

## Probe battery (probes/probes.json)

The battery is locked experimental design. Methodology constraints that must not be violated:

- Each probe variant runs in a **separate session/conversation** per image per model.
- Probe C checklist questions are asked **individually and sequentially**, never as a list (listing them causes models to confabulate a coherent narrative across answers).
- Probe A (recognition) is a logged covariate — record verbatim, never score it.
- B-enriched runs **only after** B-plain, in a separate session.
- Probe C is expert-scored with semantic matching, not exact-match.

`B_enriched.subject_descriptions` still contains `"TODO"` entries that must be written and expert-locked before that probe can run.

## Downloader gotchas

- RKD URLs like `media.rkd.nl/iiif/<id>` redirect internally to `/iiif/2/<id>`. `fetch_info()` resolves the canonical `@id` from info.json and `download_from_service` uses it for image requests — bypassing this yields SVG error pages saved as `.jpg`.
- Some servers (Frick/Zeri via `iiif.artresearch.net`, Hertziana) enforce `maxArea`/`maxWidth` caps below native size; the downloader detects this (and silent downscaling) and assembles the image from full-resolution tiles automatically.
- `--skip-existing` matches on output filename only. To force a re-download after changing a URL in the TSV, delete `data/images/<id>.jpg` first.
- `media.rkd.nl` returns 403 without a User-Agent header; the script sends one, but ad-hoc curl/urllib checks must too.
- Known persistent failures: the two Warburg images (`moses-law-sinai`, `abraham-isaac`) fail while `iconographic.warburg.sas.ac.uk` is down (503) — retry later with `--skip-existing`; `belshazzar-feast` (MFA Boston) is WAF-blocked, its `iiif_url` is `MANUAL_REQUIRED` and must be resolved manually via browser DevTools on https://collections.mfa.org/objects/31275.

## Resolving IIIF URLs from artresearch.net

The image records came from artresearch.net resource pages, which don't expose IIIF URLs in HTML (JS-rendered). Query their SPARQL endpoint (`https://artresearch.net/sparql`) for the `https://artresearch.net/custom/work_thumbnail_url` predicate; the thumbnail path contains a base64-encoded full IIIF image URL — decode it and strip `/full/...` to get the service base.
