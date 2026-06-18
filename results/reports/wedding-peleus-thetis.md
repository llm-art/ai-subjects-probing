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

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:43:45+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Joachim Wtewael",
>   "title": "The Wedding of Peleus and Thetis",
>   "date": "c. 1612",
>   "collection": "Alte Pinakothek, Munich"
> }
> ```

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

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:57+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Frans Floris",
>   "title": "The Feast of the Gods",
>   "date": "1550",
>   "collection": "Royal Museum of Fine Arts Antwerp"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:07:53+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details and artistic style, this painting depicts **"The Feast of the Gods"** (also commonly represented as **"The Banquet of the Gods"** or **"The Wedding of Peleus and Thetis"**), a popular subject in late 16th and early 17th-century Flemish Mannerist art (often associated with artists like Hendrick de Clerck, Hendrick van Balen, or Frans Floris).
> 
> ### Key Elements and Figures Depicted:
> 
> * **The Central Figures (Foreground):**
>   * **Venus (Aphrodite):** The standing nude female figure in the center, draped with a vibrant red cloak behind her, representing beauty and love.
>   * **Ceres and Bacchus (Left):** To the left, figures representing agriculture and wine are shown. A seated figure with a red drape reaches toward a dark-skinned child holding fruit, while another figure behind them holds a platter of grain/bread (Ceres). This composition often references the classical proverb *"Sine Cerere et Baccho friget Venus"* (Without Ceres/food and Bacchus/wine, Venus/love freezes).
>   * **Putti/Cupids:** In the lower foreground, several young children (putti) are shown: one carrying a silver plate of red cherries/berries, and another on the bottom right playing with a large melon.
>   * **Hebe or Ganymede (Far Right):** A female figure dressed in red pours nectar or wine from a large silver ewer (pitcher) into a cup, serving the assembly.
> 
> * **The Banquet (Background):**
>   * A long table draped in a white tablecloth is filled with various Olympian gods and goddesses dining. 
>   * Near the center of the table sits a crowned male figure holding a golden goblet, representing **Jupiter (Zeus)**, the king of the gods.
> 
> * **Still Life and Setting:**
>   * **Abundance of Fruit:** The foreground features a rich display of harvested fruits, including baskets of grapes, apples, pears, and various gourds/melons, symbolizing fertility, nature's bounty, and celebration.
>   * **Lush Landscape:** The feast takes place in a wooded, twilight glade, with dense forest foliage framing the scene.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:08:12+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This is a European oil painting depicting **The Feast of the Gods** (also commonly referred to as *The Banquet of the Gods* or *The Wedding of Peleus and Thetis*), a highly popular mythological subject in Renaissance and Baroque art (particularly within Flemish Mannerism).
> 
> ### **The Scene**
> The painting depicts the Olympian gods gathered for a grand outdoor banquet, celebrating with an abundance of food, wine, and fruit, symbolizing harmony, peace, and divine luxury.
> 
> ### **Key Figures Depicted**
> * **Venus (Aphrodite):** The central, prominent standing nude female figure, representing beauty and love.
> * **Jupiter (Zeus):** Seated at the center of the banquet table wearing a golden crown, presiding over the feast.
> * **Juno (Hera):** Seated next to Jupiter at the table.
> * **Hebe (or Ganymede):** On the far right, wearing a red robe and pouring nectar or wine from a large silver pitcher into a cup.
> * **Bacchus (Dionysus) & Ceres (Demeter):** Represented through the themes of wine and harvest. The figures on the left handling grapes and the abundance of melons, squashes, and fruit baskets in the foreground pay tribute to these deities of agriculture and wine.
> * **Cupid (Amor) and Putti:** The young children in the foreground, one carrying a plate of cherries, another playing with a melon, and a dark-skinned child offering grapes on the left.
> * **Mercury (Hermes):** Visible further down the table wearing his characteristic traveler's hat/helmet.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:08:33+00:00_

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

