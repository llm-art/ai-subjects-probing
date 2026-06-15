# Probe report — `meeting-dido-aeneas`

[![meeting-dido-aeneas](https://media.rkd.nl/iiif/2/9115963/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9115963/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9115963/info.json)_

- **Ground-truth subject:** The meeting of Dido and Aeneas
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/meeting-dido-aeneas.jpg` — native 2520×1832 px, sent 2048×1489 px
- **SHA-256:** `8501a0e4a7d9c50e381d8e328b6342fcfa03c1e3abf455c852f90f2556424bae`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:44:26+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a famous work of art.
> 
> **Artist:** Giovanni Battista Tiepolo (also known as Giambattista Tiepolo)
> 
> **Title:** The artwork depicts a scene from Virgil's *Aeneid* and is commonly known as *The Meeting of Aeneas and Dido* or *Aeneas Presented to Dido*. The scene shows the Trojan hero Aeneas, guided by his mother Venus and her son Cupid (seen in the clouds above), arriving in Carthage and being welcomed by its queen, Dido.
> 
> **Approximate Date:** c. 1757
> 
> **Collection:** This is a fresco and is part of a larger cycle of paintings decorating the walls of the Villa Valmarana "Ai Nani" in Vicenza, Italy.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:44:44+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual elements in the image and knowledge of classical mythology and art history, this painting depicts **the arrival of Aeneas in Carthage and his meeting with Queen Dido**.
> 
> This scene is from Virgil's epic poem, the *Aeneid*. Here is a breakdown of the elements in the painting that support this identification:
> 
> *   **The Protagonists:** The central male figure, dressed in Roman-style armor with a plumed helmet and a flowing red cape, is **Aeneas**, the Trojan hero. He is shown arriving from the sea, as indicated by the ships and other soldiers in the background on the left. The regal woman on the right, emerging from a grand classical palace and attended by her ladies-in-waiting, is **Dido**, the founder and queen of Carthage.
> 
> *   **The Narrative Action:** The painting captures the moment of their first encounter. Aeneas and his men have just landed on the shores of Carthage after a long and perilous journey from the ruins of Troy. Dido, the powerful queen, graciously welcomes the strangers to her new city. The composition shows Aeneas being led towards Dido, setting the stage for their fateful and tragic romance.
> 
> *   **Divine Intervention:** Floating on a cloud in the upper left corner are the goddess **Venus** (Aeneas's mother) and her son, **Cupid**, who is holding his bow. In the *Aeneid*, Venus orchestrates this meeting and sends Cupid to make Dido fall deeply in love with Aeneas to ensure her son's safety and aid. The presence of these deities confirms the mythological subject and highlights the divine manipulation behind the human drama.
> 
> *   **Artistic Style:** The style of the painting is characteristic of the Venetian School during the late Baroque or Rococo period, likely the work of **Giovanni Battista Tiepolo**. His work is known for its grand, theatrical compositions, light-filled atmosphere, pastel color palette, and elegant, elongated figures, all of which are evident in this image. The scene is presented with a sense of operatic grandeur, from the classical architecture and opulent court to the divine figures observing from above.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:45:03+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge of art history and classical mythology, this painting depicts a scene from Virgil's epic poem, the *Aeneid*.
> 
> **Episode:** The meeting of **Aeneas and Dido** in Carthage.
> 
> **Figures and Scene:**
> 
> *   **Aeneas:** The central male figure in Roman-style armor with a prominent red cape. He is the Trojan hero, son of the goddess Venus, who has just been shipwrecked on the coast of North Africa with his followers. His posture is one of humility and respect as he presents himself to the queen. His men and ships can be seen in the background on the left.
> *   **Dido:** The central female figure in the elegant white and blue gown. She is the founder and Queen of Carthage. She is shown welcoming the stranger to her new city, attended by her ladies-in-waiting.
> *   **Venus and Cupid:** The two figures reclining on a cloud in the upper left sky. The nude woman is **Venus**, the goddess of love and Aeneas's mother. She is watching over her son and orchestrating events to ensure his safety. The winged boy with the bow is her son **Cupid**. In the *Aeneid*, Venus will later have Cupid disguise himself as Aeneas's son, Ascanius, and breathe a passion for Aeneas into Dido, leading to their tragic love affair.
> 
> The setting contrasts the rugged shore where the Trojans have landed with the magnificent classical architecture of Dido's rising city of Carthage. The overall composition is grand and theatrical, typical of large-scale history painting from the Baroque or Rococo periods. The artist is most likely the Venetian master **Giovanni Battista Tiepolo**, for whom this was a recurring and famous subject.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:45:28+00:00_

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

> The meeting of Dido and Aeneas

