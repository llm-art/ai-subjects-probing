# Probe report — `balaam-ass`

[![balaam-ass](https://media.rkd.nl/iiif/2/10418101/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10418101/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10418101/info.json)_

- **Ground-truth subject:** Balaam strikes his ass; the ass lies down and starts to speak
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/balaam-ass.jpg` — native 2743×3735 px, sent 1504×2048 px
- **SHA-256:** `0a2f4ff75cb307f43dd4b27722602cf406bef93348f3eb5de32bfbd7fd8e36fb`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:46:57+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a well-known painting.
> 
> **Artist:** Rembrandt van Rijn
> **Title:** *Balaam and the Ass*
> **Date:** c. 1626
> **Collection:** Musée Cognacq-Jay, Paris, France
> 
> The painting depicts the biblical story from the Book of Numbers (22:21-39). The prophet Balaam is on his way to curse the Israelites as requested by the Moabite king Balak. God sends an angel with a drawn sword to block his path. While Balaam cannot see the angel, his donkey can and refuses to move forward. The painting captures the dramatic moment when the enraged Balaam raises his staff to strike the donkey for the third time, just as the angel appears, visible to the viewer but not yet to Balaam. This work is a prime example of Rembrandt's early style, characterized by its dramatic composition, rich colors, and intense emotional expression.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:47:13+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of Western art and biblical narratives, this painting depicts the story of **Balaam and the Angel** from the Book of Numbers in the Old Testament.
> 
> Here is a breakdown of the scene:
> 
> *   **Balaam:** The central figure is the prophet Balaam, an elderly man with a white beard and a turban. He is shown in a moment of rage, raising a staff to strike his donkey. He is on a journey to curse the Israelites at the behest of the Moabite king, Balak, against God's will.
> *   **The Donkey:** Balaam's donkey has stopped abruptly and is cowering or kneeling on the path. Its mouth is open as if in distress. According to the biblical story, the donkey can see a divine being that is invisible to its master.
> *   **The Angel:** To the left, emerging from the clouds, is an angel of the Lord. The angel has large wings, is draped in white cloth, and brandishes a sword, blocking the path. This is the divine presence that the donkey sees and Balaam does not. The angel is there to prevent Balaam from proceeding.
> *   **The Narrative Moment:** The painting captures the dramatic climax of the story. The donkey has refused to move forward three times to avoid the angel, and each time the enraged and unseeing Balaam has beaten it. This is the moment just before God opens the donkey's mouth to speak to Balaam, and then opens Balaam's own eyes to see the angel and understand his folly.
> *   **Other Figures:** In the background, other members of Balaam's party, including what appear to be Moabite princes or servants, look on, also seemingly unaware of the angel's presence.
> 
> In essence, the painting illustrates a moment of divine intervention, highlighting themes of obedience, spiritual blindness, and the idea that even a humble animal can possess greater perception than a wayward prophet. The dramatic composition, with its dynamic figures and strong lighting, is characteristic of the Baroque style often used for such religious subjects.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:47:32+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge of art history and biblical narratives, this painting depicts the Old Testament story of **Balaam and the Angel**.
> 
> The episode is from the Book of Numbers, Chapter 22. Here is a breakdown of the figures and the scene:
> 
> *   **Balaam:** The central figure is the prophet Balaam. He is depicted as an old man with a white beard, wearing a turban and rich, fur-lined robes. He is enraged, raising a staff or stick to strike his donkey. His anger stems from the donkey repeatedly stopping on their journey.
> 
> *   **Balaam's Donkey:** The donkey has stopped abruptly and is cowering because it can see a divine being that its master, Balaam, cannot. Its mouth is open, which in the biblical story is the moment God allows it to speak and question Balaam's cruelty.
> 
> *   **The Angel of the Lord:** Appearing from the clouds on the left is a winged angel, brandishing a sword. The angel has been sent by God to block Balaam's path because God is displeased with his journey to the land of Moab, where he has been summoned by King Balak to curse the Israelites.
> 
> *   **Balaam's Attendants:** In the background, there are other figures on foot and on horseback. These are the princes of Moab or Balaam's servants who were accompanying him on his journey. They appear unaware of the divine confrontation happening in the foreground.
> 
> The painting captures the dramatic climax of the story: the moment of supernatural intervention where the humble animal sees the divine truth before the supposedly wise prophet, highlighting themes of spiritual blindness and divine will. The style is characteristic of the Dutch Golden Age, likely from the circle of Rembrandt, known for its dramatic use of light and shadow (chiaroscuro) and emotional intensity.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:47:50+00:00_

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

> Balaam strikes his ass; the ass lies down and starts to speak

