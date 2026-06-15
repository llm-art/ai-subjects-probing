# Probe report — `abduction-amphitrite`

[![abduction-amphitrite](https://media.rkd.nl/iiif/2/11127255/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/11127255/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/11127255/info.json)_

- **Ground-truth subject:** Abduction of Amphitrite by Poseidon
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/abduction-amphitrite.jpg` — native 5507×4499 px, sent 2048×1673 px
- **SHA-256:** `0ee63e57ed3a117804eeb5dc88f270fad19b2196945de9ed035500451f39e39b`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:42:00+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this artwork is:
> 
> **Artist:** Hendrick van den Broeck (also known as Arrigo Fiammingo)
> 
> **Title:** *Perseus and Andromeda* (sometimes referred to as *The Wedding of Perseus and Andromeda*)
> 
> **Approximate Date:** c. 1570
> 
> **Collection:** Palatine Gallery, Palazzo Pitti, Florence, Italy.
> 
> The painting depicts the celebration following Perseus's rescue of Andromeda. The hero Perseus is the prominent figure in the foreground, seen from the back, wearing a helmet and holding the head of the gorgon Medusa, which he used to defeat the sea monster. The central female figure is Andromeda, now freed, being honored by a retinue of Nereids (sea nymphs) and Tritons. The scene is a characteristic example of Mannerism, with its crowded composition, dynamic and elegant figures in complex poses, and mythological subject matter.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:42:25+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided and my internal knowledge, this painting depicts a scene from Greek mythology: **the triumph following the rescue of Andromeda by Perseus.**
> 
> Here is a detailed breakdown of what is visible in the image:
> 
> *   **Central Scene:** In the water, a grand procession celebrates a fair-skinned woman, who is **Andromeda**. She is reclining on a red cloth, being carried by sea creatures and attended by Nereids (sea nymphs) and Tritons (mermen). A winged putto (a cherubic figure) flies above her, holding a laurel wreath to crown her, symbolizing victory and honor.
> 
> *   **The Hero:** In the right foreground, with his back mostly to the viewer, stands the hero **Perseus**. He is identifiable by his attributes:
>     *   A plumed, ornate helmet.
>     *   A long spear in his right hand.
>     *   In his left hand, he holds the severed **head of Medusa**, which he used to turn the sea monster Cetus to stone to save Andromeda. The head is depicted as a grotesque, mask-like face.
> 
> *   **Mythological Creatures:** The sea is teeming with mythological beings. Besides the Nereids and Tritons, there are fantastical sea monsters they ride upon, some with fish-like bodies and others with griffin-like heads.
> 
> *   **The Setting:** The scene is set in a coastal landscape. To the right are rocky cliffs and gnarled trees. In the background, across the water, a city with towers and bridges can be seen.
> 
> *   **Celestial Observers:** In the sky, seated on clouds, are several figures who appear to be gods and goddesses observing the celebration below.
> 
> In summary, the painting does not depict the battle itself, but rather the joyous aftermath. Perseus, the victorious hero, stands

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:42:47+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and knowledge of Greek mythology, this painting depicts the mythological episode of **The Origin of Coral**.
> 
> This story comes from Ovid's

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:51:22+00:00_

**Prompt:**

> This painting depicts one of the following subjects. Which one is it?
> — Prometheus chained by Vulcan
> — Aeneas rescues his father Anchises from the burning Troy
> — Abduction of Amphitrite by Poseidon
> — The wedding of Peleus and Thetis
> — The Competition of Apollo and Pan and the judgment of Midas
> — Marriage of Cupid and Psyche
> — The Triumph of Bacchus
> — Apollo in Vulcan's forge revealing Venus' love-affair with Mars
> — The Triumph of Mars: an Allegory of War
> — The meeting of Nausicaa and Ulysses
> — The meeting of Dido and Aeneas
> — The sacrifice of Iphigenia
> — The goddess Pallas Athena and the horse Pegasus
> — Dido's sacrifice to Juno
> — Sacrifice to Venus in a temple
> Answer with the subject only.

**Response (verbatim):**

> The wedding of Peleus and Thetis

