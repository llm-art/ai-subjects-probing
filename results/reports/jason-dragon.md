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

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:46:02+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Stefano da Ferrara",
>   "title": "Miracle of Saint Maurelius",
>   "date": "c. 1480",
>   "collection": "Pinacoteca Nazionale, Ferrara"
> }
> ```

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

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:50:30+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Stefano da Ferrara",
>   "title": "Jason and the Golden Fleece",
>   "date": "c. 1490",
>   "collection": null
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:15:35+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details and the inscription at the bottom, this image depicts the mythological story of **Jason and the Golden Fleece** (specifically, Jason subduing or slaying the dragon guarding the Golden Fleece), attributed to the 15th-century Italian painter **Stefano da Ferrara** (as inscribed: *"STEPHANO DA FERRARA"*).
> 
> ### Key Elements Depicted:
> * **Jason and the Dragon:** On the right, Jason is shown in mid-strike, raising a weapon to slay the serpent/dragon coiled around a tree.
> * **The Golden Fleece:** Next to the tree, the Golden Fleece is represented by a ram standing atop a classical stone altar. 
> * **The Altar and Skull:** Beneath the ram, inside the arched niche of the altar, a human skull is visible.
> * **The Onlookers:** On the left, a crowd of spectators in Renaissance-style clothing watches the event. A prominent seated man in the lower-left foreground looks on.
> * **Background:** Classical architectural ruins, arches, and distant figures set the scene in an ancient landscape.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:15:48+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual details and historical context, this painting depicts the mythological story of **Jason and the Golden Fleece** (specifically, Jason slaying or taming the dragon guarding the Golden Fleece). 
> 
> ### **The Scene and Figures Depicted:**
> 
> * **Jason:** The central heroic figure on the right, shown in mid-swing wielding a weapon (a club or sword) to defeat the guardian serpent.
> * **The Dragon/Serpent:** Coiled around the tree trunk, guarding the prize.
> * **The Golden Fleece (The Ram):** Represented here as a living ram standing on a stone altar/pedestal to the right of the tree.
> * **King Aeëtes of Colchis:** The seated ruler on the far left, wearing a hat and robes, watching Jason perform this seemingly impossible task.
> * **Medea:** The young woman standing in the crowd on the left, looking on. In the myth, she is Aeëtes' daughter who fell in love with Jason and gave him the magical herbs/potions necessary to subdue the dragon.
> * **The Colchian Court / Spectators:** The crowd of onlookers on the left dressed in Renaissance-era and exoticized Eastern costumes (turbans and hats), watching the trial.
> 
> ### **Artist Attribution:**
> As inscribed at the bottom of the frame, the painting is historically attributed to **Stefano da Ferrara** (Stefano di Benedetto), a 15th-century Italian painter of the Ferrarese School.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:16:01+00:00_

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

