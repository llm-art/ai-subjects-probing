# Probe report — `marriage-cupid-psyche`

[![marriage-cupid-psyche](https://media.rkd.nl/iiif/2/9880831/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9880831/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9880831/info.json)_

- **Ground-truth subject:** Marriage of Cupid and Psyche
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/marriage-cupid-psyche.jpg` — native 3079×2063 px, sent 2048×1372 px
- **SHA-256:** `2c7aefe0aaa45a9f4a6cdb6b02d981ee3682fc369f1433b12469dabcce3649b8`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:51:22+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this artwork is:
> 
> *   **Artist:** Eustache Le Sueur
> *   **Title:** *The Marriage of Cupid and Psyche*
> *   **Approximate Date:** c. 1640s
> *   **Collection:** Musée du Louvre, Paris
> 
> This painting depicts a scene from the mythological story of Cupid and Psyche, as told by Apuleius in *The Golden Ass*. The central figures are Psyche (the bride) and Cupid (the winged youth placing a ring on her finger). Presiding over the ceremony is Hymen, the god of marriage, who holds the nuptial torch. On the left, Cupid's mother, Venus, sits in her golden chariot, holding a bow and seemingly giving her consent or bearing witness to the union she once opposed. At the bottom, two doves yoked together symbolize love and marriage. This work was part of a larger decorative cycle illustrating the story of Cupid and Psyche, originally created for the Hôtel Lambert in Paris.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:43:29+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology, this painting depicts **the wedding of Cupid and Psyche**.
> 
> Here is a breakdown of the scene and its characters:
> 
> *   **Central Action:** The focal point is the union of two figures. A young, winged boy, **Cupid** (the Roman god of desire), is placing a ring on the finger of a beautiful woman, **Psyche**. Psyche was a mortal princess whose beauty rivaled that of Venus.
> *   **Hymen:** Standing behind Cupid and Psyche is another winged figure in a red-orange robe, holding a flaming torch aloft. This is **Hymen**, the Greek god of marriage ceremonies. The marriage torch is his primary attribute.
> *   **Goddess in the Chariot:** To the left, a goddess arrives in a golden chariot that rests on clouds. She is dressed in a rich blue robe and holds a bow. This could be **Venus**, Cupid's mother, who initially persecuted Psyche but is now present for the union, or perhaps **Juno**, the goddess of marriage, giving her blessing.
> *   **Other Divine Figures:** In the upper right, another winged figure, possibly a wind god like **Zephyr**, reclines on a cloud, observing the ceremony.
> *   **Symbolism:** On the floor at Psyche's feet are two doves, birds sacred to Venus, symbolizing love and peace. One of the doves appears to be holding an olive branch or a similar item in its beak.
> *   **Setting:** The scene is set in a grand, classical interior with fluted columns and a balustrade overlooking a serene landscape. The presence of clouds on the floor and supporting the figures indicates a divine location, likely Mount Olympus, where the wedding took place after Psyche was made immortal.
> 
> In summary, the painting captures the culminating moment of the myth of Cupid and Psyche, a story about the triumph of love over adversity, as the mortal Psyche is finally and formally united with the god Cupid in marriage among the gods. The style is classical, with idealized figures, rich colors, and a balanced, theatrical composition characteristic of Baroque or Neoclassical art.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:43:49+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and knowledge of classical mythology, this painting depicts the **Marriage of Cupid and Psyche**.
> 
> This scene represents the culmination of the long and arduous tale of the mortal princess Psyche and the god of love, Cupid (Eros in Greek mythology). After enduring a series of cruel trials set by Cupid's jealous mother, Venus, Psyche is ultimately granted immortality by the gods and permitted to marry her beloved.
> 
> The figures can be identified as follows:
> 
> *   **Psyche:** The central female figure in the orange and white gown. She is the bride, receiving the wedding ring. Her story is an allegory for the soul's journey to unite with divine love.
> *   **Cupid:** The winged youth placing the ring on Psyche's finger. He is the god of love and the groom. His quiver of arrows can be seen at his side.
> *   **Hymen (or Hymenaeus):** The winged figure in the red cloak standing behind the couple and holding a flaming torch. He is the god of marriage ceremonies, and the marriage torch is his primary attribute.
> *   **Venus (or Aphrodite):** The goddess on the left, arriving in a golden chariot that rests on clouds. She is Cupid's mother, who initially opposed the union but is now present at the sanctioned wedding. She holds a bow, likely belonging to her son. At the bottom of the painting, near Psyche's feet, are two yoked doves, birds sacred to Venus that often pull her chariot and symbolize love and fidelity.
> *   **A Zephyr or another attendant deity:** The winged figure in the upper right, reclining on a cloud, is likely a wind god (a Zephyr) or another divine attendant witnessing the celestial event.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:44:08+00:00_

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

> Marriage of Cupid and Psyche

