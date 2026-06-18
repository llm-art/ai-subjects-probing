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

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:02:56+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, I can identify this artwork.
> 
> **Artist:** Hendrick Bloemaert
> **Title:** *Lot and His Daughters*
> **Approximate Date:** c. 1630
> **Collection:** The Cleveland Museum of Art
> 
> This painting depicts the biblical story from the Book of Genesis. After fleeing the destruction of Sodom, which is visible as a burning city in the background, Lot and his two daughters take refuge in a cave. Believing they are the last people on earth, his daughters conspire to get him drunk on wine so they can sleep with him and preserve their family line. The image captures the moment one daughter pours wine while the other encourages her, as Lot, unaware of their intentions, drinks from a cup.

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

