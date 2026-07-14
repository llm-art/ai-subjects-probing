# Probe report — `raft-of-the-medusa`

[![raft-of-the-medusa](https://upload.wikimedia.org/wikipedia/commons/8/85/Le_Radeau_de_la_M%C3%A9duse_-_Th%C3%A9odore_G%C3%A9ricault_-_Mus%C3%A9e_du_Louvre_Peintures_INV_4884_%3B_C_51.jpg/full/!800,800/0/default.jpg)](https://upload.wikimedia.org/wikipedia/commons/8/85/Le_Radeau_de_la_M%C3%A9duse_-_Th%C3%A9odore_G%C3%A9ricault_-_Mus%C3%A9e_du_Louvre_Peintures_INV_4884_%3B_C_51.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://upload.wikimedia.org/wikipedia/commons/8/85/Le_Radeau_de_la_M%C3%A9duse_-_Th%C3%A9odore_G%C3%A9ricault_-_Mus%C3%A9e_du_Louvre_Peintures_INV_4884_%3B_C_51.jpg/info.json)_

- **Ground-truth subject:** The Raft of the Medusa
- **Category:** historical
- **Institution:** wikimedia
- **Image:** `data/images/raft-of-the-medusa.jpg` — native 10244×6924 px, sent 2048×1384 px
- **SHA-256:** `4c525af79589c5e37f5be2c0873397f2e79e37f02744b25aaea41bb45fb42465`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:16:23+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Théodore Géricault",
>   "title": "The Raft of the Medusa",
>   "date": "1818–1819",
>   "collection": "Louvre Museum"
> }
> ```

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-07-14T12:17:04+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {"recognized": true, "artist": "Théodore Géricault", "title": "The Raft of the Medusa", "date": "1818–1819", "collection": "Musée du Louvre"}

