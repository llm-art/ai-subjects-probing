# Probe report — `finding-moses`

[![finding-moses](https://hertz-foto-os1.biblhertz.it/iiif/3/bhex-si-2018-30-074/full/!800,800/0/default.jpg)](https://hertz-foto-os1.biblhertz.it/iiif/3/bhex-si-2018-30-074/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://hertz-foto-os1.biblhertz.it/iiif/3/bhex-si-2018-30-074/info.json)_

- **Ground-truth subject:** The finding of Moses: Pharaoh's daughter comes to bathe with her maidens in the river and discovers the child floating on the water
- **Category:** old_testament
- **Institution:** hertziana
- **Image:** `data/images/finding-moses.jpg` — native 7176×5659 px, sent 2048×1615 px
- **SHA-256:** `2129dfa70d63a10556ccf38ee3f35dd069a7befc03a6ed07c91a51beb150b3c2`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:44:43+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": false,
>   "artist": "Unknown",
>   "title": "The Finding of Moses",
>   "date": "17th century",
>   "collection": "Unknown"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:46:09+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and common art historical themes, this painting depicts the biblical story of **the Finding of Moses**.
> 
> Here is a detailed description of the scene:
> 
> *   **Central Subject:** The narrative comes from the Book of Exodus, where the Pharaoh of Egypt orders all newborn Hebrew boys to be killed. A Hebrew woman places her infant son, Moses, in a basket and sets him adrift on the Nile River to save him. The Pharaoh's daughter comes to the river to bathe and discovers the baby.
> 
> *   **Key Figures:**
>     *   **Pharaoh's Daughter:** The central, standing figure is depicted as a noble or royal woman. She is the focal point, illuminated by a strong light. She wears an elegant white and gold gown with a flowing orange-gold mantle and a crown or diadem on her head, signifying her high status. Her expression is one of calm compassion as she looks down towards the infant.
>     *   **The Infant Moses:** In the lower right, a group of women attend to a newborn baby, who is Moses. He is wrapped in a white cloth and is being presented to or examined by the women.
>     *   **Handmaidens and Attendants:** The Pharaoh's daughter is surrounded by her attendants. The women on the right are clustered around the baby, their expressions showing tenderness and surprise. On the left, a woman kneels in a pose of supplication or reverence, looking up at the royal figure. This kneeling woman could represent Miriam, Moses's sister, who watched from a distance and then offered to find a Hebrew nurse (Moses's own mother) for the child.
> 
> *   **Setting and Atmosphere:**
>     *   The scene is set outdoors, likely on the banks of a river, though the water itself is not clearly visible.
>     *   The background features a dramatic landscape with classical-style architecture, including towers, a round building, and a bridge. This is typical of historical or biblical paintings from the Baroque period, which often used classical ruins to evoke a sense of the ancient past.
>     *   The lighting is dramatic, with a strong contrast between light and shadow (chiaroscuro). The sky is dark and moody, suggesting either dawn or dusk, which adds to the theatricality of the moment of discovery.
> 
> *   **Artistic Style:**
>     The painting is in a style characteristic of the Baroque period, likely from the 17th or 18th century. This is evident in the dynamic composition, the dramatic use of light, the rich but somber color palette, and the emotional expressions of the figures. The surface of the painting shows significant craquelure, indicating its age.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:46:28+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and common subjects in European art history, this painting depicts the biblical episode of **The Finding of Moses**.
> 
> Here is a breakdown of the scene and the figures:
> 
> *   **The Subject:** The scene is from the Old Testament, specifically the Book of Exodus (Chapter 2). To save her infant son from the Pharaoh's decree that all newborn Hebrew boys be killed, Jochebed places him in a basket and sets him afloat on the Nile River. The baby is discovered by the Pharaoh's daughter, who has come to the river to bathe with her attendants.
> 
> *   **The Figures:**
>     *   **Pharaoh's Daughter:** The central, standing figure is the Egyptian princess. Her royal status is indicated by her elegant gown, the golden-orange mantle, and the crown or diadem on her head. She looks down with a compassionate expression.
>     *   **The Infant Moses:** The baby, held by one of the women on the right, is the infant Moses. He has just been taken from the river.
>     *   **Handmaidens/Attendants:** The women surrounding the princess and the baby are her attendants who accompanied her to the river. They show a mixture of curiosity, concern, and tenderness towards the child.
>     *   **Miriam (possibly):** The kneeling woman on the left, looking up pleadingly or gratefully at the princess, could be interpreted as Miriam, Moses's sister, who was watching from a distance to see what would happen to her brother. In the biblical account, she steps forward to offer to find a Hebrew nurse for the baby (who is, in fact, the baby's own mother).
> 
> The setting, with a river and classical-style architecture in the background, is a typical European artistic convention for representing ancient Egypt. The dramatic, dark lighting (chiaroscuro) and the emotional composition are characteristic of the Baroque period.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:46:46+00:00_

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

_Run: 2026-06-18T13:48:55+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Giovanni Francesco Romanelli",
>   "title": "The Finding of Moses",
>   "date": "17th century",
>   "collection": "Galleria Nazionale d'Arte Antica, Rome"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:11:05+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This painting depicts the biblical scene of **The Finding of Moses** (also known as *Moses Saved from the Water*), from the Book of Exodus. 
> 
> Key elements shown in the image include:
> 
> * **Pharaoh's Daughter:** The central, prominent figure dressed in royal attire, wearing a crown with a white feather and a yellow-orange mantle. She is gesturing toward the baby.
> * **Baby Moses:** Located on the right side, the infant is lying in a basket/cradle on the riverbank, surrounded and tended to by the princess's handmaidens.
> * **Miriam (Moses' sister):** The woman kneeling on the left, looking up at Pharaoh's daughter. In the biblical narrative, she approaches the princess to suggest hiring a Hebrew nurse (who would be Moses' biological mother, Jochebed) to care for the baby.
> * **The Setting:** A riverbank (representing the Nile) with classical-style architecture, a bridge, and a tall column in the background, characteristic of 17th-century European depictions of historical and biblical scenes.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:11:12+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual elements, this painting depicts the biblical scene of **The Finding of Moses** (also known as *Moses Saved from the Water*), from the Book of Exodus. 
> 
> The key figures depicted in the scene are:
> * **Pharaoh's Daughter:** The central, elegantly dressed royal figure wearing a crown/tiara with a feather, who has discovered the child.
> * **The Infant Moses:** The baby lying in the basket/cradle on the right, being tended to by the princess's handmaidens.
> * **Miriam (Moses' sister):** The young woman kneeling on the left, gesturing as she speaks to Pharaoh's daughter, offering to find a Hebrew nurse (their mother, Jochebed) to care for the baby.
> * **The Handmaidens:** The other women on the right who have retrieved the basket from the River Nile (visible in the background).

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:11:27+00:00_

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

