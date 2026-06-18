# Probe report — `aeneas-anchises-troy`

[![aeneas-anchises-troy](https://media.rkd.nl/iiif/2/9223046/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9223046/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9223046/info.json)_

- **Ground-truth subject:** Aeneas rescues his father Anchises from the burning Troy
- **Category:** mythology · **Tier:** A
- **Institution:** rkd
- **Image:** `data/images/aeneas-anchises-troy.jpg` — native 1878×1239 px, sent 1878×1239 px
- **SHA-256:** `fa3672d6e740e968bf5a3848413209c22dfcd3a28921dc659fd351c08fd71a32`
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
>   "artist": "El Greco (Doménikos Theotokópoulos)",
>   "title": "The Fall of Troy",
>   "date": "c. 1596-1600",
>   "collection": "National Gallery of Greece"
> }
> ```

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

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:50+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Gillis van Valckenborch",
>   "title": "The Burning of Troy",
>   "date": "c. 1600",
>   "collection": null
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:07:47+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This painting depicts the **Fall of Troy** (or the **Sack of Troy**), a famous event from Greek mythology and Virgil's epic poem, the *Aeneid*. 
> 
> Key elements visible in the scene include:
> 
> *   **The Trojan Horse:** Located in the middle-left, the large wooden horse stands near the city walls as the Greek soldiers invade.
> *   **The Burning City:** The grand classical architecture of Troy is engulfed in raging fires, with thick, dramatic plumes of red and black smoke filling the night sky.
> *   **Aeneas Fleeing Troy:** In the bottom right foreground, the Trojan hero **Aeneas** is shown escaping the destruction. He is carrying his elderly father, **Anchises**, on his back and is accompanied by his young son, **Ascanius** (holding his hand), and his wife, Creusa, following behind.
> *   **Fleeing Citizens:** In the foreground and throughout the city, terrified citizens are shown panicking, fleeing, and seeking shelter amidst the ruins.
> *   **The Harbor:** On the right side, ships are docked in the harbor, representing either the returning Greek fleet or the means of escape for the survivors.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:07:54+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the **Sack of Troy** (also known as the *Burning of Troy* or the *Fall of Troy*), a famous episode from Greek mythology and Virgil's epic poem, the *Aeneid*. 
> 
> ### Key Figures and Details:
> * **Aeneas, Anchises, and Ascanius (bottom right):** The prominent group fleeing in the lower right corner represents the Trojan hero **Aeneas** escaping the burning city. He is carrying his elderly, paralyzed father, **Anchises**, on his back, while leading his young son, **Ascanius** (Iulus), by the hand. His wife, **Creusa**, follows closely behind them.
> * **The Trojan Horse (middle-left background):** The giant wooden horse used by the Greeks to infiltrate and destroy the city is clearly visible standing near the city walls.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:08:04+00:00_

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

_Run: 2026-06-18T13:08:18+00:00_

**Element 1: Pietas motif**

Q: Is there a figure carrying another person on their back? Describe the two figures.

> Yes, there is a figure carrying another person on their back. This group is located in the **lower right foreground** of the painting, depicting the classical scene of Aeneas fleeing the burning city of Troy with his family.
> 
> Here is a description of the two figures:
> 
> *   **The Carrier (Aeneas):** He is a strong, younger man shown in profile, moving toward the right. He is wearing a light blue-grey short tunic or classical armor and is bent forward slightly to support the weight of the person on his back. 
> *   **The Person Being Carried (Anchises):** He is an elderly man with white hair and a white beard. He is draped over the younger man's shoulders, clinging to him for safety, and is dressed in a light-colored robe. 
> 
> Directly behind them, a smaller figure (representing Aeneas's young son, Ascanius) follows closely.

_Reference:_ Yes — young adult male carrying older male

- [ ] Expert score (1 = correctly identified, semantic match)

**Element 2: Child present**

Q: Is there a child accompanying the central group? Where is the child positioned relative to the carrying figure?

> Yes, there is a small child-sized figure accompanying them (traditionally representing Aeneas's young son, Ascanius). 
> 
> The child is positioned **directly to the right (in front of)** the carrying figure, walking ahead of him toward the right edge of the painting while looking back.

_Reference:_ Yes — small child beside/holding hand of carrier

- [ ] Expert score (1 = correctly identified, semantic match)

**Element 3: Burning setting**

Q: What is happening in the background? Is there fire, smoke, or destruction visible?

> Yes, there is widespread fire, smoke, and destruction depicted throughout the background, illustrating the dramatic fall and burning of the city:
> 
> *   **Fire and Smoke:** The entire upper half of the painting is dominated by a dramatic, apocalyptic sky. A massive, glowing orange and red firestorm rages behind the city, casting a hellish light over the buildings. Thick, billowing plumes of dark black smoke rise from the flames, completely choking out the sky at the top and on the right side.
> *   **The Trojan Horse:** In the middle ground to the left of center, the wooden Trojan Horse stands near the city walls, surrounded by tiny figures of soldiers and citizens running in panic and chaos.
> *   **Ruined Architecture:** On the far left, a large, classical stone structure with arches is heavily damaged, darkened, and crumbling, symbolizing the physical destruction of the city. 
> *   **Chaos in the Harbor:** To the right, ships are packed into the harbor as people desperately try to escape by water, set against the backdrop of the burning city.

_Reference:_ Yes — burning city, smoke, ruins

- [ ] Expert score (1 = correctly identified, semantic match)

**Element 4: Classical architecture**

Q: Describe the architectural setting visible in the image.

> The architectural setting is a grand, sprawling cityscape that blends classical antiquity with Italian Renaissance and medieval styles, creating an anachronistic depiction of ancient Troy:
> 
> *   **Crumbling Classical Ruins (Foreground Left):** On the far left stands a massive, dark, and ruined classical structure. It features heavy, fluted columns with ornate capitals (resembling the Corinthian order), a thick entablature, and a crumbling brick archway above, emphasizing the theme of destruction.
> *   **Medieval Fortifications (Middle Ground):** In the center, a dark stone fortress wall with crenellated towers and ramparts divides the foreground from the inner city. A ramp or bridge leads up to these defensive walls.
> *   **Renaissance-Style Palaces and Domes (Background):** 
>     *   Behind the walls lies a vast public square (piazza) lined with grand, white-facaded buildings featuring classical columns, pediments, and arches reminiscent of Renaissance *palazzi*.
>     *   Several prominent domes dot the skyline. Most notable is a large, highly detailed blue-and-white dome on the far right, resembling a Renaissance cathedral or baptistery.
> *   **Towers and Obelisks:** Tall, square medieval-style towers and turrets rise above the city center, while a monumental, free-standing triumphal column (similar to Trajan's Column in Rome) stands near the harbor on the right.
> *   **The Harbor (Right):** The city meets the water with stone docks, embankments, and waterfront buildings where ships are moored, framing the escape route.

_Reference:_ Arches, columns, stone — classical/ancient city

- [ ] Expert score (1 = correctly identified, semantic match)

**Element 5: Small dog**

Q: Is there an animal in the image? If so, describe it and its position.

> Yes, there are animals depicted in the image, both as a monumental object and as living creatures:
> 
> 1.  **The Trojan Horse (Wooden Statue):** 
>     *   **Description:** This is the most prominent animal figure in the painting. It is a large, stylized, brown wooden statue of a horse standing on a wheeled platform.
>     *   **Position:** It is located in the middle ground, slightly to the left of the center, positioned on a ramp or plaza just outside the inner city walls.
> 
> 2.  **Living Horses (Cavalry):**
>     *   **Description:** There are several tiny, active horses being ridden by soldiers. 
>     *   **Position:** They are located in the middle ground, clustered around the base of the Trojan Horse and on the ramp below it, caught up in the chaotic battle and panic.

_Reference:_ Small dog, lower right — iconographically non-obvious; reporting it is strong evidence of genuine visual processing

- [ ] Expert score (1 = correctly identified, semantic match)

