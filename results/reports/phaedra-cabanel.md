# Probe report — `phaedra-cabanel`

[![phaedra-cabanel](https://upload.wikimedia.org/wikipedia/commons/c/c5/Alexandre_Cabanel_Ph%C3%A8dre.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/c/c5/Alexandre_Cabanel_Ph%C3%A8dre.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/c/c5/Alexandre_Cabanel_Ph%C3%A8dre.jpg/info.json)_

- **Ground-truth subject:** Phaedra
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/phaedra-cabanel.jpg` — native 2090×1430 px, sent 2048×1401 px
- **SHA-256:** `5733bd157867fadbda859f33fb42dfd3a22b71d673dd6474aef563876edb2309`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:31+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Alexandre Cabanel",
>   "title": "Cleopatra Testing Poisons on Condemned Prisoners",
>   "date": "1887",
>   "collection": "Royal Museum of Fine Arts Antwerp"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:10+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Alexandre Cabanel",
>   "title": "Phaedra",
>   "date": "1880",
>   "collection": "Musée Fabre"
> }

