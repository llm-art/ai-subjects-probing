# Probe report — `belshazzar-feast`

[![belshazzar-feast](https://media.rkd.nl/iiif/2/9231863/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9231863/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9231863/info.json)_

- **Ground-truth subject:** Belshazzar's Feast (Daniel 5:5-7)
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/belshazzar-feast.jpg` — native 2154×1474 px, sent 2048×1401 px
- **SHA-256:** `b31a49b881fdb7c3dcbf27ee227c09f97cffeed0df6717826bc230fac03abbf6`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:12+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Frans van der Keulen",
>   "title": "Belshazzar's Feast",
>   "date": "1701",
>   "collection": null
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-12T09:32:25+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general art historical knowledge, this painting depicts the biblical story of **Belshazzar's Feast**.
> 
> Here are the key elements from the image that identify the scene:
> 
> *   **The Writing on the Wall:** In the upper part of the painting, a disembodied hand is seen writing glowing words on the wall. The visible words are "MENE THETEL PHANES," a variation of "Mene, Mene, Tekel, Upharsin" from the Book of Daniel. This is the central, miraculous event of the story.
> *   **The Feast:** The setting is a lavish banquet in a grand, dark hall. Numerous guests are seated around a long table, dressed in opulent and exotic attire, including turbans and rich robes. They are eating and drinking from golden vessels.
> *   **The King:** A central figure, likely King Belshazzar of Babylon, is seated at the head of the table. He and the guests around him are shown reacting with shock and confusion to the supernatural writing.
> *   **The Sacred Vessels:** The story specifies that Belshazzar and his court profaned the sacred golden and silver vessels taken from the Temple in Jerusalem. The painting is filled with ornate golden goblets, ewers, and dishes, consistent with this part of the narrative.
> *   **Dramatic Lighting:** The scene is painted in a style typical of the Baroque period, using dramatic chiaroscuro (strong contrasts between light and dark). The main sources of light are the candles on the table, an elaborate chandelier, and the divine light from the writing itself, which highlights the main figures and the supernatural event.
> 
> In summary, the painting captures the dramatic moment from the Old Testament (Daniel 5) when God delivers a judgment upon King Belshazzar for his arrogance and sacrilege, foretelling the imminent fall of his kingdom. The signature and date in the lower right corner appear to read "F.C. Keulen 1701."

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-12T09:32:43+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting, particularly the glowing words on the wall, this scene depicts the biblical episode of **Belshazzar's Feast**.
> 
> This story comes from the Book of Daniel in the Old Testament. The key figures and elements are:
> 
> *   **King Belshazzar:** The main figure, likely the man in the ornate turban and cape seated at the head of the table under the large golden canopy. He was the last king of Babylon.
> *   **The Feast:** Belshazzar is shown hosting a grand banquet for his lords, wives, and concubines. They are using sacred golden and silver vessels that his father, Nebuchadnezzar, had looted from the Temple in Jerusalem.
> *   **The Writing on the Wall:** The most crucial element is visible in the background, above the archway. The glowing words "**MENE THEKEL PHARES**" (a variation of "Mene, Mene, Tekel, Upharsin") have miraculously appeared on the wall. According to the biblical account, a disembodied hand wrote this message, which none of the king's wise men could interpret. The prophet Daniel was summoned and explained it as a judgment from God, foretelling the imminent fall of Belshazzar and his kingdom.
> 
> The painting captures the dramatic moment during the feast when the divine message appears, causing alarm and confusion among the revelers.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-12T09:32:59+00:00_

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

> Belshazzar's Feast

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:49:24+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "F. C. Keilles",
>   "title": "Belshazzar's Feast",
>   "date": "1701",
>   "collection": null
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:13:32+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This painting depicts the biblical story of **Belshazzar's Feast** (from the Book of Daniel). 
> 
> Key elements visible in the image include:
> 
> * **The Writing on the Wall:** In the upper center-right, a disembodied hand emerges from the darkness to write the words **"MANE THETEL PHARES"** (a version of the Aramaic phrase *Mene, Mene, Tekel, Upharsin*) on the wall, foretelling the fall of Babylon.
> * **The Banquet:** King Belshazzar and his royal guests are shown feasting at a long table. They are using the sacred golden vessels plundered from the Temple of Jerusalem, which are displayed on the table and being brought in by servants.
> * **The Atmosphere:** The scene is filled with figures in exotic, orientalist costumes, turbans, and crowns. The room is dramatically lit by candles, including a unique chandelier featuring sculpted figures holding lights.
> * **Artist Signature:** In the bottom right corner, the painting is signed and dated **"F. C. Keicher 1701"**.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:13:40+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts the biblical scene of **Belshazzar's Feast** (from the Book of Daniel, Chapter 5). 
> 
> ### **The Episode Depicted**
> The scene shows the Babylonian King Belshazzar hosting a lavish banquet for his nobles, wives, and concubines. During the feast, they impiously drink wine from the sacred golden and silver vessels looted from the Temple of Jerusalem. 
> 
> In the midst of the revelry, a disembodied hand appears and writes a mysterious message on the palace wall. In the background of this painting, the Latinized version of the divine warning is clearly visible: **"MANE THETEL PHARES"** (traditionally *Mene, Mene, Tekel, Upharsin*), which the prophet Daniel later interprets as a prophecy of Belshazzar's imminent downfall and the division of his kingdom.
> 
> ### **Key Figures and Details**
> * **King Belshazzar:** Seated on the left under the grand canopy, wearing a crown and looking back in terror and shock toward the writing on the wall.
> * **The Mysterious Hand:** Visible near the top right, pointing toward the glowing inscription on the wall.
> * **The Guests and Courtiers:** Seated along the banquet table, reacting with confusion and concern.
> * **The Sacred Vessels:** Elaborate golden chalices, plates, and pitchers are displayed on the table and carried by servants on the right, representing the plundered treasures of Jerusalem.
> * **Artist Signature:** In the bottom right corner, the painting is signed and dated **"F. C. Keicher, 1701"** (by the German Baroque painter Franz Carl Keicher).

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:13:47+00:00_

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

> Belshazzar's Feast

