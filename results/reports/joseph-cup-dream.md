# Probe report — `joseph-cup-dream`

[![joseph-cup-dream](https://iiif.artresearch.net/iiif/3/frick/57196_POST.tif/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/57196_POST.tif/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/57196_POST.tif/info.json)_

- **Ground-truth subject:** Two Scenes in the Life of Joseph: The Discovery of Joseph's Cup in Benjamin's Sack and Joseph Interpreting Pharaoh's Dream
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/joseph-cup-dream.jpg` — native 8401×6568 px, sent 2048×1601 px
- **SHA-256:** `0ad60d113f2553657ea10150703b684214bfa7e12f4d0acb0474479c9ee45147`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:03:33+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a well-known painting.
> 
> **Artist:** Jan Tengnagel
> **Title:** *The discovery of the silver cup in Benjamin's sack* (or *Joseph's Silver Cup is Found in Benjamin's Sack*)
> **Date:** 1618
> **Collection:** Rijksmuseum, Amsterdam
> 
> The painting depicts a dramatic scene from the biblical story of Joseph in the Book of Genesis (Genesis 44:1-13). Joseph, now a powerful vizier in Egypt, tests his brothers who have come to buy grain. He secretly has his personal silver cup placed in the sack of his youngest brother, Benjamin. As the brothers depart, Joseph's steward overtakes them and accuses them of theft. The painting captures the moment the cup is discovered in Benjamin's sack, showing the shock, dismay, and anger of the brothers.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:03:49+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this is a black-and-white reproduction of a painting depicting a dramatic biblical scene.
> 
> The image portrays the story of **Joseph and his brothers** from the Book of Genesis, specifically the moment when Joseph's silver cup is "found" in his brother Benjamin's sack of grain.
> 
> Here is a breakdown of the scene:
> 
> *   **Central Action:** A man, stripped to the waist, is kneeling by a large, open sack filled with grain. He is holding up an ornate, silver-colored cup that he has just pulled from the sack. His expression is one of anguish or distress as he looks towards the man on the left.
> *   **The Brothers:** Surrounding this central action is a group of men, Joseph's brothers, reacting with a mixture of shock, anger, and despair. The man to the left of the sack, wearing a white turban, looks down in disbelief with his hands open in a gesture of protest. Another brother behind him has a furious expression, his mouth open as if shouting and his hands raised in agitation.
> *   **The Accuser:** To the right stands a commanding figure, likely Joseph's steward or Joseph himself, dressed in a long robe with a large, elaborate turban. He points an accusatory finger towards the cup and the sack. His stance is authoritative, with one hand on his hip near the hilt of a weapon tucked into his sash, and his expression is stern and unwavering.
> *   **Setting and Atmosphere:** The scene is crowded and filled with tension. The presence of a donkey, partially visible behind the central figures, indicates that the brothers were on a journey. The artist uses dramatic lighting and expressive figures to convey the high emotional stakes of the moment—the false accusation of theft that Joseph has orchestrated to test his brothers. The clothing, such as the turbans and robes, is typical of how European artists of the Baroque or later periods would have imagined an ancient Near Eastern setting.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:04:08+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting, this is a depiction of a dramatic biblical scene from the Old Testament.
> 
> **Episode:** The discovery of Joseph's silver cup in Benjamin's sack of grain. This story is found in the Book of Genesis, chapter 44.
> 
> **Subject and Figures:**
> 
> The scene portrays the moment when Joseph's brothers, having bought grain in Egypt during a famine, are stopped on their journey home. Joseph, now a powerful Egyptian official unrecognized by his brothers, has secretly ordered his steward to place his personal silver cup into the sack of his youngest brother, Benjamin. This is a test to see if the brothers have changed and will stand by Benjamin, unlike how they betrayed Joseph years earlier.
> 
> *   **Joseph's Steward:** The prominent, well-dressed figure on the right, with the large turban and his hand on the hilt of a weapon, is most likely Joseph's steward. He is pointing accusingly, having "found" the cup as instructed.
> *   **Joseph's Brothers:** The other men are Joseph's brothers. Their expressions range from shock, anger, and despair to pleading innocence.
>     *   The central, muscular figure is likely the one whose sack is being searched (biblically, this would be **Benjamin**), shown in the act of discovering the cup with a look of horror.
>     *   The man to the left, in the white turban, looks down into the sack with dismay.
>     *   The man behind him, with an angry and contorted face, seems to be protesting vehemently.
> *   **The Silver Cup:** The ornate, shell-shaped cup is visible in the hands of the central figure, being pulled from the sack of grain.
> 
> The overall composition is filled with tension and high drama, capturing the climax of Joseph's test of his brothers' character. The donkey in the background reinforces the context of their journey.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:04:27+00:00_

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

> The Gathering of Manna

