# Probe report — `finding-moses`

[![finding-moses](https://hertz-foto-os1.biblhertz.it/iiif/3/bhex-si-2018-30-074/full/!800,800/0/default.jpg)](https://hertz-foto-os1.biblhertz.it/iiif/3/bhex-si-2018-30-074/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://hertz-foto-os1.biblhertz.it/iiif/3/bhex-si-2018-30-074/info.json)_

- **Ground-truth subject:** The finding of Moses: Pharaoh's daughter comes to bathe with her maidens in the river and discovers the child floating on the water
- **Category:** old_testament
- **Institution:** hertziana
- **Image:** `data/images/finding-moses.jpg` — native 7176×5659 px, sent 2048×1615 px
- **SHA-256:** `2129dfa70d63a10556ccf38ee3f35dd069a7befc03a6ed07c91a51beb150b3c2`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:45:47+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, here is an analysis of the artwork.
> 
> I do not recognize this specific work by a known artist. However, I can identify its subject, style, and likely period.
> 
> **Title:** The subject of the painting is almost certainly **"The Finding of Moses."** This is a well-known story from the Old Testament (Book of Exodus 2:1-10). The key iconographic elements are present:
> *   A royal or noble woman, identifiable by her crown and fine clothing, who represents the Pharaoh's daughter.
> *   A newborn baby being presented to her by her attendants. The baby, Moses, was placed in a basket in the reeds of the Nile to save him from the Pharaoh's decree to kill all newborn Hebrew boys.
> *   A group of female attendants or handmaidens reacting to the discovery.
> *   The setting on what appears to be a riverbank, with a bridge and water visible in the background, representing the Nile River.
> 
> **Artist and Style:** The painting is executed in the **Baroque style**, likely from the **Italian school of the 17th century**. The characteristics supporting this are:
> *   **Dramatic Lighting (Chiaroscuro):** There is a strong contrast between light and shadow, which models the figures and creates a sense of drama.
> *   **Composition:** The figures are arranged in a dynamic, somewhat theatrical grouping. The central figure of the princess creates a focal point, and the other figures guide the viewer's eye around the scene.
> *   **Classical Influences:** The architecture in the background, including round temples, towers, and a prominent column, evokes ancient Rome. This classicizing landscape is typical of artists working in Rome during the Baroque period, such as Nicolas Poussin and his followers, or artists of the Bolognese school like Domenichino. The artist of this work was likely influenced by this classicizing trend within the Italian Baroque.
> 
> **Approximate Date:** Based on the style of painting, the composition, and the clothing, the work was likely created in the **mid-17th century (circa 1640-1670)**.
> 
> **Collection:** The text at the bottom left of the image reads "BIBLIOTHECA HERTZIANA - MAX-PLANCK-INSTITUT FÜR KUNSTGESCHICHTE" along with an inventory number. This indicates that the *photograph* of the artwork is held in the photographic archive of the Bibliotheca Hertziana

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:46:09+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and common art historical themes, this painting depicts the biblical story of **the Finding of Moses**.
> 
> Here is a detailed description of the scene:
> 
> *   **Central Subject:** The narrative comes from the Book of Exodus, where the Pharaoh of Egypt orders all newborn Hebrew boys to be killed. A Hebrew woman places her infant son, Moses, in a basket and sets him adrift on the Nile River to save him. The Pharaoh's daughter comes to the river to bathe and discovers the baby.
> 
> *   **Key Figures:**
>     *   **Pharaoh's Daughter:** The central, standing figure is depicted as a noble or royal woman. She is the focal point, illuminated by a strong light. She wears an elegant white and gold gown with a flowing orange-gold mantle and a crown or diadem on her head, signifying her high status. Her expression is one of calm compassion as she looks down towards the infant.
>     *   **The Infant Moses:** In the lower right, a group of women attend to a newborn baby, who is Moses. He is wrapped in a white cloth and is being presented to or examined by the women.
>     *   **Handmaidens and Attendants:** The Pharaoh's daughter is surrounded by her attendants. The women on the right are clustered around the baby, their expressions showing tenderness and surprise. On the left, a woman kneels in a pose of supplication or reverence, looking up at the royal figure. This kneeling woman could represent Miriam, Moses's sister, who watched from a distance and then offered to find a Hebrew nurse (Moses's own mother) for the child.
> 
> *   **Setting and Atmosphere:**
>     *   The scene is set outdoors, likely on the banks of a river, though the water itself is not clearly visible.
>     *   The background features a dramatic landscape with classical-style architecture, including towers, a round building, and a bridge. This is typical of historical or biblical paintings from the Baroque period, which often used classical ruins to evoke a sense of the ancient past.
>     *   The lighting is dramatic, with a strong contrast between light and shadow (chiaroscuro). The sky is dark and moody, suggesting either dawn or dusk, which adds to the theatricality of the moment of discovery.
> 
> *   **Artistic Style:**
>     The painting is in a style characteristic of the Baroque period, likely from the 17th or 18th century. This is evident in the dynamic composition, the dramatic use of light, the rich but somber color palette, and the emotional expressions of the figures. The surface of the painting shows significant craquelure, indicating its age.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:46:28+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and common subjects in European art history, this painting depicts the biblical episode of **The Finding of Moses**.
> 
> Here is a breakdown of the scene and the figures:
> 
> *   **The Subject:** The scene is from the Old Testament, specifically the Book of Exodus (Chapter 2). To save her infant son from the Pharaoh's decree that all newborn Hebrew boys be killed, Jochebed places him in a basket and sets him afloat on the Nile River. The baby is discovered by the Pharaoh's daughter, who has come to the river to bathe with her attendants.
> 
> *   **The Figures:**
>     *   **Pharaoh's Daughter:** The central, standing figure is the Egyptian princess. Her royal status is indicated by her elegant gown, the golden-orange mantle, and the crown or diadem on her head. She looks down with a compassionate expression.
>     *   **The Infant Moses:** The baby, held by one of the women on the right, is the infant Moses. He has just been taken from the river.
>     *   **Handmaidens/Attendants:** The women surrounding the princess and the baby are her attendants who accompanied her to the river. They show a mixture of curiosity, concern, and tenderness towards the child.
>     *   **Miriam (possibly):** The kneeling woman on the left, looking up pleadingly or gratefully at the princess, could be interpreted as Miriam, Moses's sister, who was watching from a distance to see what would happen to her brother. In the biblical account, she steps forward to offer to find a Hebrew nurse for the baby (who is, in fact, the baby's own mother).
> 
> The setting, with a river and classical-style architecture in the background, is a typical European artistic convention for representing ancient Egypt. The dramatic, dark lighting (chiaroscuro) and the emotional composition are characteristic of the Baroque period.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:46:46+00:00_

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

> The finding of Moses: Pharaoh's daughter discovers the child floating on the river

