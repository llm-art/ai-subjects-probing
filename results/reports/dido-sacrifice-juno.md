# Probe report — `dido-sacrifice-juno`

[![dido-sacrifice-juno](https://media.rkd.nl/iiif/2/10904504/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10904504/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10904504/info.json)_

- **Ground-truth subject:** Dido's sacrifice to Juno
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/dido-sacrifice-juno.jpg` — native 5521×3924 px, sent 2048×1456 px
- **SHA-256:** `1737ef4206a1c14a6256c4b4ba5395ef809e181ac3400da11fe27f3099c01e64`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:44:39+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Jacob Jordaens",
>   "title": "Dido's Sacrifice to Juno",
>   "date": "c. 1650",
>   "collection": null
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:45:59+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general art historical knowledge, this is a black and white photograph of a large, classical-style painting. The scene depicts a religious ceremony, specifically a sacrifice, taking place in what appears to be the courtyard of a temple or palace.
> 
> Here is a detailed breakdown of what is depicted:
> 
> *   **Central Action:** A group of figures is gathered around a large, ornate, circular altar or brazier. A crowned woman, the central figure, is making an offering into the brazier, from which smoke or steam is rising. A bearded man, likely a priest, stands opposite her, wearing a laurel wreath and gesturing with his hands. Other figures, including a boy playing a double-pipe instrument (an aulos), surround the altar.
> 
> *   **Figures and Roles:**
>     *   **The Priestess/Queen:** On the left, a woman wearing a spiky crown and elaborate robes leads the ceremony. She is attended by other women, one of whom carries a large jug, and a small child holding an ornate box.
>     *   **The Priest:** On the right, a bearded man in robes and a laurel crown presides over the ritual.
>     *   **Attendants and Worshippers:** Various other figures participate. A muscular, bare-backed man kneels in the foreground, holding a large ewer. Another man holds a large basin. In the background, a figure kneels in prayer.
>     *   **The Sacrifice:** In the foreground, a young bull or heifer with a garland around its neck lies on the ground, apparently prepared for sacrifice.
> 
> *   **Setting and Iconography:**
>     *   The setting is defined by massive classical columns, suggesting a grand temple.
>     *   In the upper right background, a statue of a goddess is seated on a pedestal. Next to her is a **peacock**, which is the traditional attribute of the Roman goddess **Juno** (the Greek Hera).
> 
> **In summary, the image depicts a scene of a sacrifice to the goddess Juno, led by a queen or high priestess in a classical temple setting. The painting is in a grand, likely Baroque or Neoclassical style, characterized by its dynamic composition, dramatic gestures, and classical subject matter.**

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:51:22+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts a scene from classical literature: **The Sacrifice of Dido**.
> 
> This episode is from Book IV of Virgil's epic poem, the *Aeneid*.
> 
> Here is a breakdown of the figures and elements in the scene:
> 
> *   **Dido, Queen of Carthage:** She is the central figure, the woman wearing a crown or diadem. She is shown making an offering, likely a libation of wine or incense, into the fire on the central altar. In the story, consumed by her love for the Trojan hero Aeneas, she performs sacrifices to the gods, particularly Juno, to seek their blessing for her union.
> *   **The Priest:** The bearded man to the right of the altar, wearing a laurel wreath, is the priest officiating the ceremony.
> *   **The Sacrificed Animal:** In the foreground lies a sacrificed bull or heifer, adorned with a wreath. This was a common element of major religious rites in antiquity.
> *   **Attendants:** The scene is filled with Dido's court and temple attendants. We see women carrying ewers (jugs), a child holding a box (perhaps containing incense), a youth playing a double flute (an aulos) to accompany the ritual, and men assisting with the sacrificial elements.
> *   **The Statue of Juno:** In the upper right background, a statue of a seated goddess is visible. Next to her is a **peacock**, which is the sacred animal and primary attribute of the Roman goddess **Juno** (Hera in Greek mythology). This detail is crucial as it confirms the sacrifice is being made in a temple dedicated to Juno, who was the patron goddess of Carthage and of marriage.
> 
> The overall composition, with its grand classical architecture, dramatic gestures, and numerous figures, is typical of a history painting from the Baroque period, a style that favored such epic and emotional subjects.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:46:40+00:00_

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

> Dido's sacrifice to Juno

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:48:49+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Eustache Le Sueur",
>   "title": "Sacrifice to Juno",
>   "date": "c. 1650",
>   "collection": "Musée du Louvre, Paris"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:10:58+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the classical iconography and composition, this image depicts a **classical sacrificial scene, specifically a sacrifice to the Roman goddess Juno**. 
> 
> This is highly likely a depiction of **Queen Dido of Carthage sacrificing to Juno** (a famous episode from Book IV of Virgil's *Aeneid*, where Dido performs sacrifices to Juno, the patron goddess of Carthage and marriage, to seek favor or guidance regarding her love for Aeneas).
> 
> ### Key Elements Depicted:
> * **The Priestess/Queen (Dido):** The crowned female figure on the left-center wears a royal diadem and pours a libation from a small dish (*patera*) onto the burning altar.
> * **The Sacrificial Animal:** A garlanded cow or bull lies on the ground in front of the altar. A semi-nude sacrificial attendant (*victimarius*) kneels beside it, preparing for the ritual. A sacrificial axe and a large pitcher sit on the ground nearby.
> * **The Statue of Juno:** In the background on the far right, a statue of the goddess Juno is shown seated with her sacred attribute, the **peacock**. A woman kneels in prayer at the base of her shrine.
> * **The Priest and Attendants:** To the right of the altar, a hooded priest wearing a laurel wreath (*capite velato*, a traditional Roman sacrificial practice) directs the ceremony. Other attendants carry sacrificial platters, vessels, and an incense box (*acerra*).
> * **Musician:** A youth stands behind the altar playing the double flute (*tibia* or *aulos*), which was traditionally played during Roman sacrifices to drown out any distracting or inauspicious noises.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:11:10+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the classical iconography and details in this squared artwork (likely a cartoon for a tapestry or a preparatory study for a painting), the scene depicted is **The Sacrifice of Dido to Juno**, an episode from Book IV of Virgil's *Aeneid*.
> 
> ### Key Figures and Elements:
> * **Dido (Queen of Carthage):** The crowned woman on the left-center, holding a small bowl (*patera*) and pouring a libation over the burning altar.
> * **Juno:** The goddess to whom the sacrifice is dedicated, represented by the statue in the upper right background, identifiable by her sacred companion, the **peacock**, perched next to her.
> * **Anna:** Dido's sister, who encourages her love for Aeneas, is likely represented by one of the female attendants standing behind Dido on the left.
> * **The Priest:** The bearded man wearing a laurel wreath and a draped hood (*capite velato*), gesturing toward the altar.
> * **The Victimarius (Sacrificial Attendant):** The muscular, semi-nude man kneeling in the foreground next to the garlanded white heifer (the traditional sacrificial animal to Juno), holding a knife with an axe lying on the ground nearby.
> * **Attendants:** Youthful figures playing the double pipes (*tibia*) and carrying platters and vessels for the ritual.
> 
> ### Context:
> In the *Aeneid*, Dido, consumed by her growing passion for the Trojan hero Aeneas, visits the temples with her sister Anna to make sacrifices to the gods—particularly to Juno, the goddess of marriage and patron deity of Carthage—to bless their potential union and seek peace of mind.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:11:35+00:00_

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

> Dido's sacrifice to Juno

