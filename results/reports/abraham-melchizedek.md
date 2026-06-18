# Probe report — `abraham-melchizedek`

[![abraham-melchizedek](https://iiif.artresearch.net/iiif/3/frick/56823_POST.tif/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/56823_POST.tif/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/56823_POST.tif/info.json)_

- **Ground-truth subject:** Abraham Meeting Melchizedek
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/abraham-melchizedek.jpg` — native 8674×6460 px, sent 2048×1525 px
- **SHA-256:** `269766a3cc17f66b719f864c93822efaf09e228ee20e6d11b45e96182287aa95`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:46:47+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Peter Paul Rubens",
>   "title": "The Meeting of Abraham and Melchizedek",
>   "date": "c. 1626",
>   "collection": "National Gallery of Art, Washington D.C."
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:03:54+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general knowledge of art history and biblical narratives, this painting depicts the Old Testament scene of **the meeting of Abraham and Melchizedek**.
> 
> Here is a detailed description of what is visible:
> 
> The scene is set in a lush, wooded landscape with rolling hills in the background. It portrays an encounter between two distinct groups of people.
> 
> *   **On the right**, stands a group of religious figures. The most prominent is a venerable, white-bearded high priest, representing **Melchizedek**, the king of Salem. He is dressed in the anachronistic but iconographically typical vestments of a Christian bishop, including a tall mitre on his head and ornate robes. He extends his hands towards the kneeling figure, offering him what appears to be bread. He and his attendants stand before a stone altar on which are placed baskets and ornate liturgical vessels. Another priest, seen from the back, wears a highly decorated chasuble.
> 
> *   **On the left**, a military leader, representing **Abraham**, kneels in reverence before Melchizedek. He is clad in armor, with his plumed helmet resting on the ground beside him. Behind him is his retinue of soldiers and followers, some on horseback, suggesting they have just returned from a battle. A woman is visible among them, riding a light-colored horse. A dark dog stands in the lower-left foreground.
> 
> The painting captures the moment from the Book of Genesis (14:18-20) where Melchizedek, "priest of God Most High," brings out bread and wine to bless Abraham after his victory in battle. In Christian art, this event is often interpreted as a prefiguration of the Eucharist, which explains the depiction of Melchizedek in Christian priestly attire. The overall composition and dramatic interaction are characteristic of Baroque history painting.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:04:15+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history and biblical narratives, this painting depicts the Old Testament scene of **The Meeting of Abraham and Melchizedek**.
> 
> Here is a breakdown of the figures and the episode:
> 
> *   **The Episode:** The scene is from the Book of Genesis (14:18-20). After defeating several kings and rescuing his nephew Lot, the patriarch Abraham is met by Melchizedek, the king of Salem and a priest of God. Melchizedek brings out bread and wine, blesses Abraham, and Abraham gives him a tenth of all the spoils of his victory.
> 
> *   **The Figures:**
>     *   **Abraham:** He is the central figure on the left, depicted as a warrior in armor. He is kneeling in a gesture of respect and reverence, having removed his helmet, which lies on the ground before him. He is reaching out to receive the offering. Behind him are his soldiers and retinue, some on horseback, representing his victorious army.
>     *   **Melchizedek:** He is the prominent figure on the right, portrayed as a high priest with a long white beard. He wears ornate liturgical vestments, including a tall, pointed hat known as a mitre, which signifies his high priestly status. He is offering bread and wine to Abraham.
> 
> **Symbolism and Context:**
> 
> This subject was very popular in European Christian art, particularly during the Counter-Reformation. The scene holds significant theological importance as it is seen as a **prefiguration of the Eucharist** (or Holy Communion) in Christianity. Melchizedek's offering of bread and wine is interpreted as a foreshadowing of Christ's offering of his body and blood at the Last Supper. For this reason, Melchizedek is considered a "type" of Christ, a priest-king who stands outside the traditional Levitical priesthood. The painting thus serves not just as a historical narrative but as a theological statement about the sacrament of the Eucharist.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:04:33+00:00_

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

> The Gathering of Manna

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:51:04+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Gaspar de Crayer",
>   "title": "The Conversion of Saint Bavo",
>   "date": "c. 1630-1650",
>   "collection": "Museum of Fine Arts, Ghent"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:17:52+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this image depicts a historical or biblical meeting between a military leader and a high priest, most likely **Alexander the Great before the High Priest of Jerusalem (Jaddua)** or **The Meeting of Abraham and Melchizedek**. 
> 
> Key elements visible in the scene include:
> * **The Kneeling Warrior:** On the left, a commander or king in full classical/medieval armor kneels in reverence, having placed his helmet on the ground before the priest. Behind him is his retinue of soldiers and horses.
> * **The High Priest / Bishop:** On the right stands a religious figure dressed in elaborate liturgical vestments, including a mitre and an embroidered cope, gesturing toward the kneeling warrior.
> * **The Altar:** To the far right, there is a classical stone pedestal supporting a large, burning urn or sacrificial vessel, symbolizing a temple or place of sacrifice.
> * **The Setting:** The encounter takes place outdoors in a hilly, wooded landscape, with a dog in the lower-left foreground.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:18:06+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the iconographical details, this painting depicts the Old Testament scene of **The Meeting of Abraham and Melchizedek** (from Genesis 14:18–20). 
> 
> ### Key Figures and Scene Details:
> * **Abraham** is the figure kneeling in the center in full contemporary (17th-century style) plate armor, having laid his helmet on the ground. He has just returned from his military victory over Chedorlaomer to rescue his nephew Lot.
> * **Melchizedek**, the King of Salem and "priest of God Most High," is depicted on the right. In line with Counter-Reformation Catholic theology, he is represented here as a Christian bishop wearing a mitre and an embroidered cope, offering bread (resembling a Eucharistic host) to Abraham. 
> * **The Assistants and Altar:** To the right, behind Melchizedek, assistants prepare the wine (represented by the large ornate chalice/ewer on the ground). On the far right, a sacrificial altar features a large burning urn, symbolizing a sacred offering.
> * **Abraham's Retinue:** On the left, Abraham's soldiers and horses wait in a wooded landscape, accompanied by a dog in the foreground.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:18:33+00:00_

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

> The painting depicts **The meeting of Abraham and Melchizedek** (Melchizedek offering bread and wine to Abraham). 
> 
> *(Note: This correct subject is missing from the provided list of options).*

