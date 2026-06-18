# Probe report — `tobit-tobias`

[![tobit-tobias](https://iiif.artresearch.net/iiif/3/frick/4107100295918_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100295918_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100295918_0001.jp2/info.json)_

- **Ground-truth subject:** Tobit Blessing Tobias
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/tobit-tobias.jpg` — native 5783×4315 px, sent 2048×1528 px
- **SHA-256:** `52e700fb7082460e74fecc0ff76e90599516d356f54e37eba6345182584d745b`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:08:04+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the style and subject matter visible in the image, I can identify this artwork.
> 
> This is a black and white photograph of the painting:
> 
> *   **Artist:** Mattia Preti
> *   **Title:** *Tobias Healing His Father* (or *The Healing of Tobit*)
> *   **Approximate Date:** c. 1656-1659
> *   **Collection:** Musée du Louvre, Paris
> 
> The painting depicts a scene from the biblical Book of Tobit. The young Tobias, guided by the Archangel Raphael (the figure with wings), anoints the eyes of his blind father, Tobit, with the gall of a fish to restore his sight. Tobit's wife, Anna, looks on. The style is characteristic of Mattia Preti, a prominent Italian Baroque painter who was heavily influenced by Caravaggio, as seen in the dramatic use of light and shadow (tenebrism) and the realistic depiction of the figures.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:08:25+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual elements in the image and common subjects in art history, this black and white photograph shows a painting depicting a scene from the **Book of Tobit**, a story from the Old Testament Apocrypha.
> 
> The scene most likely portrays **Tobias Taking Leave of His Father, Tobit**.
> 
> Here is a breakdown of the figures and the narrative:
> 
> *   **Tobit:** The elderly, bearded man seated on the left, wearing a turban. He is blind, and he is shown giving a blessing to his son, with his hand extended over the boy's head.
> *   **Tobias:** The young boy in the center, who is about to embark on a long journey. He looks up towards his father to receive the blessing.
> *   **The Archangel Raphael:** The figure on the right with prominent wings. In the story, Raphael accompanies Tobias on his journey, disguised as a human guide. Here, the artist has chosen to reveal his angelic nature to the viewer. He gently guides or presents Tobias.
> *   **Anna:** The older woman in the background is Tobias's mother, Anna. Her expression is one of sorrow and concern for her son's departure.
> 
> The painting is executed in a dramatic, Baroque style, characterized by **chiaroscuro**—strong contrasts between light and dark. The light source, coming from the left, illuminates the key figures and their emotional expressions, while plunging the background into deep shadow. This technique heightens the emotional intensity and solemnity of the moment of farewell and blessing.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:08:41+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge of art history and religious iconography, this painting depicts a scene from the **Book of Tobit**, which is part of the Catholic and Orthodox Old Testament.
> 
> The specific episode is most likely **The Angel Raphael Taking Leave of Tobit and his Family**.
> 
> The figures can be identified as follows:
> 
> *   **Tobit:** The elderly, bearded man seated on the left, wearing a turban. He is the patriarch of the family. His hand is raised in a gesture of blessing or awe towards his son.
> *   **Tobias:** The young boy in the center, receiving the blessing from his father. He has just returned from a long journey.
> *   **The Archangel Raphael:** The figure with wings on the right. He accompanied Tobias on his journey disguised as a human named Azarias. Here, he has revealed his true angelic form before ascending to heaven. He gestures towards Tobias, presenting him safely back to his family.
> *   **Anna:** The older woman in the background. She is Tobit's wife and Tobias's mother, looking on with a somber and emotional expression.
> 
> The painting captures the dramatic and emotional climax of the story. The use of strong light and shadow (chiaroscuro) is characteristic of the Baroque period and heightens the sense of divine revelation and familial emotion.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:08:59+00:00_

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

