# Probe report — `bathsheba-letter`

[![bathsheba-letter](https://media.rkd.nl/iiif/2/10661333/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10661333/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10661333/info.json)_

- **Ground-truth subject:** Bathsheba receives a letter from David
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/bathsheba-letter.jpg` — native 2104×1650 px, sent 2048×1606 px
- **SHA-256:** `5b5f06ed50787f9111f682996ad7f241d467a920200fadd1d9b4e431553ffc60`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:15+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Hieronymus Francken the Younger",
>   "title": "Bathsheba at her Fountain",
>   "date": "c. 1625-1635",
>   "collection": null
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:48:28+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a classical painting, likely from the Baroque period, depicting a scene of opulent leisure in a grand garden setting.
> 
> **Central Figures:**
> The focal point of the painting is a group of three people on the right side.
> *   A fair-skinned woman with light-colored hair is seated, her upper body partially exposed as her white chemise is pulled down off her shoulders. She looks towards her left, with a calm and contemplative expression. She is adorned with a pearl bracelet and appears to be holding a string of pearls.
> *   Behind her, another woman with dark hair, dressed in purple, leans over to attend to the seated woman's hair.
> *   To the left of the seated woman, a dark-skinned attendant in a blue tunic holds up a small mirror for her. A vibrant red cloth is draped over the attendant's lap and the balustrade.
> 
> **Setting and Environment:**
> The scene is set on a stone terrace next to a decorative fountain.
> *   **The Fountain:** The fountain features a sculptural element of a fantastical sea creature or dolphin, from which water flows into a large stone basin. The area behind the fountain is a rocky grotto decorated with seashells.
> *   **The Terrace and Garden:** A classical stone balustrade separates the terrace from a meticulously manicured formal garden (a parterre) with geometric patterns. In the background, a large, elegant building with arches, possibly a villa or palace, is visible on the left.
> *   **Landscape:** Beyond the formal garden, a hazy, atmospheric landscape of rolling hills and trees stretches into the distance under a cloudy sky.
> 
> **Animals and Objects:**
> The scene is populated with various animals, which often carried symbolic meaning in paintings of this era:
> *   A blue-and-yellow macaw is perched on the balustrade.
> *   A monkey sits on the ground near the balustrade, seemingly tethered.
> *   A small dog

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:48:50+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and knowledge of art history, this painting depicts a **"Toilet Scene,"** which is most likely an **Allegory of Vanity (Vanitas)** or an **Allegory of the Five Senses**.
> 
> Here is a breakdown of the scene and its figures:
> 
> *   **The Subject:** The central theme is a wealthy, fair-skinned woman at her toilette (the process of grooming, dressing, and applying makeup). She is the focal point, embodying beauty and worldly luxury. While it borrows conventions from mythological scenes like the "Toilet of Venus," the collection of specific symbolic elements suggests a broader allegorical meaning rather than a specific narrative episode.
> 
> *   **The Figures:**
>     *   **The Lady:** The main figure is a noblewoman, or a personification of Vanity itself. Her chemise is slipping off her shoulder, a common device in Baroque art to display beauty and add a touch of sensuality. She is looking into a mirror, the primary symbol of vanity.
>     *   **The Dark-Skinned Page:** To her left, a young, dark-skinned servant or page holds up a mirror for her. In 17th-century European painting, the inclusion of such figures often served to highlight the whiteness and status of the main subject, as well as to signify the family's wealth and global connections.
>     *   **The Handmaiden:** Behind the lady, another female attendant is arranging her hair, further emphasizing the theme of adornment and preparation.
> 
> *   **Symbolism and Allegory:**
>     The scene is rich with symbolic objects that point towards an allegory:
>     *   **The Mirror:** The most direct symbol of **Vanity** and the sense of **Sight**.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:49:12+00:00_

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

> Bathsheba receives a letter from David

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:49:29+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Jan Brueghel the Younger and Hendrick van Balen",
>   "title": "Bathsheba at her Bath",
>   "date": "c. 1625-1630",
>   "collection": null
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:13:03+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this is a Flemish Baroque painting depicting a classical or biblical scene, most likely **Bathsheba at her Toilet** (or a similar mythological subject like Venus at her toilet). 
> 
> Here is a detailed breakdown of what is depicted:
> 
> *   **Central Figures:** 
>     *   A fair-skinned, semi-nude woman sits on a terrace, draped in a white chemise that exposes her breasts. 
>     *   Standing behind her, a female attendant in a purple dress styles her blonde hair.
>     *   To her left, a dark-skinned servant in a blue tunic sits on a red cloak, holding a small object (likely a mirror or cosmetic tool) toward her.
> *   **The Fountain:** To the right, water pours from a sculpted dolphin-shaped spout into a large stone basin. The rocky wall behind the fountain is decorated with various seashells.
> *   **Animals:** The scene is filled with symbolic animals typical of Flemish cabinet paintings:
>     *   A blue-and-yellow **parrot** perched on the stone balustrade.
>     *   A small **monkey** sitting on the ground near the balustrade.
>     *   A small **dog** standing near the central woman's feet.
>     *   A **peacock** on the far left near the garden urns.
> *   **Setting and Background:** 
>     *   The figures are on a stone terrace overlooking a grand, formal Renaissance/Baroque garden with geometric parterres (hedges).
>     *   On the left stands a classical stone archway and palace structure.
>     *   In the distance, a soft, hazy landscape stretches toward the horizon under a cloudy sky.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:13:29+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This is a European Baroque painting depicting the biblical episode of **Bathsheba at her Bath** (or *Bathsheba at her Toilet*), from the Second Book of Samuel (2 Samuel 11).
> 
> ### Figures Depicted:
> * **Bathsheba:** The central semi-nude woman seated by the fountain, preparing her toilet.
> * **Maidservants:** 
>   * One maidservant stands behind Bathsheba, styling and combing her hair.
>   * A Black servant sits to her left, holding a mirror or presenting King David's letter.
> * **King David:** He can be seen as a tiny, distant figure standing on the high balcony/terrace of the palace on the far left, observing Bathsheba from afar.
> 
> ### Setting and Details:
> The scene is set in a lavish palace garden featuring a formal Renaissance/Baroque parterre, a classical archway, and a fountain decorated with a dolphin sculpture. The composition is enriched with symbolic animals typical of 17th-century Flemish painting, including a parrot (symbol of luxury or mimicry), a monkey (symbol of vanity or base desires), a small dog (fidelity), and a peacock (pride).

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:13:43+00:00_

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

> Bathsheba receives a letter from David

