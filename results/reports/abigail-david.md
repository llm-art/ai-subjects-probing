# Probe report — `abigail-david`

[![abigail-david](https://iiif.artresearch.net/iiif/3/frick/4107100263573_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100263573_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100263573_0001.jp2/info.json)_

- **Ground-truth subject:** Abigail in Supplication before David
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/abigail-david.jpg` — native 3882×5041 px, sent 1577×2048 px
- **SHA-256:** `54bb4bb657fa1b994bb192c654c8e40538284bf8fcfb7dc5a8cb56fff5bfb426`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:03:50+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history, this is the painting:
> 
> *   **Artist:** Master of the David Scenes in the Grimani Breviary
> *   **Title:** *The Meeting of David and Abigail*
> *   **Approximate Date:** about 1515
> *   **Collection:** The J. Paul Getty Museum, Los Angeles
> 
> The painting depicts the Old Testament story from 1 Samuel 25. Abigail, the wife of the wealthy but foolish Nabal, kneels before King David to plead for her household. David, on his way to destroy Nabal for an insult, is placated by Abigail's wisdom and humility. In the painting, David is the central figure on the white horse, leading his army (seen on the left). Abigail kneels before him, accompanied by her attendants. The army with camels in the right background likely represents the provisions Abigail brought as a gift for David and his men. In the sky, God the Father with angels looks down, signifying divine approval of this act of peacemaking.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:04:54+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general art historical knowledge, here is a description of what is depicted:
> 
> This is a black and white photograph of a complex and detailed narrative painting, characteristic of the late Gothic or early Northern Renaissance period (circa 15th century). The scene is crowded with figures and action, set within a deep landscape.
> 
> **Central Scene:**
> In the foreground, the main focus is on an interaction between three figures.
> *   A central figure, likely a saint as indicated by a faint halo, is mounted on a white horse. This figure is androgynous but appears to be male, dressed in ornate, dark, brocaded clothing over armor. He holds a long lance and looks down with a gentle expression. The horse is adorned with a decorative harness.
> *   Kneeling before the saint is a noblewoman in a long, flowing gown with rich, patterned trim. She wears an elaborate headdress with a veil and holds her hands up in a gesture of reverence or supplication.
> *   Standing between them is a younger figure, possibly a page or squire, holding a large banner.
> 
> **Surrounding Figures and Background:**
> The painting is filled with activity that extends into the background.
> *   **To the left:** A group of soldiers in full plate armor stands near the saint. Behind them, a large army with spears and banners marches up a hill.
> *   **To the right:** Behind the kneeling woman are several female attendants (ladies-in-waiting), also dressed in fine clothing. Further in the background, a caravan with figures riding camels proceeds through the landscape, suggesting a long journey or a setting in a distant land.
> *   **Landscape:** The setting is a vast landscape with rolling hills, dense forests of meticulously rendered trees, and distant mountains. In the middle ground, a military-style encampment with tents is visible.
> *   **Sky:** The sky is filled with clouds. At the very top center, a celestial vision appears: a crowned figure, likely God the Father or Christ, is seated on a throne in the heavens, flanked by angels.
> 
> **Overall Interpretation:**
> The painting depicts a scene from a Christian legend. The combination of a warrior saint, a large retinue of soldiers and women, a journey (indicated by the camels and marching armies), and divine oversight from heaven strongly suggests a specific hagiography (story of a saint). The most likely subject is a scene from the **Legend of Saint Ursula**, a British princess who, according to legend, made a pilgrimage to Rome with 11,000 virgin companions before they were all martyred in Cologne. The numerous figures would represent her vast entourage. The style, with its attention to detail in fabrics and armor, elongated figures, and complex composition, is typical of painters from the German or Netherlandish schools of the 15th century.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:05:19+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history, this painting depicts a scene from the **Legend of Saint Ursula**.
> 
> The specific episode shown is the **meeting of Saint Ursula and her betrothed, Prince Conan** (sometimes called Etherius).
> 
> Here is a breakdown of the figures and elements in the scene:
> 
> *   **Saint Ursula:** She is the richly dressed noblewoman kneeling in the foreground on the right. She is arriving to meet her future husband. Behind her stand some of her 11,000 virgin companions who, according to the legend, accompanied her on a pilgrimage.
> *   **Prince Conan (or Etherius):** He is the figure on the white horse, depicted as a noble knight. Although he was a pagan prince who agreed to convert to Christianity to marry Ursula, he is shown here with a faint halo, foreshadowing his own martyrdom and sainthood alongside her. He leads his army to greet her.
> *   **The Armies:** The vast number of soldiers in the background on both sides of the composition represent the military retinues of both the prince and the princess, emphasizing the importance and scale of this royal meeting.
> *   **Celestial Vision:** In the sky at the top, there is a divine apparition on a cloud, likely God the Father or Christ with angels, bestowing a blessing upon the holy pilgrimage and the union of the couple.
> 
> The style of the painting is characteristic of the **Early Netherlandish school** of the late 15th century, known for its meticulous detail, rich colors (though seen here in black and white), and complex compositions. The artist is known as the **Master of the Saint Ursula Legend**, an anonymous painter active in Bruges, who is named after a famous altarpiece depicting this very story. This painting is one of the panels from that altarpiece.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:05:46+00:00_

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

> Jephtha welcomed by his daughter (Judges 11:29-40)

