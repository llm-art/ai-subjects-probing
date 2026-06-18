# Probe report — `sacrifice-iphigenia`

[![sacrifice-iphigenia](https://media.rkd.nl/iiif/2/9109625/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9109625/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9109625/info.json)_

- **Ground-truth subject:** The sacrifice of Iphigenia
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/sacrifice-iphigenia.jpg` — native 2374×1731 px, sent 2048×1493 px
- **SHA-256:** `b9fc4b77e1a1f8afa26d60b23794cad0d2419da63828a68c6380aafcb4948a17`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:44:28+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Jan Victors",
>   "title": "The Sacrifice of Iphigenia",
>   "date": "c. 1640-1650",
>   "collection": "Rijksmuseum"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:44:52+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual elements in this black and white image of a painting, this appears to be a depiction of the **Sacrifice of Iphigenia**, a well-known story from Greek mythology.
> 
> Here is a breakdown of the scene:
> 
> *   **Central Action:** In the center, a young woman in a white gown, Iphigenia, is being led to a sacrificial altar. She is surrounded by several older, bearded men, likely including her father, King Agamemnon, and the priest Calchas, who stands behind the altar. Her expression and posture suggest distress and pleading.
> *   **Divine Intervention:** In the upper left corner, a divine scene unfolds. A goddess, identifiable as **Artemis** (or the Roman Diana) by the crescent moon on her head, is descending from the heavens on a cloud. She is intervening to stop the sacrifice. In some versions of the myth, she whisks Iphigenia away to become her priestess, replacing her on the altar with a deer. The image captures the moment of this miraculous rescue. Another figure, possibly Iphigenia herself, is shown being lifted into the air above the altar.
> *   **Setting and Onlookers:** The scene is crowded with figures reacting to the event. To the left are Greek soldiers and nobles, their expressions a mix of awe, grief, and shock. In the background, the masts of ships are visible, alluding to the reason for the sacrifice: to appease Artemis and allow the Greek fleet to sail for the Trojan War.
> *   **Foreground Details:** In the foreground, a servant arranges ornate vessels and treasures, likely offerings for the ceremony. A soldier kneels in the lower left, and a scribe or official sits on the right, documenting the event.
> *   **Artistic Style:** The painting exhibits characteristics of the Baroque style, with its dramatic composition, strong contrasts between light and shadow (chiaroscuro), emotional intensity, and dynamic movement in the figures and drapery.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:45:09+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history and mythology, this painting depicts the classical story of **The Sacrifice of Iphigenia**.
> 
> This episode comes from Greek mythology, specifically from the prelude to the Trojan War. Here is a breakdown of the scene and the figures:
> 
> *   **The Subject:** The Greek fleet, assembled at the port of Aulis to sail for Troy, is unable to depart due to a lack of wind. The seer Calchas reveals that the goddess Artemis (Diana in Roman mythology) is angry with the Greek leader, King Agamemnon, and demands the sacrifice of his eldest daughter, Iphigenia, to appease her and allow the winds to blow.
> 
> *   **Key Figures and Elements in the Painting:**
>     *   **Iphigenia:** She is the young woman in the center, dressed in white (symbolizing innocence and sacrifice), being led towards the altar. Her expression is one of pleading or resignation.
>     *   **Agamemnon:** The regal, bearded figure standing over Iphigenia is likely her father, King Agamemnon, torn between his duty as a commander and his love for his daughter.
>     *   **Calchas:** The figure acting as the priest at the altar, with his hands raised, is the seer Calchas, who must perform the sacrifice.
>     *   **Artemis (Diana):** In the upper left corner, a divine figure descends from the heavens on a cloud. This is the goddess Artemis. The painting captures the climactic moment of *deus ex machina*, where the goddess intervenes at the last second to save Iphigenia, often by substituting a deer in her place and whisking her away. The cropped image shows this figure has a crescent moon on her head, a primary attribute of Artemis/Diana.
>     *   **The Greek Army:** The surrounding figures, including soldiers in armor and other onlookers, represent the Greek leaders and army who are witnesses to the event.
>     *   **The Setting:** The altar signifies the place of sacrifice. In the background to the left, the masts of ships are visible, representing the becalmed Greek fleet at Aulis. The treasures and vessels in the foreground are likely offerings to the goddess.
> 
> The painting's dramatic composition, with strong contrasts between light and dark (chiaroscuro), and the heightened emotion of the figures are characteristic of the Baroque style of European painting.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:45:30+00:00_

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

> The sacrifice of Iphigenia

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:48:33+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Pieter Lastman",
>   "title": "The Sacrifice of Iphigenia",
>   "date": "1614",
>   "collection": "Rijksmuseum, Amsterdam"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:10:10+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This image depicts **"The Sacrifice of Iphigenia"**, a famous painting by the Dutch Golden Age artist **Jan Steen** (painted in 1671). 
> 
> ### Key Elements of the Scene:
> * **Iphigenia:** Kneeling in the center in a glowing white dress, prepared to be sacrificed to the goddess Diana (Artemis) so that the Greek fleet can obtain favorable winds to sail to Troy.
> * **Agamemnon:** Her father, depicted on the right side sitting down, overcome with grief and weeping with his head resting in his hand next to a large open book.
> * **Diana (Artemis):** Appearing in the upper-left corner in the clouds, bringing a deer (hind) to replace Iphigenia on the altar at the last moment, thereby saving her.
> * **The Greek Fleet:** Visible in the background on the far left, anchored at the port of Aulis.
> * **The Altar and Onlookers:** Surrounding the central scene are the high priest, soldiers, and various onlookers witnessing the miraculous intervention.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:10:25+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual details, this painting depicts the mythological scene of **The Sacrifice of Iphigenia** (specifically the moment of her miraculous rescue at Aulis). 
> 
> ### **The Episode**
> According to Greek mythology, the Greek fleet was stranded at Aulis on their way to Troy because the goddess Artemis (Diana) calmed the winds. To appease her, the high priest Calchas declared that King Agamemnon must sacrifice his eldest daughter, **Iphigenia**. Just as the sacrifice is about to take place, Diana relents, snatches Iphigenia away to safety, and replaces her on the altar with a deer (hind).
> 
> ### **Key Figures Depicted**
> * **Iphigenia:** The young woman kneeling in the center in a white gown, resigned to her fate.
> * **Diana (Artemis):** Appearing in the upper-left corner in the clouds, identified by the crescent moon on her forehead, accompanied by the hind (deer) she is sending to replace Iphigenia.
> * **Calchas:** The high priest standing by the altar, preparing to perform the sacrifice.
> * **Agamemnon:** Iphigenia's father, the King of Mycenae. In classical art tradition (originating from the ancient painter Timanthes), he is depicted hiding his face in deep grief (the seated figure on the right with his hand covering his face).
> * **Greek Soldiers and Onlookers:** Surrounding the altar, reacting with awe and sorrow to the impending sacrifice and the divine intervention.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:10:36+00:00_

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

> The sacrifice of Iphigenia

