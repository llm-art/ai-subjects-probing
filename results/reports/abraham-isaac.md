# Probe report — `abraham-isaac`

[![abraham-isaac](https://iiif.artresearch.net/iiif/3/zeri/120000/111200/111041.jpg/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/zeri/120000/111200/111041.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/zeri/120000/111200/111041.jpg/info.json)_

- **Ground-truth subject:** The sacrifice of Isaac (Abraham and Isaac)
- **Category:** old_testament
- **Institution:** zeri
- **Image:** `data/images/abraham-isaac.jpg` — native 2365×3072 px, sent 1577×2048 px
- **SHA-256:** `6d50ff99237146ee36d07d636e57676591f9784f585ebafa927cab24371a47b2`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:45:47+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this artwork is:
> 
> *   **Artist:** Mattia Preti (also known as Il Cavalier Calabrese)
> *   **Title:** *The Sacrifice of Isaac*
> *   **Approximate Date:** c. 1650-1660
> *   **Collection:** Museo e Real Bosco di Capodimonte, Naples, Italy
> 
> The painting depicts the biblical story from the Book of Genesis where God tests Abraham by commanding him to sacrifice his son, Isaac. At the last moment, an angel intervenes to stop Abraham, providing a ram for the sacrifice instead. The style is characteristic of the Italian Baroque period, with its dramatic use of light and shadow (chiaroscuro), intense emotion, and dynamic composition, heavily influenced by the work of Caravaggio.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:46:09+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual elements in the image and common knowledge of religious art, this painting depicts the biblical story of the **Sacrifice of Isaac** (also known as the Binding of Isaac) from the Book of Genesis.
> 
> Here is a breakdown of the scene and its characters:
> 
> *   **Abraham:** The older, bearded man in the center. He is depicted with a look of anguish and determination, holding a knife or short sword, poised to sacrifice his son as commanded by God to test his faith. His other hand rests on his son's head.
> *   **Isaac:** The young, semi-nude boy lying on what appears to be an altar or pyre. He is blindfolded, symbolizing his submission and trust.
> *   **The Angel of the Lord:** The winged figure appearing from the upper left. The angel is intervening at the last possible moment, gesturing to stop Abraham from carrying out the sacrifice. The angel's expression is serious and commanding.
> *   **The Ram:** In the lower-left corner, partially obscured, is the head of a ram. In the biblical narrative, after stopping Abraham, the angel directs him to a ram caught in a thicket, which Abraham then sacrifices in place of his son.
> 
> The painting captures the dramatic climax of the story. The use of strong contrast between light and shadow (chiaroscuro) heightens the emotional intensity and focuses the viewer's attention on the expressions and actions of the figures. This style is characteristic of Baroque painting, particularly the work of Caravaggio and his followers.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:46:26+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge, this is a depiction of a well-known biblical episode.
> 
> **Episode:** The Binding of Isaac (also known as the Sacrifice of Isaac), from the Book of Genesis (Chapter 22).
> 
> **Figures:**
> *   The elderly, bearded man is **Abraham**. He is shown with a knife in his hand, ready to sacrifice his son as a test of his faith in God. His expression is one of intense emotion and shock as he looks up.
> *   The blindfolded youth lying on the altar is **Isaac**, Abraham's son.
> *   The figure with wings appearing from the upper left is an **Angel of the Lord**. The angel is intervening at the last moment, stopping Abraham's hand and indicating that the sacrifice is not to be completed.
> 
> In the lower-left corner, the head of a **ram** is partially visible, which, according to the biblical narrative, was provided by God as a substitute for the sacrifice of Isaac.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:46:43+00:00_

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

> The sacrifice of Isaac (Abraham and Isaac)

