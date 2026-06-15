# Probe report — `prodigal-son-brothel`

[![prodigal-son-brothel](https://media.rkd.nl/iiif/2/9159469/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/9159469/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/9159469/info.json)_

- **Ground-truth subject:** The Prodigal Son chased from the brothel after spending all his money (Luke 15:13)
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/prodigal-son-brothel.jpg` — native 3124×2421 px, sent 2048×1587 px
- **SHA-256:** `ec49c3c82d894a8b1279250d3774fb2f69c45a22cfdbe5f1d76c6b5bfe5bf132`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:48:59+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual characteristics of the painting and my internal knowledge, this artwork is:
> 
> **Artist:** Faustino Bocchi
> **Title:** *La Cacciata* (The Expulsion)
> **Approximate Date:** c. 1720-1730
> **Collection:** Pinacoteca Tosio Martinengo, Brescia, Italy
> 
> The painting is a lively genre scene, or *bambocciata*, depicting a chaotic public event. In the center, a man is being accosted and driven away by a mocking crowd, some of whom are brandishing what appear to be brooms or skewers. From a window above, a woman pours water on the scene. To the left, a man in a yellow tunic authoritatively points the way out, while on the right, musicians and other onlookers react to the commotion. Faustino Bocchi, a painter from Brescia, was known for such animated and often humorous scenes, though he is most famous for his paintings featuring dwarves.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:49:21+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a lively and chaotic narrative painting, likely from the 17th or 18th century, depicting a scene of conflict outside a rustic building, probably an inn or tavern.
> 
> **Central Action:**
> The focal point is a brawl or confrontation taking place on the steps of the building. A man in a white shirt and red breeches is being accosted by a group of angry people, both men and women, who appear to be staff or patrons of the establishment. They are grabbing him, shouting, and brandishing implements that look like mops or brooms on long sticks. A small black and white dog is in the middle of the fray, seemingly barking. Adding to the chaos, a woman leans out of an upper-story window and is pouring a pitcher of water down on the group below.
> 
> **Other Figures:**
> *   **On the left:** Two men stand apart from the main group. One, dressed in a yellow tunic and a dark cloak, points authoritatively towards the brawl, as if giving an order or directing the expulsion. The man beside him looks on.
> *   **On the right:** A group of people are reacting to the scene. Two musicians, one carrying a large string instrument like a cello or viola da gamba, seem to be leaving or walking past. A woman with a small child stands in a doorway, looking on with an expression of alarm, her hands held to her head.
> 
> **Setting:**
> The scene is set outdoors in front of a weathered, multi-level building with arches and climbing vines. Hanging from a branch is a woven, spherical object, which traditionally served as a sign for a tavern. In the background, a wider landscape with another building and smaller figures can be seen under a cloudy sky. The foreground features some foliage and what appears to be a fragment of a classical column, suggesting a setting in or near Italian ruins.
> 
> Overall, the painting captures a moment of high drama and commotion, telling a story of a dispute or punishment being carried out publicly. The artist has filled the scene with expressive figures and dynamic action, creating a theatrical and engaging composition.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:49:43+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and common art historical themes, this painting depicts a scene from the New Testament: the **Parable of the Wedding Feast** (or the Parable of the Great Banquet), found in the Gospels of Matthew (22:1-14) and Luke (14:15-24).
> 
> Specifically, the painting illustrates the dramatic climax from Matthew's version of the parable, where a guest who is not wearing a proper wedding garment is discovered and cast out.
> 
> Here is a breakdown of the figures and the scene:
> 
> *   **The Man Being Expelled:** The central figure in the white shirt and red breeches is the guest who came to the feast without a wedding garment. He is being violently seized and driven out by the household staff. His expression is one of shock and protest.
> 
> *   **The Host's Servants:** The group attacking the man are the servants of the king or master who gave the feast. They are depicted as cooks and kitchen staff, identifiable by their aprons. Instead of swords, they wield kitchen implements like skewers with meat still on them as makeshift weapons. A woman in the window above is also participating by pouring water on the scene.
> 
> *   **The Master of the House (or his Steward):** On the far left, the man in the yellow tunic and dark cloak, pointing authoritatively, represents the master of the house (the king in the parable) or his chief steward who has given the order to "Bind him hand and foot, and take him away, and cast him into outer darkness."
> 
> *   **Other Guests and Onlookers:**
>     *   To the right, a group of people are reacting to the violent expulsion. A woman holds her hands to her head in shock, while a small

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:50:03+00:00_

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

