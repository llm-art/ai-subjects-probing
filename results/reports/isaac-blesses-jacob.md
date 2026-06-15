# Probe report — `isaac-blesses-jacob`

[![isaac-blesses-jacob](https://media.rkd.nl/iiif/2/10685638/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10685638/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10685638/info.json)_

- **Ground-truth subject:** Isaac blesses Jacob disguised in Esau's clothes; Jacob's hands and neck covered with goatskins
- **Category:** old_testament
- **Institution:** rkd
- **Image:** `data/images/isaac-blesses-jacob.jpg` — native 4888×3906 px, sent 2048×1637 px
- **SHA-256:** `77f831994927497c95ed9136b927de21f51535b259426b16a04ca3550489ae1e`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:46:59+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a well-known painting from the Dutch Golden Age.
> 
> **Artist:** Govert Flinck
> **Title:** *Isaac Blessing Jacob*
> **Approximate Date:** c. 1638
> **Collection:** Rijksmuseum, Amsterdam
> 
> The painting depicts the biblical story from the Book of Genesis. The elderly and blind Isaac is in bed, intending to give his blessing to his firstborn son, Esau. However, he is being deceived by his younger son, Jacob (kneeling), who, at the urging of his mother Rebekah (standing at the head of the bed), has disguised himself as Esau to steal the blessing. The quiver of arrows on Jacob's back is a prop in this deception, as Esau was a skillful hunter.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:47:12+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this painting depicts the biblical story of **Isaac Blessing Jacob**, from the Book of Genesis (Chapter 27).
> 
> Here is a breakdown of the scene and the characters depicted:
> 
> *   **Isaac:** The elderly, white-bearded man lying in bed is the patriarch Isaac. In the biblical account, he is old and blind. He is shown here propped up on pillows, with one hand raised to bestow a blessing and the other touching the arm of his son. His frailness and sightlessness are central to the story's plot.
> 
> *   **Jacob:** The younger man kneeling by the bedside is Jacob. He is deceiving his father to receive the blessing intended for his older twin brother, Esau. He is shown wearing fine robes but also has a quiver of arrows on his back, an attribute of his brother Esau, who was a "skillful hunter." This detail visually represents the deception.
> 
> *   **Rebekah:** The older woman standing behind the bed is Rebekah, Isaac's wife and the mother of the twins. She is the architect of this deception, as she favored Jacob over Esau. Her intense, watchful expression suggests her complicity and anxiety as she ensures her plan succeeds.
> 
> *   **Esau (possibly):** In the deep shadow to the far left, another figure can be seen. This is often interpreted as Esau, the rightful recipient of the blessing, returning from his hunt. His presence in the background, just as the deception is completed, adds a powerful element of dramatic irony and foreshadows the conflict that will erupt when the truth is revealed.
> 
> **The Narrative Moment:**
> 
> The painting captures the climax of the deception. Isaac, unable to see, is tricked by Jacob (with Rebekah's help) into believing he is Esau. He is in the very act of giving Jacob the powerful patriarchal blessing, which, once given, cannot be revoked. The scene is filled with tension, conveyed through the dark, dramatic lighting (chiaroscuro), the rich, heavy fabrics, and the focused, emotional expressions of the characters.
> 
> The artwork is a prime example of Dutch Golden Age painting, likely from the school of Rembrandt, known for its dramatic interpretation of historical and biblical scenes with a deep focus on human psychology and emotion. The artist is **Govert Flinck**, a pupil of Rembrandt, and this work, *Isaac Blessing Jacob* (c. 1638), clearly shows his master's influence.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:47:30+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and my internal knowledge, this is a depiction of a famous biblical scene from the Book of Genesis.
> 
> **Episode:** **Isaac Blessing Jacob** (Genesis 27)
> 
> **Figures:**
> 
> *   **Isaac:** The old, blind man with a long white beard, lying in bed. As the patriarch, he is about to bestow the birthright blessing on his son. His blindness is central to the story's deception.
> *   **Jacob:** The younger man kneeling by the bed. He is impersonating his older twin brother, Esau. The quiver of arrows on his back is part of the disguise, as Esau was a skillful hunter. Jacob is receiving the blessing that was intended for his brother.
> *   **Rebekah:** The older woman standing behind the bed. She is Isaac's wife and the mother of Jacob and Esau. She orchestrated this deception because she favored Jacob. Her tense, watchful expression shows her investment in the success of the ruse.
> *   **Esau:** The figure barely visible in the shadows in the far-left background is most likely Esau, the wronged brother, returning from the hunt only to find he has been tricked out of his blessing. His presence adds a layer of dramatic irony to the scene.
> 
> The painting captures the moment of deception and tension, using dramatic lighting (chiaroscuro) to focus on the central interaction between the blind father and the deceiving son, while the co-conspirator mother looks on. The rich textures of the fabrics, like the ornate bedspread and fur-lined robes, are characteristic of the Dutch Golden Age style of painting.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:47:48+00:00_

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

> Isaac blesses Jacob disguised in Esau's clothes

