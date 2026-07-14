# Probe report — `beccafumi-codrus-sacrifice`

[![beccafumi-codrus-sacrifice](https://upload.wikimedia.org/wikipedia/commons/2/27/Domenico_Beccafumi_-_Public_Virtues_of_Greek_and_Roman_Heroes-_The_Sacrifice_of_King_Codron_of_Athens_-_Google_Art_Project.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/2/27/Domenico_Beccafumi_-_Public_Virtues_of_Greek_and_Roman_Heroes-_The_Sacrifice_of_King_Codron_of_Athens_-_Google_Art_Project.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/2/27/Domenico_Beccafumi_-_Public_Virtues_of_Greek_and_Roman_Heroes-_The_Sacrifice_of_King_Codron_of_Athens_-_Google_Art_Project.jpg/info.json)_

- **Ground-truth subject:** The Sacrifice of King Codrus of Athens
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/beccafumi-codrus-sacrifice.jpg` — native 1636×1080 px, sent 1636×1080 px
- **SHA-256:** `be8d51c0fbe3e1c9e4794add91f47d3eb5bffb7831a04451c602d431522e30d8`
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
>   "artist": "Francesco Salviati",
>   "title": "The Triumph of Furius Camillus",
>   "date": "c. 1543-1545",
>   "collection": "Palazzo Vecchio, Florence"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:59+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Nicolò dell'Abate",
>   "title": "Cincinnatus Called from the Plow",
>   "date": "c. 1550",
>   "collection": "Palazzo Poggi, Bologna"
> }

