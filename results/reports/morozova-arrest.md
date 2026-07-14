# Probe report — `morozova-arrest`

[![morozova-arrest](https://upload.wikimedia.org/wikipedia/commons/c/c4/Vasily_Surikov_-_%D0%91%D0%BE%D1%8F%D1%80%D1%8B%D0%BD%D1%8F_%D0%9C%D0%BE%D1%80%D0%BE%D0%B7%D0%BE%D0%B2%D0%B0_-_Google_Art_Project.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/c/c4/Vasily_Surikov_-_%D0%91%D0%BE%D1%8F%D1%80%D1%8B%D0%BD%D1%8F_%D0%9C%D0%BE%D1%80%D0%BE%D0%B7%D0%BE%D0%B2%D0%B0_-_Google_Art_Project.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/c/c4/Vasily_Surikov_-_%D0%91%D0%BE%D1%8F%D1%80%D1%8B%D0%BD%D1%8F_%D0%9C%D0%BE%D1%80%D0%BE%D0%B7%D0%BE%D0%B2%D0%B0_-_Google_Art_Project.jpg/info.json)_

- **Ground-truth subject:** Arrest of the Old Believer noblewoman Feodosia Morozova
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/morozova-arrest.jpg` — native 4000×2059 px, sent 2048×1054 px
- **SHA-256:** `245e9354bd067dff83bcb527ba7b0348506e8fc26845ee4405cfa1785c61f030`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:47+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Vasily Surikov",
>   "title": "Boyarynya Morozova",
>   "date": "1887",
>   "collection": "State Tretyakov Gallery"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:18+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {"recognized": true, "artist": "Vasily Surikov", "title": "Boyarynya Morozova", "date": "1887", "collection": "Tretyakov Gallery"}

