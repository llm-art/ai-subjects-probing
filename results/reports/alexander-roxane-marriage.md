# Probe report — `alexander-roxane-marriage`

[![alexander-roxane-marriage](https://upload.wikimedia.org/wikipedia/commons/4/48/Il_Sodoma._Villa_Farnesina_fresco1.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/4/48/Il_Sodoma._Villa_Farnesina_fresco1.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/4/48/Il_Sodoma._Villa_Farnesina_fresco1.jpg/info.json)_

- **Ground-truth subject:** The Marriage of Alexander and Roxane
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/alexander-roxane-marriage.jpg` — native 1463×965 px, sent 1463×965 px
- **SHA-256:** `34ca2f9bc7075458bc394d35cd47e7a0fa6461647856962d923fdaf8edf6fb41`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:10+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Il Sodoma (Giovanni Antonio Bazzi)",
>   "title": "The Marriage of Alexander and Roxana",
>   "date": "c. 1517",
>   "collection": "Villa Farnesina"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:56+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Il Sodoma",
>   "title": "The Wedding of Alexander and Roxana",
>   "date": "c. 1519",
>   "collection": "Villa Farnesina, Rome"
> }

