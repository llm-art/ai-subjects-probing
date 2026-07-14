# Probe report — `lady-godiva-lefebvre`

[![lady-godiva-lefebvre](https://upload.wikimedia.org/wikipedia/commons/5/59/Lady_Godiva_%E2%80%93_J._J._Lefebvre.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/5/59/Lady_Godiva_%E2%80%93_J._J._Lefebvre.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/5/59/Lady_Godiva_%E2%80%93_J._J._Lefebvre.jpg/info.json)_

- **Ground-truth subject:** Lady Godiva
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/lady-godiva-lefebvre.jpg` — native 5200×8000 px, sent 1331×2048 px
- **SHA-256:** `0b74647769c6efbefbfd35fc2cf0fb0e30a8043c2930c9af976ddb3d2334b4f5`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:41+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Jules Lefebvre",
>   "title": "Lady Godiva",
>   "date": "1890",
>   "collection": "Musée d'Orsay, Paris"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:14+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Jules Joseph Lefebvre",
>   "title": "Lady Godiva",
>   "date": "1890",
>   "collection": "Musée de Picardie"
> }

