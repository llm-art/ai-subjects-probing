# Probe report — `feast-esther`

[![feast-esther](https://iiif.artresearch.net/iiif/3/frick/4107100289960_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100289960_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100289960_0001.jp2/info.json)_

- **Ground-truth subject:** Feast of Esther
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/feast-esther.jpg` — native 5821×3526 px, sent 2048×1241 px
- **SHA-256:** `f13cc355bf221d7034086b05046e248a981557b8fa09ec8d31837190c741a863`
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
>   "artist": "Pietro della Vecchia",
>   "title": "The Feast of Esther",
>   "date": "c. 1645-1650",
>   "collection": "J. Paul Getty Museum"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:48:15+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided and the text visible at the bottom, this is a black and white photograph of a painting titled **"Feast of Esther."**
> 
> The painting depicts a dramatic banquet scene with a group of people gathered around a long table covered with a white tablecloth. The composition is dynamic and filled with emotion.
> 
> **Key elements in the scene include:**
> 
> *   **Central Figures:** At the head of the table sits a woman, presumably Queen Esther. She is dressed in a light-colored gown and looks directly forward with a serious, intense expression. A man to her right (our left) leans across the table towards her, gesturing as if in mid-conversation.
> *   **Other Guests:** The table is surrounded by other figures in various attire. On the right, there are several men, some with beards and wearing elaborate headwear like turbans, observing the central interaction. Other guests are visible in the background.
> *   **Foreground Action:** In the lower-left foreground, a figure with their back partially to the viewer is presenting a large, round platter. On the platter are numerous small, upright items that resemble candles on a cake.
> *   **Atmosphere and Style:** The painting uses strong contrasts between light and shadow (chiaroscuro), which highlights the faces and hands of the main characters and creates a sense of drama and tension. The figures' postures and expressions suggest a pivotal and serious moment is unfolding, consistent with the biblical story where Esther reveals Haman's plot to the king during a feast. The style appears to be from the Baroque period, known for its emotional intensity and dynamic compositions.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:48:32+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge, this is a depiction of a famous biblical scene from the Old Testament.
> 
> **Episode:** The scene is the **Feast of Esther**. Specifically, it captures the dramatic moment at a banquet where Queen Esther reveals the plot of Haman to her husband, King Ahasuerus of Persia.
> 
> **Figures:**
> *   The woman seated at the center of the table is **Queen Esther**. She is the focal point, and her expression is serious as she makes her accusation.
> *   The man in the turban and rich robes on the right is **King Ahasuerus** (also known as Xerxes). He appears to be listening intently, perhaps in shock or contemplation.
> *   The man leaning across the table towards Esther is **Haman**, the king's chief minister. His animated and somewhat aggressive posture suggests he is either being accused or is trying to plead his case.
> 
> The painting captures the tense climax of the story, where Esther risks her life to expose Haman's plan to annihilate the Jewish people, leading to his downfall. The other figures are likely courtiers and attendants present at the royal banquet.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:48:47+00:00_

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

> Feast of Esther

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:49:23+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {"recognized": true, "artist": "Pietro della Vecchia", "title": "Feast of Esther", "date": "ca. 1640", "collection": "J. Paul Getty Museum"}

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:12:31+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the text at the bottom of the image and the visual content, this image depicts:
> 
> * **Artwork Title:** *The Feast of Esther* (or *The Banquet of Esther*)
> * **Artist:** Pietro della Vecchia (Italian, 1602/3–1678)
> * **Location:** J. Paul Getty Museum
> 
> ### Description of the Scene:
> The painting depicts the biblical story from the Book of Esther. Queen Esther is shown seated at the center of a banquet table in a white gown. She is surrounded by guests, including King Ahasuerus (wearing a turban on the right) and Haman. The figures are captured in dramatic, expressive poses typical of the Baroque style, with a servant on the far left leaning in to present a platter of small upright items (possibly candles or sweetmeats) to the table.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:12:36+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the painting and the text visible at the bottom of the image, this is ***The Feast of Esther*** (also known as *The Banquet of Esther and Ahasuerus*) by the Italian Baroque painter **Pietro della Vecchia** (held in the collection of the J. Paul Getty Museum).
> 
> ### **The Episode Depicted**
> The scene depicts the dramatic climax from the biblical **Book of Esther (Chapter 7)**. Queen Esther has invited her husband, King Ahasuerus, and his chief minister, Haman, to a private banquet. During this feast, Esther reveals her Jewish identity and denounces Haman's secret plot to massacre all the Jews in the Persian Empire. 
> 
> ### **Key Figures**
> * **Queen Esther:** The central female figure dressed in a white gown, calmly presenting her case.
> * **King Ahasuerus (Xerxes):** The figure on the far right, distinguished by his royal turban and ermine-trimmed cloak, listening to the accusation.
> * **Haman:** The prime minister, typically depicted in a state of shock, fear, or defensive gesturing as his treachery is exposed to the king. 
> * **Servants and Attendants:** Surrounding the table, including the figure in the foreground on the left carrying a platter.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:12:45+00:00_

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

> Feast of Esther

