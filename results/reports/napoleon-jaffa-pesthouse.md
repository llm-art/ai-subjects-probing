# Probe report — `napoleon-jaffa-pesthouse`

[![napoleon-jaffa-pesthouse](https://upload.wikimedia.org/wikipedia/commons/1/19/Antoine-Jean_Gros_-_Bonaparte_visitant_les_pestif%C3%A9r%C3%A9s_de_Jaffa.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/1/19/Antoine-Jean_Gros_-_Bonaparte_visitant_les_pestif%C3%A9r%C3%A9s_de_Jaffa.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/1/19/Antoine-Jean_Gros_-_Bonaparte_visitant_les_pestif%C3%A9r%C3%A9s_de_Jaffa.jpg/info.json)_

- **Ground-truth subject:** Bonaparte Visiting the Pesthouse in Jaffa
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/napoleon-jaffa-pesthouse.jpg` — native 2763×1972 px, sent 2048×1462 px
- **SHA-256:** `7779d28d84fab623c71c7b3977e16ee901c680c2d9fe095a74f55b2fc1fdc261`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:49+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Antoine-Jean Gros",
>   "title": "Bonaparte Visiting the Plague-Stricken of Jaffa",
>   "date": "1804",
>   "collection": "Louvre Museum"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:19+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Antoine-Jean Gros",
>   "title": "Bonaparte Visiting the Plague Victims of Jaffa",
>   "date": "1804",
>   "collection": "Musée du Louvre"
> }

