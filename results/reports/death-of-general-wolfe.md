# Probe report — `death-of-general-wolfe`

[![death-of-general-wolfe](https://upload.wikimedia.org/wikipedia/commons/4/4f/Benjamin_West_005.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/4/4f/Benjamin_West_005.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/4/4f/Benjamin_West_005.jpg/info.json)_

- **Ground-truth subject:** Death of General Wolfe at the Battle of Quebec
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/death-of-general-wolfe.jpg` — native 3456×2304 px, sent 2048×1365 px
- **SHA-256:** `194881d54e1f3ff77e202472cbe66319732569fb604a9e472908ee4d388789dc`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:53+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Benjamin West",
>   "title": "The Death of General Wolfe",
>   "date": "1770",
>   "collection": "National Gallery of Canada"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:20+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {"recognized": true, "artist": "Benjamin West", "title": "The Death of General Wolfe", "date": "1770", "collection": "National Gallery of Canada"}

