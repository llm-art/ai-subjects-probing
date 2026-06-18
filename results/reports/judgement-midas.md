# Probe report — `judgement-midas`

[![judgement-midas](https://iiif.artresearch.net/iiif/3/frick/4107100318926_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100318926_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100318926_0001.jp2/info.json)_

- **Ground-truth subject:** The Judgement of Midas
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/judgement-midas.jpg` — native 4573×4650 px, sent 2014×2048 px
- **SHA-256:** `50215640b396ff01692f8f57849585a3a0740d0d161896fab25aed3c1bc36d0d`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:45:54+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Cima da Conegliano",
>   "title": "The Judgment of Midas (The Contest between Apollo and Marsyas)",
>   "date": "c. 1505-1510",
>   "collection": "Statens Museum for Kunst, Copenhagen"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T07:59:26+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology, this artwork depicts the **Musical Contest between Apollo and Marsyas**, with **King Midas** as the judge.
> 
> Here is a breakdown of the figures and the story being told:
> 
> *   **Apollo:** The figure on the left is Apollo, the Greek god of music, poetry, and the arts. He is depicted as a youthful, idealized nude figure, holding a stringed instrument similar to a *lira da braccio* (a Renaissance instrument often used in art to represent the classical lyre). He stands calmly, representing divine order and sophisticated music.
> 
> *   **King Midas:** The central, bearded figure is King Midas. The most telling detail is the pair of donkey's ears sticking out from under his crown. According to the myth, Midas was chosen to judge the musical contest. He foolishly declared the satyr's rustic music superior to Apollo's. As a punishment for his poor judgment and lack of taste, Apollo cursed him with the ears of an ass.
> 
> *   **Marsyas (or Pan):** The figure on the right is a satyr, a mythological creature with the upper body of a man and the legs of a goat, along with horns and pointed ears. This is most likely Marsyas, who challenged Apollo to the contest. He is often depicted with a flute or, as seen here, panpipes (syrinx), representing the wild, untamed music of nature.
> 
> The scene captures the moment of judgment in the mythological tale. Midas is gesturing, likely delivering his ill-fated verdict, while Apollo and the satyr await the outcome. The composition is a *tondo*, a circular work of art, set in a classical pastoral landscape.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T07:59:44+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the figures and their attributes visible in the image, this painting depicts a scene from Greek mythology: **The Judgement of Midas**, which is part of the story of the musical contest between Apollo and Pan (or sometimes the satyr Marsyas).
> 
> Here are the figures identified:
> 
> *   **On the left:** The youthful, idealized, and mostly nude figure holding a stringed instrument (a Renaissance-era *lira da braccio*, standing in for the classical lyre) is **Apollo**, the Greek god of music, poetry, and the arts.
> *   **In the center:** The bearded man wearing a crown and robes is **King Midas**. His most telling feature is the pair of donkey's ears protruding from his crown.
> *   **On the right:** The figure with the upper body of a man and the horns and furry, goat-like legs of a satyr is most likely **Pan**, the god of the wild, or the satyr **Marsyas**. He is holding his signature instrument, the panpipes (or syrinx).
> 
> **The Episode:**
> 
> The myth tells of a musical competition between Apollo and Pan. Pan, boastful of his rustic music, challenged Apollo to a contest. The mountain god Tmolus was chosen as the judge and declared Apollo the winner. However, King Midas, who was also present, foolishly disagreed and proclaimed Pan's music superior. As a punishment for his poor musical judgment and "ears of an ass," the enraged Apollo transformed Midas's human ears into those of a donkey, a mark of his stupidity that he tried to hide under a cap.
> 
> This painting captures the three central characters of the story, likely at the moment of or just after the fateful judgment.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:00:06+00:00_

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

> The Competition of Apollo and Pan and the judgment of Midas

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:50:22+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> {
>   "recognized": true,
>   "artist": "Cima da Conegliano",
>   "title": "The Judgment of Midas",
>   "date": "c. 1507-1509",
>   "collection": "Statens Museum for Kunst"
> }

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:14:51+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This image depicts the mythological scene of **The Judgment of Midas** (specifically the musical contest between the god Apollo and the satyr Pan), painted in a circular format (tondo) by the Italian Renaissance artist **Cima da Conegliano** (c. 1507–1509). 
> 
> The three figures shown are:
> * **Apollo (left):** The youthful, nude Greek god of music, depicted playing a *lira da braccio* (a Renaissance stringed instrument representing his classical lyre).
> * **King Midas (center):** Wearing a crown and already sporting the long donkey ears given to him by Apollo as punishment for foolishly judging Pan's rustic music to be superior to Apollo's divine music.
> * **Pan (right):** The wild god of nature, depicted as a satyr with goat legs and horns, holding his musical pipes.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:14:58+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This painting depicts **The Judgment of Midas** (specifically, the musical contest between the gods **Apollo** and **Pan**), a famous episode from Greek mythology (most famously recounted in Ovid's *Metamorphoses*).
> 
> ### The Figures Depicted:
> * **Apollo (left):** The god of music, depicted as a beautiful, idealized youth playing a stringed instrument (specifically a Renaissance *lira da braccio*).
> * **King Midas (center):** The judge of the contest, wearing a crown. Because he foolishly judged Pan's rustic music to be superior to Apollo's divine music, Apollo punished him by turning his ears into those of a donkey (clearly visible protruding from his crown).
> * **Pan (right):** The god of the wild and shepherds, depicted as a satyr with goat legs, horns, and holding his musical pipes. 
> 
> ### Artist Attribution:
> This circular painting (tondo) is by the Italian Renaissance master **Cima da Conegliano** (painted c. 1505–1510).

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:15:05+00:00_

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

> The Competition of Apollo and Pan and the judgment of Midas

