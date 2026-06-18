# Probe report — `lot-daughters`

[![lot-daughters](https://iiif.artresearch.net/iiif/3/frick/4107100322001_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100322001_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100322001_0001.jp2/info.json)_

- **Ground-truth subject:** Lot and His Daughters
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/lot-daughters.jpg` — native 4743×3655 px, sent 2048×1578 px
- **SHA-256:** `f49d469b2c7a70cef7ec176810d5a9132491755fd064fa02bd7d80d2dea3e8c3`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:46:29+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Guido Reni",
>   "title": "Lot and His Daughters",
>   "date": "c. 1615-1616",
>   "collection": "National Gallery, London"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:05:27+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of common subjects in Western art, this painting depicts the biblical story of **Lot and his daughters**.
> 
> Here is a breakdown of the scene and its elements:
> 
> *   **The Figures:** The three main figures are an older, bearded man (Lot) and two younger women (his daughters).
> *   **The Action:** Lot is shown drinking wine from a cup or shell. His daughters are attending to him; one has her arm around the other and is pointing towards Lot, while the other holds a pitcher, ready to pour more wine. The partial nudity of one of the daughters is a key element, alluding to the seductive and incestuous nature of the event.
> *   **The Setting:** In the background, a city is engulfed in flames. This represents the destruction of Sodom and Gomorrah, from which Lot and his family have just fled. They appear to have taken refuge in a desolate, rocky area, consistent with the biblical account of them hiding in a cave in the mountains.
> 
> **The Story:**
> According to the Book of Genesis (Chapter 19), after God destroyed Sodom and Gomorrah, Lot and his two daughters were the sole survivors of their family (his wife having been turned into a pillar of salt). Believing they were the last people on Earth, the daughters decided to ensure the continuation of their family line by having children with their father. To achieve this, they conspired to get him drunk on two consecutive nights so that he would not be aware of their actions.
> 
> This painting captures the moment the daughters begin to ply their father with wine, initiating their plan. The scene is a popular subject in art, particularly during the Renaissance and Baroque periods, as it allowed artists to combine a dramatic biblical narrative with the depiction of the human form and complex emotional states.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:03:31+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts the biblical episode of **Lot and his daughters**.
> 
> Here is a breakdown of the scene and figures:
> 
> *   **The Episode:** This story comes from the Book of Genesis (Chapter 19). After fleeing the destruction of the cities of Sodom and Gomorrah, Lot and his two daughters take refuge in a cave. Believing they are the last people on Earth, the daughters decide to preserve their family line by intoxicating their father with wine and then sleeping with him.
> 
> *   **The Figures:**
>     *   **Lot:** The older, bearded man on the right, wearing a turban, is Lot. He is shown drinking wine from a cup, becoming intoxicated and unaware of his daughters' intentions.
>     *   **Lot's Daughters:** The two younger women on the left are his daughters. One daughter is actively pouring wine from a pitcher, while the other has her arm around her sister, seemingly encouraging her or conspiring with her. Their partial nudity and suggestive poses allude to the incestuous nature of their plan.
> 
> *   **Key Visual Clues:**
>     *   The act of the daughters giving their father wine is central to the narrative.
>     *   In the background, between the figures, you can see the city of Sodom in flames, signifying the divine judgment from which they have just escaped.
>     *   The setting appears to be a desolate, rocky landscape, consistent with the story of them taking refuge outside the city.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:03:47+00:00_

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

_Run: 2026-06-18T13:50:56+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Guercino (Giovanni Francesco Barbieri)",
>   "title": "Lot and his Daughters",
>   "date": "1650",
>   "collection": "Musée du Louvre, Paris"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:16:48+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this image depicts the biblical story of **Lot and his daughters** (from the Book of Genesis). 
> 
> Key elements of the scene include:
> * **Lot:** The bearded older man on the right wearing a turban, shown drinking wine from a cup.
> * **His Daughters:** The two young women on the left who are getting him drunk. One is partially undressed and gesturing, while the other stands behind her holding a large wine jug. Another vessel sits on the ground near them.
> * **The Burning City:** In the background, the city of Sodom is shown engulfed in flames and smoke.
> * **Lot's Wife:** In the middle distance between the figures, a small white silhouette represents Lot's wife, who was turned into a pillar of salt for looking back at the burning city. 
> 
> This is a grayscale photograph of a Baroque-style painting depicting this classic Old Testament narrative.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:16:55+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual details, this painting depicts the biblical story of **Lot and his Daughters** (from the Book of Genesis, Chapter 19). 
> 
> ### Key Figures and Scene Details:
> * **Lot:** The bearded man on the right wearing a turban, who is being made drunk with wine.
> * **Lot's Daughters:** The two young women on the left who are serving him wine from the urns to intoxicate him.
> * **The Background:** In the distance, the city of **Sodom** is shown burning in flames. Between the foreground figures and the burning city, a small white silhouette can be seen representing **Lot's wife**, who was turned into a pillar of salt for looking back at the destruction.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:17:00+00:00_

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

> Lot and his daughters

