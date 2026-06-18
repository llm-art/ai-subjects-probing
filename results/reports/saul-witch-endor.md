# Probe report — `saul-witch-endor`

[![saul-witch-endor](https://iiif.artresearch.net/iiif/3/frick/4107100263571_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100263571_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100263571_0001.jp2/info.json)_

- **Ground-truth subject:** Saul Coming to Consult the Witch of Endor
- **Category:** old_testament
- **Institution:** frick
- **Image:** `data/images/saul-witch-endor.jpg` — native 6487×4609 px, sent 2048×1455 px
- **SHA-256:** `917010527e5bd6bd9e2f24a73dab1e1f49bb380e0fa50de0342caf440bb11244`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T08:04:21+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, I can identify this artwork.
> 
> **Artist:** Jacopo de' Barbari
> 
> **Title:** *Victory and Fame* (also known as *Allegory of Fortune* or *Saul and the Witch of Endor*)
> 
> **Approximate Date:** c. 1500 (The date "1500" is partially visible at the bottom center of the image).
> 
> **Collection:** This is an engraving, so multiple impressions (prints) exist. They are held in the collections of major museums worldwide, including The British Museum in London, the Rijksmuseum in Amsterdam, and the Metropolitan Museum of Art in New York.
> 
> The artwork is a complex allegory. The scene on the left depicts the biblical story of King Saul consulting the Witch of Endor to summon the spirit of the prophet Samuel, as referenced by the Latin text on the banner. The right side of the composition is filled with imagery associated with witchcraft and classical mythology, including witches, satyrs, and figures riding goats, contrasting different forms of prophecy and power.

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:04:42+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image, here is a description of what is depicted:
> 
> This is a complex and dense allegorical or mythological scene, rendered in a monochrome (sepia or black and white) format, likely a print or drawing. The style is reminiscent of Northern Renaissance artists like Hieronymus Bosch, filled with symbolic figures and multiple narratives occurring simultaneously.
> 
> The scene can be broken down into several key areas:
> 
> **Foreground and Center:**
> *   A central, semi-nude female figure is enthroned on a large globe or sphere. She holds a long staff or scepter in her raised left hand. At her feet is a small owl and a lit brazier.
> *   To her right sits another woman, and to her left is a satyr (a figure with human torso and goat legs) with a wreath of leaves in his hair, holding open a book of sheet music.
> *   To the right of this central group is a scene of revelry. Several women are gathered, one drinking from a pitcher, another pouring liquid into a bowl. One woman sits atop a large goat. A man with a leafy crown, possibly Bacchus, is also among them. A small banner held by one woman reads "Sybilla Sambetha," identifying her as the Samian Sibyl.
> 
> **Left Side:**
> *   In the mid-ground, a group of men, some in armor, are gathered under a stone archway. They appear to be interacting with a woman.
> *   Above this group stands a prominent, rough-hewn Christian cross.
> *   In the lower-left corner, a fantastical, demonic creature with a bird-like head and a shield on its back runs towards the central brazier.
> 
> **Background and Sky:**
> *   A large, ruined Roman-style archway dominates the center of the composition. Through the main arch, a chaotic scene of figures in a landscape is visible.
> *   Perched atop the arch is a demonic, dragon-like creature unfurling a long banner with Latin text.
> *   In the upper right sky, several figures are flying. One prominent nude female figure rides a goat-like animal, holding a bow, reminiscent of the goddess Diana or a witch. She is followed by a swarm of what appear to be insects or small demons. Another nude figure is seen falling or flying nearby.
> 
> **Overall Theme and Interpretation:**
> The image presents a powerful allegory, contrasting various belief systems and moral states. Key themes include:
> *   **Paganism vs. Christianity:** The Bacchic revelry, the satyr, the Sibyl, and the flying witches are set against the stark symbol of the Christian cross. The ruined Roman arch may symbolize the decay of the old pagan world.
> *   **Sin and Temptation:** The scene is filled with imagery associated with a Witches' Sabbath or a Bacchanal—drunkenness, chaos, and demonic presences—representing a world given over to worldly pleasures and evil.
> *   **Allegory of Folly or the World:** The central figure on the unstable globe could be an personification of Fortune, Folly, or the vanity of the world, presiding over the chaos around her.
> 
> In summary, the image is a moralizing allegory depicting a world of sin, false belief, and chaos, using a rich vocabulary of symbols from Christian, classical, and folkloric traditions.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:05:06+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image, this is a complex Christian allegory about the choice between salvation and damnation, or virtue and vice. The painting juxtaposes scenes from the life of Christ with scenes of pagan revelry and witchcraft.
> 
> Here is a breakdown of the different elements and their likely meaning:
> 
> **Subject:** The overall subject is a moral allegory, contrasting the path of Christian salvation with the path of worldly sin.
> 
> **Key Episodes and Figures:**
> 
> *   **The Path of Salvation (Left Side):**
>     *   In the background on the left, the **Crucifixion of Christ** is depicted, representing the ultimate sacrifice for humanity's salvation.
>     *   In the left foreground, a group of men, some in armor, are shown. This likely represents **Judas receiving the thirty pieces of silver** for his betrayal of Jesus, the event that set the Passion in motion.
> 
> *   **The Path of Damnation (Right Side):**
>     *   This side is filled with scenes of debauchery and the occult, representing a world given over to sin.
>     *   A woman sits atop a **goat**, a symbol of lust and the devil, while drinking from a pitcher. This is a common motif in depictions of a **Witches' Sabbath** or a bacchanal.
>     *   In the sky, a nude **witch** flies on a broom or creature, holding a platter. Above her, another figure, possibly representing Diana as the leader of the mythical "Wild Hunt," rides a beast through the sky.
>     *   A small sign near the revelers reads **"Sybilla Samia"** (The Samian Sibyl). Sibyls were pagan prophetesses who were later incorporated into Christian tradition as having foretold the coming of Christ. Her presence here among the sinful revelers is ambiguous—she could be a bridge between the pagan and Christian worlds, or simply another element of the pre-Christian world being contrasted with the true faith.
> 
> *   **The Central Allegory:**
>     *   The central figure is a semi-nude woman, an allegorical figure representing **the World, Fortune, or Vanity (Vanitas)**. She sits precariously on a large sphere, symbolizing the instability and transience of worldly existence.
>     *   Next to her, a small **satyr** (a creature associated with the pagan god of wine and revelry, Bacchus) holds open a book of music, symbolizing the seductive but fleeting pleasures of the world.
>     *   An **owl**, often a symbol of folly or darkness in this context, sits near the base of the sphere.
>     *   The entire scene is framed by a large, ruined Roman arch, symbolizing the decay of the old pagan world and the passage of time.
> 
> *   **The Unifying Message (Top Center):**
>     *   A banner unfurls from the cross with a Latin inscription. The visible text begins: **"Saul Saul quid me persequeris..."** This is a direct quote from the Bible (Acts 9:4), meaning **"Saul, Saul, why do you persecute me?"** These are the words Christ speaks to Saul (the future St. Paul) on the road to Damascus, leading to his conversion.
>     *   In the context of this painting, this quote serves as the central message. It is a direct address to the viewer, asking why they would "persecute" Christ by choosing the path of sin and worldly pleasure (depicted on the right) when the path to salvation through his sacrifice (depicted on the left) is available. It transforms the painting into a powerful call for conversion and moral choice.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:05:32+00:00_

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

