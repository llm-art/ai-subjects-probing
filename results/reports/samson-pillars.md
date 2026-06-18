# Probe report — `samson-pillars`

[![samson-pillars](https://iiif.artresearch.net/iiif/3/zeri/160000/123200/123130.jpg/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/zeri/160000/123200/123130.jpg/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/zeri/160000/123200/123130.jpg/info.json)_

- **Ground-truth subject:** Samson breaks the pillars; the temple of Dagon collapses
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/samson-pillars.jpg` — native 3072×2286 px, sent 2048×1524 px
- **SHA-256:** `2ee7b169925be514a92c060cc6ecb9fb8dad8f6fa5694bacdb1a44c0d718460e`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:00+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Peter Paul Rubens",
>   "title": "The Death of Samson",
>   "date": "c. 1605",
>   "collection": "J. Paul Getty Museum"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:47:18+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general knowledge of Western art and biblical narratives, this painting depicts the biblical story of **Samson destroying the Philistine temple**.
> 
> Here is a breakdown of the scene:
> 
> *   **The Central Figure:** The muscular man in the center, with his back to the viewer, is Samson. He is shown exerting immense strength to topple a massive stone pillar. This is his final act, as told in the Book of Judges in the Old Testament.
> *   **The Action:** After being captured, blinded, and humiliated by the Philistines, Samson was brought to their temple of Dagon to be mocked. He prayed to God for one last burst of strength, and he pushed against the central pillars supporting the roof, causing the entire structure to collapse.
> *   **The Surrounding Figures:** The people around Samson are the Philistines, who are shown in a state of panic and terror. They are screaming, falling, and trying to escape the collapsing building. The man on the right, with his mouth agape and hands raised in horror, is a particularly dramatic example. On the left, figures, including what appears to be a woman holding a child, are being crushed by the falling debris.
> *   **The Setting:** The architecture, with its grand pillars and arches, represents the Philistine temple. The entire scene is one of chaos, destruction, and divine retribution.
> 
> The painting's style is characteristic of the Baroque period, with its dramatic use of light and shadow (chiaroscuro), dynamic composition, and intense emotional expression, all designed to capture the most climactic moment of the story.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:47:33+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts a famous biblical scene.
> 
> **Episode:** The Death of Samson, or Samson Destroying the Temple of Dagon. This story is from the Old Testament, specifically the Book of Judges (Chapter 16).
> 
> **Figures and Scene:**
> 
> *   **Samson:** The central figure is Samson, an Israelite judge known for his superhuman strength, which was granted by God and linked to his uncut hair. In the painting, he is shown with his back to the viewer, his powerful muscles straining as he pushes apart a massive pillar of the temple. This is his final act. After being betrayed by Delilah, captured by the Philistines, and blinded, he was brought to their temple to be mocked. He prayed for one last burst of strength to take vengeance on his enemies.
> *   **The Philistines:** The other figures in the painting are the Philistines, Samson's enemies. They are depicted in a state of panic and terror as the temple collapses around them. The man on the right, with his mouth agape in a scream and hands thrown up in horror, is a prime example. Other figures, including women and children (visible on the left), are shown trying to flee or shield themselves from the falling debris.
> 
> The painting captures the climactic and chaotic moment of destruction, using dramatic lighting (chiaroscuro) and dynamic composition typical of the Baroque style to emphasize the power, tragedy, and divine retribution of the event.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:47:49+00:00_

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

> Samson breaks the pillars; the temple of Dagon collapses

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:49:21+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Valerio Castello",
>   "title": "Samson Destroying the Temple",
>   "date": "c. 1650",
>   "collection": "Hermitage Museum, St. Petersburg"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:12:24+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this image depicts the biblical story of **Samson destroying the Temple of Dagon** (from the Book of Judges). 
> 
> Key elements shown in the scene include:
> * **Samson:** The central, highly muscular figure shown from behind, using his legendary strength to push and break a massive, fluted stone column, dislodging it from its base.
> * **The Collapsing Temple:** The architectural structure is crumbling, with cracks in the columns and debris beginning to fall.
> * **The Panicking Philistines:** 
>   * On the right, a bearded man falls backward in terror, his mouth open in a scream and his hands raised defensively.
>   * On the left, a crowd of people, including a mother clutching her infant, flee in chaos and fear.
> * **Artistic Style:** The composition is rendered in a dramatic Baroque style, utilizing strong *chiaroscuro* (stark contrasts between light and shadow) to emphasize the muscular tension, dynamic movement, and intense emotion of the scene.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:12:33+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the biblical episode of **Samson destroying the Temple of Dagon** (from the Book of Judges, 16:29–30). 
> 
> ### Key Figures and Details:
> * **Samson:** The central, highly muscular figure shown from behind, using his restored strength to push and break the massive stone columns supporting the temple.
> * **The Philistines:** The terrified figures surrounding him, including the panicked man on the right and the fleeing women and children on the left, who are being crushed by the collapsing architecture of the temple dedicated to their god, Dagon.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:12:42+00:00_

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

> Samson breaks the pillars; the temple of Dagon collapses

