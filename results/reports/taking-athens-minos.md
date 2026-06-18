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

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:02:00+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the style and composition of the artwork, I can identify it.
> 
> **Artist:** Albrecht Altdorfer
> **Title:** This is a scene from the painted version of the *Triumphal Procession of Emperor Maximilian I*. This specific section is often identified as depicting the **Burgundian War** or the **Return of the Imperial Army**. It is part of a larger, unfinished series of miniatures.
> **Approximate Date:** c. 1512–1515
> **Collection:** The surviving fragments of this work are housed in the Albertina Museum in Vienna, Austria.
> 
> The artwork is a highly detailed miniature, likely executed in watercolor and gouache on parchment, although the provided image is a black-and-white reproduction. It showcases Altdorfer's mastery of complex, crowded compositions and his characteristic Danube School style, with a strong emphasis on landscape and atmospheric effects. In the foreground, a vast army with knights on horseback, foot soldiers, and standard-bearers proceeds through a rocky landscape. In the background on the left, a city is being besieged, with soldiers scaling the walls, adding a narrative layer to the triumphal procession. The number "202" in the top left corner is not part of the original artwork but is likely an inventory or photographic plate number.

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

