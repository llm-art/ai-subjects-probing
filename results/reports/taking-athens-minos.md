# Probe report — `taking-athens-minos`

[![taking-athens-minos](https://iiif.artresearch.net/iiif/3/frick/4107100296561_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100296561_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100296561_0001.jp2/info.json)_

- **Ground-truth subject:** The Taking of Athens by Minos
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/taking-athens-minos.jpg` — native 6743×2639 px, sent 2048×802 px
- **SHA-256:** `89714876bd19fcc8b35bb18d80645463833363b0fa9e6929306933b7d31bb9fd`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:46:21+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Albrecht Altdorfer",
>   "title": "The Victory of Charlemagne over the Avars near Regensburg",
>   "date": "c. 1518",
>   "collection": "Gabinetto dei Disegni e delle Stampe, Uffizi Gallery"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:02:44+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a black and white image, likely a photograph of a historical painting or print, depicting a large and detailed military scene. The composition is a long horizontal frieze, filled with figures and action, characteristic of Northern Renaissance art. The number "202" is visible in the upper left corner.
> 
> The scene can be divided into three main parts:
> 
> **1. The Background (Left): A City Under Siege**
> In the upper left background, a walled city is being violently assaulted. Soldiers are using ladders to scale the fortified walls, and figures can be seen fighting and falling from the battlements. In front of the city walls, there is a military camp with several tents, indicating a prolonged siege that has culminated in this final attack.
> 
> **2. The Midground and Foreground: A Victorious Procession**
> The main focus of the image is a massive procession of soldiers moving from left to right. This appears to be a victory march leaving the conquered city.
> 
> *   **The Leaders:** At the head of the main mounted group is a prominent, elderly figure with a long white beard and hair. He wears ornate armor and a crown or diadem, identifying him as a king or commander. He is riding a white horse and gesturing forward with his right hand. He is surrounded by a dense throng of knights in full armor, many carrying upright lances that create a forest-like effect. Several banners and standards are held high, one of which has the letters "MESS" or "MISS" visible.
> *   **The Army:** The procession includes both cavalry and infantry. The mounted knights are on armored or decorated horses. Marching alongside them are foot soldiers. Some are in armor, one is seen carrying a flanged mace. A notable figure among the foot soldiers is a shirtless man playing a transverse flute or fife, providing music for the march. In the lower-left foreground, a soldier in armor carries a large, heavy piece of wood, possibly part of a battering ram or other siege engine, away from the battle.
> 
> **3. The Destination (Right): A Rocky Passage**
> The procession is moving towards the right side of the image, where the landscape changes to a rocky cliff face with a dark opening, possibly a cave or a narrow pass that the army is about to enter. The vanguard of the procession, including more figures on horseback, is already nearing this passage.
> 
> Overall, the image captures a narrative moment: the successful conclusion of a siege and the subsequent departure of the victorious army. The artwork is highly detailed, with careful attention paid to the armor, weaponry, and the dynamic movement of the crowd of people and horses.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:03:06+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of art history and biblical narratives, this painting depicts a scene from the Old Testament.
> 
> **Episode:** The scene is **The Victory of Saul over the Amalekites**, from the Book of 1 Samuel, chapter 15. In this story, the prophet Samuel, on behalf of God, commands King Saul to attack and utterly destroy the Amalekites for their past transgressions against Israel.
> 
> **Figures and Scene Description:**
> 
> *   **King Saul:** The central figure on the prancing white horse is King Saul. He is depicted as an elderly, bearded king wearing a crown over his helmet, leading his victorious army.
> *   **The Israelite Army:** The foreground and middle ground are filled with Saul's army, shown as a triumphant procession. The soldiers are depicted in anachronistic early 16th-century European armor, with knights on horseback, foot soldiers carrying long pikes, and musicians (one man is visible playing a fife or flute). This was a common practice in Renaissance art, where biblical or historical events were imagined in contemporary settings.
> *   **The Sacking of the Amalekite City:** In the background on the left, the violent fulfillment of God's command is shown. A walled city is being besieged and sacked. Soldiers are climbing ladders against the walls, fighting on the battlements, and figures are being thrown from the ramparts, illustrating the brutal destruction of the city and its inhabitants. Outside the walls, a military camp with tents is visible.
> 
> The painting uses a technique of continuous narrative, showing both the triumphant procession of the victors in the foreground and the violent battle that led to the victory in the background simultaneously. The style, with its crowded composition, detailed armor, and dramatic landscape, is characteristic of the German Danube School of the early 16th century, and this work is often attributed to the circle of artist **Albrecht Altdorfer**. The number "202" in the top left corner is likely an inventory or collection number added later.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:03:31+00:00_

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

> The Triumph of Mars: an Allegory of War

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:50:45+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": false,
>   "artist": null,
>   "title": null,
>   "date": null,
>   "collection": null
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:17:23+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details in this Renaissance-style narrative painting (likely a cassone panel or similar historical/biblical depiction), the image depicts a continuous narrative of a military campaign or biblical/classical story:
> 
> * **On the left:** A city is under siege, with soldiers scaling the walls using ladders, tents pitched outside, and active combat taking place.
> * **In the center:** A large army of knights and soldiers on horseback and on foot is marching. A prominent banner displays the letters **"MISS..."** (possibly referring to a mission, messenger, or a specific historical name/motto). A knight on a white horse raises a weapon, while another figure on foot is being apprehended or guided.
> * **On the right:** A group of figures, including soldiers and captives, is shown moving toward a rocky cave opening in the hillside, while a horseman on the far right observes the procession.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:18:29+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual details, style, and iconography, this painting depicts the **Justice of Trajan** (specifically, the legendary episode of the Roman Emperor Trajan and the widow).
> 
> ### **Episode and Figures Depicted:**
> * **The Justice of Trajan:** According to medieval legend (popularized in Dante's *Purgatorio*), as Emperor Trajan was setting out with his army for a military campaign (indicated by the city under siege on the left and the marching soldiers), a widow stopped him to demand justice for her son, who had been murdered. 
> * **The Widow and Trajan:** In the center-left, the **widow** (or a figure representing her) stands pleading on foot, pointing downwards, while **Emperor Trajan**, clad in armor and riding a rearing white horse, halts his march to listen to her plea and grant her justice.
> * **The Army:** Surrounding them are Roman soldiers, horsemen, and standard-bearers. The banner flying above the army bears the inscription **"MISS"** (likely referring to *Mission* or a specific military legion/motto).
> * **The Cave/Chasm (Right):** On the far right, soldiers are shown entering a rocky cave or mountain pass, representing the continuation of the military expedition.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:19:35+00:00_

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

