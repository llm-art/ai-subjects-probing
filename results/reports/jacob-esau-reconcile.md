# Probe report — `jacob-esau-reconcile`

[![jacob-esau-reconcile](https://iiif.artresearch.net/iiif/3/frick/4107100298515_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100298515_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100298515_0001.jp2/info.json)_

- **Ground-truth subject:** Reconciliation of Jacob and Esau
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/jacob-esau-reconcile.jpg` — native 6229×4641 px, sent 2048×1526 px
- **SHA-256:** `950d011dfa9e3ae55720c225c61c2dc4843d1cacd289be6ef712432b035a0c4d`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:08:27+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a photograph of a famous Baroque painting.
> 
> **Artist:** Pietro da Cortona
> 
> **Title:** *The Rape of the Sabine Women* (Il Ratto delle Sabine). It is important to note that while this is the common title, the painting actually depicts a later event in the story: the *Intervention of the Sabine Women*, where the women, now wives and mothers, rush between the battle lines of their Roman husbands and their Sabine fathers and brothers to force a reconciliation.
> 
> **Approximate Date:** c. 1629–1631
> 
> **Collection:** Pinacoteca Capitolina (Capitoline Museums), Rome, Italy.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:08:48+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this black and white photograph depicts a painting of a famous historical and mythological subject: **The Rape of the Sabine Women**.
> 
> Here is a breakdown of what is depicted:
> 
> *   **The Subject:** The scene illustrates the legendary incident from early Roman history where the men of Rome, under their founder Romulus, committed a mass abduction of young women from the neighboring Sabine people. The Romans, lacking wives to establish families and ensure the future of their city, invited the Sabines to a festival and then, at a signal, seized their unmarried women.
> 
> *   **Composition and Figures:** The painting is a dynamic and chaotic composition, characteristic of the Baroque style often used for this subject.
>     *   On the right, we see muscular Roman soldiers, identifiable by their helmets, armor (cuirasses and greaves), and determined actions as they seize the women.
>     *   On the left and in the center, the Sabine women and children are shown in various states of distress, fear, and resistance. They are pleading, trying to escape, or being forcefully carried away. The figures are arranged in dramatic, twisting poses to convey the turmoil of the moment.
>     *   In the background, there are hints of a larger crowd and animals, possibly camels or horses, suggesting the context of a large gathering or journey.
> 
> *   **Artistic Style:** The dramatic use of light and shadow (chiaroscuro), the emotional intensity of the figures' expressions and gestures, and the complex, swirling composition are all hallmarks of the **Baroque period** of art. Artists like Peter Paul Rubens and Nicolas Poussin famously depicted this scene, and this work is very much in that tradition.
> 
> In summary, the image shows a photograph of a dramatic, multi-figure history painting illustrating the mythological abduction of the Sabine women by Roman soldiers.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:09:11+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge of art history, this painting depicts a famous episode from early Roman history: **The Women of Rome Pleading with Coriolanus**.
> 
> Here is a breakdown of the scene and the figures:
> 
> *   **The Episode:** The story, told by historians like Plutarch and Livy, concerns the Roman general Gaius Marcius Coriolanus. After being exiled from Rome, he allies himself with Rome's enemies, the Volsci, and leads their army to the very gates of the city, intending to sack it. All attempts by Roman senators to dissuade him fail. As a last resort, a delegation of Rome's most noble women, including his own family, comes to his camp to plead for him to spare the city.
> 
> *   **The Figures:**
>     *   **Coriolanus:** He is the central figure on the right, dressed in Roman-style military armor (cuirass and helmet). He is shown in a moment of emotional turmoil, turning away from the women but being embraced or held by another man, seemingly overcome by their pleas.
>     *   **Veturia (his mother) and Volumnia (his wife):** The delegation is led by these two women. While it's difficult to distinguish them individually in this monochrome reproduction, they are among the prominent, pleading women in the foreground and center-left. One of them is likely the figure kneeling at his feet. They brought his children with them to heighten the emotional appeal.
>     *   **The Children of Coriolanus:** Several small children are visible among the women, looking up at the soldiers.
>     *   **The Roman Women:** The crowd of women and children on the left represents the delegation of Roman matrons who accompanied Coriolanus's family.
>     *   **The Volscian Soldiers:** The other men in armor or military attire are Coriolanus's Volscian allies, who look on as their commander's resolve is broken by his family.
> 
> The painting captures the dramatic climax of the story: Coriolanus, faced with the choice of destroying his homeland or betraying his new allies, ultimately relents to his mother's appeal, famously crying out, "O mother, what have you done to me? You have saved Rome, but you have destroyed your son." This subject was popular in European art, especially from the 17th to the 19th centuries, as it exemplified themes of patriotism, filial piety, and the conflict between personal honor and civic duty.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:09:33+00:00_

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

