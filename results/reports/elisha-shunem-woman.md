# Probe report — `elisha-shunem-woman`

[![elisha-shunem-woman](https://iiif.artresearch.net/iiif/3/frick/4107100212912_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100212912_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100212912_0001.jp2/info.json)_

- **Ground-truth subject:** The Prophet Elisha and the Rich Woman of Shunem
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/elisha-shunem-woman.jpg` — native 4611×6050 px, sent 1561×2048 px
- **SHA-256:** `76857cc0e3706937198dc3f37ab59cb492951b571b4502e2bdeddfb3872be5fc`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:39+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Gaspard Dughet",
>   "title": "Landscape with Elijah and the Angel",
>   "date": "c. 1650-1660",
>   "collection": "The National Gallery, London"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:09:30+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual information in the image and general art historical knowledge, here is a description of what is depicted:
> 
> This is a black and white photograph of a painting, likely from the Baroque period, depicting a narrative scene set within a vast and dramatic landscape.
> 
> **The Figures:**
> In the lower-left foreground, there are three figures:
> *   An elderly, bearded man is seated on a rock or the ground. He is dressed in robes, with a light-colored cloth draped over his lap and a darker garment on his upper body. He is looking up towards the woman, with one hand resting on his knee and the other slightly raised as if in conversation.
> *   A woman stands and leans towards the seated man. She is also wearing classical-style robes and appears to be offering him something or speaking to him intently.
> *   A small, young child stands beside the woman, holding onto her hand or garment. The child is clad in a simple, light-colored tunic.
> 
> **The Setting:**
> The figures are situated in a dark, wooded area. The landscape dominates the composition:
> *   The foreground and midground are filled with dense, dark trees, rocks, and foliage, creating a sense of enclosure and shadow. A small waterfall or stream appears to be flowing from the rocks behind the figures.
> *   The trees frame a view into a distant, brighter landscape. In this background, one can see a body of water, rolling hills, and mountains under a cloudy sky.
> *   The painting uses strong contrast between light and shadow (chiaroscuro). The figures are illuminated, drawing the viewer's eye, while the surrounding forest is deep in shadow. This dramatic lighting enhances the emotional and narrative quality of the scene.
> 
> **Interpretation of the Subject:**
> The iconography—an elderly, prophetic-looking man in the wilderness being attended to by a woman and child—strongly suggests a biblical story. A very likely subject is **Elijah and the Widow of Zarephath** from the Old Testament (1 Kings 17:8-16). In this story, the prophet Elijah, hiding during a famine, meets a poor widow and her son and asks them for food and water. Despite having only enough for one last meal, she shares it with him, and in return, God miraculously ensures her flour and oil never run out. The scene captures the moment of their interaction in the wilderness.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:09:51+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of European art history and religious iconography, this painting depicts a biblical scene.
> 
> **Episode:** The **Rest on the Flight into Egypt**.
> 
> **Figures:**
> *   The elderly, bearded man seated on the rock is **Saint Joseph**.
> *   The standing woman is the **Virgin Mary**.
> *   The small child holding Mary's hand is the infant **Jesus Christ**.
> 
> This scene illustrates an episode from the Gospel of Matthew (2:13-15), where an angel warns Joseph to take Mary and Jesus and flee to Egypt to escape King Herod's order to kill all male infants in Bethlehem. The "Rest on the Flight" is a popular subject in Christian art, depicting the Holy Family pausing on their arduous journey. The vast, dark, and wild landscape emphasizes their vulnerability and the difficulty of their travel, while the tender interaction between the figures provides a moment of quiet humanity and divine grace amidst the hardship.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:10:14+00:00_

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

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:52:21+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Francisque Millet",
>   "title": "Landscape with Elijah and the Widow of Zarephath",
>   "date": "c. 1670-1679",
>   "collection": "National Gallery, London"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:22:18+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This image depicts the painting ***Landscape with Elijah and the Widow of Zarephath*** by the French-Italian Baroque landscape painter **Gaspard Dughet** (also known as Gaspard Poussin), created around 1660–1665. 
> 
> ### Subject and Details:
> * **The Biblical Story:** The scene illustrates a passage from the Old Testament (1 Kings 17). The prophet **Elijah** (depicted as the seated, bearded elderly man on the right) meets the **widow of Zarephath** (standing on the left) and her young son in the wilderness during a drought.
> * **Setting:** The figures are placed in a classical, dramatic landscape characteristic of Dughet's style, featuring dense, dark foliage, a small stream/waterfall behind the figures, and a distant mountain visible through a clearing in the trees on the right.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:22:33+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the composition and details of this 17th-century classical landscape painting (highly characteristic of the French-Italian painter **Gaspard Dughet**), the scene depicted is:
> 
> ### **Subject / Episode**
> * **Elijah and the Widow of Zarephath** (from the Old Testament, 1 Kings 17:8–16). 
> 
> ### **Figures Depicted**
> 1. **Elijah** – The bearded prophet seated on the right, gesturing as he asks the widow for water and a piece of bread during a drought.
> 2. **The Widow of Zarephath** – The woman standing on the left, who is gathering sticks to prepare a final meal for herself and her son before they starve.
> 3. **The Widow's Son** – The young child standing on the far left, holding his mother's hand.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:22:44+00:00_

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

