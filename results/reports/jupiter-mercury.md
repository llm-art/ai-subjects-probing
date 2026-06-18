# Probe report — `jupiter-mercury`

[![jupiter-mercury](https://iiif.artresearch.net/iiif/3/frick/4107100314981_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100314981_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100314981_0001.jp2/info.json)_

- **Ground-truth subject:** Jupiter and Mercury
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/jupiter-mercury.jpg` — native 3419×2621 px, sent 2048×1570 px
- **SHA-256:** `b51229cae5aa7b075bf3cb93a2e11488b13b0db32bfcc43bee35f9ef70f57f42`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-18T07:59:04+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this is a well-known painting from the Italian Renaissance.
> 
> **Artist:** Dosso Dossi (Giovanni di Niccolò de Luteri)
> 
> **Title:** *Jupiter, Mercury and Virtue* (also known as *Allegory of Virtue*)
> 
> **Approximate Date:** c. 1524
> 
> **Collection:** Kunsthistorisches Museum, Vienna, Austria
> 
> The painting is an allegory. The figure on the left, painting butterflies, is Jupiter, the king of the gods. The central figure with the winged hat (petasus) and winged sandals (talaria) is Mercury, the messenger god, who makes a gesture for silence. The woman on the right, adorned with flowers, is the personification of Virtue, who appears to be complaining to Mercury that she is being ignored by Jupiter, who is busy with trivial pursuits (the ephemeral butterflies).

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T07:59:20+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual information in the image and my internal knowledge, this is a depiction of a complex allegorical painting from the Italian Renaissance.
> 
> The scene features three main figures set in a mythical landscape with a rainbow in the sky.
> 
> 1.  **The Central Figure:** This is the Roman god **Mercury** (the Greek Hermes). He is identifiable by his iconic attributes: the winged hat (petasus), the winged sandals (talaria), and the staff he holds, which is a caduceus (though the snakes are not clearly visible, the form is correct). He is depicted as a youthful, athletic nude, looking directly at the viewer with his finger to his lips in a "shushing" gesture, demanding silence.
> 
> 2.  **The Figure on the Left:** This is a bearded, older man robed in red, who is depicted as an artist. He is seated before a canvas on an easel, holding a palette and a paintbrush. He is in the act of painting three butterflies that appear to be fluttering near his canvas. In some interpretations of this specific painting, this figure is identified as **Jupiter**, the king of the gods, engaging in the delicate act of creation, thus elevating the status of painting to a divine pursuit.
> 
> 3.  **The Figure on the Right:** This is a woman dressed in rich, golden-hued robes. She wears a crown of flowers and has floral garlands on her arms. She is leaning towards Mercury with a pleading or concerned expression, her hand to her chest. She is an allegorical figure, often identified as **Virtue**.
> 
> **Overall Scene and Interpretation:**
> 
> The painting is an allegory, a story with a hidden moral or political meaning. The exact interpretation is a subject of art historical debate, but it generally revolves around the relationship between divine power, art, eloquence, and virtue.
> 
> Virtue appears to be pleading with Mercury, who is the god of eloquence and a messenger. However, Mercury silences her (and the viewer), perhaps indicating that her pleas are futile or that words are useless in this context. Meanwhile, the most powerful god, Jupiter, is completely absorbed in his art—the creation of something as delicate and ephemeral as butterflies. The butterflies themselves can symbolize the soul (from the Greek word *psyche*), transformation, or the fleeting nature of life and beauty.
> 
> Therefore, the painting can be interpreted as an allegory on the supremacy of art and creation. Divine power (Jupiter) is not concerned with the pleas of Virtue or the words of Eloquence (Mercury) because it is engrossed in the act of artistic creation, capturing the ephemeral soul of nature.
> 
> The artist of this work is **Dosso Dossi**, and the painting is commonly known as **"Jupiter, Mercury and Virtue"** or sometimes "Jupiter Painting Butterflies," created around 1524.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T07:59:45+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and my internal knowledge, this is a famous Italian Renaissance painting.
> 
> **Subject and Episode:**
> 
> The painting is an allegorical scene, not a depiction of a specific mythological story. Its most common title is **_Jupiter, Mercury and Virtue_**.
> 
> **Figures Identified:**
> 
> 1.  **Jupiter (left):** The bearded man in the red robe, seated at an easel, is Jupiter (the Roman equivalent of the Greek Zeus), the king of the gods. He is shown in the unconventional role of an artist. He is painting butterflies. In ancient Greek, the word for butterfly was *psyche* (ψυχή), which was also the word for "soul." Therefore, Jupiter is depicted in the act of creating human souls.
> 
> 2.  **Mercury (center):** The youthful, nearly nude figure is Mercury (the Roman equivalent of Hermes). He is identifiable by his iconic attributes: the winged hat (petasus) and the winged sandals (talaria). He holds his finger to his lips in a gesture demanding silence, indicating that the process of divine creation is a profound secret not to be revealed.
> 
> 3.  **Virtue (right):** The woman dressed in gold with a floral wreath is the personification of Virtue. She appears to be pleading with the gods, but Jupiter is preoccupied with his creation, and Mercury is silencing her, effectively turning her away.
> 
> **Interpretation of the Scene:**
> 
> The painting is a complex allegory. It suggests that the gods are busy with the mysterious act of creating life (souls), a secret guarded by Mercury. Meanwhile, Virtue is being ignored or cast aside. This has been interpreted as a commentary on the state of the world, where virtue is no longer heeded or valued, even by the gods themselves, who are absorbed in other matters. The entire scene takes place on clouds, with a rainbow and a distant landscape, signifying its divine and otherworldly setting.
> 
> The artist of this work is **Dosso Dossi**, and it was painted around 1524.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:00:08+00:00_

**Prompt:**

> This painting depicts one of the following subjects. Which one is it?
> — Prometheus chained by Vulcan
> — Aeneas rescues his father Anchises from the burning Troy
> — Abduction of Amphitrite by Poseidon
> — The wedding of Peleus and Thetis
> — The Competition of Apollo and Pan and the judgment of Midas
> — Marriage of Cupid and Psyche
> — The Triumph of Bacchus
> — Apollo in Vulcan's forge revealing Venus' love-affair with Mars
> — The Triumph of Mars: an Allegory of War
> — The meeting of Nausicaa and Ulysses
> — The meeting of Dido and Aeneas
> — The sacrifice of Iphigenia
> — The goddess Pallas Athena and the horse Pegasus
> — Dido's sacrifice to Juno
> — Sacrifice to Venus in a temple
> Answer with the subject only.

**Response (verbatim):**

> Marriage of Cupid and Psyche

