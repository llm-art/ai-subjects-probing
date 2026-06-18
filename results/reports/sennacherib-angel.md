# Probe report — `sennacherib-angel`

[![sennacherib-angel](https://iiif.artresearch.net/iiif/3/frick/4107100223194_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100223194_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100223194_0001.jp2/info.json)_

- **Ground-truth subject:** The Forces of Sennacherib put to Rout by the Angel
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/sennacherib-angel.jpg` — native 3668×5918 px, sent 1269×2048 px
- **SHA-256:** `f5f4f3cabbdb3d94ee0c16e1ce3971014cd1902eb20df895aa2885fa439e349e`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:14+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Peter Paul Rubens",
>   "title": "The Defeat of Sennacherib",
>   "date": "c. 1612-1614",
>   "collection": "Alte Pinakothek, Munich"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:06:20+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general art historical knowledge, this is a black and white photograph of a painting depicting a scene of divine wrath and destruction.
> 
> The painting is divided into two main sections:
> 
> 1.  **The Celestial Realm (Top):** An angel, or a divine winged figure, swoops down from a dark, cloudy sky. Beams of light emanate from this figure, directed towards the scene below. The angel is depicted in a powerful, dynamic pose, holding what appears to be a sword or a scepter, signifying its role as an agent of judgment or destruction.
> 
> 2.  **The Earthly Realm (Bottom):** Below, a chaotic battle scene unfolds, or rather, a massacre. A multitude of muscular, mostly nude or lightly clad soldiers are in disarray. They are shown in contorted poses of agony and death. Some lie dead on the ground, others are falling, and some appear to be trying to shield themselves or flee in terror. There are shields, spears, and at least one horse caught in the melee. In the background on the right, a fortified city or castle is visible.
> 
> **Interpretation of the Subject:**
> 
> This scene is characteristic of a popular Old Testament subject in Baroque art: **The Destruction of the Army of Sennacherib**. According to the biblical account (2 Kings 19:35), the Angel of the Lord went out and put to death 185,000 men in the Assyrian camp as they besieged Jerusalem. The painting captures the moment of divine intervention, with the angel single-handedly destroying the vast army.
> 
> **Artistic Style:**
> 
> The style is clearly **Baroque**. This is evident in:
> *   **Dramatic Composition:** The strong diagonal lines and the division between heaven and earth create a sense of dynamic action and high drama.
> *   **Chiaroscuro:** The intense contrast between light and shadow is used to heighten the emotional impact and model the muscular figures.
> *   **Emotional Intensity:** The figures on the ground display extreme emotions of pain, fear, and despair.
> *   **Muscular Figures:** The emphasis on powerful, idealized, and contorted anatomy is reminiscent of the work of Michelangelo and was a hallmark of many Baroque painters.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:06:39+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts a dramatic biblical scene from the Old Testament.
> 
> **Episode:** **The Destruction of the Army of Sennacherib**.
> 
> This story is recounted in the Bible (2 Kings 19:35 and Isaiah 37:36). The Assyrian King Sennacherib besieged Jerusalem, threatening to conquer it. King Hezekiah of Judah prayed to God for deliverance. In response, God sent an angel who, in a single night, struck down 185,000 soldiers in the Assyrian camp, forcing Sennacherib to abandon the siege and return to his own land.
> 
> **Figures and Scene:**
> 
> *   **The Angel of the Lord:** The figure in the upper part of the painting, descending from the heavens amidst clouds and divine light, is the **Angel of the Lord**. He is depicted as a powerful, winged being, holding a sword, which is the instrument of God's judgment. His dynamic, downward-swooping pose emphasizes the swift and overwhelming nature of the divine intervention.
> *   **The Assyrian Soldiers:** The chaotic mass of figures in the lower two-thirds of the composition represents the **army of Sennacherib**. They are shown in utter disarray and agony. Men and horses are collapsing, dying, and writhing in pain. Their muscular, classicized bodies, typical of the Baroque style, are used to convey the drama and tragedy of their sudden demise. Some soldiers look up in terror, shielding themselves from the divine light, while others are already dead or trampled.
> *   **Jerusalem:** The fortified city or castle visible in the background on the right represents **Jerusalem**, the city that is being saved by this miraculous event.
> 
> The painting's style, with its dramatic use of light and shadow (chiaroscuro), swirling composition, and intense emotional display, is characteristic of High Baroque history painting. The artist has chosen the most dramatic moment of the story to illustrate the immense power of God and the futility of opposing him.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:06:58+00:00_

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

_Run: 2026-06-18T13:51:54+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Tanzio da Varallo",
>   "title": "The Defeat of Sennacherib",
>   "date": "ca. 1627-1629",
>   "collection": "Museo Civico, Novara"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:20:45+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the composition and figures, this image depicts **"The Defeat of Sennacherib"** (also known as *The Destruction of Sennacherib's Army*), a famous Baroque painting by the Flemish master **Peter Paul Rubens** (circa 1612–1614). 
> 
> ### Key Depicted Elements:
> * **The Angel of the Lord:** In the upper left, an angel descends dramatically from dark clouds, illuminated by rays of divine light, wielding a sword to strike down the besieging Assyrian army.
> * **The Terrified Soldiers:** Below, the Assyrian soldiers are shown in a state of chaotic panic and defeat. Several figures are depicted in muscular, dynamic poses, desperately raising their shields to protect themselves from the heavenly wrath.
> * **The Fallen Horse:** On the right, a horse and its rider have collapsed in a dramatic, tangled heap, emphasizing the sudden and overwhelming nature of the divine intervention.
> * **The City of Jerusalem:** In the background on the right, the fortified towers of Jerusalem (the city being besieged by Sennacherib's army) stand under a dark, tempestuous sky.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:20:54+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the composition and iconography, this European Baroque oil painting depicts the biblical episode of **The Defeat of Sennacherib** (also known as **The Destruction of Sennacherib's Army** or **The Angel of the Lord Striking the Assyrians**), described in the Old Testament (2 Kings 19:35 and Isaiah 37:36).
> 
> ### **Key Figures and Elements Depicted:**
> * **The Angel of the Lord (often identified as the Archangel Michael):** Shown at the top left, descending dynamically from the heavens amidst clouds and rays of divine light, wielding a sword to smite the besieging army.
> * **The Assyrian Army:** The soldiers of King Sennacherib are shown in utter chaos, panic, and death on the ground below. They cower under their shields, look up in terror, and fall from their horses (as seen with the tumbling horse and rider on the right).
> * **The City of Jerusalem:** The fortress/castle in the background represents the besieged city of Jerusalem, which was saved from the Assyrian siege by this divine intervention.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:21:12+00:00_

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

> The painting depicts **The Defeat of Sennacherib** (also known as *The Destruction of Sennacherib's Army* by Peter Paul Rubens), which is not listed among the options provided.

