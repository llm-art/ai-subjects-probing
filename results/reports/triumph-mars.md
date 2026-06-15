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

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:43:32+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, I can identify this artwork.
> 
> **Artist:** Guilliam van Nieulandt II (also known as Willem van Nieulandt II)
> 
> **Title:** *The Triumph of a Roman General*
> 
> **Date:** 1620 (The date and the artist's signature, "GVR. NIEVLANT 1620", are visible in the bottom right corner of the painting).
> 
> **Collection:** Royal Collection Trust, United Kingdom.

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

