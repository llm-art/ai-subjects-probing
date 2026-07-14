# Probe report — `vercingetorix-caesar`

[![vercingetorix-caesar](https://upload.wikimedia.org/wikipedia/commons/0/02/Vercing%C3%A9torix_se_rend_%C3%A0_C%C3%A9sar_1886_HPMotte.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/0/02/Vercing%C3%A9torix_se_rend_%C3%A0_C%C3%A9sar_1886_HPMotte.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/0/02/Vercing%C3%A9torix_se_rend_%C3%A0_C%C3%A9sar_1886_HPMotte.jpg/info.json)_

- **Ground-truth subject:** Vercingetorix throws down his arms at the feet of Julius Caesar
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/vercingetorix-caesar.jpg` — native 2899×2019 px, sent 2048×1426 px
- **SHA-256:** `79c7a41e3c7353a0e0823afb5650f75fa9601215f87e5203daeb7db246957009`
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
>   "artist": "Henri-Paul Motte",
>   "title": "Vercingetorix se rend à César (Vercingetorix surrenders to Caesar)",
>   "date": "1886",
>   "collection": "Musée d'Orsay"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:55+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Henri-Paul Motte",
>   "title": "Vercingetorix surrenders to Caesar",
>   "date": "1886",
>   "collection": "Musée Crozatier"
> }

