# Probe report — `rape-deianira`

[![rape-deianira](https://iiif.artresearch.net/iiif/3/frick/4107100295528_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100295528_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100295528_0001.jp2/info.json)_

- **Ground-truth subject:** The Rape of Deianira
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/rape-deianira.jpg` — native 5771×4042 px, sent 2048×1434 px
- **SHA-256:** `08b3630eeeac0d1377d8c1ae4dffd84267fc8b852c548165dd1effc4c7acd5ca`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:46:13+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Antonio del Pollaiuolo",
>   "title": "The Rape of Deianira",
>   "date": "c. 1470-1475",
>   "collection": "Yale University Art Gallery"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:01:28+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image and my internal knowledge, this is a black and white photograph of a painting depicting a famous scene from Greek mythology: **The Abduction of Deianira by the Centaur Nessus**.
> 
> Here is a breakdown of what is depicted:
> 
> *   **The Central Action:** On the left, a centaur (a creature with the upper body of a man and the lower body of a horse) named Nessus is forcefully carrying a woman, Deianira, across a river. Deianira looks distressed, turning back and raising her arms as she is being abducted.
> *   **The Hero:** On the right bank, the hero Hercules (Heracles) is shown in a dynamic pose, drawing a bow and aiming an arrow at the centaur to rescue his wife, Deianira. His muscular physique is emphasized, highlighting his heroic nature.
> *   **The Setting:** The scene is set in a vast, detailed landscape with a winding river, rolling hills, and trees, which is characteristic of Italian Renaissance painting.
> 
> The caption at the bottom of the image identifies the artist as **POLLAIUOLO, ANTONIO**, a prominent Florentine artist of the Renaissance, and the title as "THE RAPE OF DEI...", which would be "The Rape of Deianira". In this historical context, the word "rape" primarily means abduction or seizure, rather than its modern-day connotation.
> 
> In summary, the image captures the dramatic climax of the myth where Hercules must act swiftly to save his wife from the treacherous centaur Nessus.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:01:48+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts a famous episode from Greek mythology.
> 
> The scene is **The Rape of Deianira**, which in this classical context refers to her abduction.
> 
> The figures depicted are:
> *   **Nessus:** The centaur (half-man, half-horse) who is carrying the woman across the river.
> *   **Deianira:** The woman being abducted by Nessus. She is the wife of Hercules.
> *   **Hercules (Heracles):** The muscular man on the right bank, drawing his bow to shoot an arrow at Nessus to save his wife.
> 
> The painting captures the dramatic moment when the centaur Nessus, having offered to carry Deianira across a river, attempts to run off with her. Her husband, Hercules, having already crossed, takes aim to kill the centaur.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:02:01+00:00_

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

> Based on the visual evidence in the image, none of the provided options are correct.
> 
> The painting depicts the myth of the abduction of Deianira by the centaur Nessus, who is then shot by Hercules with a bow and arrow. This subject is commonly known as "The Rape of Deianira." The label at the bottom of the photograph confirms the artist, Pollaiuolo, and the title, which begins "THE RAPE OF DEI...".

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:50:41+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Antonio del Pollaiuolo",
>   "title": "Hercules and Deianira",
>   "date": "c. 1470",
>   "collection": "Yale University Art Gallery"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:15:53+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details and the text at the bottom, this image depicts the famous Renaissance painting ***The Rape of Deianira*** (also known as *Hercules and Deianira*) by the Italian artist **Antonio del Pollaiuolo** (c. 1470). 
> 
> The scene illustrates a well-known story from Greek mythology:
> 
> * **The Centaur Nessus (left):** He is shown carrying away **Deianira**, the wife of Hercules, across the river Evenus under the pretense of helping her cross, but instead attempting to abduct her.
> * **Hercules (right):** Standing on the riverbank, Hercules draws his bow to shoot Nessus with an arrow poisoned with the blood of the Lernaean Hydra to rescue his wife.
> * **The Landscape:** The background features a detailed, sweeping view of a river valley, which is historically identified as a depiction of the Arno River valley near Florence, Italy. 
> 
> The image itself is a black-and-white archival photograph or print of the original painting, which is housed in the Yale University Art Gallery.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:16:01+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting is **"Hercules and Deianira"** (also known as *The Rape of Deianira* or *Hercules, Deianira and the Centaur Nessus*), painted by the Italian Renaissance artist **Antonio del Pollaiuolo** (c. 1470).
> 
> ### **The Episode and Figures Depicted:**
> * **The Episode:** The scene depicts the mythological rescue of **Deianira** from the centaur **Nessus** by her husband, the hero **Hercules** (Heracles). 
> * **The Figures:**
>   * **Hercules (Heracles)** (on the right): Standing on the riverbank, aiming his bow to shoot Nessus with an arrow dipped in the lethal poison of the Lernaean Hydra.
>   * **Nessus** (on the left): The centaur who offered to carry Deianira across the rushing river Evenus, but instead attempted to abduct and assault her once they reached the other side.
>   * **Deianira** (clinging to the centaur): Hercules' wife, crying out for help as she is carried away.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:16:08+00:00_

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

> The painting depicts **The Rape of Deianira** (also known as *Hercules and Nessus* or *Hercules, Deianira and the Centaur Nessus*) by Antonio del Pollaiuolo. 
> 
> *(Note: This correct subject is not present in the provided list of options, but it is the actual subject of the artwork, as also indicated by the label at the bottom of the image).*

