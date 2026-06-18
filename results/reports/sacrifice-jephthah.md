# Probe report — `sacrifice-jephthah`

[![sacrifice-jephthah](https://iiif.artresearch.net/iiif/3/frick/4107100290801_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100290801_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100290801_0001.jp2/info.json)_

- **Ground-truth subject:** Sacrifice of Jephthah
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/sacrifice-jephthah.jpg` — native 5674×4508 px, sent 2048×1627 px
- **SHA-256:** `fc8956c40f7884dd48379250b9f4b8d9744c870fc048170cc3f2529f4ce1b624`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:47:25+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Peter Paul Rubens",
>   "title": "The Massacre of the Innocents",
>   "date": "c. 1636-1638",
>   "collection": "Alte Pinakothek, Munich"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:08:03+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this is a black and white reproduction of a painting depicting a dramatic and violent historical or biblical scene. The subject is most likely the **Massacre of the Innocents**.
> 
> Here is a detailed description of what is depicted:
> 
> *   **Setting:** The scene takes place within a grand, classical architectural setting, possibly a temple or palace. Massive, fluted columns with ornate capitals and large arches dominate the background, creating a sense of monumental scale that contrasts with the human chaos in the foreground.
> 
> *   **Central Action:** The composition is filled with numerous figures in a state of turmoil. The scene is one of violence, panic, and despair.
>     *   On the **right**, a powerful, muscular figure with his back mostly to the viewer stands on a raised platform, pointing authoritatively. He appears to be a soldier or a commander directing the violence.
>     *   In the **center**, a man is recoiling dramatically from a large, ornate urn or font, as if struck or in shock. Another figure behind him seems to be part of this struggle. A priest-like figure with a beard and a distinctive hat stands behind the urn, looking on.
>     *   On the **left**, there is a dense and chaotic group of figures, primarily women and children. They are shown in various states of distress: a woman is being pulled by her hair, others are screaming or trying to protect their infants from unseen assailants.
> 
> *   **Themes and Mood:** The overall mood is one of terror and brutality. The artist uses dramatic lighting (chiaroscuro) with strong contrasts between light and shadow to heighten the emotional intensity and chaos of the moment. The figures' bodies are contorted in dynamic, expressive poses, characteristic of the Baroque style of painting, which aimed to evoke strong emotions in the viewer. The scene captures the helplessness of the victims against an organized, brutal force.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:08:23+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history and biblical narratives, this is a depiction of the **Massacre of the Innocents**.
> 
> Here is a breakdown of the scene and its figures:
> 
> *   **The Episode:** This is a dramatic and violent scene from the New Testament (Gospel of Matthew 2:16-18). After being tricked by the Magi, King Herod the Great, in a fit of paranoid rage, orders the execution of all male children two years old and under in the vicinity of Bethlehem to eliminate the newborn "King of the Jews."
> 
> *   **The Setting:** The event takes place within a grand, classical temple or palace, characterized by the massive columns, arches, and a large ceremonial font or altar in the center. This grand setting contrasts with the brutal and chaotic human drama unfolding.
> 
> *   **Key Figures and Actions:**
>     *   **The Soldier/Executioner:** On the right, a large, muscular man with his back mostly to the viewer points authoritatively. He is clearly a soldier or captain directing the slaughter, a figure of brutal authority.
>     *   **The Mothers and Children:** The scene is filled with terrified mothers desperately trying to protect their infants. On the left, women are screaming and cowering. In the foreground, children are seen on the ground, either already killed or in peril.
>     *   **The Central Group:** The focus of the composition is a dramatic struggle around the central font. A man, possibly a priest or a father, is in a state of extreme distress, being restrained or attacked. In his struggle, he is knocking over a censer (an incense burner), which is swinging wildly. Behind the font stands a figure who appears to be a high priest, identifiable by his headdress. This specific focus might allude to an apocryphal story associated with the massacre: the murder of Zacharias (the father of John the Baptist) in the temple when he refused to reveal his son's whereabouts to Herod's soldiers.
> 
> *   **Artistic Style:** The painting is executed in the **Baroque** style. This is evident in the dramatic use of light and shadow (chiaroscuro), the dynamic and swirling composition, the heightened emotional intensity, and the powerful, muscular figures, all of which are characteristic of artists like Peter Paul Rubens, to whom this style of composition is often attributed.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:08:48+00:00_

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

> Samson breaks the pillars; the temple of Dagon collapses

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:52:00+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Jean-Honoré Fragonard",
>   "title": "Coresus Sacrificing Himself to Save Callirhoe",
>   "date": "1765",
>   "collection": "Musée du Louvre"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:21:15+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual details, this image depicts a dramatic biblical scene, most likely **The Sacrifice at Lystra** (from the Acts of the Apostles, Chapter 14), depicting the Apostles Paul and Barnabas protesting against being worshipped as pagan gods. 
> 
> ### Key Elements Depicted:
> * **The Central Action:** A bearded man (likely St. Paul) stands near the center, dramatically tearing open his tunic at his chest—a traditional biblical gesture of grief and protest against blasphemy.
> * **The Pagan Temple Setting:** The scene is set inside a grand, classical temple featuring massive columns, arches, and stone steps. 
> * **The Ritual:** Next to the central figure is a circular altar or font, with a priest wearing a ceremonial headdress standing behind it. To the left, a figure swings a smoking censer (thurible) on chains.
> * **The Pagan Idol:** Visible through the large central archway in the background is a classical statue of a deity standing atop a tall column.
> * **The Agitated Crowd:** A large group of onlookers reacts with intense emotion. On the left, figures are swooning and falling in shock, while on the right, a prominent figure seen from behind points dramatically toward the central event. 
> 
> The composition is rendered in a highly dynamic **Baroque style**, characterized by theatrical gestures, complex grouping, and strong contrast between light and shadow (chiaroscuro).

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:21:34+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the iconography and details in the painting, this scene depicts the biblical episode of **The Sacrifice at Lystra** (also known as **St. Paul and St. Barnabas at Lystra**), from the New Testament (*Acts of the Apostles*, Chapter 14).
> 
> ### **The Episode and Figures Depicted:**
> * **Saint Paul:** The central figure who is dramatically tearing open his garments at the chest. After healing a lame man, the citizens of Lystra mistook Paul and Barnabas for the gods Mercury (Hermes) and Jupiter (Zeus) and attempted to offer sacrifices to them. In protest of this blasphemy, Paul tore his clothes to show he was merely a mortal man.
> * **Saint Barnabas:** Depicted alongside Paul, attempting to restrain the crowd and stop the pagan ritual.
> * **The Pagan Priest of Jupiter:** The figure wearing a ceremonial headdress standing behind the circular sacrificial altar in the center.
> * **The Healed Lame Man:** His discarded wooden crutch is visible lying on the floor in the bottom right corner, symbolizing the miracle that triggered the crowd's reaction.
> * **The Statue of Jupiter:** Visible in the background through the central arch, standing atop a high column outside the temple. 
> * **The Crowd of Lystrans:** Bringing vessels, incense, and preparing to perform a sacrifice in astonishment of the miracle.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:21:47+00:00_

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

> The Prodigal Son chased from the brothel (Luke 15:13)

