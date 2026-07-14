# Probe report — `francesca-da-rimini-death`

[![francesca-da-rimini-death](https://upload.wikimedia.org/wikipedia/commons/8/8e/Alexandre_cabanel%2C_morte_di_francesca_da_rimini_e_paolo_malatesta%2C_1870.JPG/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/8/8e/Alexandre_cabanel%2C_morte_di_francesca_da_rimini_e_paolo_malatesta%2C_1870.JPG/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/8/8e/Alexandre_cabanel%2C_morte_di_francesca_da_rimini_e_paolo_malatesta%2C_1870.JPG/info.json)_

- **Ground-truth subject:** Death of Francesca da Rimini and of Paolo Malatesta
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/francesca-da-rimini-death.jpg` — native 2680×2100 px, sent 2048×1605 px
- **SHA-256:** `ae04072c275f20252d289e64a36f76e36ffeccf7b73a99c350e7b8330667be12`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:35+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Charles-Édouard de Beaumont",
>   "title": "Paolo and Francesca da Rimini",
>   "date": "1875",
>   "collection": null
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:12+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {"recognized": true, "artist": "Alexandre Cabanel", "title": "The Death of Francesca da Rimini and Paolo Malatesta", "date": "1870", "collection": "Musée d'Orsay"}

