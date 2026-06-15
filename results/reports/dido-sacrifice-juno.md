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

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:45:41+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, I can identify this artwork.
> 
> **Artist:** Jacob Jordaens
> 
> **Title:** The artwork depicts a scene from Virgil's Aeneid, likely titled *Dido Sacrificing to Juno* or simply *The Sacrifice to Juno*.
> 
> **Approximate Date:** Mid-17th century (circa 1630-1640).
> 
> **Analysis:** The scene is identifiable as a classical sacrifice. The central figure is a queen, indicated by her crown, who is officiating at an altar. In the background, a statue of a goddess is seated next to a peacock, the traditional attribute of the Roman goddess Juno (Hera in Greek mythology). This identifies the recipient of the sacrifice. The queen is therefore likely Dido, Queen of Carthage, whose patron goddess was Juno. The style, with its robust figures, dynamic composition, and dramatic lighting, is characteristic of the Flemish Baroque painter Jacob Jordaens, a contemporary of Peter Paul Rubens. In the foreground, a bull has been sacrificed, and various attendants, priests, and musicians participate in the ceremony.

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

