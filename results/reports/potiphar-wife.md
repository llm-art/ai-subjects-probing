# Probe report — `potiphar-wife`

[![potiphar-wife](https://hertz-foto-os1.biblhertz.it/iiif/3/bh001666/full/!800,800/0/default.jpg)](https://hertz-foto-os1.biblhertz.it/iiif/3/bh001666/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://hertz-foto-os1.biblhertz.it/iiif/3/bh001666/info.json)_

- **Ground-truth subject:** Potiphar's wife catches Joseph by his robe; Joseph escapes leaving his cloak behind
- **Category:** old_testament
- **Institution:** hertziana
- **Image:** `data/images/potiphar-wife.jpg` — native 7367×5774 px, sent 2048×1605 px
- **SHA-256:** `54faa31ad2a61ac0b48c690ff31acad94a5e8a5b299802913d5e696a8d32e76c`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:46:50+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the information visible in the image, this is a photograph of a painting. Here are the details:
> 
> *   **Artist:** Giovanni Biliverti. The printed text misspells the name as "Belivart," but a handwritten correction below it reads "Biliverti."
> *   **Title:** *La castità di Giuseppe* (The Chastity of Joseph). This title refers to the biblical story of Joseph and Potiphar's wife from the Book of Genesis.
> *   **Approximate Date:** Giovanni Biliverti was active in the first half of the 17th century, so the painting dates to that period.
> *   **Collection:** At the time the photograph was taken, the painting was in the Galleria Barberini in Rome (now part of the Gallerie Nazionali di Arte Antica).
> 
> The photograph itself was taken by Anderson and is part of the collection of the Bibliotheca Hertziana - Max Planck Institute.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:47:06+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual information in the image and my internal knowledge, this is a photograph of a Baroque painting.
> 
> **The Subject of the Painting:**
> 
> The painting depicts the biblical story of **Joseph and Potiphar's Wife** from the Book of Genesis. The title is provided in Italian at the bottom of the photograph: **"La castità di Giuseppe,"** which translates to "The Chastity of Joseph."
> 
> In the scene:
> *   **Potiphar's wife**, seated on an opulent bed, is attempting to seduce **Joseph**. She is grabbing his arm and hand, trying to pull him towards her.
> *   **Joseph** is actively resisting her advances. His body is turned away from her, and he is trying to pull free. His upward gaze suggests an appeal to heaven or a demonstration of his piety and resolve to remain chaste.
> *   The setting is luxurious, with rich, patterned drapery over the bed and a small table with a string of pearls, befitting the home of Potiphar, a high-ranking Egyptian official.
> 
> **Information from the Inscriptions:**
> 
> The text on the cardboard mount provides specific details about the artwork and the photograph:
> 
> *   **Title:** "La castità di Giuseppe" (The Chastity of Joseph)
> *   **Artist:** The printed name is "Belivart," but it has been corrected by hand to **"Biliverti."** This refers to the Florentine Baroque painter **Giovanni Bilivert** (c. 1585–1644).
> *   **Location:** "Gall. Barberini" indicates the painting was located in the **Galleria Barberini** (Barberini Gallery) in **Rome** ("ROMA").
> *   **Photographer:** "Anderson" refers to the 19th-century photographer **James Anderson**, who was known for his photographic documentation of art in Italy.
> *   **Numbers:** "721" and "600" are likely inventory or catalog numbers for the photograph.
> 
> In summary, the image is a 19th-century photograph by Anderson of the painting "The Chastity of Joseph" by Giovanni Bilivert, located in the Barberini Gallery in Rome.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:47:24+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts the biblical episode of **Joseph and Potiphar's Wife**.
> 
> The scene shows the dramatic climax of the story from the Book of Genesis (39:7-12). The figures are:
> 
> *   **Joseph:** The young man on the right, who is resisting and attempting to flee.
> *   **Potiphar's Wife:** The woman on the bed, who is trying to seduce Joseph by grabbing his arm and his outer garment.
> 
> The painting captures the moment Joseph chooses to maintain his virtue by fleeing from her advances, leaving his cloak behind in her hands. The title printed at the bottom of the photograph, "La castità di Giuseppe" (Italian for "The Chastity of Joseph"), confirms this identification.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:47:40+00:00_

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

> Potiphar's wife catches Joseph by his robe; Joseph escapes

