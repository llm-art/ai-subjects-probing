# Probe report — `athena-pegasus`

[![athena-pegasus](https://media.rkd.nl/iiif/2/9166525/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9166525/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9166525/info.json)_

- **Ground-truth subject:** The goddess Pallas Athena and the horse Pegasus
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/athena-pegasus.jpg` — native 5698×4317 px, sent 2048×1552 px
- **SHA-256:** `30d70fc5739e09fb5ed881f054256199ed51f37c5621a15e5028743ed2ca761e`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:44:33+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Cornelis Schut I",
>   "title": "Minerva with Pegasus",
>   "date": "1644",
>   "collection": null
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:44:54+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general knowledge of classical mythology, here is a description of what is depicted:
> 
> This is a painting of a scene from classical mythology, featuring the goddess Athena (or her Roman equivalent, Minerva) with the winged horse, Pegasus.
> 
> **Key Figures and Elements:**
> 
> *   **Athena/Minerva:** The central figure is a woman dressed in the attire of a warrior goddess. She wears an ornate black helmet with a large red plume, a metal breastplate over a white and grey tunic, and a flowing red cloak. She holds a long spear in her right hand and is using both hands to hold the golden bridle of Pegasus.
> *   **Pegasus:** To the left is the mythological winged horse, Pegasus. He is depicted as a powerful white stallion with large, feathered wings. He stands calmly as the goddess holds his bridle.
> *   **A Putto (or Cherubic Boy):** To the right of Athena, a small, muscular boy, resembling a putto, struggles to carry her large, ornate shield. The shield is decorated with golden, swirling patterns.
> *   **The Owl:** In the lower right corner, nestled amongst some plants, is a small owl looking out at the viewer. The owl is the primary symbol of Athena/Minerva, representing wisdom.
> 
> **Setting and Style:**
> 
> The scene is set in a dramatic, moody landscape under a dark, cloudy sky that brightens at the horizon. The style of the painting is characteristic of the Baroque period, with its dynamic composition, rich colors, and dramatic use of light and shadow (chiaroscuro) to model the figures and create a sense of volume and movement.
> 
> In summary, the painting depicts the goddess of wisdom and warfare, Athena/Minerva, taming or presenting the divinely-inspired Pegasus, accompanied by her symbolic owl and an attendant carrying her shield.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:45:09+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge of classical mythology and art history, this is a depiction of a scene from Greek/Roman mythology.
> 
> **Subject:** The painting shows the goddess **Minerva** (the Roman equivalent of the Greek goddess **Athena**) with the winged horse, **Pegasus**.
> 
> **Figures and Episode:**
> 
> *   **Minerva/Athena:** The central figure is identifiable as Minerva/Athena. She is depicted as a warrior goddess, wearing a helmet with a red plume, a metal cuirass (breastplate), and carrying a spear. Her primary symbol, an **owl**, is visible in the lower right corner, confirming her identity as the goddess of wisdom and strategic warfare.
> *   **Pegasus:** The magnificent white horse with large, feathered wings is Pegasus, one of the most famous creatures from Greek mythology.
> *   **Putto/Attendant:** To the right, a small, cherubic figure (a putto) acts as an attendant or squire, struggling to carry Minerva's large, ornate shield.
> 
> The specific episode depicted is likely **Minerva taming Pegasus**. According to myth, the hero Bellerophon wished to ride the untamable Pegasus. The goddess Minerva appeared to him in a dream and gave him a magical golden bridle, which is visible in the painting in Minerva's hand as she holds the horse. This bridle allowed Bellerophon to tame the creature. This painting captures the moment of Minerva's mastery over the wild, divine horse, symbolizing wisdom and intellect (Minerva) taming poetic inspiration or untamed nature (Pegasus).

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:45:26+00:00_

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

> The goddess Pallas Athena and the horse Pegasus

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:48:41+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Theodoor van Thulden",
>   "title": "Minerva and Pegasus",
>   "date": "1654",
>   "collection": "Royal Museum of Fine Arts Antwerp"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:10:27+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This painting is titled ***Minerva Bridling Pegasus*** (also known as *Minerva and Pegasus*), created in 1654 by the Flemish Baroque painter **Theodoor van Thulden** (whose signature and date are visible in the bottom-left corner). 
> 
> The artwork depicts a scene from classical mythology rich in allegorical symbolism:
> 
> * **Minerva (Athena):** The Roman goddess of wisdom, war, and the arts stands in the center. She is depicted as a strong, elegant warrior wearing a classical helmet with a large red plume, a dark breastplate, a flowing red cloak, and a long skirt. She is shown taming or guiding the mythical winged horse, **Pegasus**, by holding his golden bridle. This act traditionally symbolizes the taming of wild impulses, passion, or poetic inspiration through wisdom and reason.
> * **Pegasus:** The magnificent white winged horse stands on the left, looking towards Minerva with one hoof raised.
> * **The Putto and Shield:** To the right, a young boy (putto or attendant) struggles to hold up Minerva's large, ornate golden shield (the *Aegis*), which features the sculpted face of Medusa. 
> * **The Owl:** In the bottom-right corner, Minerva's sacred owl—the symbol of wisdom and vigilance—is perched on the ground near some leafy plants.
> * **The Spear:** A tall spear stands upright behind Minerva, pointing toward the sky.
> 
> The painting is rendered in a classic Baroque style, characterized by dramatic lighting, rich colors (particularly the contrast of the white horse and the vibrant red cloak), and a sense of dynamic movement set against a dark, cloudy sky.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:10:36+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the mythological scene of **Minerva (Athena) bridling Pegasus** (often titled *Minerva and Pegasus* or *Minerva Bridling Pegasus*). 
> 
> ### Figures and Elements Depicted:
> * **Minerva (Athena):** The Roman/Greek goddess of wisdom and war, shown in classical armor, a plumed helmet, and a red cloak, placing a golden bridle on the winged horse.
> * **Pegasus:** The mythical winged white horse, born from the blood of Medusa.
> * **Putto/Squire:** A young boy behind Minerva who struggles to hold her heavy shield (the Aegis, which traditionally bears the image of Medusa's head).
> * **The Owl:** Located in the bottom right corner, the owl is the traditional symbol of Minerva, representing wisdom.
> 
> ### Artist and Context:
> This work is by the Flemish Baroque painter **Theodor van Thulden**, signed and dated in the bottom-left corner (*"Theod. Thulden fec. 1654"*). The scene allegorically represents Wisdom (Minerva) guiding and controlling poetic inspiration or fame (Pegasus).

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:10:47+00:00_

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

> The goddess Pallas Athena and the horse Pegasus

