# Probe report — `abduction-helen`

[![abduction-helen](https://iiif.artresearch.net/iiif/3/frick/4107100317886_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100317886_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100317886_0001.jp2/info.json)_

- **Ground-truth subject:** The Abduction of Helen
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/abduction-helen.jpg` — native 4867×4945 px, sent 2016×2048 px
- **SHA-256:** `11e522d87573bbd8c5d7d2f1011c77a2f5da8d25bfb73221dd208adf4d4c4ba7`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:02:15+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a well-known masterpiece of Venetian painting.
> 
> **Artist:** Jacopo Tintoretto (also known as Jacopo Robusti)
> **Title:** *The Abduction of Helen* (or *The Rape of Helen*)
> **Approximate Date:** c. 1578–1579
> **Collection:** Museo Nacional del Prado, Madrid
> 
> The painting depicts the mythological event that triggered the Trojan War. The Trojan prince Paris, in the center wearing a helmet, leads Helen, the wife of the Spartan king Menelaus, towards the ships waiting in the harbor to take her to Troy. The scene is filled with dynamic action and numerous figures, including soldiers and Helen's attendants. The presence of cupids (one flying with a torch, another on the ground with a bow) signifies that the event is driven by love and passion, instigated by the goddess Venus (Aphrodite). The dramatic composition, energetic figures, and flickering light are all characteristic of Tintoretto's late style.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:02:33+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology and art history, this black and white photograph shows a painting depicting **The Abduction of Helen**, also known as **The Rape of Helen**.
> 
> Here is a detailed description of what is depicted:
> 
> **Central Narrative and Figures:**
> The scene portrays the moment when the Trojan prince, Paris, leads Helen away from her home in Sparta to his ships, an event that triggered the Trojan War.
> 
> *   **Helen:** The central female figure, dressed in flowing light-colored robes, is Helen of Sparta. Her expression appears contemplative or perhaps reluctant as she is led away.
> *   **Paris:** The main male figure, likely the one gesturing forward towards the sea, is Paris. He is depicted as a heroic figure in armor, a plumed helmet, and a cape, confidently leading the procession. Another young warrior stands between him and Helen, possibly a companion or another representation of Paris.
> *   **Helen's Attendants:** To the left, a group of women, presumably Helen's ladies-in-waiting, look on with expressions of concern and dismay.
> *   **Soldiers:** Following Paris are other soldiers in helmets and armor, part of his Trojan entourage.
> 
> **Symbolic and Mythological Elements:**
> The painting is rich with symbolism that clarifies the story:
> 
> *   **Cupids (Amorini/Putti):** Two winged cherubs are present. One flies in the sky above, holding a flaming torch, symbolizing the burning passion of love that drives the event. The other stands in the lower right corner, holding a bow, directly identifying him as Cupid, the god of love, whose arrow is responsible for Helen's infatuation with Paris. Their presence indicates that this abduction is fated and orchestrated by the gods of love.
> *   **The Fleet:** In the background on the right, a large fleet of ships with sails waits in the harbor. This is the Trojan fleet, ready to carry Helen and Paris to Troy, and it foreshadows the massive naval expedition the Greeks will later launch in response.
> 
> **Other Details:**
> *   **Setting:** The group is moving from a grand architectural structure on the left, representing the palace or city of Sparta, towards the open sea on the right, signifying their departure and journey.
> *   **Attendants and Animals:** In the lower left, a young Black page holds a long cord or leash. In the foreground, there are two small dogs (one resembling a spaniel) and what appears to be a small monkey, which in Renaissance and Baroque art could symbolize themes of fidelity (the dog, which Helen is leaving behind) and lust or base instincts (the monkey).
> 
> **Overall Composition and Style:**
> The painting is composed in a grand, classical style, typical of Renaissance or Baroque history painting. The figures are arranged in a frieze-like procession across the foreground, with their movement directing the viewer's eye from left to right, following the narrative of departure. The image is a black and white photograph of this painting, which is set within an ornate, carved frame.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:02:56+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology and art history, this painting depicts **The Abduction of Helen**, also known as the **Rape of Helen**. This is the mythological event that triggered the Trojan War.
> 
> Here is a breakdown of the figures and scene:
> 
> *   **Helen of Sparta:** She is the central female figure, dressed in elegant robes. Her expression is somber and she appears to be led away, possibly against her will or with some reluctance.
> *   **Paris of Troy:** He is the Trojan prince leading Helen by the arm. He wears a plumed helmet and armor, looking back at her as he guides her towards the ships.
> *   **Trojans:** The other men in armor are Paris's companions, assisting in the abduction and preparing to depart. The figure on the far right gestures emphatically towards the fleet of ships, urging the party to move quickly.
> *   **Helen's Attendants:** The group of women on the left are Helen's ladies-in-waiting. Their expressions convey distress, sorrow, and concern as they watch their queen being taken away.
> *   **The Cupids (Putti/Erotes):** The presence of two winged, cherubic figures confirms the theme of love and passion.
>     *   The cupid in the lower right holds a bow, the classic attribute of Eros (Cupid), the god of love, signifying that this event is driven by desire.
>     *   The cupid flying in the sky holds a lit torch, symbolizing the "flame of love" that has ignited this affair, and also foreshadowing the burning of Troy and the devastation of the war to come.
> *   **The Setting:** The background clearly shows a harbor filled with sailing ships, representing the Trojan fleet waiting to carry Helen away from her home in Sparta to her new life in Troy.
> 
> The scene captures the pivotal moment of departure. The composition leads the viewer's eye from the grieving attendants on the left, through the central couple, to the waiting ships on the right, encapsulating the entire narrative of the abduction in a single, dramatic frame. The inclusion of courtly details like the small dogs and the young page holding a leash adds to the richness of the scene, typical of Renaissance or Baroque interpretations of classical subjects.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:03:16+00:00_

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

