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

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:47:54+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a famous work of art from the Venetian School.
> 
> **Artist:** Jacopo Tintoretto (born Jacopo Robusti)
> **Title:** *The Drunkenness of Noah*
> **Approximate Date:** c. 1555-1558
> **Collection:** Gallerie dell'Accademia, Venice, Italy
> 
> The painting depicts the biblical story from Genesis (9:20-27) where Noah, after the Great Flood, plants a vineyard, becomes drunk on wine, and lies naked in his tent. In the foreground, Noah is seen asleep and exposed. His son Ham, the central figure, discovers his father and gestures, looking back towards his brothers Shem and Japheth, who are visible in the background preparing to cover their father with a garment while averting their gaze. The powerful, muscular figures and dramatic composition are characteristic of Tintoretto's style.

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

