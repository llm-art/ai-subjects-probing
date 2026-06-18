# Probe report — `jeremiah-baruch`

[![jeremiah-baruch](https://iiif.artresearch.net/iiif/3/frick/3107100095324_001.tif/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/3107100095324_001.tif/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/3107100095324_001.tif/info.json)_

- **Ground-truth subject:** Jeremiah Dictating His Prophecy of the Destruction of Jerusalem to Baruch the Scribe
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/jeremiah-baruch.jpg` — native 4940×5838 px, sent 1733×2048 px
- **SHA-256:** `4ab4e48e4df2f7015c839bbde36f2aca4e4668199e4ac7efc8225a71b4c212c7`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:05:49+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a photograph of the painting:
> 
> *   **Artist:** Washington Allston
> *   **Title:** *Jeremiah Dictating His Prophecy of the Destruction of Jerusalem to Baruch the Scribe*
> *   **Approximate Date:** 1820
> *   **Collection:** Yale University Art Gallery
> 
> The painting depicts the biblical scene from the Book of Jeremiah, where the prophet Jeremiah, imprisoned, dictates his prophecies to his faithful scribe, Baruch. The work is a prime example of American Romanticism, combining a grand, historical subject in the Neoclassical tradition with dramatic lighting (chiaroscuro) and emotional intensity that are characteristic of the Romantic movement. The monumental, muscular figure of Jeremiah and the somber, architectural setting contribute to the painting's powerful and solemn mood.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:06:46+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the image provided, here is a description of what is depicted:
> 
> This is a black and white photograph of a painting, rendered in a classical or neoclassical style. The scene is dramatic and contemplative, featuring two figures in an architectural setting.
> 
> **The Main Figure:**
> A large, muscular man with a full, dark beard and curly hair is the central focus. He is seated in an elevated, throne-like chair, conveying a sense of authority and intellectual power. He is dressed in classical-style robes: a tunic-like garment held by straps over his shoulders and cinched below the chest, with a heavier cloak draped over him. He is barefoot. His expression is intense and pensive as he gazes off to the side, with his right hand raised to his face in a thoughtful gesture.
> 
> **The Second Figure:**
> Seated on a lower level at the man's feet is a younger person, possibly a woman or a youth, with short, dark hair. This figure is shown in profile, looking up attentively at the man. They are holding what appears to be a stylus or a small brush in one hand and a tablet or board in the other, suggesting they are either drawing the man's portrait or taking dictation as a scribe. Their clothing is simpler and darker than the main figure's, and they are also barefoot.
> 
> **The Setting and Atmosphere:**
> The setting appears to be an interior space made of stone. In the background, a series of receding, illuminated arches creates a sense of depth and grandeur. The lighting is dramatic, employing strong contrast between light and shadow (chiaroscuro), with a light source coming from the left that highlights the figures and models their forms. To the lower left, a large ceramic urn or pot rests on the floor.
> 
> Overall, the image portrays a scene of mentorship, creation, or the transmission of knowledge, such as a philosopher with a student, a poet dictating to a scribe, or an artist and their model. The mood is serious, focused, and timeless.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:07:06+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history, this painting depicts a famous episode from classical antiquity: **The Origin of Painting**.
> 
> The figures depicted are:
> 
> 1.  **Kora of Sicyon** (also known as Callirhoe, or simply as the "Corinthian Maid" or Dibutades), the woman seated on the right.
> 2.  Her **lover**, the man seated on the left, who is about to depart on a journey.
> 
> **The Episode:**
> 
> The story, most famously recounted by the Roman author Pliny the Elder in his *Natural History*, is a foundational myth about the invention of art, specifically portraiture. According to the legend, Kora, the daughter of the potter Butades, was so saddened by her lover's impending departure that she traced the outline of his shadow, cast by a lamp upon a wall, to preserve his image. Her father then filled the outline with clay, creating the first relief sculpture.
> 
> This painting captures the essence of that moment of artistic creation born from love and the desire to capture a likeness. While the original legend specifies tracing a shadow, many artists, particularly in the Neoclassical period, interpreted the scene more broadly as the first act of portraiture. Here, we see Kora not tracing a shadow, but drawing her lover directly onto a tablet with a stylus, intently studying his form.
> 
> The visual elements supporting this identification include:
> 
> *   **Classical Attire and Setting:** The figures wear simple, toga-like garments, and both are barefoot. The background features classical arches, and a simple earthenware pot sits on the floor, all evoking an ancient Greek or Roman setting.
> *   **The Act of Creation:** The woman is clearly an artist at work, holding a drawing tool and a surface, her gaze fixed on her subject.
> *   **The Subject/Model:** The man sits in a pensive, static pose, befitting a model. His thoughtful expression and the gesture of his hand to his head suggest a quiet, contemplative moment before his departure.
> *   **Composition:** The scene is intimate and focused, emphasizing the connection between the artist and her subject, which is the emotional core of the legend.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:07:31+00:00_

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

