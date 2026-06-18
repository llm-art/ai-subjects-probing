# Probe report — `jason-dragon`

[![jason-dragon](https://iiif.artresearch.net/iiif/3/frick/56480_POST.tif/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/56480_POST.tif/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/56480_POST.tif/info.json)_

- **Ground-truth subject:** Episode from the Legend of the Argonauts: Jason Slaying the Sleepless Dragon
- **Category:** mythology
- **Institution:** pharos
- **Image:** `data/images/jason-dragon.jpg` — native 8706×7522 px, sent 2048×1769 px
- **SHA-256:** `70e03f7a4c9b4eaef5e92735ba262aaa9ab5dca1d7bb026bf2ee2610e7d754fb`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:00:22+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, I can identify this artwork.
> 
> **Artist:** Stefano da Ferrara (Stefano di Benedetto)
> The artist's name, "STEPHANO DA FERRARA," is inscribed at the bottom of the painting.
> 
> **Title:** *A Miracle of St. Maurelius* (sometimes referred to as *An Exorcism*)
> 
> **Approximate Date:** c. 1480
> 
> **Collection:** The Walters Art Museum, Baltimore
> 
> This painting depicts a miracle performed by Saint Maurelius, a patron saint of Ferrara, Italy. The scene is an exorcism. On the right, a possessed man is shown in a violent struggle, wrestling with a demon or embodying a demonic, bestial force. A crowd of onlookers, including a seated, pensive figure on the left, witnesses the event in a classical architectural setting. The figure in the white robe in the center appears to be directing or presiding over the miracle. The style is characteristic of the Ferrarese school of painting in the 15th century.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:00:57+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a black-and-white photograph of a Renaissance-era painting. The artist's name, "STEPHANO DA FERRARA," is visible at the bottom center. The painting portrays a dramatic and crowded narrative scene set in a city square with classical architecture.
> 
> The main action takes place on the right side of the composition, where a muscular, barefoot man is in the process of violently killing a serpentine, dragon-like monster. He is forcefully pulling the creature's jaws apart with his bare hands.
> 
> On the left, a diverse crowd of onlookers watches the event. Key figures in the crowd include:
> *   A seated, bearded man in dark robes in the immediate foreground, looking on contemplatively.
> *   Several men and women behind him, some wearing elaborate hats and turbans, typical of Renaissance depictions of historical or biblical scenes.
> *   A man in a white robe in the middle ground, who is gesturing emphatically towards the man fighting the monster.
> 
> The setting is an open plaza framed by grand, classical-style buildings. In the background, more buildings and a city gate are visible. A single tree stands prominently in the right half of the scene.
> 
> To the far right, next to the struggle, is a small, altar-like structure. A lamb or sheep stands on top of it, and inside its arched opening, a skull and bones are visible, suggesting themes of death, sacrifice, and innocence.
> 
> Overall, the painting depicts a heroic or miraculous event, likely a story from mythology or a saint's legend, being witnessed by the public.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:01:19+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of art history and biblical narratives, this painting depicts the story of **David and Goliath**.
> 
> Here is a breakdown of the scene and figures:
> 
> *   **The Episode:** The painting captures the climactic moment from the Old Testament (1 Samuel 17) where the young shepherd David confronts the giant Philistine champion, Goliath. The artist shows the instant David is about to unleash the stone from his sling.
> 
> *   **The Figures:**
>     *   **David:** The dynamic, barefoot figure on the right is David. He is shown in the act of swinging his sling, with stones visible on the ground near his feet. His youth and simple attire contrast with the might of his unseen foe.
>     *   **King Saul and the Israelites:** The crowd on the left represents the Israelite army and court. The prominent, seated, bearded figure in dark robes is most likely **King Saul**, watching the duel with a concerned or contemplative expression. The other figures are his courtiers and soldiers, observing the unlikely champion.
>     *   **Goliath (Symbolic Representation):** Instead of a giant man, the artist has depicted the defeated foe as a monstrous, dragon-like creature lying on the ground. This is a symbolic representation of Goliath as a force of evil and monstrosity, a common artistic convention in the Renaissance to heighten the sense of good triumphing over evil.
> 
> *   **Symbolism:**
>     *   **The Lamb/Sheep:** The sheep standing on the pedestal is a direct reference to David's identity as a shepherd. In Christian iconography, the lamb also symbolizes innocence and can be a prefiguration of Christ (the Lamb of God).
>     *   **The Skull:** The skull visible in the niche below the lamb is a *memento mori*, a reminder of death. It likely represents the fate of Goliath and the triumph of life (the lamb) over death.
> 
> The artist's name, **STEPHANO DA FERRARA**, is inscribed at the bottom of the painting. He was an Italian painter of the Ferrarese School during the Renaissance.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:01:40+00:00_

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

> The Competition of Apollo and Pan and the judgment of Midas

