# Probe report — `sacrifice-venus-temple`

[![sacrifice-venus-temple](https://media.rkd.nl/iiif/2/10889194/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10889194/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10889194/info.json)_

- **Ground-truth subject:** Sacrifice to Venus in a temple
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/sacrifice-venus-temple.jpg` — native 4122×3854 px, sent 2048×1915 px
- **SHA-256:** `add80dac510aada3b60874a8399e1307e13403586842ba59a697f15bbb050534`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:45:43+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a famous painting from the Baroque period.
> 
> **Artist:** Peter Paul Rubens
> 
> **Title:** *The Feast of Venus* (or *The Worship of Venus*)
> 
> **Approximate Date:** c. 1636–1637
> 
> **Collection:** Kunsthistorisches Museum, Vienna
> 
> This painting is Rubens's interpretation of a subject famously depicted by the Renaissance master Titian. The scene is based on the writings of the ancient Greek author Philostratus, who described a painting of cupids gathering apples in a garden sacred to the goddess Venus. In the painting, numerous putti (cherubic infants) celebrate in a fertile landscape before a statue of Venus, the goddess of love, who is being honored by nymphs.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:45:55+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, this is a large and dynamic Baroque painting depicting a mythological scene, likely **The Worship of Venus** or **The Feast of Venus**.
> 
> Here is a detailed description of what is depicted:
> 
> **Central Theme and Figures:**
> The painting is a vibrant celebration dedicated to Venus, the Roman goddess of love, beauty, and fertility. Her presence is represented in two ways:
> 1.  **A Statue:** On the right, there is a classical-style stone statue of a nude Venus standing on an ornate pedestal. A dolphin-like creature is carved at her feet, a common attribute of the goddess who was born from the sea.
> 2.  **In the Sky:** In the upper right corner, a chariot pulled by two white swans flies through the clouds. This is another traditional representation of Venus.
> 
> Two female figures, likely nymphs or priestesses, are shown making an offering to the statue. One, in a red skirt and white blouse, kneels and holds up a golden, ornate mirror towards the statue, as if to show the goddess her own beauty. Another woman, in a blue dress, stands behind her, also looking up at the statue.
> 
> **The Multitude of Putti (Cupids):**
> The most striking feature of the painting is the immense crowd of chubby, winged infants, known as putti or *Amores* (Cupids). They fill the landscape with energetic and playful activity, symbolizing the various facets of love:
> *   **Play and Merriment:** Many are dancing, wrestling, embracing, and kissing. Some raise their arms in joyous celebration.
> *   **Fertility and Abundance:** They are seen climbing fruit trees (likely apple trees, another symbol of Venus) and harvesting the fruit. A basket of grapes and other fruits sits in the foreground. Some putti are eating the fruit.
> *   **The Power of Love:** In the lower right, one cupid aims a bow and arrow, the classic tool for inspiring love.
> *   **General Frolicking:** They are everywhere—tumbling out of the sky, playing in a wooden tub, and swarming across the grassy landscape.
> 
> **Setting and Atmosphere:**
> The scene is set in a lush, idyllic landscape. A dense grove of dark trees dominates the left side, while the right side opens up to a more distant view of rolling hills and a bright, cloud-filled sky. The lighting is dramatic, with a warm glow on the horizon suggesting either dawn or dusk, creating a sense of magical realism. The overall mood is one of joyous, chaotic, and sensuous celebration.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:46:14+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts a mythological scene known as **The Worship of Venus** or **The Feast of Venus**.
> 
> Here is a breakdown of the figures and the episode:
> 
> *   **The Subject:** The scene is an allegorical celebration of the Roman goddess of love, beauty, and fertility, Venus. It is not based on a single narrative myth but is inspired by the *Imagines*, a text by the 3rd-century Greek writer Philostratus the Elder, who described a painting of such a festival.
> 
> *   **Venus:** The goddess herself is represented by the stone **statue** on the pedestal on the right side of the composition. She is depicted as a classical nude, the traditional way of showing her. In the sky at the top right, her chariot, pulled by her sacred birds (swans or doves), can be seen.
> 
> *   **The Worshippers:** The two women on the right are nymphs or human worshippers participating in the festival. One, in a red and white dress, holds a **mirror** up to the statue. The mirror is a classic attribute of Venus, symbolizing beauty and vanity. This act is one of devotion and offering.
> 
> *   **The Putti (or Amorini/Cupids):** The scene is dominated by a multitude of playful, winged, cherubic infants. These are the attendants of Venus, known as *putti* or *amorini*. They embody the various aspects of love. Their activities are central to the theme:
>     *   They are gathering **apples** from the trees, a fruit sacred to Venus.
>     *   They play, dance, wrestle, and kiss, representing the joyful and sometimes contentious nature of love.
>     *   In the lower right, one putto aims a **bow and arrow**, the traditional weapon of Cupid, used to incite love or desire.
> 
> The overall painting is a vibrant, dynamic, and sensuous celebration of love in all its forms, from innocent play to divine power. The lush landscape and the sheer abundance of figures create an atmosphere of fertility and life.
> 
> This specific work is a famous masterpiece of the Flemish Baroque painter **Peter Paul Rubens**, painted around 1636.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:46:32+00:00_

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

> Sacrifice to Venus in a temple

