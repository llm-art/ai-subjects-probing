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

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:22+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Giovanni Battista Tiepolo",
>   "title": "The Adoration of the Magi",
>   "date": "ca. 1753",
>   "collection": "The Metropolitan Museum of Art"
> }
> ```

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

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:51:58+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Giovanni Battista Tiepolo",
>   "title": "The Presentation in the Temple",
>   "date": "c. 1735-1740",
>   "collection": "Gemäldegalerie Alte Meister, Dresden"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:20:37+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the composition, figures, and style, this image depicts the biblical scene of **Hannah Presenting her Son Samuel to the High Priest Eli** (from the First Book of Samuel). 
> 
> ### Key Elements Depicted:
> * **Hannah:** The central female figure dressed in elegant, flowing light-colored robes, presenting her young son.
> * **Samuel:** The young, nude child standing on the draped table in the center.
> * **Eli:** The elderly, bearded high priest seated on the right in rich, dark robes, looking thoughtfully at the child.
> * **Supporting Figures:** A young page kneeling on the far left, a female attendant standing behind Hannah, and spectators visible in the background.
> * **Setting:** A grand, theatrical architectural setting typical of 18th-century Venetian painting, featuring classical columns, an archway, an upper balustrade, and a checkered tiled floor.
> 
> This composition is highly characteristic of the Venetian Rococo master **Giovanni Battista Tiepolo** (or his circle/workshop), who frequently painted biblical and historical scenes with this dramatic, grand-scale theatricality.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:20:46+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the rare Old Testament/apocryphal episode of **The Infant Moses Trampling on Pharaoh's Crown** (also known as *Moses and the Crown of Pharaoh*), painted by the Italian Rococo master **Giovanni Battista Tiepolo** (Giambattista Tiepolo) around 1730–1735.
> 
> ### **The Scene and Figures:**
> * **The Infant Moses:** The young, naked child standing on the table.
> * **Pharaoh’s Daughter (Thermutis/Bithiah):** The elegantly dressed woman in the center who has brought Moses to the court.
> * **Pharaoh:** The bearded, turbaned ruler seated on the right, looking on with concern and surprise.
> * **Attendants and Counselors:** A page boy on the far left and court advisors in the background.
> 
> ### **The Story:**
> The subject comes from historical and midrashic accounts of Moses's childhood (notably recorded by the Jewish historian Flavius Josephus in *Antiquities of the Jews*). According to the legend, Pharaoh's daughter brought the young Moses to her father. When Pharaoh playfully placed his royal crown on the child's head, the infant Moses grabbed the crown, threw it to the ground, and trampled on it. 
> 
> This act was interpreted by Pharaoh's priests and counselors as a dangerous omen foretelling that the child would one day overthrow the king's power, leading them to demand his execution (which led to the subsequent test of the burning coals).

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:20:59+00:00_

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

