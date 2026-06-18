# Probe report — `embassy-hippolyta`

[![embassy-hippolyta](https://iiif.artresearch.net/iiif/3/frick/4107100308468_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100308468_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100308468_0001.jp2/info.json)_

- **Ground-truth subject:** The Embassy of Hippolyta Queen of the Amazons to Theseus King of Athens
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/embassy-hippolyta.jpg` — native 5187×3675 px, sent 2048×1451 px
- **SHA-256:** `18d7eb331bdaeea0072d62bdd043c5ec2019ddd9c80a68fa2f8aab7bc05c7179`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:58+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Antonio Pisanello",
>   "title": "The Tournament of Louvezerp",
>   "date": "c. 1447-1448",
>   "collection": "Palazzo Ducale, Mantua"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T07:59:22+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a black and white reproduction of a complex narrative artwork, likely a late medieval or early Renaissance painting or tapestry. The scene is divided into two main parts.
> 
> **On the left:**
> *   An ornate, elevated pavilion or royal box is filled with figures.
> *   A central, enthroned figure of an elderly man with a very long white beard and hair dominates the box. He wears a pointed hat and robes and holds a staff or scepter, suggesting he is a king, judge, or patriarch.
> *   He is flanked by several other figures, both male and female, who appear to be courtiers or members of a royal family, observing the event below.
> *   Below the main box, a scribe with long hair is seated at a lectern, diligently writing with a quill, as if recording the proceedings.
> *   A slender dog, possibly a greyhound, stands on the ground near the scribe, looking towards the right.
> 
> **On the right:**
> *   A procession of figures on horseback emerges from a wooded area.
> *   The riders appear to be predominantly women, dressed in elaborate armor and ornate headdresses.
> *   The lead rider, on a dark horse, is positioned centrally in the composition. She wears a helmet topped with a dragon-like crest and appears to be presenting herself to the figures in the pavilion.
> *   Behind her, other riders on light and dark horses follow, some carrying tall lances or banners.
> *   The background consists of a forest and a distant landscape. The ground is detailed with grass and flowers, reminiscent of a "millefleurs" (thousand flowers) style often seen in tapestries.
> 
> Overall, the image portrays a formal, ceremonial event, such as a tournament, a parade, or the presentation of a company of knights or amazons to a royal court. The style suggests a scene from a chivalric romance, legend, or historical pageant.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T07:59:42+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence and art historical knowledge, this is a black and white reproduction of a famous Italian Renaissance fresco.
> 
> **Scene/Subject:**
> This painting depicts scenes from the court of Duke Borso d'Este in Ferrara. It is a section from the larger fresco cycle known as the **Allegory of the Months** in the **Salone dei Mesi** (Hall of the Months) at the **Palazzo Schifanoia** in Ferrara, Italy.
> 
> **Episode and Figures:**
> This specific panel represents the month of **April**, painted by the artist **Francesco del Cossa** around 1470. The scene is divided into different episodes celebrating the life and rule of the Duke.
> 
> *   **On the left:** We see **Duke Borso d'Este** (the man with the long white beard, though some interpretations suggest it's one of his judges acting on his behalf) seated in a loggia, **administering justice and receiving petitioners**. Below him, a scribe records the proceedings, symbolizing orderly and just governance. The figures surrounding him are members of his court.
> 
> *   **On the right:** A lively procession of courtiers on horseback is depicted. This represents the famous **Palio of Ferrara**, a horse race and festival held in the city. The elegantly dressed women on horseback are noble ladies of the court participating in the festivities. They are not warriors, but their formal attire, banners, and the context of the parade give them a chivalric appearance.
> 
> In essence, the fresco is a piece of political propaganda, glorifying Duke Borso d'Este by showcasing the peace, justice, and prosperity of his domain through scenes of good government and the happy, leisurely activities of his subjects.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:00:04+00:00_

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

_Run: 2026-06-18T13:50:23+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Apollonio di Giovanni",
>   "title": "Penthesilea before Priam",
>   "date": "c. 1450-1460",
>   "collection": null
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:15:09+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the style and iconography, this image depicts a 15th-century Italian Renaissance painting (likely a *cassone* or chest panel, often associated with the Florentine workshop of Apollonio di Giovanni). 
> 
> The scene represents a classical or mythological narrative, most likely **Penthesilea, Queen of the Amazons, presenting herself before King Priam of Troy** (or a similar subject, such as the warrior maiden Camilla before King Latinus).
> 
> ### Key Elements Depicted:
> * **The Ruler (Left):** An elderly, bearded king (representing King Priam of Troy) sits on an elevated throne under an ornate loggia. He wears a tall, pointed Eastern-style hat (typical of Renaissance depictions of Byzantine or Trojan royalty) and holds a scepter.
> * **The Scribe (Foreground Left):** A notary or scribe sits at a desk below the throne, writing on a scroll to record the alliance or treaty, with a greyhound standing nearby.
> * **The Amazon Procession (Right):** A group of female warriors on horseback emerges from a wooded landscape. The leading figure, Queen Penthesilea, rides a dark horse and wears armor with an elaborate, crested helmet. She gestures toward the king, offering her army's aid in the Trojan War.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:15:30+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the iconography and style of this 15th-century Italian Renaissance painting (likely a Florentine *cassone* or *spalliera* panel), the scene depicted is **Penthesilea, Queen of the Amazons, presenting herself before King Priam of Troy** (often titled *The Arrival of Penthesilea at Troy* or *Penthesilea before King Priam*).
> 
> ### Key Figures and Elements:
> * **King Priam of Troy:** The elderly, wise king with the long white beard, seated on the high throne under the loggia on the left, holding a scepter.
> * **Penthesilea:** The Queen of the Amazons, depicted on the dark horse in the center. She wears armor and a helmet with a prominent dragon/winged crest as she offers her alliance to Troy.
> * **The Amazons:** Her retinue of female warriors on horseback behind her, also wearing helmets and armor.
> * **The Scribe/Notary:** Seated at the desk in the lower left, recording the alliance or treaty between the Trojans and the Amazons. 
> * **The Greyhound:** A classic symbol of courtly nobility and fidelity standing near the desk.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:15:46+00:00_

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

