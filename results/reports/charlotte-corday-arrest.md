# Probe report — `charlotte-corday-arrest`

[![charlotte-corday-arrest](https://upload.wikimedia.org/wikipedia/commons/0/08/Chaffer_corday_1860.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/0/08/Chaffer_corday_1860.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/0/08/Chaffer_corday_1860.jpg/info.json)_

- **Ground-truth subject:** The Arrest of Charlotte Corday
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/charlotte-corday-arrest.jpg` — native 800×638 px, sent 800×638 px
- **SHA-256:** `6aba8b1aa37be3ebd9991c3833c6d5812479ab74a360b82e5a81470cc9a44a1b`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:28+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Henry Chaffer",
>   "title": "Charlotte Corday being led to her execution",
>   "date": "1860",
>   "collection": "Warrington Museum & Art Gallery"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:03+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Henry Chaffer",
>   "title": "An Episode of the French Revolution",
>   "date": "1860",
>   "collection": "Salford Museum and Art Gallery"
> }

