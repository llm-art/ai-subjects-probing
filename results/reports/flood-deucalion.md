# Probe report — `flood-deucalion`

[![flood-deucalion](https://iiif.artresearch.net/iiif/3/frick/4107100323284_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100323284_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100323284_0001.jp2/info.json)_

- **Ground-truth subject:** A Scene from Greek Mythology: The Flood of the Age of Deucalion
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/flood-deucalion.jpg` — native 6141×4570 px, sent 2048×1524 px
- **SHA-256:** `0f4577e909d144eed76519d9c08d624f701a3ff36c5aad79326e1dac5fe34821`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:02:07+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this is a photograph of the following artwork:
> 
> **Artist:** Gabriel-François Doyen
> **Title:** *The Flood* (French: *Le Déluge*)
> **Approximate Date:** 1766
> **Collection:** Musée du Louvre, Paris
> 
> The painting depicts the mythological flood sent by the gods to punish humanity, a theme found in various cultures, including the Greek myth of Deucalion and Pyrrha. The scene is filled with dramatic chaos and despair as people struggle futilely against the rising waters. The dynamic, emotional, and complex composition is characteristic of late Baroque or early Neoclassical history painting. This work was Doyen's reception piece for the French Royal Academy of Painting and Sculpture (Académie Royale de Peinture et de Sculpture).

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:02:23+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general knowledge of art history and mythology, this is a black and white photograph of a large, dramatic painting.
> 
> The painting depicts a catastrophic event, specifically a great flood, as suggested by the text at the bottom which reads "A SCENE FROM GREEK MYTHOLOGY - THE FLOOD...". The scene is one of chaos, despair, and death.
> 
> Here is a detailed description of what is depicted:
> 
> *   **Overall Scene:** A multitude of people, including men, women, and children, are shown struggling to survive on a rocky outcrop or high ground as floodwaters rise around them. The composition is crowded and tumultuous, emphasizing the scale of the disaster.
> 
> *   **The People:** The figures are depicted in various states of distress:
>     *   In the center, a woman with her back to the viewer raises her arms to the sky in a gesture of supplication or despair.
>     *   Throughout the scene, families cling to one another. Mothers are shown trying to protect their children.
>     *   Many bodies, seemingly lifeless, are strewn across the rocks. One prominent figure in the center is a woman lying on her back, possibly dead, with a man grieving over her.
>     *   Figures on the left appear to be in the water, trying to climb to safety.
>     *   The figures are mostly nude or partially draped in cloth, a convention in classical and historical painting that emphasizes the vulnerability and heroism of the human form.
> 
> *   **The Environment:** The setting is a dark and stormy landscape.
>     *   The sky is filled with dark, swirling clouds.
>     *   In the upper left corner, a winged, muscular male figure flies through the clouds, looking down on the tragedy below. This is likely a deity or a personification of a divine force, overseeing the destruction.
>     *   Trees are visible in the background, one with a piece of white cloth caught in its branches, suggesting a powerful wind.
> 
> *   **Mood and Style:** The painting's style is dramatic and emotional, characteristic of the Baroque or Neoclassical periods. The use of strong light and shadow (chiaroscuro), the dynamic and contorted poses of the figures, and the intense emotional content all contribute to a powerful sense of tragedy and the sublime power of nature or the gods.
> 
> In summary, the image depicts the mythological Great Flood, focusing on the human suffering and terror of those caught in the cataclysm sent by the gods to punish humanity.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:02:42+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts a scene from Greek mythology: **The Great Flood**, also known as the Flood of Deucalion.
> 
> Here is a breakdown of the scene and figures:
> 
> *   **The Episode:** In Greek mythology, Zeus, the king of the gods, became disgusted with the impiety and wickedness of humanity during the Iron Age. He decided to wipe them out with a massive flood. This painting captures the moment of cataclysm, focusing on the terror and despair of the people as the waters rise and destroy them. It is a scene of divine punishment and human suffering on a grand scale.
> 
> *   **The Figures:**
>     *   **Humanity:** The numerous figures scrambling on the rocks and in the water represent the wicked race of mortals being punished. They are not specific named individuals but archetypes of suffering: mothers clutching their children, people raising their arms to the heavens in a final, futile plea, and others already succumbing to the deluge. The artist has composed them in dramatic, writhing poses to convey chaos and agony.
>     *   **The Winged Figure:** In the upper left corner, a powerful, winged male figure flies through the storm clouds, looking back at the destruction. This is not a benevolent angel but a divine agent of the catastrophe. It could be interpreted as Zeus himself, or a personification of divine vengeance or the storm winds (Anemoi) he unleashed upon the world. His presence emphasizes that this is not a random natural disaster but a deliberate act of the gods.
> 
> The overall composition, with its dramatic lighting (chiaroscuro), dynamic and emotional figures, and chaotic scene, is characteristic of large-scale history painting in the Baroque or Neoclassical traditions, which often drew on such epic mythological and biblical themes.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:03:02+00:00_

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

> The painting depicts a catastrophic scene of mass destruction, with numerous nude and semi-nude figures, including men, women, and children, struggling against rising waters or lying dead. In the sky, a winged male deity flies through dark clouds, overseeing the devastation. This imagery is characteristic of a great flood, a common theme in mythology representing divine punishment.
> 
> From the provided list of subjects, we must find the one that best matches this scene of widespread suffering and death caused by a divine power.
> 
> *   Many options, such as weddings ("The wedding of Peleus and Thetis," "Marriage of Cupid and Psyche"), meetings ("The meeting of Nausicaa and Ulysses," "The meeting of Dido and Aeneas"), or specific, less cataclysmic events ("Prometheus chained by Vulcan," "The sacrifice of Iphigenia"), can be immediately ruled out as they do not match the scale or nature of the disaster shown.
> 
> *   The scene is one of overwhelming destruction. "The Triumph of Mars: an Allegory of War" is the option that best captures this theme. Mars is the god of war, and his "triumph" represents the victory of war itself, which brings with it widespread death, chaos, and suffering for humanity—the very elements depicted in the painting. The flood can be interpreted as a powerful allegory for the overwhelming and indiscriminate destruction unleashed by war. The winged figure in the sky can be seen as Mars, triumphant over the ruin of mankind.
> 
> Therefore, the subject depicted is best described as an allegory for the consequences of war.
> 
> **The Triumph of Mars: an Allegory of War**

