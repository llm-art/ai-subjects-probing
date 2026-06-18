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

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:43:46+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Giorgio Vasari",
>   "title": "Perseus and Andromeda",
>   "date": "c. 1570-1572",
>   "collection": "Palazzo Vecchio, Florence"
> }
> ```

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

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:51+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Hendrick de Clerck",
>   "title": "The Triumph of Amphitrite",
>   "date": "c. 1610",
>   "collection": "Museo del Prado"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:07:44+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This painting is a late 16th or early 17th-century Flemish Mannerist artwork, typically attributed to **Hendrick de Clerck** (or a contemporary from the circle of Frans Francken II or Joachim Wtewael), depicting a classical mythological scene—most likely **The Triumph of Neptune and Amphitrite** or **The Contest between Minerva and Neptune** for the patronage of Athens.
> 
> ### Key Elements Depicted:
> 
> *   **Minerva (Athena) in the Foreground:** On the right, the goddess Minerva stands on the shore with her back to the viewer. She is identified by her plumed helmet, her spear, a draped pink sash, and her shield resting at her feet, which features the *Gorgoneion* (the head of Medusa).
> *   **The Sea Procession (Triumph of Neptune and Amphitrite):** 
>     *   In the center, **Amphitrite** (or Galatea) reclines gracefully on a large shell or sea creature, surrounded by sea nymphs (nereids) and tritons.
>     *   Behind her, **Neptune (Poseidon)** is visible holding his signature trident.
>     *   Various tritons blow conch shells, and putti (cupids) ride fantastical sea monsters and dolphins through the water.
> *   **The Celestial Realm:** In the clouds above, several Olympian deities look down upon the scene:
>     *   On the left, a winged figure of **Fame** blows a trumpet.
>     *   In the center, a male deity (likely **Jupiter/Zeus**) sits atop a globe holding a scepter.
>     *   On the right, another female deity (possibly **Juno** or **Venus**) rests on a cloud.
> *   **The Landscape:** The background features a dramatic coastal landscape with a stone arch bridge, a castle perched on a cliff, and distant ships on the horizon. On the left, an olive tree branch hangs over the scene, which is a key symbol of Minerva's victory in her contest against Neptune.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:07:58+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This is a Flemish Mannerist oil painting by **Hendrick de Clerck** (c. 1560–1630), titled ***The Triumph of Amphitrite*** (or *Neptune and Amphitrite*). 
> 
> ### **Subject and Scene**
> The painting depicts a mythological scene celebrating the triumph of the sea goddess **Amphitrite**, watched from the shore by the goddess **Minerva**. 
> 
> ### **Key Figures Depicted**
> * **Minerva (Athena):** Standing in the right foreground with her back to the viewer. She is identified by her plumed helmet, her spear, and her shield (the Aegis) bearing the face of Medusa.
> * **Amphitrite:** The central nude female figure reclining on a shell in the water, being crowned with a laurel wreath by a hovering putto (cupid).
> * **Neptune (Poseidon):** The bearded sea god standing just behind Amphitrite, holding his signature trident.
> * **Tritons and Nereids:** The sea-dwelling creatures, half-human and half-fish, who accompany the procession, blowing conch shells and riding sea monsters.
> * **Putti (Cupids):** Winged infants riding dolphins and sea beasts in the water.
> * **Celestial Figures (in the clouds):** 
>   * On the left, **Fame** (or Pheme) is depicted blowing a trumpet.
>   * In the center and right, other allegorical figures (possibly representing Divine Providence or the Liberal Arts) look down upon the scene.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:08:13+00:00_

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

