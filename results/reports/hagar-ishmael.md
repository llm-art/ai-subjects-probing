# Probe report — `hagar-ishmael`

[![hagar-ishmael](https://iiif.artresearch.net/iiif/3/zeri/120000/106400/106241.jpg/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/zeri/120000/106400/106241.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/zeri/120000/106400/106241.jpg/info.json)_

- **Ground-truth subject:** Hagar Ishmael and the Angel in the Wilderness
- **Category:** old_testament
- **Institution:** zeri
- **Image:** `data/images/hagar-ishmael.jpg` — native 3072×2356 px, sent 2048×1571 px
- **SHA-256:** `a58a4d3a33b89e8a616055c171fe2dca01a5191b0df61b3a7c9c2ff01675700d`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:26+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Pompeo Batoni",
>   "title": "Hagar and the Angel",
>   "date": "1776",
>   "collection": "Galleria Nazionale d'Arte Antica - Palazzo Corsini"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:49:20+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual elements in the image and common themes in Western art, this painting depicts the biblical story of **Hagar and Ishmael in the wilderness**.
> 
> Here is a breakdown of the scene:
> 
> *   **The Figures:**
>     *   **Hagar:** The woman reclining on the left, dressed in flowing robes and a turban-like head covering. Her expression is one of distress and surprise as she looks up at the angel. Her hand is raised in a gesture of appeal or astonishment.
>     *   **Ishmael:** The young boy next to her, looking up with a pleading expression and outstretched hands towards the angel.
>     *   **The Angel:** A winged, youthful figure descending from the right. The angel gestures towards Hagar and Ishmael with an open palm, a sign of comfort, reassurance, and divine intervention.
> 
> *   **The Narrative:**
>     This scene illustrates a specific moment from the Book of Genesis. Hagar, the Egyptian handmaiden of Sarah, and her son by Abraham, Ishmael, were cast out into the wilderness of Beersheba. When their water ran out, Hagar placed her son under a bush to die and sat a distance away, weeping. In this moment of despair, an angel of God appeared, told her not to be afraid, and revealed a well of water, saving them from death.
> 
> *   **The Setting:**
>     The landscape is wild and rugged, with large trees, rocks, and a somewhat barren background, representing the wilderness where Hagar and Ishmael were abandoned.
> 
> The painting captures the dramatic climax of the story: the moment of divine rescue, where despair is met with heavenly mercy. The style, with its dramatic lighting, dynamic composition, and idealized figures, is characteristic of the Baroque period of art.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:49:36+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual elements in the painting and my internal knowledge of art history and biblical narratives, this painting depicts the episode of **Hagar and Ishmael in the Wilderness**.
> 
> The figures are:
> *   **Hagar:** The woman seated on the left, identifiable by her distressed expression and her presence with a young boy in a desolate landscape. Her turban-like headwear often signifies her Egyptian origin in European art.
> *   **Ishmael:** The young boy, her son by Abraham.
> *   **An Angel of the Lord:** The winged figure who has appeared to save them.
> 
> The scene illustrates a specific moment from the Book of Genesis (Chapter 21). After being cast out into the wilderness of Beersheba by Abraham at Sarah's insistence, Hagar and Ishmael run out of water. Believing her son will die, Hagar places him under a bush and sits a distance away to weep. The painting captures the moment of divine intervention when an angel appears, comforts Hagar, and reveals a well of water, saving them from death and promising that Ishmael will become the father of a great nation. The gestures of Hagar and Ishmael show a mixture of despair and pleading, while the angel's gesture is one of comfort and guidance.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:49:53+00:00_

**Prompt:**

> This painting depicts one of the following subjects. Which one is it?
> — The finding of Moses: Pharaoh's daughter discovers the child floating on the river
> — The sacrifice of Isaac (Abraham and Isaac)
> — Potiphar's wife catches Joseph by his robe; Joseph escapes
> — Balaam strikes his ass; the ass lies down and starts to speak
> — Isaac blesses Jacob disguised in Esau's clothes
> — Samson breaks the pillars; the temple of Dagon collapses
> — The drunkenness of Noah
> — Feast of Esther
> — Belshazzar's Feast
> — Bathsheba receives a letter from David
> — The Gathering of Manna
> — Hagar, Ishmael and the Angel in the Wilderness
> — The Prodigal Son chased from the brothel (Luke 15:13)
> — Jephtha welcomed by his daughter (Judges 11:29-40)
> — Judah's love-affair with Tamar; he gives her his signet-ring and staff
> Answer with the subject only.

**Response (verbatim):**

> Hagar, Ishmael and the Angel in the Wilderness

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:49:36+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Carlo Maratta",
>   "title": "Hagar and Ishmael in the Wilderness",
>   "date": "c. 1680",
>   "collection": "Museo del Prado"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:13:06+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this image depicts the biblical scene of **Hagar and Ishmael in the Wilderness** (from the Book of Genesis). 
> 
> In the scene:
> * **Hagar** is shown on the left, reclining in exhaustion and despair after being cast out into the desert of Beersheba.
> * Her young son, **Ishmael**, sits beside her, looking up toward the divine messenger.
> * **The Angel of the Lord** appears on the right with outstretched wings, gesturing to comfort them and direct them to a well of water, saving them from dying of thirst. 
> 
> This is a classic subject in Baroque art, rendered here in a classical Italian style (likely a 17th-century painting by an artist such as Francesco Cozza, Pier Francesco Mola, or a similar master of the Roman Baroque school).

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:13:27+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the biblical scene of **the Angel appearing to Hagar and Ishmael in the Wilderness** (from the Book of Genesis, Chapter 21). 
> 
> ### Figures Depicted:
> 1. **Hagar** (the reclining woman on the left): Abraham's handmaid who was cast out into the wilderness of Beersheba with her son.
> 2. **Ishmael** (the young boy next to her): Hagar's son, who was dying of thirst before divine intervention.
> 3. **The Angel of God** (the winged figure on the right): Sent by God to comfort Hagar, save Ishmael, and reveal a nearby well of water.
> 
> ### The Episode:
> After being banished by Abraham, Hagar and Ishmael ran out of water in the desert. Unable to bear watching her child die, Hagar placed Ishmael under a bush and sat a distance away, weeping. God heard the boy crying, and an angel appeared to Hagar, comforting her, promising that Ishmael would father a great nation, and showing her a well of water to save their lives.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:13:42+00:00_

**Prompt:**

> This painting depicts one of the following subjects. Which one is it?
> — The finding of Moses: Pharaoh's daughter discovers the child floating on the river
> — The sacrifice of Isaac (Abraham and Isaac)
> — Potiphar's wife catches Joseph by his robe; Joseph escapes
> — Balaam strikes his ass; the ass lies down and starts to speak
> — Isaac blesses Jacob disguised in Esau's clothes
> — Samson breaks the pillars; the temple of Dagon collapses
> — The drunkenness of Noah
> — Feast of Esther
> — Belshazzar's Feast
> — Bathsheba receives a letter from David
> — The Gathering of Manna
> — Hagar, Ishmael and the Angel in the Wilderness
> — The Prodigal Son chased from the brothel (Luke 15:13)
> — Jephtha welcomed by his daughter (Judges 11:29-40)
> — Judah's love-affair with Tamar; he gives her his signet-ring and staff
> Answer with the subject only.

**Response (verbatim):**

> Hagar, Ishmael and the Angel in the Wilderness

