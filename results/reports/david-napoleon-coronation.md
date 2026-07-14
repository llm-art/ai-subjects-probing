# Probe report — `david-napoleon-coronation`

[![david-napoleon-coronation](https://upload.wikimedia.org/wikipedia/commons/8/82/Jacques_Louis_David_-_Le_Sacre_de_Napoleon_et_le_couronnement_de_Josephine_a_Notre_Dame_de_Paris%2C_2_decembre_1804_-_Google_Arts_ProjectFXD.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/8/82/Jacques_Louis_David_-_Le_Sacre_de_Napoleon_et_le_couronnement_de_Josephine_a_Notre_Dame_de_Paris%2C_2_decembre_1804_-_Google_Arts_ProjectFXD.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/8/82/Jacques_Louis_David_-_Le_Sacre_de_Napoleon_et_le_couronnement_de_Josephine_a_Notre_Dame_de_Paris%2C_2_decembre_1804_-_Google_Arts_ProjectFXD.jpg/info.json)_

- **Ground-truth subject:** The Consecration of the Emperor Napoleon and the Coronation of the Empress Josephine
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/david-napoleon-coronation.jpg` — native 10000×6230 px, sent 2048×1276 px
- **SHA-256:** `28f29a6be94d459cdd23e1db65abb728f3f15be68d6d53e98d026231b82cdb0f`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:22+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Jacques-Louis David",
>   "title": "The Coronation of Napoleon",
>   "date": "1807",
>   "collection": "Louvre Museum"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:01+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {"recognized": true, "artist": "Jacques-Louis David", "title": "The Coronation of Napoleon", "date": "1807", "collection": "Louvre Museum"}

