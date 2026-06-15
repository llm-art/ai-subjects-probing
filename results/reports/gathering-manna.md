# Probe report — `gathering-manna`

[![gathering-manna](https://iiif.artresearch.net/iiif/3/frick/4107100309903_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100309903_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100309903_0001.jp2/info.json)_

- **Ground-truth subject:** The Gathering of Manna
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/gathering-manna.jpg` — native 5628×3578 px, sent 2048×1302 px
- **SHA-256:** `4af72b58b00bf86d9ed9a8ecb1650c5beaf7f05ca81d5351c302544ab3330f46`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:48:07+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a well-known work of the Italian Renaissance.
> 
> **Artist:** Ercole de' Roberti (also known as Ercole Ferrarese)
> **Title:** *The Israelites Gathering Manna*
> **Approximate Date:** c. 1473
> **Collection:** The National Gallery, London
> 
> This painting depicts the biblical story from the Book of Exodus where God provides manna, or "bread from heaven," to the Israelites wandering in the desert.
> 
> In the image, we can see:
> *   At the top center, the face of God the Father appears in a cloud, from which the white, wafer-like manna is falling to the ground.
> *   Below, various figures representing the Israelites are collecting the manna. In the center, a man and a woman kneel to gather it into bowls. On the right, a woman stands holding a basket, while a small child also gathers the food.
> *   On the far left, two elderly, bearded men, likely representing Moses and Aaron, stand and look up towards the heavens.
> *   The setting is a rocky, verdant landscape with a fortified town visible in the distance.
> 
> The style is characteristic of the Ferrarese School of the 15th century, known for its expressive figures, sharp and complex drapery, and detailed, imaginative landscapes. This panel was originally part of the *predella* (the base) of a large altarpiece known as the Griffoni Polyptych, which was painted for a chapel in the Basilica of San Petronio in Bologna.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:48:26+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general art historical knowledge, this black and white image depicts the biblical story of the **Gathering of the Manna**.
> 
> Here is a detailed description of the scene:
> 
> *   **Central Theme:** The image illustrates the Old Testament account from the Book of Exodus where God provides food, called manna, for the Israelites wandering in the desert.
> 
> *   **Divine Presence:** At the top center, the face of God the Father appears in a cluster of clouds, looking down upon the people. From these clouds, small white flakes, representing the manna, are falling like rain or snow onto the landscape below.
> 
> *   **The People (Israelites):** Various figures are scattered throughout the landscape, reacting to the miracle.
>     *   On the **left**, two elderly, bearded men in flowing robes stand together. One looks up towards the heavens, perhaps in prayer or gratitude. These figures likely represent Moses and Aaron.
>     *   In the **center foreground**, a man and a woman are kneeling to collect the manna from the ground. The man uses a shallow bowl to gather the flakes.
>     *   On the **right**, a woman stands looking up towards God, holding a small basket partially filled with manna. Near her, a small child is on the ground, also gathering the food. Another figure can be seen in the mid-ground behind them.
> 
> *   **Setting and Landscape:** The scene is set in a lush, hilly landscape, which is characteristic of European Renaissance art rather than a literal depiction of the Sinai desert. In the background, a fortified town or city with towers and a church steeple is visible. Trees frame the composition on both the left and right sides.
> 
> *   **Artistic Style:** The style of the figures, their clothing (which appears to be Renaissance-era dress), and the detailed landscape suggest the artwork originates from the Italian or Northern European Renaissance. The image itself is a monochrome reproduction of what was likely a colorful painting.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:48:42+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of Western art history and biblical narratives, this painting depicts the Old Testament episode of **The Gathering of Manna**.
> 
> Here is a breakdown of the scene and figures:
> 
> *   **The Episode:** This scene comes from the Book of Exodus (Chapter 16). After escaping from Egypt, the Israelites wandered in the desert for forty years. When they ran out of food and complained, God provided them with "bread from heaven," which they called manna. It appeared on the ground each morning like dew or frost, and they were instructed to gather enough for one day.
> 
> *   **The Figures and Elements:**
>     *   **God the Father:** The face appearing in the clouds at the top center of the painting is God the Father, who is the source of the miracle. The manna, depicted as small white flakes, is shown falling from the clouds below him.
>     *   **Moses and Aaron:** The two elderly, bearded men in robes on the left are most likely Moses and Aaron, the leaders of the Israelites. They are shown looking up towards God, acknowledging the divine gift.
>     *   **The Israelites:** The other figures in the painting are the Israelites. They are shown in various postures of gathering the manna from the ground. In the center, a man and a woman kneel to collect it, with the man using a shallow bowl. On the right, a standing woman holds a basket, and a small child is also on the ground gathering the flakes. These figures represent the community receiving God's providence.
> 
> The landscape, with its distant fortified city, is typical of Renaissance paintings, which often set biblical scenes in contemporary European-style settings rather than historically accurate ones. The style of the figures and the composition are characteristic of the Italian or Northern Renaissance.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:48:59+00:00_

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

> The Gathering of Manna

