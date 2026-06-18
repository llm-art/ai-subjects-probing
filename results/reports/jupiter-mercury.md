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

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:50+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Dosso Dossi (Giovanni di Niccolò de Luteri)",
>   "title": "Jupiter, Mercury and Virtue",
>   "date": "c. 1524",
>   "collection": "Kunsthistorisches Museum, Vienna"
> }
> ```

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

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:50:14+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Dosso Dossi",
>   "title": "Jupiter, Mercury and Virtue",
>   "date": "c. 1524",
>   "collection": "Wawel Royal Castle, Kraków"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:14:40+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This image depicts the famous Renaissance painting ***Jupiter, Mercury and Virtue*** (also known as *Jupiter Painting Butterflies*), created around 1524 by the Italian artist **Dosso Dossi**. 
> 
> The painting is an allegory containing three mythological figures:
> 
> 1. **Jupiter (left):** Depicted not as a powerful ruler of the gods, but as a quiet artist wearing a red robe, focused on painting butterflies onto a canvas. His powerful weapon, the thunderbolt, lies neglected on the ground near his feet.
> 2. **Mercury (center):** The messenger god, recognizable by his winged hat, winged sandals, and the caduceus in his hand. He places a finger to his lips, gesturing for silence.
> 3. **Virtue (right):** A female figure crowned with flowers who approaches imploringly, seeking Jupiter's help or attention. Mercury hushes her so she does not interrupt Jupiter's creative work. 
> 
> The painting is often interpreted as an allegory of the creative process, suggesting that even the supreme ruler of the cosmos prefers the peaceful, quiet pursuit of art over the demanding complaints of the world.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:14:46+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting is ***Jupiter, Mercury and Virtue*** (also known as *Jupiter Painting Butterflies*), a famous work by the Italian Renaissance master **Dosso Dossi** (painted around 1523–1524). 
> 
> ### **The Figures and Scene Depicted:**
> 
> * **Jupiter (Zeus) on the left:** Depicted not with his usual thunderbolts (which lie discarded on the floor beside him), but as a bearded artist peacefully painting butterflies on a canvas. This serves as an allegory for divine creation and the nobility of painting.
> * **Mercury (Hermes) in the center:** Recognizable by his winged hat (*petasos*), winged sandals, and the caduceus in his hand. He places a finger to his lips, gesturing for silence.
> * **Virtue (*Virtus*) on the right:** A female figure crowned with flowers. According to the mythological allegory (derived from a dialogue by the humanist Leon Battista Alberti), Virtue has come to complain to the king of the gods about how she is mistreated and ignored on Earth. However, Mercury silences her, warning her not to interrupt Jupiter while he is deeply absorbed in his creative work.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:14:52+00:00_

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

> Jupiter, Mercury and Virtue

