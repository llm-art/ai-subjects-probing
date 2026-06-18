# Probe report — `judgement-solomon`

[![judgement-solomon](https://iiif.artresearch.net/iiif/3/frick/4107100304439_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100304439_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100304439_0001.jp2/info.json)_

- **Ground-truth subject:** Judgement of Solomon
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/judgement-solomon.jpg` — native 6050×4602 px, sent 2048×1558 px
- **SHA-256:** `f933444778ca5fdf152c545e6a70ba6a8928083b675d69a06df7cd7257b8aec1`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:07:55+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the style and subject matter visible in the image, this is a photograph of the painting:
> 
> *   **Artist:** Valentin de Boulogne
> *   **Title:** *The Judgment of Solomon*
> *   **Date:** c. 1625
> *   **Collection:** Musée du Louvre, Paris
> 
> The painting is a prime example of the Caravaggesque style, characterized by its dramatic use of light and shadow (tenebrism) and its intense, naturalistic depiction of figures. The scene illustrates the biblical story from the First Book of Kings, where King Solomon wisely identifies the true mother of a baby by threatening to split the child in two. The real mother, seen kneeling in distress, reveals herself by her willingness to give up the child to save its life.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:08:12+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general knowledge of art history and biblical narratives, this black and white photograph shows a painting depicting the **Judgment of Solomon**.
> 
> This is a famous story from the Old Testament (1 Kings 3:16–28). The scene captures the dramatic climax of the tale:
> 
> *   **King Solomon**, the figure seated on a throne-like structure to the left, is portrayed as a wise judge. He points authoritatively, delivering his verdict. A figure, likely the false mother, leans over his shoulder, gesturing towards the center.
> *   In the center, a woman, the **true mother**, is kneeling on the floor in anguish. Her expression is one of desperate pleading as she looks up towards the king. Near her on the floor lies her own deceased infant, or perhaps the living infant she is trying to protect.
> *   To the right, a muscular man, acting as an **executioner or guard**, is shown holding the living infant upside down by one leg, seemingly ready to carry out Solomon's order to cut the child in two.
> *   The story goes that two women came before King Solomon, both claiming to be the mother of a single living baby. To reveal the truth, Solomon ordered the baby to be split in half, with each woman receiving a part. The true mother, horrified, begged the king to spare the child and give it to the other woman. The false mother agreed to the division. Solomon then knew who the real mother was and gave the child to her.
> 
> The painting's style is characteristic of the **Baroque period**, with its dramatic use of light and shadow (chiaroscuro/tenebrism) to heighten the emotional intensity of the scene. The composition is theatrical, focusing the viewer's attention on the key figures and their powerful emotions: Solomon's authority, the mother's desperation, and the grim reality of the impending act.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:08:33+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts the biblical episode known as **The Judgment of Solomon**.
> 
> This story comes from the Old Testament (1 Kings 3:16-28). Two women came before King Solomon, both claiming to be the mother of a living infant. The other woman's baby had died in the night. To determine the true mother, Solomon called for a sword and declared that the living child should be cut in two, so each woman could have a half. The true mother, in her love for the child, cried out for the king to spare the baby and give it to the other woman. The false mother agreed to the division. Solomon, recognizing the true mother's compassion, awarded the baby to her.
> 
> The figures in the painting can be identified as:
> 
> *   **King Solomon:** The figure seated on the throne-like structure to the left, wearing a turban or crown. He is pointing, delivering his seemingly cruel but wise judgment.
> *   **The True Mother:** The woman kneeling in the center, her face filled with anguish as she pleads for her child's life.
> *   **The Living Infant:** The baby being held up by a man on the right, about to be subjected to the king's order.
> *   **The Executioner/Soldier:** The man in the center, bent over, preparing to draw his sword (implied) to carry out the king's command.
> *   **The Second Infant:** There is another baby on the floor near the kneeling mother. This likely represents the deceased infant from the story, which is the cause of the dispute.
> *   **Courtiers/Onlookers:** The figures standing on the right are members of Solomon's court, observing the dramatic scene unfold.
> 
> The painting's dramatic use of light and shadow (chiaroscuro), intense emotion, and realistic depiction of the figures are characteristic of the Baroque period, particularly the style of Caravaggio and his followers (the Caravaggisti).

