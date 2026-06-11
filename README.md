# AI Subjects Probing

Probing vision-language models' ability to identify iconographic subjects in
European paintings, separating visual reasoning from memorisation.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 1. Download full-resolution images from IIIF

Edit `data/images.tsv` (the authoritative manifest) — one row per image:

| column   | meaning                                                        |
|----------|----------------------------------------------------------------|
| id       | slug used as the output filename                               |
| iiif_url | info.json URL, Image API base URL, manifest URL, or direct URL |
| tier     | A (canonical calibration) / B / C (obscure)                    |
| notes    | free text, carried into the log                                |

```bash
python download_images.py
# options: --all-canvases  --skip-existing  --input ... --out ... --log ...
```

Images land in `data/images/`, with `data/download_log.json` recording the
resolved URL, native vs downloaded dimensions, and a `full_resolution` flag.
If a server caps single-request size (maxWidth/maxArea), the script
automatically assembles the image from full-resolution tiles.

## 2. Probe battery

The locked battery lives in `probes/probes.json`:

- **A — Recognition** (logged covariate, never scored): contamination flag.
- **B-plain / B-framed / B-forced-choice**: the core open-vs-closed contrast.
  Each variant runs in a separate session.
- **B-enriched** (intervention test): runs only after B-plain, separate
  session. ⚠️ `subject_descriptions` currently has 3 of 15 entries — complete
  the remaining 12 one-sentence descriptions before running.
- **C — Closed verification checklists** (per image, expert-locked): ask
  questions individually and sequentially, never as a list. Expert-scored
  out of 5 with semantic matching.

## 3. Run the probes

Put API keys in a `.env` file in the project root (gitignored — copy
`.env.example` and fill it in):

```
GEMINI_API_KEY=...      # Google Generative Language API
HARVARD_API_KEY=...     # HUIT AIS OpenAI Direct gateway
# optional: HARVARD_API_BASE=https://go.apis.huit.harvard.edu/ais-openai-direct/v1
```

Environment variables with the same names take precedence over `.env`.

```bash
.venv/bin/python run_probes.py \
    --models gemini:gemini-2.5-pro harvard:gpt-4o \
    --probes A B_plain B_framed B_forced C \
    --dry-run            # remove to actually run
```

Model specs are `provider:model` (`gemini:...` or `harvard:...`). Other flags:
`--images <id ...>` to restrict to specific images, `--workers` (parallel
workers, default 4 — each handles one model×image unit at a time), `--delay`
(min seconds between calls to the same provider across all workers, default
2), `--max-edge` (resize long edge before sending, default 2048), `--force`
to re-run existing results, `--reports-only` to rebuild the markdown reports
from existing raw results without any API calls.

The runner enforces the locked methodology:

- every probe is a fresh stateless session per image per model;
- every session carries the `global_system_instruction` from `probes.json`
  as the system message — it forbids web search, retrieval, and external
  tools, so answers come only from the image and the model's own knowledge;
- Probe C questions are sent one at a time as sequential turns;
- `B_enriched` refuses to run until `B_plain` exists for that image+model
  **and** all `subject_descriptions` for the image's category are written
  (no `TODO`s in `probes.json`);
- forced-choice option lists come from `probes.json` per category;
- all prompts are read from `probes/probes.json`, never hardcoded.

Outputs:

- `results/raw/<model>/<image_id>/<probe>.json` — one JSON per session, with
  the verbatim transcript, system instruction, image provenance (SHA-256,
  native vs sent resolution), generation params, and timestamp. **Gitignored**
  (regenerable). Re-running skips existing files, so interrupted runs resume.
- `results/reports/<image_id>.md` — per-image report, **tracked in git**,
  regenerated from the raw JSONs each time a model finishes that image. It
  contains the full verbatim transcripts for every model and probe, plus
  Probe C element-by-element answers with empty expert-score checkboxes
  (semantic scoring, not exact match). Probe A sections are labelled
  "record only, do not score".
