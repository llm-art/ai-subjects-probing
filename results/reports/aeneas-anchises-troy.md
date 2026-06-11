# Probe report — `aeneas-anchises-troy`

- **Ground-truth subject:** Aeneas rescues his father Anchises from the burning Troy
- **Category:** mythology · **Tier:** A
- **Institution:** rkd
- **Image:** `data/images/aeneas-anchises-troy.jpg` — native 1878×1239 px, sent 1878×1239 px
- **SHA-256:** `fa3672d6e740e968bf5a3848413209c22dfcd3a28921dc659fd351c08fd71a32`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-11T13:02:32+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this artwork is:
> 
> *   **Artist:** Frans Francken the Younger
> *   **Title:** *The Fall of Troy* (or *The Burning of Troy*)
> *   **Approximate Date:** c. 1630-1635
> *   **Collection:** I cannot identify the specific collection for this painting.
> 
> The painting depicts the mythological sack of the city of Troy. Key elements from the story are visible: the city is engulfed in flames under a dark, smoky sky. In the middle ground,

### Probe B-plain — Open identification, no context

_Run: 2026-06-11T13:02:54+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general knowledge of classical mythology, this painting depicts the **Sack of Troy**.
> 
> Here are the key elements that identify the scene:
> 
> *   **The Trojan Horse:** In the middle ground, the massive wooden horse, the central element of the myth, is shown inside the city walls. This was the subterfuge used by the Greeks to infiltrate the city.
> *   **The Burning City:** The entire city in the background is engulfed in flames under a dark, smoky, and fiery sky, illustrating the destruction and fall of Troy.
> *   **Fleeing Citizens:** The foreground is filled with panicked Trojans attempting to escape the chaos. Their expressions and postures convey terror and desperation.
> *   **Aeneas and his Family:** On the lower right, a specific and famous group is depicted. A man (the hero Aeneas) is carrying an elderly man (his father, Anchises) on his shoulders, while a young boy (his son, Ascanius) follows. This is a classic iconographic representation of Aeneas's escape from Troy as described in Virgil's *Aeneid*.
> *   **Classical Architecture:** The scene is set amidst grand, albeit now ruined, classical architecture, such as the large arch and columns in the foreground, signifying the downfall of a great civilization.
> 
> In summary, the painting is a dramatic narrative depiction of the final moments of the Trojan War, capturing the destruction of the city and the tragic flight of its survivors.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-11T13:03:11+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge, this painting depicts the **Sack of Troy**.
> 
> This famous episode from Greek mythology describes the end of the Trojan War. The key elements visible in the painting that identify this scene are:
> 
> 1.  **The Trojan Horse:** In the middle ground, a massive wooden horse is visible inside the city walls, confirming the subject. This was the Greeks' stratagem to infiltrate the heavily fortified city of Troy.
> 2.  **The Burning City:** The entire city is engulfed in flames under a dark, smoke-filled sky, illustrating the destruction and chaos of the sack, which took place at night.
> 3.  **Fleeing Figures:** People are shown in panic, fleeing the city. In the lower right foreground, a specific and famous group can be identified:
>     *   The man carrying an elderly man on his shoulders is the Trojan hero **Aeneas**.
>     *   The elderly man he is carrying is his father, **Anchises**.
>     *   The small boy clutching Aeneas's hand is his son, **Ascanius** (or Iulus).
> 
> This depiction of Aeneas escaping the fallen city with his family is a classic and central theme of the story, famously recounted in Virgil's epic poem, the *Aeneid*.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-11T13:03:25+00:00_

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

> Aeneas rescues his father Anchises from the burning Troy

### Probe C — Closed verification checklist (expert-scored, semantic match)

_Run: 2026-06-11T13:03:39+00:00_

**Element 1: Pietas motif**

Q: Is there a figure carrying another person on their back? Describe the two figures.

> Yes, there is a figure carrying another person on their back in the lower right portion of the painting.
> 
> Based on the image and common artistic depictions of this scene:
> 
> *   **The person being carried** is an elderly man with white or gray hair and a beard. He is wearing a light-colored tunic and is being carried piggyback style.
> *   **The person doing the carrying** is a younger, muscular man who appears to be a soldier or warrior. He is wearing a short tunic and is striding forward, away from the burning city.
> 
> This is a classic depiction of the hero Aeneas escaping the burning city of Troy, carrying his elderly father, Anchises, on his back.

_Reference:_ Yes — young adult male carrying older male

- [ ] Expert score (1 = correctly identified, semantic match)

**Element 2: Child present**

Q: Is there a child accompanying the central group? Where is the child positioned relative to the carrying figure?

> Yes, there is a child accompanying the group.
> 
> The child is positioned to the right of the figure carrying the elderly man. The child is walking alongside him, slightly behind his right leg, and appears to be holding his hand while looking back towards the burning city.

_Reference:_ Yes — small child beside/holding hand of carrier

- [ ] Expert score (1 = correctly identified, semantic match)

**Element 3: Burning setting**

Q: What is happening in the background? Is there fire, smoke, or destruction visible?

> Yes, the background is filled with dramatic scenes of fire, smoke, and destruction.
> 
> *   **Smoke and Sky:** The sky above the city is a tumultuous vortex of dark smoke and glowing embers. It's painted in fiery shades of red, orange, and black, indicating a massive fire is raging.
> *   **Fire:** Flames and thick plumes of black smoke can be seen rising from numerous buildings throughout the city, suggesting the fire is widespread.
> *   **Destruction:** The entire scene portrays a city in the midst of a catastrophic event, being completely consumed by fire. On the left side of the painting, a large classical archway is depicted in a state of ruin, with parts of it crumbling. The overall impression is one of chaos and total devastation.

_Reference:_ Yes — burning city, smoke, ruins

- [ ] Expert score (1 = correctly identified, semantic match)

**Element 4: Classical architecture**

Q: Describe the architectural setting visible in the image.

> Based on the image, the architectural setting is a grand and sprawling classical city, depicted in a state of chaos and destruction. Here's a breakdown of the visible elements:
> 
> *   **Foreground Ruins:** The scene is framed on the left by large, dark, and crumbling classical ruins. This structure features massive fluted columns with ornate Corinthian-style capitals, a heavy entablature, and a large, broken archway. Its dilapidated state sets a tone of decay and disaster.
> 
> *   **The City Proper:** The main city in the background is dense and magnificent. It is built on a waterfront or harbor. The architecture is a mix of styles, suggesting a wealthy and powerful metropolis:
>     *   **Classical Structures:** Many buildings are white or light-colored, featuring classical elements like columns, pediments, and rectangular forms, reminiscent of ancient Greek and Roman cities.
>     *   **Ornate Buildings:** To the right, there are more elaborate, multi-tiered buildings topped with striking blue domes and cupolas. These have a more fantastical or perhaps later architectural influence, adding to the epic quality of the scene.
>     *   **Fortifications and Infrastructure:** The city appears to be walled. A prominent stone bridge or causeway leads into the city from the left, upon which a giant wooden horse is being moved.
> 
> *   **Waterfront and Harbor:** The city is built around a body of water, with buildings rising directly from the edge. Several large, masted sailing ships are docked in the harbor, suggesting it is a major port city.
> 
> Overall, the architecture portrays a majestic, classical city of great scale and importance, making its fiery destruction all the more dramatic and tragic.

_Reference:_ Arches, columns, stone — classical/ancient city

- [ ] Expert score (1 = correctly identified, semantic match)

**Element 5: Small dog**

Q: Is there an animal in the image? If so, describe it and its position.

> Yes, there is a very prominent animal figure in the image.
> 
> It is a **massive wooden horse**, often identified as the Trojan Horse.
> 
> *   **Description:** The horse is a colossal structure, appearing to be made of wood planks. It is much larger than the surrounding people and buildings. It is depicted in a stylized, somewhat blocky form.
> *   **Position:** It is located in the middle ground, to the left of the center of the painting. It stands on a wide bridge or ramp that leads into the city, and it is surrounded by a crowd of people who appear to be pulling it towards the city gates.

_Reference:_ Small dog, lower right — iconographically non-obvious; reporting it is strong evidence of genuine visual processing

- [ ] Expert score (1 = correctly identified, semantic match)

