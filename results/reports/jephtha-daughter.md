# Probe report — `jephtha-daughter`

[![jephtha-daughter](https://media.rkd.nl/iiif/2/9229920/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9229920/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9229920/info.json)_

- **Ground-truth subject:** Jephtha welcomed by his daughter (Judges 11:29-40)
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/jephtha-daughter.jpg` — native 5782×4204 px, sent 2048×1489 px
- **SHA-256:** `e0aebb74bd3833b3eb56f4e25031f89d58e4b3693b7e4f18903cf5442444eaa1`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:49:12+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this artwork is:
> 
> **Artist:** Attributed to the **Circle of Frans Francken the Younger** (c. 1581–1642).
> 
> **Title:** ***The Return of Jephthah*** or ***Jephthah and His Daughter***.
> 
> **Approximate Date:** First half of the 17th century.
> 
> **Collection:** This work has appeared at auction and is likely in a private collection.
> 
> The painting depicts a dramatic and tragic scene from the Old Testament (Book of Judges, Chapter 11). The Israelite judge Jephthah, returning victorious from battle, is met by his only daughter, who comes out to greet him with music (playing a tambourine) and dancing.
> 
> The central tragedy of the scene, which the artist captures, is Jephthah's reaction. Before the battle, he had made a rash vow to God to sacrifice the first thing that came out of his house to greet him upon his return. The painting shows the precise moment of horror and anguish on Jephthah's face as he realizes the terrible consequence of his vow, contrasting sharply with the joyous celebration of his daughter and her companions. His soldiers look on from the right, while the city from which the women emerged is visible in the background. The dark, tumultuous sky enhances the dramatic and somber mood of the event.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:49:32+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual elements in the image and my internal knowledge of art history and biblical narratives, this painting depicts the Old Testament story of **Jephthah's Vow**.
> 
> Here is a breakdown of the scene:
> 
> *   **The Central Figure:** The man in the center, dressed in armor with a flowing red cape and a turban-like helmet, is **Jephthah**, a judge of Israel. He has just returned victorious from a battle against the Ammonites. His expression is one of horror and anguish, and he clutches his chest in despair.
> *   **The Young Woman:** The woman at the left, stepping forward joyfully while playing a tambourine, is **Jephthah's daughter**. She is his only child and is coming out to celebrate her father's triumphant return, unaware of the tragedy about to unfold.
> *   **The Narrative:** Before the battle, Jephthah made a rash vow to God, promising that if he were granted victory, he would sacrifice whatever first came out of the door of his house to greet him upon his return. The painting captures the dramatic and terrible moment when Jephthah sees his beloved daughter is the first to greet him, meaning he is bound by his vow to sacrifice her.
> *   **The Supporting Figures:** To the left are the daughter's female companions, also celebrating with music and dance. To the right are Jephthah's soldiers on horseback and on foot, carrying spears and banners, representing his victorious army.
> *   **The Atmosphere:** The dark, stormy sky and the dramatic lighting (chiaroscuro) heighten the sense of tragedy and doom, contrasting sharply with the celebratory actions of the women. The artist uses this contrast to emphasize the emotional climax of the story.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:49:48+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge, this painting depicts a dramatic and tragic episode from the Old Testament.
> 
> **Scene:** The Return of Jephthah.
> 
> **Figures and Episode:**
> 
> The central figure in the red cloak and armor is **Jephthah**, a judge and military leader of Israel. He is shown returning victorious from battle with his soldiers, who are visible behind him on horseback with spears and banners.
> 
> The young woman in the foreground playing a tambourine (or timbrel) is **Jephthah's daughter**, his only child. She has come out from the city with other women to celebrate her father's victory with music and dancing.
> 
> The painting captures the moment of tragic realization. Before going into battle against the Ammonites, Jephthah made a rash vow to God (Judges 11:30-31): if God granted him victory, he would sacrifice whatever came out of the doors of his house to meet him upon his return.
> 
> The artist has depicted the precise moment Jephthah sees his beloved daughter emerging as the first to greet him. Instead of the joy of a returning hero, his face is a mask of anguish and despair. His dramatic gesture of clutching his cloak signifies his grief and the biblical act of rending one's garments. The dark, stormy sky overhead reinforces the tragic and fateful nature of the scene, contrasting sharply with the joyful celebration of the women.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:50:05+00:00_

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

> Jephtha welcomed by his daughter (Judges 11:29-40)

