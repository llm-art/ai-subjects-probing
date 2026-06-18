# Probe report — `drunkenness-noah`

[![drunkenness-noah](https://media.rkd.nl/iiif/2/9171059/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9171059/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9171059/info.json)_

- **Ground-truth subject:** The drunkenness of Noah
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/drunkenness-noah.jpg` — native 2048×1584 px, sent 2048×1584 px
- **SHA-256:** `6be146a95da35993a1646b88285359b2ff1ab2197506387225e562da8e8e7b6b`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:02+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Jacopo Tintoretto",
>   "title": "The Drunkenness of Noah",
>   "date": "c. 1550-1560",
>   "collection": "Musée des Beaux-Arts de Bordeaux"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:48:10+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual elements in the image and knowledge of common subjects in Western art, this painting depicts the biblical story of **The Drunkenness of Noah**.
> 
> Here is a breakdown of the scene:
> 
> *   **Noah:** The older, bearded man lying on the ground, mostly unclothed and asleep, is Noah. He is depicted as having passed out from drinking wine, which is symbolized by the large jug he uses as a pillow, the grapevines on the tree to the right, and the bunch of grapes on the ground. This event takes place after the Great Flood, when Noah plants a vineyard.
> *   **Ham:** The man standing over Noah is his son, Ham. He has discovered his father in this vulnerable state. His mocking expression and gesture of calling to others indicate his disrespect. In the biblical account (Genesis 9:20-27), Ham sees his father's nakedness and tells his brothers about it.
> *   **Shem and Japheth:** The two figures in the background to the left are Noah's other sons, Shem and Japheth. They are shown holding up a garment, preparing to cover their father. According to the story, they walked backward to avoid looking upon their father's nakedness, an act of filial piety and respect that contrasts sharply with Ham's behavior.
> 
> The painting captures the pivotal moment of discovery and the differing reactions of Noah's sons, which ultimately leads to Noah cursing Ham's son, Canaan, and blessing Shem and Japheth. The style of the painting, with its muscular figures, dramatic composition, and rich colors, is characteristic of the Baroque period.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:48:27+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge, this is a depiction of the biblical episode known as **The Drunkenness of Noah**.
> 
> This story comes from the Book of Genesis (9:20-27) in the Old Testament. The figures can be identified as:
> 
> *   **Noah:** The elderly, bearded man lying naked and asleep in the foreground. After the Great Flood, Noah planted a vineyard, made wine, became drunk, and passed out in his tent. The jug he is using as a pillow and the grapes nearby allude to the cause of his state.
> *   **Ham:** The central figure in the dark cap, looking at his father's nakedness. In the biblical account, Ham saw his father and, instead of covering him, went to tell his two brothers in a mocking or disrespectful manner. His gesture here, pointing towards Noah while looking away, captures this moment of discovery and indiscretion.
> *   **Shem and Japheth:** The two figures in the background on the left. They are Noah's other two sons. They are depicted holding a garment, preparing to cover their father. According to the story, they walked backward to avoid seeing their father's nakedness, showing him respect.
> 
> The painting captures the dramatic crux of the story: Ham's disrespectful act, contrasted with the piety of his brothers, Shem and Japheth. This event leads to Noah cursing Ham's son, Canaan, and blessing his other two sons. The scene was a popular subject in European art, often serving as a moral lesson about filial piety and the dangers of intemperance.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:48:44+00:00_

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

> The drunkenness of Noah

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:49:22+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Bernardo Strozzi",
>   "title": "The Drunkenness of Noah",
>   "date": "c. 1630",
>   "collection": "Palazzo Rosso, Genoa"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:12:13+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this image depicts the biblical story of **The Drunkenness of Noah** (from the Book of Genesis), painted by the Italian Baroque artist **Andrea Sacchi** (c. 1640–1645).
> 
> ### Key Elements Depicted:
> * **Noah:** The elderly, bearded patriarch lies asleep on the ground in a state of drunken stupor, partially uncovered. He rests his head near a large earthenware wine jug, with grapes on the vine and on the ground beside him, symbolizing his vineyard.
> * **Ham:** Noah's son stands over him wearing a dark cap and a brown-and-yellow robe. He is gesturing toward his father's nakedness with a mocking or shocked expression.
> * **Shem and Japheth:** In the background on the left, Noah's other two sons are shown walking backward, holding up a cloak to cover their father's nakedness while respectfully averting their eyes.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:12:31+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the biblical scene of **The Drunkenness of Noah** (from the Book of Genesis, 9:20–27). 
> 
> ### Figures and Scene Details:
> * **Noah:** The elderly, bearded patriarch lying asleep and naked on the ground, resting against a large wine jug (amphora) beneath a grapevine, having grown drunk on the wine from his vineyard.
> * **Ham:** Noah's son in the foreground, wearing a dark cap and brown-yellow robes. He has discovered his father's nakedness and is gesturing and pointing mockingly.
> * **Shem and Japheth:** Noah's other two sons, depicted in the background on the left. Having been told of their father's condition, they walk backward with a cloak held over their shoulders to cover Noah's nakedness without looking directly at him.
> 
> ### Art Historical Info:
> This work is by the Italian Baroque painter **Domenico Fetti** (painted circa 1615), currently housed in the Alte Pinakothek in Munich, Germany.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:12:44+00:00_

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

> The drunkenness of Noah

