# Probe report — `abram-lot-divide`

[![abram-lot-divide](https://iiif.artresearch.net/iiif/3/frick/4107100269574_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100269574_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100269574_0001.jp2/info.json)_

- **Ground-truth subject:** Abram and Lot Dividing up the World between Them
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/abram-lot-divide.jpg` — native 5977×4275 px, sent 2048×1465 px
- **SHA-256:** `7d7bb27de46432dc0a3fa15f0837c85bb8be4a9478bda7f910d3c8177659de8c`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:06+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Antonio Zanchi",
>   "title": "The Philosophers (Pythagoras and his pupils)",
>   "date": "c. 1665",
>   "collection": "Accademia Carrara, Bergamo"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:05:52+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a black and white photograph of a dramatic, multi-figure painting in the Baroque style. The scene is characterized by intense lighting and shadow (chiaroscuro) and features a group of people gathered in a dark, atmospheric setting.
> 
> **Central Action and Figures:**
> The composition is centered around a large, plain sphere or globe. Several figures are intently focused on it:
> 
> *   **An elderly, bearded man**, seated on the left, is the primary actor. He wears flowing robes and is using a large pair of dividers or a compass to measure the surface of the globe. His expression is one of deep concentration.
> *   **A muscular, semi-nude man** is seated in the foreground on the right, with his back to the viewer. He holds a large tablet or board that appears to have some form of notation on it. He is looking towards the central group.
> *   **A dynamic figure**, standing behind the globe, leans forward with one arm raised in a dramatic gesture, as if making a proclamation or having a moment of inspiration. This person wears a headband or turban.
> *   **Other figures** crowd around the central action. To the left and in the background, other men, some hooded, and what appear to be women or children, look on with varied expressions of curiosity, concern, or awe.
> 
> **Setting and Atmosphere:**
> The setting is dark and indistinct, possibly an interior space at night or a cave. In the upper right, a patch of turbulent, cloudy sky is visible, adding to the dramatic mood. The strong light source seems to come from the left, illuminating the key figures and casting deep shadows, which heightens the sense of drama and focuses the viewer's attention on the intellectual activity taking place.
> 
> **Interpretation:**
> The scene is likely an allegory, possibly representing the pursuit of knowledge, or a gathering of the Arts and Sciences. The man with the compass represents Geometry, Astronomy, or Architecture. The muscular figure with the tablet could personify Music, Mathematics, or perhaps Sculpture. The overall theme is one of intense intellectual endeavor, the measurement and understanding of the world, rendered with the passion and dynamism characteristic of Baroque art.
> 
> A small label visible at the bottom of the image in one of the cropped views reads "A. ZANCHI".

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:06:15+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history, this painting depicts an **allegorical gathering of ancient philosophers, mathematicians, and scholars**. This type of scene is often titled **"The School of Athens"** or **"The Philosophers,"** a theme popularized by Raphael and reinterpreted by later artists.
> 
> Here is a breakdown of the figures and the scene's meaning:
> 
> *   **The Subject:** The painting is an allegory for the pursuit of human knowledge, particularly in the arts and sciences. It brings together great thinkers from different eras into a single, dramatic composition.
> *   **The Central Figure (Left):** The elderly, bearded man seated on the left is the focal point of the intellectual activity. He is using a pair of compasses (or calipers) to measure a large globe. This figure is often identified as **Archimedes** or **Euclid**, representing the sciences of **Geometry** and **Mathematics**.
> *   **The Figure on the Right:** A muscular, semi-nude man is seated in the foreground, holding a tablet or a musical instrument (like a kithara or lyre). He represents the practical arts, sculpture, or **Music**, especially if the object is interpreted as a stringed instrument, linking mathematics to harmony, a concept associated with **Pythagoras**.
> *   **The Gesticulating Figure:** Above the central group, a man with a turban raises his arm and points upward. This dramatic gesture can symbolize **Astronomy** or **Astrology** (pointing to the heavens), or it can represent **Divine Inspiration** that guides human discovery.
> *   **Other Figures:** The surrounding figures are other scholars, students, and personifications of different disciplines. The hooded, pensive man behind Archimedes/Euclid could represent **Philosophy**. The women and children in the background may represent the Muses or humanity benefiting from this accumulated wisdom.
> 
> The style of the painting is distinctly **Baroque**, characterized by its dramatic use of light and shadow (chiaroscuro), dynamic and swirling composition, and the intense, emotional engagement of the figures.
> 
> From a small label visible in one of the cropped images, the artist can be identified as **Antonio Zanchi** (1631–1722), a prominent Venetian painter of the late Baroque period, known for such large-scale, dramatic historical and allegorical works.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:06:42+00:00_

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

> Belshazzar's Feast

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:51:51+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Antonio Zanchi",
>   "title": "Archimedes",
>   "date": "ca. 1670",
>   "collection": null
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:19:30+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details and the label at the bottom of the image, this is a photograph of a Baroque painting by the Venetian artist **Antonio Zanchi** (1631–1722). 
> 
> The painting depicts **an astronomy lesson or a gathering of philosophers/cosmographers** (often identified as **Archimedes** or an **Allegory of Astronomy**):
> 
> * **Central Action:** An elderly, bearded philosopher or astronomer on the left is using a pair of dividers (compasses) to measure a large globe situated in the center of the composition.
> * **Key Figures:** 
>   * On the right, a muscular, semi-nude young man is seated with his back partially turned, holding a tablet or slate containing diagrams or calculations.
>   * Behind the globe, another figure stands with an arm raised, holding a plumb line or pointing upward.
>   * Several other onlookers (men and women) surround the globe, watching the demonstration with intense curiosity.
> * **Style:** The work is executed in a dramatic Venetian Baroque style, characterized by strong *chiaroscuro* (the stark contrast between deep shadows and bright highlights) and dynamic, expressive figures.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:19:41+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting by the Venetian Baroque artist **Antonio Zanchi** (1631–1722) depicts the historical/philosophical episode of **Anaxarchus and Alexander the Great** (specifically, *Anaxarchus explaining the multiplicity of worlds to Alexander*).
> 
> ### Key Figures and Details:
> * **Anaxarchus** (on the left): The ancient Greek philosopher is shown as an elderly, bearded man seated with a pair of compasses (dividers) over a large globe, illustrating his cosmological theory that there are infinite worlds.
> * **Alexander the Great** (on the right): Depicted as a muscular, athletic young man, listening intently to the philosopher. According to historical anecdotes (recorded by Valerius Maximus and Plutarch), upon hearing from Anaxarchus that there was an infinite number of worlds, Alexander wept because he had not yet conquered even one.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:19:51+00:00_

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

> The sacrifice of Isaac (Abraham and Isaac)

