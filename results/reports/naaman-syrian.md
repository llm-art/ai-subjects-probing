# Probe report — `naaman-syrian`

[![naaman-syrian](https://iiif.artresearch.net/iiif/3/frick/4107100250039_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100250039_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100250039_0001.jp2/info.json)_

- **Ground-truth subject:** The Story of the Syrian Captain Naaman
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/naaman-syrian.jpg` — native 7878×6425 px, sent 2048×1670 px
- **SHA-256:** `9c4c9ac6140aa3ef076a1b90bad07c31955aae89f9aab2e253490291b81926bf`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:04+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Hieronymus Bosch",
>   "title": "Triptych of the Baptism of Christ",
>   "date": "c. 1500",
>   "collection": "Royal Museums of Fine Arts of Belgium"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:05:38+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual information in the image, this is a monochrome photograph of a triptych, a three-paneled artwork, characteristic of Early Netherlandish painting. The central panel depicts a major religious scene, while the side panels, or wings, feature other figures and continue the landscape.
> 
> Here is a breakdown of what is depicted in each panel:
> 
> **Central Panel:**
> The main subject is the **Baptism of Christ**.
> *   In the foreground, a bearded, long-haired, and nearly nude man, representing **Jesus Christ**, stands waist-deep in a river. His arms are crossed over his chest in a gesture of humility.
> *   To his right, on the riverbank, stands a man in robes with a turban-like headdress, representing **John the Baptist**. He is in the act of baptizing Jesus.
> *   The scene is set in an expansive and detailed landscape filled with numerous other figures, buildings, and natural elements. Winding paths, bridges, and a river lead the eye into the background.
> *   The background is a vast "world landscape," featuring fantastical and contemporary architecture, including castles, fortified towns, and rocky crags. This style, combining a religious event with a panoramic, detailed world, is typical of the period.
> 
> **Left Panel (Left Wing):**
> *   In the foreground, a prominent figure, likely the **donor** who commissioned the altarpiece, is seated. He is depicted as a high-ranking clergyman, possibly an abbot or bishop, wearing elaborate vestments and a mitre-like headdress. He looks towards the central scene with a gesture of piety.
> *   Behind him is an entourage of figures, some on horseback, suggesting a procession.
> *   The landscape and architecture seamlessly continue from the central panel, showing a fortified city gate.
> 
> **Right Panel (Right Wing):**
> *   In the foreground, another seated figure is depicted, mirroring the donor on the left. This man is older, with a gaunt and intense expression. He is dressed in more common, slightly ragged clothing and holds a long staff that resembles a poleaxe or halberd. He points towards the central scene. This figure could be a patron saint of the donor or another significant individual.
> *   Behind him, another group of figures, some mounted on horses with packs, continues the theme of a world bustling with activity.
> *   The cityscape from the central panel extends into this wing, with more towers and buildings visible.
> 
> **Overall Style:**
> The artistic style is characteristic of the circle of **Hieronymus Bosch** (c. 1450–1516). This is evident in the detailed and imaginative landscape, the slightly strange and expressive (sometimes verging on grotesque) character of the figures in the crowd, and the combination of a sacred narrative with a complex, worldly setting. The entire composition is unified by the continuous landscape that flows across all three panels.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:06:04+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history and religious iconography, this is a triptych (a three-paneled artwork) depicting the **Baptism of Christ**.
> 
> Here is a breakdown of the scene and figures:
> 
> *   **Central Panel:** The main event is in the center.
>     *   **Jesus Christ:** The nearly nude figure standing in the river is Jesus. His pose, with arms crossed over his chest, suggests humility and acceptance.
>     *   **John the Baptist:** The man standing on the riverbank to the right is John the Baptist. He is gesturing towards Jesus and appears to be holding Jesus's garment. In the background, a vast and detailed "world landscape" unfolds, filled with mountains, castles, bridges, and numerous small figures going about their lives, which was a common feature in Northern Renaissance painting.
> 
> *   **Left Panel:**
>     *   **Donor Portrait:** The seated figure in the foreground is a donor portrait, likely the person who commissioned the altarpiece. His rich clerical robes, including an ornate headpiece (a form of mitre), suggest he was a high-ranking ecclesiastic, such as an abbot or a bishop. He gazes towards the central scene, making him a perpetual witness to the sacred event. Behind him are his attendants and followers, part of a procession that seems to lead into the central landscape.
> 
> *   **Right Panel:**
>     *   **Donor Portrait or Patron Saint:** The seated figure in the foreground is likely another donor or a patron saint associated with the first donor. He is dressed more plainly and holds a long staff or poleaxe. Like the figure on the left, he is turned towards the Baptism, acting as an observer. Behind him, more figures on horseback and foot populate the continuous landscape that connects all three panels.
> 
> In summary, the artwork uses the triptych format to present the biblical episode of the Baptism of Christ as the central focus, flanked by portraits of the patrons who are shown participating in the scene through their devout observation. The entire scene is set within an expansive, meticulously detailed landscape characteristic of Early Netherlandish painting from the late 15th or early 16th century.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:06:24+00:00_

**Prompt:**

> This painting depicts one of the following subjects. Which one is it?
> — The finding of Moses: Pharaoh's daughter discovers the child floating on the river
> — The sacrifice of Isaac (Abraham and Isaac)
> — Potiphar's wife catches Joseph by his robe; Joseph escapes
> — Balaam strikes his ass; the ass lies down and starts to speak
> — Isaac blesses Jacob disguised in Esau's clothes
> — Samson breaks the pillars; the temple of Dagon collapses
> — The drunkenness of Noah
> — Feast of Esther
> — Belshazzar's Feast
> — Bathsheba receives a letter from David
> — The Gathering of Manna
> — Hagar, Ishmael and the Angel in the Wilderness
> — The Prodigal Son chased from the brothel (Luke 15:13)
> — Jephtha welcomed by his daughter (Judges 11:29-40)
> — Judah's love-affair with Tamar; he gives her his signet-ring and staff
> Answer with the subject only.

**Response (verbatim):**

> Hagar, Ishmael and the Angel in the Wilderness

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:51:25+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Lucas van Leyden",
>   "title": "Triptych with the Baptism of Christ",
>   "date": "1521",
>   "collection": "Museo Nacional Thyssen-Bornemisza, Madrid"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:19:08+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This image is a black-and-white photograph of a Northern Renaissance triptych depicting the Old Testament story of **Naaman the Syrian being cured of his leprosy** by bathing in the River Jordan (from 2 Kings 5). 
> 
> Here is a breakdown of what is depicted in each panel:
> 
> *   **Central Panel (Naaman Bathing in the Jordan):** 
>     In the center, Naaman is shown standing nude in the River Jordan, washing himself and inspecting his skin to see if his leprosy has been healed. On the right bank, a servant or companion dressed in rich Eastern attire (including a turban) holds Naaman's garments. The background features a detailed landscape with a winding river, a stone bridge, a prominent tower, and a castle on a hill, along with figures from Naaman's caravan.
> 
> *   **Left Panel (The King of Israel Receiving the Letter):** 
>     This panel depicts the King of Israel (Jehoram) seated in the foreground, looking distressed and gesturing with his hand. This represents the moment he received the letter from the King of Syria asking him to cure Naaman, which caused him to tear his clothes in despair, fearing it was a pretext for war. He is surrounded by his courtiers and soldiers.
> 
> *   **Right Panel (Naaman's Retinue):** 
>     In the foreground, a guard or soldier sits holding a halberd, pointing toward the central scene. In the background, Naaman's horses, carriages, and soldiers are shown waiting near a castle. 
> 
> The artwork is executed in the early 16th-century Netherlandish style, characteristic of the Leiden school (associated with artists like **Lucas van Leyden** or **Cornelis Engelbrechtsz**).

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:19:39+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This is a Netherlandish triptych painting (often attributed to **Cornelis Engelbrechtsz** or his workshop, circa 1515–1520) depicting the Old Testament story of **Naaman the Syrian bathing in the River Jordan** to cure his leprosy (from **2 Kings 5**).
> 
> ### Depicted Scene and Figures:
> 
> * **Central Panel (Naaman Bathing in the Jordan):** 
>   The central figure is **Naaman**, the commander of the army of the King of Syria. He stands naked in the River Jordan, looking down at his arm to see his skin being miraculously healed and restored ("like the flesh of a little child"). On the right bank, his servants and retinue wait with his rich garments and horses.
>   
> * **Left Panel (Naaman before the King of Israel):** 
>   This panel depicts the earlier part of the narrative where Naaman, sent by the King of Syria with a letter and treasures, presents himself to the **King of Israel** (seated on the left in royal robes) to be cured. 
> 
> * **Right Panel (Naaman's Retinue / Gehazi):** 
>   This panel shows Naaman's servants and horses preparing to return home, or Elisha's servant **Gehazi** pursuing Naaman's caravan to greedily demand the gifts that Elisha had previously refused.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:19:50+00:00_

**Prompt:**

> This painting depicts one of the following subjects. Which one is it?
> — The finding of Moses: Pharaoh's daughter discovers the child floating on the river
> — The sacrifice of Isaac (Abraham and Isaac)
> — Potiphar's wife catches Joseph by his robe; Joseph escapes
> — Balaam strikes his ass; the ass lies down and starts to speak
> — Isaac blesses Jacob disguised in Esau's clothes
> — Samson breaks the pillars; the temple of Dagon collapses
> — The drunkenness of Noah
> — Feast of Esther
> — Belshazzar's Feast
> — Bathsheba receives a letter from David
> — The Gathering of Manna
> — Hagar, Ishmael and the Angel in the Wilderness
> — The Prodigal Son chased from the brothel (Luke 15:13)
> — Jephtha welcomed by his daughter (Judges 11:29-40)
> — Judah's love-affair with Tamar; he gives her his signet-ring and staff
> Answer with the subject only.

**Response (verbatim):**

> thought
> The painting shown is the famous **Triptych with the Baptism of Christ** (1521) by the Dutch Renaissance artist Lucas van Leyden, currently in the collection of the Rijksmuseum in Amsterdam. 
> 
> However, none of the options provided in the list correspond to "The Baptism of Christ." Since the prompt asks to choose from the provided list, and the central panel depicts a naked man standing in a river (the Jordan) while another man on the bank holds his robe, this scene is sometimes iconographically compared to or misidentified in certain databases as **The finding of Moses: Pharaoh's daughter discovers the child floating on the river** (due to the river setting and figures on the bank) or **The drunkenness of Noah** (due to the nakedness and the covering with a garment). 
> 
> Among the options, the closest thematic and visual misclassification in automated datasets for this specific image is:
> 
> — The finding of Moses: Pharaoh's daughter discovers the child floating on the river

