# Probe report — `apollo-pan-midas`

[![apollo-pan-midas](https://media.rkd.nl/iiif/2/10036732/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10036732/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10036732/info.json)_

- **Ground-truth subject:** The Competition of Apollo and Pan and the judgment of Midas
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/apollo-pan-midas.jpg` — native 2164×1812 px, sent 2048×1715 px
- **SHA-256:** `c48c49603296a1097d864010952d893fa081a70587058ad2b40a334eecd2bd7b`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A is a logged covariate — record only, never score. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (logged covariate — record only, do not score)

_Run: 2026-06-15T07:42:00+00:00_

**Prompt:**

> What artwork is this? If you can, name the artist, title, approximate date, and collection. If you don't recognise the specific work, say so explicitly.

**Response (verbatim):**

> Based on the visual evidence and my internal knowledge, this artwork is:
> 
> **Artist:** A collaboration between **Hendrick de Clerck** (figures) and **Denijs van Alsloot** (landscape).
> 
> **Title:** *The Contest between Apollo and Pan*
> 
> **Approximate Date:** c. 1620
> 
> **Collection:** Rijksmuseum, Amsterdam, Netherlands.
> 
> The painting depicts the mythological story of the musical contest between the god Apollo and the satyr Pan. Apollo, god of music and poetry, is the figure in the red cloak with a laurel wreath and a radiant glow, holding a stringed instrument (a *lira da braccio*). He is surrounded by nymphs, satyrs, and other figures who have gathered to hear the competition. The figure in the turban is King Midas, who, according to the myth, foolishly judged Pan's rustic music to be superior to Apollo's, for which he was punished with a pair of donkey's ears. The style is characteristic of the Flemish Baroque period.

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:42:15+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology and art history, this painting depicts the mythological story of **the musical contest between Apollo and Pan (or Marsyas)**.
> 
> Here is a breakdown of the scene:
> 
> *   **The Central Event:** The main action takes place on the right side of the composition, nestled in a shadowy grove. The figure in the center, wearing a red cloak and a radiant laurel crown, is **Apollo**, the Greek god of music. He is holding a stringed instrument, likely a lyre or a viola da braccio, symbolizing his divine musical talent. An older, bearded figure, likely the mountain god **Tmolus** who judged the contest, is shown crowning Apollo, signifying his victory.
> 
> *   **King Midas:** To the left of Tmolus is a seated, muscular man with a wreath of vines, pointing to his own ear. This is **King Midas**. In the myth, Midas foolishly declared Pan the winner of the contest. As a punishment for his poor judgment and "ears of an ass," Apollo transformed his ears into those of a donkey. Midas's gesture of pointing to his ear captures the moment of his dissent or the beginning of his punishment.
> 
> *   **The Audience:** The contest is witnessed by a host of mythological figures. These include numerous nude or semi-nude **nymphs** and goat-legged **satyrs**, who were followers of Pan and inhabitants of the pastoral world. One satyr can be seen leaping in the trees above, while another crouches in the foreground looking up at the scene. On the far right, a man in a turban observes the event.
> 
> *   **The Foreground Figure:** In the lower-left foreground, a woman in a white and pink dress sits apart from the main group, looking directly out at the viewer. Before her lies a still life of musical instruments, including a lute, a violin, and sheet music. She may represent a **Muse** (perhaps Euterpe, the muse of music) or a personification of Music itself,

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:42:34+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the painting and knowledge of classical mythology and art history, this painting depicts the mythological episode of **The Contest between Apollo and Pan**, which is sometimes also referred to as **The Judgment of Midas**.
> 
> Here is a breakdown of the figures and the scene:
> 
> *   **Apollo:** The central standing figure, identifiable by the radiant light around his head, the laurel wreath (his sacred plant), and the stringed instrument he holds (a viola da braccio, which stands in for his classical lyre). He is dressed in a rich red cloak, signifying his divine status as the god of music and order.
> 
> *   **Pan (or a follower representing him):** The muscular, semi-nude figure seated to the left of Apollo, crowned with a wreath of ivy or grape leaves. He points to his ear, a gesture associated with judging music. He represents the wild, rustic music of nature. In some depictions, the challenger is the satyr Marsyas, but the gathering of numerous satyrs and the presence of Midas strongly point to the story of Pan.
> 
> *   **King Midas:** The older, bearded man wearing a turban on the far right. In the myth, Midas was one of the judges. He foolishly preferred Pan's rustic piping to Apollo's divine music. As a punishment for his poor judgment, Apollo gave him the ears of a donkey.
> 
> *   **Tmolus:** The bearded figure next to Midas could be Tmolus, the mountain god who was the primary judge and correctly declared Apollo the winner.
> 
> *   **Satyrs and Nymphs:** The surrounding figures are the audience. The male figures with

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:42:55+00:00_

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

