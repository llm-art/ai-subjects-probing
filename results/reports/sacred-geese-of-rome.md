# Probe report — `sacred-geese-of-rome`

[![sacred-geese-of-rome](https://upload.wikimedia.org/wikipedia/commons/0/00/MotteGeese.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/0/00/MotteGeese.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/0/00/MotteGeese.jpg/info.json)_

- **Ground-truth subject:** The Sacred Geese of Rome
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/sacred-geese-of-rome.jpg` — native 1970×1341 px, sent 1970×1341 px
- **SHA-256:** `9006b6c2caf99a02b510aa5fc8f955ea493f642a4464f8b0f2e29045881187f6`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:31+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Jean-François Portaels",
>   "title": "The Sacred Geese of the Capitol",
>   "date": "1870",
>   "collection": "Royal Museums of Fine Arts of Belgium"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:06+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Henri-Paul Motte",
>   "title": "The Geese of the Capitol",
>   "date": "1889",
>   "collection": "Musée des Beaux-Arts de La Rochelle"
> }

