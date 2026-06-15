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

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:42:00+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a well-known Baroque painting.
> 
> **Artist:** Dirck van Baburen
> **Title:** *Prometheus Being Chained by Vulcan*
> **Approximate Date:** c. 1623
> **Collection:** Rijksmuseum, Amsterdam
> 
> The painting depicts a scene from Greek mythology. The muscular, bearded figure is Vulcan (the Roman equivalent of Hephaestus), the god of the forge, who is chaining the Titan Prometheus to a rock. This was Prometheus's punishment, ordered by Jupiter (Zeus), for stealing fire from the gods and giving it to humanity. The figure looking on with a winged helmet and holding a caduceus (a staff with two intertwined snakes) is Mercury (Hermes), the messenger of the gods. In the upper left corner, the eagle that would come to eat Prometheus's liver each day is visible in the shadows. The style, with its dramatic lighting (chiaroscuro) and gritty realism, is characteristic of the Utrecht Caravaggisti, of whom Dirck van Baburen was a leading member.

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

