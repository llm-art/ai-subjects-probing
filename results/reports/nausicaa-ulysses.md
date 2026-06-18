# Probe report — `nausicaa-ulysses`

[![nausicaa-ulysses](https://media.rkd.nl/iiif/2/9178976/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9178976/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9178976/info.json)_

- **Ground-truth subject:** The meeting of Nausicaa and Ulysses
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/nausicaa-ulysses.jpg` — native 4552×2999 px, sent 2048×1349 px
- **SHA-256:** `1ff661b875c76420e5168db057adaeb08fdf1ae5a4f3e2f52267da5ffc8a48a1`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:44:17+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Hendrik van Balen the Elder and Jan Brueghel the Elder",
>   "title": "The Feast of the Gods",
>   "date": "c. 1608-1610",
>   "collection": null
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:44:39+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general art historical knowledge, this is a large-scale oil painting in the Baroque style, depicting a mythological or allegorical scene.
> 
> Here is a detailed description of what is depicted:
> 
> **Overall Scene:**
> The painting portrays a lively outdoor feast or gathering in a lush, pastoral landscape. A large group of figures, primarily women and children, are assembled under trees, enjoying food and drink. The atmosphere is one of abundance, leisure, and revelry.
> 
> **Key Figures and Groups:**
> *   **Central Gathering:** The main focus is a group of women, likely goddesses or nymphs, reclining and sitting around a makeshift table or stone altar. They are dressed in flowing, classical-style draperies of rich colors like red, blue, and gold. They are interacting with each other, and some are being served fruit from platters. One prominent woman in a blue dress and a tiara appears to be a figure of high status.
> *   **The Spying Figure:** In the lower-left foreground, a muscular, bearded, and dark-skinned man, likely a satyr or a river god, is partially hidden by foliage and vines. He seems to be observing the gathering of women.
> *   **Putti (Cherubic Children):** Several nude, cherubic children, known as putti, are scattered throughout the scene. In the lower right, one carries a large watermelon, while two others play with fruit. Near the center, two more putti offer a bowl of fruit to the woman in the blue dress.
> *   **Background Figures:** In the background to the right, another group of women is visible. One balances a large terracotta jug on her head. To the left, a white horse, possibly part of a chariot, can be seen in a clearing in the woods.
> 
> **Setting and Composition:**
> The scene is set in an idyllic landscape with large, leafy trees framing the composition. A large, dark red canopy is draped over the main group. In the distance, a river or lake and rolling hills are visible under a soft, atmospheric sky. The composition is dynamic and crowded, with figures arranged in overlapping groups to create a sense of depth and activity. The use of light and shadow (chiaroscuro) is dramatic, highlighting the pale skin of the women and the vibrant colors of their robes against the darker tones of the landscape and the foreground satyr.
> 
> **Interpretation:**
> The subject is clearly mythological. Scenes like this were common in Flemish Baroque painting, particularly in the circle of Peter Paul

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:44:58+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of art history, this painting depicts a mythological scene, specifically a **Bacchanal** or a **Feast of the Gods**.
> 
> Here is a breakdown of the episode and figures:
> 
> *   **The Subject:** The scene is a Bacchanal, a feast or revelry in honor of Bacchus (the Roman god of wine, fertility, and ecstasy, known as Dionysus in Greek mythology). Such scenes were popular in Baroque art as they allowed for the depiction of dynamic compositions, lush landscapes, abundant still life, and the human form in various states of celebration.
> 
> *   **The Figures:**
>     *   **Nymphs or Maenads (Bacchantes):** The numerous women gathered around the table are likely nymphs (nature spirits) or Maenads, the female followers of Bacchus. They are shown feasting, conversing, and enjoying the abundance of nature. They are dressed in classical-style drapery, and some wear jewelry or have elaborate hairstyles, indicating a divine or mythological status.
>     *   **Satyr:** In the lower-left corner, partially obscured by foliage, is a muscular, bearded male figure. This is almost certainly a satyr, a mythological creature with goat-like features (though not always prominent) who was a companion of Bacchus. Sat

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:45:26+00:00_

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

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:48:27+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Peter Paul Rubens",
>   "title": "The Finding of Erichthonius",
>   "date": "ca. 1632-1633",
>   "collection": "Allen Memorial Art Museum"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:10:35+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this is a Flemish Baroque painting depicting an outdoor mythological or allegorical banquet, likely representing a **Feast of the Gods** or a celebration of abundance and fertility (associated with deities like Ceres, Bacchus, or Venus). 
> 
> Here are the key elements depicted in the image:
> 
> *   **The Banquet:** A group of elegantly draped women in classical attire (in vibrant shades of red, blue, yellow, and white) are gathered around a table laden with fruit in a lush, wooded landscape.
> *   **Putti (Cherubs):** Several winged and wingless putti interact with the women. On the left, one putto offers a plate of fruit to a seated woman wearing a blue bodice and red skirt. In the foreground, three putti play on the ground; one holds a large striped melon, while others play with fruit near an ornate silver ewer (pitcher) resting on a golden platter.
> *   **Reclining Figure:** In the bottom-left corner, a bearded, muscular male figure (likely a river god or woodland deity) reclines amidst dark foliage, watching the festivities.
> *   **Background Details:** 
>     *   On the far left, a white horse stands harnessed to a carriage or chariot under a canopy.
>     *   In the background behind the table, figures are seen playing a lute and pouring liquid from a large jug.
>     *   The scene opens up on the right to a distant landscape with hills and a cloudy sky.
> 
> The style of the painting—characterized by rich, warm colors, voluptuous figures, and a dynamic, crowded composition—is highly characteristic of the **Flemish Baroque** period, particularly the school or circle of **Peter Paul Rubens** and collaborators like **Hendrick van Balen** or **Jan Brueghel the Elder**.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:10:49+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual details and iconographical elements, this Flemish Baroque painting depicts **The Feast of the Nymphs** (also commonly referred to as *The Banquet of the Nymphs* or *The Feast of the Gods*), a popular mythological and pastoral subject in 17th-century Flemish art (highly characteristic of the **School of Peter Paul Rubens** or collaborators like **Hendrick van Balen** and **Jan Brueghel the Elder**).
> 
> ### **Key Figures and Elements Depicted:**
> 
> 1. **The Nymphs (and Goddesses):** 
>    * A group of elegant, fleshy women (nymphs) are gathered around a banquet table in a lush, wooded landscape. 
>    * The central seated figure on the left, wearing a blue and red gown and a small tiara/crown, is likely **Diana** (the goddess of the hunt and moon, who is traditionally accompanied only by her nymphs) or a leading nymph queen. She is shown receiving a plate of fruit.
>    * Other nymphs are engaged in various festive activities: one plays a **lute** in the background, others carry baskets of flowers, and one pours wine or water from a large pitcher on the right.
> 
> 2. **The River God (Bottom Left):**
>    * Reclining in the lower-left corner is a bearded **river god**, crowned with aquatic reeds and leaves. He leans on a large urn from which water flows, a classical symbol of a local river, water source, and fertility.
> 
> 3. **Putti / Cherubs (Foreground):**
>    * Several chubby **putti** (cupids) are playing in the foreground. One holds a melon/gourd, another holds grapes, and one kneels near a decorative silver **ewer and basin** (a classic Flemish still-life detail). They assist in serving fruit to the banquet.
> 
> 4. **Chariot and White Horses (Left Background):**
>    * In the background on the left, a chariot drawn by white horses is visible, which likely belongs to **Diana** (the moon goddess) or **Apollo** (the sun god), reinforcing the mythological setting.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:11:35+00:00_

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

> The meeting of Nausicaa and Ulysses

