# Probe report — `diana-actaeon`

[![diana-actaeon](https://iiif.artresearch.net/iiif/3/frick/4107100328587_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100328587_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100328587_0001.jp2/info.json)_

- **Ground-truth subject:** Diana and Actaeon
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/diana-actaeon.jpg` — native 5483×4995 px, sent 2048×1866 px
- **SHA-256:** `070ad1daddf0de84762047925dbd231e171ba7a6fe933e60b5ef17c40a31f75f`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T07:59:04+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a famous painting from the High Renaissance.
> 
> **Artist:** Titian (Tiziano Vecellio)
> 
> **Title:** *Diana and Actaeon*
> 
> **Approximate Date:** c. 1556–1559
> 
> **Collection:** The painting is jointly owned by the National Gallery, London, and the National Galleries of Scotland, Edinburgh.
> 
> The painting depicts the dramatic moment from Ovid's *Metamorphoses* when the mortal hunter Actaeon accidentally stumbles upon the goddess Diana and her nymphs bathing. The figure on the left is Actaeon, identifiable by his hunting gear. The central figure being attended to is Diana, the goddess of the hunt, identifiable by the crescent moon in her hair. The painting captures the tension and shock of the moment just before Diana, in her rage, transforms Actaeon into a stag to be killed by his own hounds. This work is one of a series of large-scale mythological paintings, known as the "poesie," that Titian created for King Philip II of Spain.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T07:59:22+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of art history and mythology, this painting depicts the classical myth of **Diana and Actaeon**.
> 
> Here is a breakdown of the scene:
> 
> *   **The Narrative:** The painting captures the dramatic moment when the mortal hunter, Actaeon, accidentally stumbles upon the goddess Diana (Artemis in Greek mythology) and her nymphs bathing in a sacred grotto.
> *   **Actaeon:** On the left, the figure of Actaeon is shown. He is dressed in a hunter's tunic, with a quiver of arrows on his back and a bow at his feet. His posture is one of shock and surprise as he pulls back a large red curtain, revealing the private scene.
> *   **Diana and her Nymphs:** On the right, the goddess Diana is the central figure among the group of nude women. She can be identified by the crescent moon diadem in her hair, a symbol of her association with the moon. She and her nymphs react with alarm and dismay at the intrusion, attempting to cover themselves. One of her attendants, a dark-skinned woman, helps shield the goddess.
> *   **The Setting:** The scene is set in a secluded, wooded landscape with a grotto and a pool or fountain. The architectural elements, like the stone arch and the carved basin, lend a classical feel to the natural setting.
> *   **The Consequence (Implied):** This moment is the catalyst for the story's tragic conclusion. Enraged at being seen naked by a mortal, Diana punishes Actaeon by transforming him into a stag. He is then hunted down and killed by his own hounds. The presence of hunting dogs in the image (one near Actaeon's leg and two small dogs near Diana's feet) foreshadows this grim fate.
> 
> The style of the painting, with its rich colors, dynamic composition, and sensual treatment of the nude form, is characteristic of the **Venetian School of the High Renaissance**, and this specific composition is famously associated with the artist **Titian**, who painted this subject as part of his "poesie" series for King Philip II of Spain.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T07:59:41+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts a famous episode from classical mythology: **Diana and Actaeon**.
> 
> The scene is taken from Ovid's *Metamorphoses*.
> 
> *   **Actaeon** is the male figure on the left. He is identifiable as a hunter by the bow on the ground at his feet and the quiver of arrows on his back. He is shown striding into the scene, pulling back a red curtain, his expression one of shock and surprise at what he has discovered.
> 
> *   **Diana** (the Roman goddess of the hunt, the moon, and chastity, equivalent to the Greek Artemis) is the main female figure on the right. She is identified by the crescent moon ornament in her hair, her primary symbol. She and her attendants are bathing in a secluded grotto. Diana is shown reacting with fury and alarm at being seen naked by a mortal man.
> 
> *   The other nude women are **nymphs**, Diana's attendants, who share in the surprise and scramble to cover themselves or their mistress. One of Diana's attendants, a Black woman, helps to shield the goddess.
> 
> The painting captures the dramatic moment of discovery. According to the myth, the enraged Diana punishes Actaeon for his transgression by splashing water on him, which transforms him into a stag. He is then tragically hunted down and killed by his own hounds. The small dogs in the lower right corner foreshadow this fate.
> 
> The style of the painting, with its rich colors, dynamic composition, and masterful handling of light and flesh, is characteristic of the Venetian Renaissance painter **Titian** (Tiziano Vecellio), for whom this is one of his most famous works.

