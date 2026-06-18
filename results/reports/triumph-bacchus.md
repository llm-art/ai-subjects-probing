# Probe report — `triumph-bacchus`

[![triumph-bacchus](https://media.rkd.nl/iiif/2/10014713/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10014713/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10014713/info.json)_

- **Ground-truth subject:** De triomf van Bacchus
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/triumph-bacchus.jpg` — native 2912×1367 px, sent 2048×961 px
- **SHA-256:** `de67ceb20742d35f97ac54333014c8724bc87d225dd47bfc39a989b69b9d2679`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:44:03+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Cornelis de Vos",
>   "title": "The Triumph of Bacchus",
>   "date": "c. 1636",
>   "collection": "Museo Nacional del Prado, Madrid"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:43:30+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, this painting depicts a **Bacchanalian procession**, a wild and celebratory parade in honor of Bacchus (the Roman god of wine, fertility, and revelry) or his Greek equivalent, Dionysus.
> 
> The scene is a chaotic and energetic cavalcade of figures moving through a classical landscape. Here are the key elements visible:
> 
> *   **Central Figure:** The focal point of the right side of the composition is a large, corpulent, and inebriated older man, likely representing **Silenus** (Bacchus's tutor and companion) or Bacchus himself. He is seated on a cart made of wine barrels, adorned with grapevines, and is being supported by other figures, including a satyr.
> *   **The Revelers:** The procession is crowded with a diverse cast of characters, including:
>     *   **Satyrs and Fauns:** Mythological creatures with human torsos and the legs and horns of goats. One is seen riding a goat on the right.
>     *   **Maenads (or Bacchantes):** Female followers of Bacchus, shown dancing and celebrating.
>     *   **Humans and Children:** Men, women, and even toddlers are part of the revelry. One child in the foreground is shown urinating, while another pair of children (one appearing to be a young satyr) are on the ground, seemingly drunk.
> *   **Action and Atmosphere:** The mood is one of ecstatic, drunken abandon. Figures are dancing, playing music (like tambourines), drinking from jugs, and carrying staffs (thyrsi). One figure on the far left is performing a handstand or cartwheel.
> *   **Animals:** The procession includes donkeys pulling a cart, a goat being ridden, and a small dog running in the foreground. A monkey is also visible, perched on a barrel near the central figure.
> *   **Setting:** The background features a hilly landscape with classical architecture, such as rotundas or temples, which firmly places the scene in a mythological, ancient world.
> 
> In summary, the painting is a dynamic and detailed illustration of a classical myth, capturing the themes of intoxication, ecstasy, and the unrestrained celebration of nature and wine associated with the cult of Bacchus.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:43:49+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image, this European oil painting depicts a **Bacchanal**, specifically a scene often titled **The Triumph of Bacchus** (or Dionysus in Greek mythology).
> 
> This is a mythological scene portraying a wild and drunken procession in honor of the god of wine, fertility, and revelry.
> 
> Here are the key figures and elements identifiable in the painting:
> 
> *   **Silenus:** The most prominent figure is the corpulent, intoxicated, older man seated on a cart made of wine barrels. This is Silenus, the tutor and loyal companion of Bacchus. He is often depicted as being too drunk to walk and is either supported by other figures or, as seen here, carried in a cart or on a donkey. He is being held up by a satyr.
> *   **Bacchus (Dionysus):** While Silenus is the focal point of the cart, Bacchus himself may be represented by one of the more youthful, athletic figures. The man with a laurel or vine wreath running ahead of the cart could be the god leading his followers.
> *   **Satyrs and Fauns:** These are the male followers of Bacchus, often depicted with goat-like features such as legs, horns, and pointed ears. Several figures in the crowd, including the one supporting Silenus and the man riding a goat on the right, are satyrs.
> *   **Maenads (or Bacchantes):** These are the ecstatic female followers of Bacchus. They are shown dancing, playing instruments like tambourines, and participating in the wild revelry.
> *   **The Procession (Thiasus):** The entire group forms a procession known as a *thiasus*. They are depicted in a state of ecstatic frenzy, fueled by wine. The scene is filled with symbols of their cult: grapevines, wine barrels, drinking vessels, and musical instruments. The overall atmosphere is one of chaotic, unrestrained celebration.
> 
> The scene includes a diverse retinue, including children, people of different ethnicities, and animals like donkeys, a goat, a monkey, and a dog, all swept up in the joyous chaos of the procession. The classical architecture in the background places the scene firmly within a mythological, ancient world setting.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:44:07+00:00_

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

> The Triumph of Bacchus

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:48:04+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Frans Francken the Younger",
>   "title": "The Triumph of Bacchus",
>   "date": "c. 1620",
>   "collection": null
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:09:13+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This image depicts a **Bacchanalian procession**, specifically a representation of **The Triumph of Bacchus** (or **The Triumph of Silenus**), a popular theme in Renaissance and Baroque art (this particular painting is in the Dutch Mannerist style, likely by or associated with **Joachim Wtewael**). 
> 
> The scene is filled with mythological figures celebrating in a chaotic, drunken revelry:
> 
> * **Silenus:** The obese, elderly, and highly intoxicated companion of Bacchus is shown seated on a barrel atop a wooden cart, being supported by satyrs and followers.
> * **Bacchus (Dionysus):** The youthful, athletic god of wine is depicted walking near the center-left, wearing a crown of vine leaves.
> * **Satyrs and Maenads:** The procession is filled with dancing, music-playing, and drinking followers. Satyrs (with goat legs) and Maenads (female followers) play tambourines, blow horns, and carry grapes.
> * **Animals:** 
>   * A donkey (traditionally ridden by Silenus) is led on the left.
>   * A monkey sits chained to a barrel on the cart.
>   * A dog runs in the right foreground.
>   * A satyr rides a goat on the far right.
> * **Foreground Details:**
>   * On the far left, a man in a red tunic performs a handstand.
>   * In the center foreground, a female satyr lies on the ground nursing a baby satyr.
>   * Next to her, a young toddler stands and urinates, a common symbolic motif in Dutch art representing the physical effects of excess and wine.
> * **Background:** A classical landscape featuring a circular temple (*tholos*) and a triumphal arch under a bright, glowing sky.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:09:34+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual details, this European oil painting depicts a **Bacchic Procession** (often titled **The Triumph of Bacchus** or **The Triumph of Silenus**), a popular mythological subject in Renaissance and Baroque art celebrating wine, fertility, and ecstatic revelry.
> 
> ### Key Figures and Elements Depicted:
> 
> * **Bacchus (Dionysus):** The youthful, athletic god of wine is shown walking near the center-left, crowned with a wreath of vine leaves and grapes.
> * **Silenus:** The elderly, obese, and perpetually drunken tutor and companion of Bacchus. He is depicted on the right, precariously balanced on a barrel atop a wooden cart, being supported by a satyr to keep him from falling off.
> * **Satyrs and Fauns:** Numerous half-man, half-goat forest deities are scattered throughout the crowd. 
>   * On the bottom right, a young satyr rides a goat.
>   * In the lower center, a **female satyr (fauness)** lies on the ground nursing a baby satyr.
> * **Maenads (Bacchantes):** The female followers of Bacchus, shown dancing, playing musical instruments (such as the tambourine on the left), and carrying grapes.
> * **Urinating Putto/Child:** In the lower-middle foreground, a young child is shown urinating, a common motif in Bacchanalian scenes symbolizing fertility and the natural flow of liquids (akin to wine).
> * **Silenus's Donkey:** On the left, the donkey traditionally ridden by Silenus is being led through the crowd, carrying a small dark figure (possibly a monkey or a small satyr).
> * **Acrobat:** On the far left, a reveler performs a handstand, emphasizing the chaotic, carnivalesque atmosphere of the festival.
> * **Animals:** A monkey sits on a barrel next to Silenus, and a small dog runs in the lower right foreground. 
> * **Background:** In the distance, a classical circular temple (*tholos*) and an arched bridge evoke an idealized ancient Roman or Greek landscape.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:09:47+00:00_

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

> The Triumph of Bacchus

