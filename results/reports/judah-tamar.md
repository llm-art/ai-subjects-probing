# Probe report — `judah-tamar`

[![judah-tamar](https://media.rkd.nl/iiif/2/9682081/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9682081/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9682081/info.json)_

- **Ground-truth subject:** Judah's love-affair with Tamar; he gives her his signet-ring and staff
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/judah-tamar.jpg` — native 3308×2512 px, sent 2048×1555 px
- **SHA-256:** `04d3395baef034f078a8992394aeae99a47ccb084ba676d5e541055f5de0639e`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:37+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Jan van Scorel",
>   "title": "Vertumnus and Pomona",
>   "date": "c. 1524",
>   "collection": "Museum Boijmans Van Beuningen"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:49:49+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a detailed description of what is depicted:
> 
> This is a black and white photograph of a painting that portrays an intimate outdoor scene with two central figures: an older, bearded man and a young woman.
> 
> **The Figures and their Interaction:**
> 
> *   **The Man:** He is an elderly figure with a long, full beard and hair. He wears a leafy or fabric wreath on his head and is dressed in rustic, loose-fitting garments. One of his legs is bare from the knee down, while the other is covered. His left arm is placed gently around the young woman's shoulder. He is actively engaged in conversation, with his right hand raised in a gesture of speech or explanation. In his other hand, he holds up a ring on his little finger, seemingly presenting it or drawing attention to it. His expression is earnest as he looks toward the woman.
> *   **The Woman:** She is youthful and fair, with her hair styled in an elaborate updo. She is dressed in fine, fashionable attire of the period, likely the 16th century, featuring a fitted bodice with puffed sleeves, a full skirt with a decorative hem, and a delicate necklace. In contrast to the man's active posture, she is passive and contemplative. Her head is bowed, her gaze is directed downwards, and she holds a long, smooth staff or rod with both hands. Her expression appears somber or melancholic.
> 
> **The Setting:**
> 
> *   **Foreground:** The pair is seated on the ground under the shade of large trees. To the left, there is a lush vine, possibly a grapevine, climbing up. The immediate ground is earthy with some sparse vegetation.
> *   **Background:** Through an opening in the trees on the right, a detailed and expansive landscape unfolds. It depicts a European town or village with various buildings, including a prominent multi-story house. Tiny figures of people can be seen in the village. Beyond the town are rolling hills and a distant mountain range under a cloudy sky.
> 
> **Overall Impression:**
> 
> The painting captures a moment of quiet drama and psychological complexity. The contrast between the old man and the young woman, their different attire (rustic vs. refined), and their opposing demeanors (active vs. passive) suggests a narrative or allegorical theme. Common interpretations for such scenes in art history include the "unequal lovers" trope, a mythological story (such as Vertumnus and Pomona), or an allegory of Youth and Old Age or Wisdom and Beauty.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:50:10+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and knowledge of common subjects in European art, this painting depicts a scene from classical mythology.
> 
> **Episode:** The wooing of Pomona by Vertumnus.
> 
> **Figures:**
> *   The old, bearded man is **Vertumnus**, the Roman god of seasons, change, and plant growth.
> *   The young woman is **Pomona**, the Roman goddess of fruitful abundance, especially orchards and gardens.
> 
> **Explanation of the Scene:**
> The story comes from Ovid's *Metamorphoses*. Vertumnus fell in love with the beautiful nymph Pomona, who was dedicated solely to her gardens and rejected all suitors. To get close to her, the shapeshifting god Vertumnus took on many disguises.
> 
> This painting captures the moment he appears in his most famous disguise, that of an old man (though in Ovid's text, it is an old woman). In this guise, he gains Pomona's trust. He sits with her, his arm around her, and speaks persuasively about the virtues of love and marriage, using the example of a vine clinging to an elm tree. He appears to be offering her a ring, a symbol of this proposed union.
> 
> Pomona's downcast eyes and pensive expression show her listening to his arguments, still hesitant but perhaps beginning to be swayed. The staff she holds is likely a pruning hook or a symbol of her domain over the garden. The setting, with grapevines and a lush landscape, is her sacred space. This subject was popular in Northern European art of the 16th and 17th centuries.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:50:30+00:00_

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

> Judah's love-affair with Tamar; he gives her his signet-ring and staff

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:49:56+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Jan Swart van Groningen",
>   "title": "Judah and Tamar",
>   "date": "ca. 1530 - 1540",
>   "collection": "Rijksmuseum, Amsterdam"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:14:12+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this image depicts the biblical story of **Judah and Tamar** (from Genesis 38). 
> 
> ### Key Elements of the Depiction:
> * **The Characters:** 
>   * **Judah** is represented as the older, bearded man wearing a turban-like head covering. He has his arm around Tamar's shoulder.
>   * **Tamar** (his daughter-in-law, disguised as a prostitute) is depicted as the younger woman sitting beside him.
> * **The Pledges:** 
>   * Tamar is holding Judah's **staff** in her right hand.
>   * Judah is holding out his **signet ring** in his left hand. In the biblical narrative, Tamar demands these items (along with his cord) as a pledge of payment before agreeing to sleep with him.
> * **The Setting:** They are seated in a wooded landscape, with a detailed Northern European-style village or manor house visible in the background to the right. 
> 
> This composition is characteristic of 16th-century Northern Renaissance (Netherlandish/Flemish) paintings of biblical narratives.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:14:25+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the Old Testament biblical episode of **Judah and Tamar** (from Genesis 38). 
> 
> ### Figures and Scene:
> * **Tamar** (left): Judah's widowed daughter-in-law, who has disguised herself as a prostitute by the roadside to conceive a child by him after he failed to give her his youngest son in marriage as promised.
> * **Judah** (right): Her father-in-law, who does not recognize her.
> 
> ### Key Iconography:
> In the story, Tamar asks Judah for a pledge of payment until he can send her a young goat from his flock. She demands three personal items as security, which are clearly depicted here:
> 1. **The Staff:** Tamar holds Judah's walking staff in her right hand.
> 2. **The Signet Ring:** She holds up Judah's signet ring in her left hand. 
> 
> These items later serve as proof of the child's paternity when Judah accuses her of harlotry, forcing him to admit his own righteousness was lacking compared to hers.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:14:35+00:00_

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

> Judah's love-affair with Tamar; he gives her his signet-ring and staff

