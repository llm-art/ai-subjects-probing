# Probe report — `circe-sorceress`

[![circe-sorceress](https://iiif.artresearch.net/iiif/3/frick/4107100289952_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100289952_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100289952_0001.jp2/info.json)_

- **Ground-truth subject:** The Sorceress Circe
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/circe-sorceress.jpg` — native 5957×4794 px, sent 2048×1648 px
- **SHA-256:** `5f1edb331dc72225138a3a2df78c5de3ae725e6399bf92787f2a8a008c887730`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:46:07+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Jacopo Bassano",
>   "title": "The Sorceress Circe",
>   "date": "c. 1570s",
>   "collection": "Kunsthistorisches Museum, Vienna"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:00:44+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a black and white photograph of a painting, likely from the Baroque period, depicting a complex mythological or allegorical scene. The composition is crowded with figures and objects, set against a dark, indistinct background, creating a dramatic and mysterious atmosphere.
> 
> **Central Figure:**
> The focal point is a woman seated on the left. She is semi-nude, with her upper body exposed and a dark, ornate cloth draped over her lap. She wears a turban-like headdress and looks off to the right with a composed, powerful expression. She leans back against a cushion, exuding an air of command.
> 
> **Animals:**
> She is surrounded by a diverse menagerie of animals:
> *   **Cow:** A large cow stands directly behind her, looking out towards the viewer.
> *   **Turkey:** In the center of the composition is a turkey.
> *   **Badger:** A badger is visible peeking out from beneath the turkey.
> *   **Dog:** On the right, a dog, possibly a hound, is seen from behind.
> *   **Owl:** In the upper right corner, an owl is perched or in flight.
> *   **Cat/Wildcat:** To the left, behind the woman's shoulder, a feline, possibly a wildcat, is perched on a ledge.
> *   **Goat/Ram:** In the upper left background, the head of a goat or ram can be seen.
> 
> **Objects:**
> The foreground is filled with various objects that seem to have been cast aside:
> *   **Left Foreground:** A stack of books, one of which is open, lies on the ground. Next to them is an ornate, lidded silver or pewter urn.
> *   **Right Foreground:** A collection of armor, including a helmet, a gauntlet, and other pieces, is scattered on the floor next to a decorated bowl.
> 
> **Interpretation:**
> The collection of elements strongly suggests a depiction of the enchantress **Circe** from Greek mythology. In the story from Homer's *Odyssey*, Circe used her magic to transform men into animals. The painting shows her in her power, surrounded by her victims in their animal forms. The discarded books (representing knowledge) and armor (representing warfare and strength) symbolize the human attributes that her victims have lost, now useless at the feet of the sorceress.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:01:06+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology and art history, this painting depicts the mythological sorceress **Circe**.
> 
> Here is a breakdown of the scene and its figures:
> 
> *   **The Subject:** The episode is from Homer's *Odyssey*. Circe was a powerful enchantress who lived on the island of Aeaea. She was known for luring sailors to her home and then, with a magic potion and a touch of her wand, transforming them into animals.
> 
> *   **The Figures and Elements:**
>     *   **Circe:** The central figure is the semi-nude woman seated in a commanding pose. Her exotic turban, confident gaze, and the magical paraphernalia around her identify her as the enchantress.
>     *   **The Animals:** The various animals surrounding her are not a random menagerie; they are her victims. They represent the companions of Odysseus and other unfortunate men who have been transformed by her magic. We can see:
>         *   A **cow** standing prominently behind her.
>         *   A **dog** (likely a hound) in the lower right.
>         *   A **turkey** and a **badger** in the center.
>         *   An **owl** in flight in the upper right, often a symbol of night, wisdom, or magic.
>         *   Other animals, possibly a **wildcat** and **goats**, are visible in the shadowy background to the left.
>     *   **Symbolic Objects:** The objects in the foreground reinforce the narrative:
>         *   **Books:** In the lower left, a pile of books, one open, symbolizes her knowledge of spells and magic.
>         *   **Armor:** In the lower right, a discarded helmet, gauntlet, and other pieces of armor likely belonged to a warrior who fell victim to her, symbolizing the triumph of her magic over martial strength.
>         *   **Ornate Vessels:** The decorative urns and bowls suggest wealth and the luxurious, seductive nature of her trap.
> 
> The painting captures Circe in her element, surrounded by the evidence of her power—the men she has turned into beasts and the spoils she has taken from them. The inclusion of a **turkey**, a bird native to the Americas, is an anachronism typical of European art from the 16th century onward, used to add an exotic and wondrous feel to the scene.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:01:28+00:00_

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

> The Triumph of Mars: an Allegory of War

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:50:31+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {"recognized": true, "artist": "Giovanni Benedetto Castiglione", "title": "The Sorceress Circe", "date": "c. 1650", "collection": "J. Paul Getty Museum"}

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:15:21+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details and historical context, this image depicts the Baroque painting **"Circe"** (also known as **"The Sorceress Circe"**) by the Italian artist **Giovanni Benedetto Castiglione** (Il Grechetto), painted around 1650. 
> 
> ### Key Elements Depicted:
> * **Circe:** The mythological sorceress is seated on the left, semi-nude and wearing a turban. She holds a wand, representing her magical power.
> * **Magical Tools:** At her feet lie large open books of magic spells, a human skull, and an ornate metal vessel, symbolizing her practice of witchcraft and alchemy.
> * **Transformed Men (Animals):** Surrounding her are various animals, which represent the companions of Odysseus (Ulysses) whom she has transformed into beasts. Visible animals include:
>   * A large **cow** standing directly behind her.
>   * A **turkey** and a **badger** in the center.
>   * A **dog** viewed from behind on the right.
>   * Birds (including an owl) in the dark background.
> * **Discarded Armor:** A pile of empty, discarded plate armor (including a helmet and gauntlets) lies on the ground, symbolizing the defeated warriors who have been stripped of their humanity and weapons.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:15:28+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual details, this painting depicts the mythological scene of **Circe the Sorceress** (from Homer's *Odyssey*). 
> 
> ### Key Figures and Elements Depicted:
> * **Circe:** The enchantress is shown seated on the left, semi-nude and wearing a turban, holding her magic wand. 
> * **Odysseus's Companions:** The various animals surrounding her—including the cow, the dog, the badger, and the large bird (turkey)—are Odysseus's men whom she has transformed into beasts.
> * **Discarded Armor:** The pile of armor on the ground represents the gear left behind by the transformed soldiers.
> * **Tools of Magic:** At her feet lie a large open book of spells (grimoire), a human skull, and an ornate vessel, symbolizing her practice of witchcraft and alchemy.
> 
> This composition is a well-known work by the Italian Baroque artist **Giovanni Benedetto Castiglione** (also known as *Il Grechetto*), painted around 1650.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:15:35+00:00_

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

> The Sorceress Circe

