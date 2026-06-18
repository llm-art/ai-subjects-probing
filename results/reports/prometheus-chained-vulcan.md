# Probe report — `prometheus-chained-vulcan`

[![prometheus-chained-vulcan](https://media.rkd.nl/iiif/2/11098208/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/11098208/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/11098208/info.json)_

- **Ground-truth subject:** Prometheus chained by Vulcan
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/prometheus-chained-vulcan.jpg` — native 3703×4096 px, sent 1852×2048 px
- **SHA-256:** `be5ee434e0b50b6a18604f93e78d91ab7ae64e3108e750ba272f47c2c7f2cc21`
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
>   "artist": "Dirck van Baburen",
>   "title": "Prometheus Being Chained by Vulcan",
>   "date": "c. 1623",
>   "collection": "Rijksmuseum"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:42:18+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology, this painting depicts the **punishment of Prometheus**.
> 
> Here is a breakdown of the scene and its characters:
> 
> *   **Prometheus:** The central figure lying on his back, being chained. In Greek mythology, the Titan Prometheus defied the gods by stealing fire and giving it to humanity. As punishment, Zeus ordered him to be bound to a rock. His expression is one of agony and defiance.
> *   **Vulcan (Hephaestus):** The older, muscular, bearded man who is actively chaining Prometheus. Vulcan (the Roman name for the Greek Hephaestus) was the god of fire, metalworking, and the forge. The tools on the ground, such as the hammer and pincers, and the fiery glow in the background are indicative of his domain. He is carrying out Zeus's orders to bind the Titan.
> *   **Mercury (Hermes):** The figure on the right, observing the scene. He is identifiable by his iconic attributes: the winged helmet (petasus) and the staff with two entwined snakes (the caduceus). As the messenger of the gods, Mercury (the Roman name for the Greek Hermes) is present to ensure Zeus's command is fulfilled. His slight smile suggests a detached or even cruel amusement at Prometheus's fate.
> *   **The Eagle:** In the upper left corner, partially obscured in shadow, is a large dark bird, an eagle. This is the eagle of Zeus, which, according to the myth, was sent to eat Prometheus's liver every day. Since Prometheus was immortal, his liver would regenerate each night, making his torment eternal.
> 
> The painting captures the dramatic and brutal moment of Prometheus's binding, using strong contrasts of light and shadow (chiaroscuro) typical of the Baroque style to emphasize the muscularity of the figures and the intensity of the emotion.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:42:35+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts a scene from Greek mythology.
> 
> **Episode:** The Punishment of Prometheus, also known as *Prometheus Bound*.
> 
> **Figures:**
> 
> 1.  **Prometheus:** The figure lying on his back, being chained. In mythology, the Titan Prometheus defied the gods by stealing fire and giving it to humanity. As a punishment, Zeus ordered him to be chained to a rock in the Caucasus Mountains. His pained expression and bound state identify him.
> 
> 2.  **Vulcan (Hephaestus):** The older, bearded, and muscular figure who is actively chaining Prometheus. Vulcan (the Roman name for the Greek Hephaestus) was the god of fire and the forge, the blacksmith of the gods. He was tasked by Zeus to forge the chains and bind Prometheus. The tools on the floor (hammer and pincers) and the fiery glow of a forge in the background further confirm his identity.
> 
> 3.  **Mercury (Hermes):** The figure on the right, observing the scene with a slight smile. He is identifiable by his iconic attributes: the winged helmet (petasus) and the staff entwined with two snakes (the caduceus). As the messenger of the gods, Mercury (the Roman name for the Greek Hermes) is present to oversee Zeus's command being carried out.
> 
> **Other details:**
> 
> *   In the upper left corner, shrouded in darkness, is a large bird, an **eagle**. This is the eagle that, as part of Prometheus's eternal punishment, would come each day to eat his liver, which would then regrow overnight.
> *   The painting's dramatic use of light and shadow (chiaroscuro), the muscular figures, and the intense emotion are characteristic of the Baroque style.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:42:55+00:00_

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

> Prometheus chained by Vulcan

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:46+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {"recognized": true, "artist": "Dirck van Baburen", "title": "Prometheus Being Chained by Vulcan", "date": "1623", "collection": "Rijksmuseum"}

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:07:37+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This painting depicts the Greek mythological scene of **Prometheus being chained to a rock by Vulcan (Hephaestus)**, under the supervision of **Mercury (Hermes)**. 
> 
> Here are the key elements and figures shown in the artwork:
> 
> *   **Prometheus (center/bottom):** He is shown bound and writhing on a stone block, looking directly at the viewer with an upside-down expression of anguish. 
> *   **Vulcan / Hephaestus (left):** The muscular blacksmith god is depicted in a loincloth, actively securing Prometheus with heavy iron chains. His blacksmith tools (a hammer and tongs) lie on the ground near his feet. He presses his foot down near Prometheus's head to hold him in place.
> *   **Mercury / Hermes (right):** Standing in a blue cloak, Mercury watches the punishment with a slight, knowing smile. He is easily identified by his winged helmet (*petasos*) and the *caduceus* (the staff entwined with two snakes) in his hand.
> *   **The Eagle (top left):** Looming in the dark shadows of the upper-left corner is the eagle of Zeus, foreshadowing Prometheus's eternal punishment of having his liver devoured daily by the bird.
> 
> ### Art Historical Context
> This is a famous Dutch Golden Age painting titled ***Prometheus Chained by Vulcan*** (1623) by the Utrecht Caravaggist painter **Dirck van Baburen**. The painting is celebrated for its dramatic use of *chiaroscuro* (strong contrasts between light and dark), realistic anatomy, and intense, theatrical emotion.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:07:45+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the mythological scene of **Prometheus being chained to a rock by Vulcan (Hephaestus)**, under the watchful eye of **Mercury (Hermes)**. 
> 
> Specifically, it is the famous Dutch Golden Age painting ***Prometheus Being Chained by Vulcan*** (1623) by the Utrecht Caravaggisti painter **Dirck van Baburen**.
> 
> ### Figures and Details Depicted:
> * **Prometheus (bottom/center):** The Titan who defied the gods by stealing fire and giving it to humanity. He is shown pinned to the rock, looking out in anguish as he is bound.
> * **Vulcan / Hephaestus (left):** The blacksmith god of fire, depicted as a muscular, weathered craftsman. He is shown actively securing the heavy iron chains around Prometheus, using his foot to hold him down. His blacksmithing tools (pliers and hammer) lie on the ground below.
> * **Mercury / Hermes (right):** The messenger of the gods, sent by Jupiter (Zeus) to oversee the punishment. He is easily identified by his winged helmet (*petasos*), blue cloak, and the caduceus staff in his hand. He looks on with a mocking, satisfied expression.
> * **The Eagle (top left):** Hovering in the dark shadows above is the eagle of Jupiter, which was sent to eternally feast on Prometheus's regenerating liver as part of his torment.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:07:52+00:00_

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

> Prometheus chained by Vulcan

