# Probe report — `triumph-mars`

[![triumph-mars](https://media.rkd.nl/iiif/2/10079601/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10079601/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10079601/info.json)_

- **Ground-truth subject:** The triumph of Mars: an Allegory of War
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/triumph-mars.jpg` — native 2506×1909 px, sent 2048×1560 px
- **SHA-256:** `ebcf2072cf966bd9d5528f5e51cc58e02292117d36f29d68f85dbde686018499`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:44:15+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Willem van Nieulandt II",
>   "title": "The Triumph of a Roman General",
>   "date": "c. 1620",
>   "collection": "Herzog Anton Ulrich-Museum"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:43:47+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This painting illustrates a Roman triumphal procession, a grand spectacle celebrating a military victory.
> 
> **Central Focus:**
> The main subject is a victorious Roman general, enthroned high on an ornate, four-wheeled chariot. He wears elaborate silver and gold armor, a plumed helmet, and a red cloak. He brandishes a large sword in his right hand, signifying his military power. Below him, a charioteer in armor and a red cloak drives the two horses, holding a flaming torch aloft. A woman sits beside the general, looking downwards. The chariot itself is laden with the spoils of war, including shields, spears, arrows, and a large banner at the back featuring an eagle.
> 
> **The Procession:**
> *   **Horses:** The chariot is pulled by two powerful horses adorned with ornate, decorative armor (barding).
> *   **Captives:** The procession includes numerous captives, showcasing the general's victory. Leading the procession on the far left are what appear to be high-status prisoners: a woman in a white and blue gown with a laurel wreath, her hands seemingly bound, and a man with wild hair looking back in distress. Following the chariot on the right are more captives, including women in tattered clothes, chained at the wrists and ankles, expressing despair.
> *   **Attendants and Onlookers:** Other figures are part of the scene. A woman in a green and cream dress walks beside the chariot carrying a pitcher. In the background, soldiers and other citizens watch the procession. A small child is held by a woman in a pink dress, and a monkey is visible in the lower right corner, often included in such scenes to represent the exotic lands that were conquered.
> 
> **Setting and Atmosphere:**
> The scene is set on a road outside a large city, visible in the background with its domes, towers, and a bridge. On the left, there is a dark, wooded area and a stone tower. The foreground is littered with the grim evidence of conflict: scattered bones, including a partial skeleton, broken weapons, and discarded tools. This creates a stark contrast between the glory of the triumph and the brutal reality of war. The sky is filled with dramatic, swirling clouds, adding to the epic and somewhat somber mood of the scene.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:44:06+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image, this painting depicts a **Roman Triumph**.
> 
> This was a grand procession held in ancient Rome to celebrate a victorious military commander (the *triumphator*). The key elements of a Roman Triumph are all visible here:
> 
> *   **The Victorious General:** The central figure is the triumphant general, seated high on an ornate chariot. He wears elaborate armor, a plumed helmet, and a red cloak, holding a sword aloft as a symbol of his military power.
> *   **The Triumphal Chariot:** The general rides in a large, decorated chariot, which is laden with the spoils of war, including captured armor, weapons, and military standards (flags). One standard clearly shows an eagle, the symbol of the Roman legions.
> *   **The Procession of Captives:** To the right of the chariot, a group of dejected figures, mostly women and children, are being paraded as prisoners of war. One woman is visibly in chains. This was a common feature of a triumph, meant to display the conquered peoples. The small monkey on the ground is likely an exotic animal brought back as part of the loot.
> *   **Spoils of War:** Besides the items on the chariot, the ground in the foreground is littered with broken weapons and tools, symbolizing the defeated enemy.
> *   **Allegorical Elements:** The skeleton and scattered bones in the foreground are a powerful *vanitas* symbol. They serve as

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:44:26+00:00_

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

_Run: 2026-06-18T13:48:24+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Willem van Nieulandt II",
>   "title": "The Triumph of Scipio Africanus",
>   "date": "1615",
>   "collection": "Rijksmuseum, Amsterdam"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:09:12+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This painting is **"A Roman Triumph"** (or **"The Triumph of a Roman General/Emperor"**), created by the Flemish Golden Age artist **Willem van Nieulandt II** (signed *"GVIL. NIEVLANT"* in the bottom right corner). 
> 
> ### Key Depicted Elements:
> * **The Triumphal Chariot:** A Roman commander or emperor sits high atop an ornate, gilded chariot drawn by two decorated horses. He wears classical Roman armor and a feathered helmet, holding a sword in one hand and a symbol of victory or power (possibly a thunderbolt or laurel) in the other.
> * **The Captives:** Seated dejectedly on the chariot next to the general is a captive woman (likely representing a conquered queen, such as Zenobia of Palmyra, or a personification of a defeated province). Other chained captives walk on foot behind the chariot.
> * **The Charioteer:** A driver in a red cloak guides the horses while holding a burning torch aloft.
> * **Foreground Figures:** 
>   * A woman in the center foreground carries a vessel and a small flame.
>   * On the far left, a woman in a white gown wearing a floral wreath walks ahead, accompanied by a wild, semi-nude figure with spiky hair.
>   * Scattered on the ground are discarded weapons, bones, and a small monkey.
> * **The Setting:** The background depicts a classical cityscape of Rome, featuring prominent Roman architecture, domes, and a bridge spanning the Tiber River (resembling the Ponte Sant'Angelo).

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:09:36+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This is a 17th-century oil painting by the Flemish artist **Willem van Nieulandt II** (signed *"GVIL. NIEVLANT"* in the bottom right corner). 
> 
> ### **Subject and Scene**
> The painting depicts a **Roman Triumphal Procession (Triumph)**, a classical subject celebrating a victorious military commander entering Rome. It is most commonly identified as **The Triumph of Scipio Africanus** (or more generally, **The Triumph of a Roman General / Emperor**).
> 
> ### **Key Figures and Elements**
> * **The Triumphal Chariot:** At the center is a highly ornate chariot drawn by two decorated horses. 
> * **The Victorious General (Scipio Africanus / Roman Commander):** Seated high on the chariot, wearing Roman armor and a feathered helmet, he holds a raised sword in one hand and a bundle of palm branches or fasces (symbols of victory and authority) in the other.
> * **The Conquered Province / Captive Queen:** Seated dejectedly on the chariot next to the general is a mourning woman, representing a conquered territory (such as Carthage or a personified province) or a captive noblewoman.
> * **The River God and Female Companion (Left):** In the left foreground, a wild-haired, semi-nude man crowned with reeds—representing a **River God** (likely the Tiber or a conquered river)—leads a woman in a white gown and floral wreath (representing Peace, Flora, or a personified province).
> * **The Charioteer:** A driver stands at the front of the chariot holding the reins and a raised torch.
> * **Captives and Spoils (Right):** Behind the chariot, chained female captives are led in the procession, accompanied by soldiers, children, and a monkey (often symbolizing defeated vice or exotic spoils).
> * **The Foreground:** Scattered on the ground are broken weapons, bones, and agricultural tools, symbolizing the destructive aftermath of war and the transition to peace.
> * **The Background:** A classical cityscape representing ancient Rome, featuring prominent domes, towers, and a bridge.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:09:59+00:00_

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

