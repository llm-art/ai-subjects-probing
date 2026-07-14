# Probe report — `richelieu-la-rochelle`

[![richelieu-la-rochelle](https://upload.wikimedia.org/wikipedia/commons/d/d8/Siege_of_La_Rochelle_1881_Henri_Motte.png/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/d/d8/Siege_of_La_Rochelle_1881_Henri_Motte.png/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/d/d8/Siege_of_La_Rochelle_1881_Henri_Motte.png/info.json)_

- **Ground-truth subject:** Cardinal Richelieu at the Siege of La Rochelle
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/richelieu-la-rochelle.jpg` — native 3000×1705 px, sent 2048×1164 px
- **SHA-256:** `fe7bb859b0a2c40513d6c5234aacac2f18e17cbe708e261dcdda45a87c229fc3`
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
>   "title": "Cardinal Richelieu at the Siege of La Rochelle",
>   "date": "1881",
>   "collection": "Musée d'Orbigny-Bernon, La Rochelle"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:54+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Henri-Paul Motte",
>   "title": "Cardinal Richelieu at the Siege of La Rochelle",
>   "date": "1881",
>   "collection": "Musée d'Orbigny-Bernon, La Rochelle"
> }

