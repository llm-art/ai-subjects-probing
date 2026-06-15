# Probe report — `wedding-peleus-thetis`

[![wedding-peleus-thetis](https://media.rkd.nl/iiif/2/9222402/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9222402/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9222402/info.json)_

- **Ground-truth subject:** The wedding of Peleus and Thetis
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/wedding-peleus-thetis.jpg` — native 4129×2848 px, sent 2048×1413 px
- **SHA-256:** `65c8e7371e57a573416f4a811f0bc2864acc3787c5875184a6705fa87c72251f`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:42:00+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the style and subject matter visible in the image, this is a well-known work of Dutch Mannerism.
> 
> **Artist:** Joachim Wtewael
> **Title:** *The Wedding of Peleus and Thetis*
> **Approximate Date:** c. 1600-1602
> **Collection:** Alte Pinakothek, Munich, Germany
> 
> The painting depicts the mythological wedding feast of the mortal king Peleus and the sea-nymph Thetis, which was attended by the gods and goddesses of Olympus. This event is famous in Greek mythology as the precursor to the Trojan War. The uninvited goddess of discord, Eris, would arrive and toss the Golden Apple inscribed "to the fairest" among the guests, sparking a rivalry between Hera, Athena, and Aphrodite that would ultimately be settled by the Judgment of Paris. Wtewael's composition is characteristic of the Mannerist style, with its crowded arrangement of elegant, elongated, and often nude figures in complex poses.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:42:17+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a classical oil painting depicting a large, festive gathering of mythological figures in a lush, outdoor setting. The scene is likely **"The Feast of the Gods"** or **"The Wedding of Peleus and Thetis,"** a popular subject in Renaissance and Baroque art.
> 
> Here are the key elements visible in the painting:
> 
> *   **Central Figures:** In the center stands a nude goddess, likely Venus (Aphrodite), with a red drapery behind her. She holds one hand to her chest in a gesture of modesty. To her left, another goddess is seated, draped in yellow and blue fabric.
> *   **The Banquet:** In the background, a long table covered with a white cloth is laden with food and drink. Numerous gods and goddesses are seated and standing around it, engaged in conversation and feasting. On the far right, a figure pours a drink from a large silver ewer.
> *   **Foreground Activity:** The foreground is filled with activity and symbols of abundance.
>     *   On the left, a muscular male figure, draped in red, interacts with a small, cherubic child (a putto or cupid).
>     *   Several other putti are present. One carries a dish of red berries, while another on the right plays with a large melon or gourd.
>     *   The ground is strewn with an abundance of fruit, including a basket of grapes and apples, cut watermelons, pears, and flowers like roses.
> *   **Setting and Style:** The scene takes place in a wooded, pastoral landscape under a dark, dramatic sky. The style is characteristic of Northern Mannerism or the late Renaissance, with its crowded composition, elongated and idealized nude figures, rich color palette, and classical subject matter. The overall mood is one of divine revelry and celebration.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:42:35+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge of art history and mythology, this painting depicts a famous episode from Greek mythology: **The Wedding of Peleus and Thetis**.
> 
> Here is a breakdown of the scene and the figures:
> 
> *   **The Episode:** This painting captures the moment that leads to the Trojan War. The scene is the wedding feast of Peleus, a mortal king, and Thetis, a sea-nymph. All the gods and goddesses of Olympus were invited to the celebration, with one crucial exception: Eris, the goddess of Discord.
> 
> *   **The Central Action (The Apple of Discord):** Angered by the snub, Eris arrived uninvited and threw a golden apple into the midst of the guests. The apple was inscribed with the words "For the Fairest." This act, known as the "Apple of Discord," immediately caused a dispute among three powerful goddesses, each of whom claimed the apple for herself.
> 
> *   **The Figures:**
>     *   The numerous figures feasting at the long table in the background are the **gods and goddesses of Olympus**.
>     *   The central group of three prominent female figures represents the three goddesses who vied for the apple: **Hera** (Juno), queen of the gods; **Athena** (Minerva), goddess of wisdom and war; and **Aphrodite** (Venus), goddess of love and beauty. The standing, central nude figure, with her hand to her chest, is likely **Aphrodite**, often depicted as the most beautiful.
>     *   The small, cherubic children are **putti** or, in this context, could include **Cupid** (Eros), the son of Aphrodite. One putto is seen presenting a bowl of fruit (perhaps containing the fateful apple) towards the goddesses, while others play with fruit in the foreground, symbolizing abundance and fertility, but also the "fruit" of discord.
>     *   The figure on the far left, handing an object (likely the apple, or grapes symbolizing the start of the affair) to a putto, could be **Hermes** (Mercury), the messenger god, who is often tasked with delivering the apple for the judgment that will follow this scene.
> 
> This event is the direct prequel to the **Judgment of Paris**, where the Trojan prince Paris was chosen to decide which of the three goddesses was the fairest. His choice of Aphrodite, who had promised him the most beautiful mortal woman (Helen of Sparta) in return, ultimately led to the Trojan War. The painting thus captures a moment of celebration that is pregnant with future conflict and tragedy.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:42:55+00:00_

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

