# Probe report — `moses-crown-pharaoh`

[![moses-crown-pharaoh](https://iiif.artresearch.net/iiif/3/frick/4107100398385_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100398385_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100398385_0001.jp2/info.json)_

- **Ground-truth subject:** The Child Moses Trampling on the Crown of the Pharaohs
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/moses-crown-pharaoh.jpg` — native 4134×5472 px, sent 1547×2048 px
- **SHA-256:** `e24db00db85900034cff258f17a0eb99b009227446935fd5e54d6e628d4c6a05`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:07:01+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the style and subject matter visible in the image, this is a well-known artwork.
> 
> **Artist:** Giovanni Battista Tiepolo
> **Title:** *The Presentation of Christ in the Temple*
> **Approximate Date:** ca. 1754–55
> **Collection:** The Metropolitan Museum of Art, New York
> 
> This monochrome oil sketch, executed in a technique known as grisaille, is a preparatory model (*modello*) for a large altarpiece. The scene depicts the biblical event from the Gospel of Luke where Mary and Joseph present the infant Jesus at the Temple in Jerusalem. The central figures are the Virgin Mary holding the Christ Child, who is being presented to the aged high priest Simeon. The dramatic use of light and shadow (chiaroscuro), the dynamic composition, and the elegant, expressive figures are all characteristic of Tiepolo's mature style.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:07:20+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual information in the image and general art historical knowledge, here is a description of what is depicted:
> 
> This is a monochrome painting, likely a grisaille (a work executed entirely in shades of grey) or an oil sketch, depicting a dramatic narrative scene set within a grand architectural interior. The style is characteristic of the Baroque period, marked by its dynamic composition, strong contrasts between light and shadow (chiaroscuro), and emotional intensity.
> 
> **The Central Scene:**
> The focal point is the interaction between three main figures in the center-left of the composition.
> *   A richly dressed woman, possibly of noble or royal status, stands in a brightly lit area. She wears an elegant gown with a high, dark collar.
> *   She is presenting a nude infant or toddler, who is standing on a draped table or altar-like structure. The child looks back towards the woman.
> *   To the right, a seated, elderly, bearded man with a turban or headdress looks up at the woman and child. His voluminous, possibly fur-lined robes and authoritative posture suggest he is a person of high rank, such as a priest, king, or sage.
> 
> **Setting and Supporting Figures:**
> The event takes place in a large hall with classical architecture, including massive columns, arches, and a balustraded balcony in the upper left background where other figures are observing the scene. The floor is made of large, checkered tiles, which creates a sense of depth and perspective.
> 
> Several other figures surround the central group, acting as witnesses:
> *   To the far left, a younger figure, perhaps a page or attendant, looks on.
> *   Behind the main female figure, another attendant is partially visible.
> *   In the shadowy background to the right, more onlookers are gathered.
> 
> **Interpretation of the Subject:**
> The iconography strongly suggests a well-known biblical scene: **The Presentation of Jesus in the Temple**.
> *   The woman would be the Virgin Mary.
> *   The infant is Jesus.
> *   The elderly man is Simeon, the devout man who, according to the Gospel of Luke, was promised he would not die until he had seen the Messiah.
> 
> In this interpretation, Mary and Joseph (who might be one of the figures in the background) have brought the infant Jesus to the Temple in Jerusalem for the customary rites, where they are met by Simeon, who recognizes the child as the savior. The grand setting represents the temple, and the onlookers emphasize the significance of the event.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:07:42+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of common subjects in European art, this painting depicts a biblical scene: **The Presentation of Jesus in the Temple**.
> 
> This episode is described in the Gospel of Luke (2:22–40). According to the narrative, Mary and Joseph took the infant Jesus to the Temple in Jerusalem forty days after his birth to consecrate him to the Lord, as was the Jewish custom for a firstborn son. There, they encountered two devout elderly people, Simeon and Anna, who recognized the baby as the Messiah.
> 
> The figures in the painting can be identified as:
> 
> *   **The Virgin Mary:** The elegantly dressed woman at the center, presenting her child.
> *   **The Infant Jesus:** The baby standing on the draped altar or table.
> *   **Simeon:** The elderly, bearded man seated on the right. He is often depicted as a high priest. His reverent posture and upward gaze suggest he is in the act of recognizing Jesus's divinity and uttering his prophecy, known as the *Nunc dimittis*.
> 
> Other figures surrounding the central group are likely **Joseph** (perhaps the man partially visible behind Mary), the prophetess **Anna**, and other temple attendants or onlookers.
> 
> The setting, with its grand arches, columns, and a balustrade in the background, represents the Temple of Jerusalem. The dramatic use of light and shadow (chiaroscuro) and the dynamic composition are characteristic of the Baroque style. The painting is a grisaille, meaning it is executed entirely in shades of grey or another neutral color, which was often used for preparatory studies or as a finished work imitating sculpture.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:08:02+00:00_

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

> The finding of Moses: Pharaoh's daughter discovers the child floating on the river

