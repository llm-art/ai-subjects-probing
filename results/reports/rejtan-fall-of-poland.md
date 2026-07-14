# Probe report — `rejtan-fall-of-poland`

[![rejtan-fall-of-poland](https://upload.wikimedia.org/wikipedia/commons/1/14/Jan_Matejko_-_Upadek_Polski_%28Reytan%29.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/1/14/Jan_Matejko_-_Upadek_Polski_%28Reytan%29.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/1/14/Jan_Matejko_-_Upadek_Polski_%28Reytan%29.jpg/info.json)_

- **Ground-truth subject:** Tadeusz Rejtan's protest against the First Partition of Poland (Rejtan)
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/rejtan-fall-of-poland.jpg` — native 3543×2049 px, sent 2048×1184 px
- **SHA-256:** `4a3d1e9e699561dfeef9b404cfc7a17a1165324f535213dc95866ac82474ef2d`
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
>   "artist": "Jan Matejko",
>   "title": "Rejtan – The Fall of Poland",
>   "date": "1866",
>   "collection": "Royal Castle, Warsaw"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:15+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Jan Matejko",
>   "title": "Rejtan, or the Fall of Poland",
>   "date": "1866",
>   "collection": "Royal Castle, Warsaw"
> }

