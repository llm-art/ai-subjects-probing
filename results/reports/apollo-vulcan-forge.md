# Probe report — `apollo-vulcan-forge`

[![apollo-vulcan-forge](https://media.rkd.nl/iiif/2/10079915/full/!800,800/0/default.jpg)](https://media.rkd.nl/iiif/2/10079915/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://media.rkd.nl/iiif/2/10079915/info.json)_

- **Ground-truth subject:** Apollo in Vulcan's forge revealing Venus' love-affair with Mars
- **Category:** mythology
- **Institution:** rkd
- **Image:** `data/images/apollo-vulcan-forge.jpg` — native 2808×2132 px, sent 2048×1555 px
- **SHA-256:** `784a2549946c13dbb5f3be7309066b18f2db6c078799809c6c90d59dcfd78e00`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:44:07+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Antoine Coypel",
>   "title": "Vulcan Presenting the Arms of Aeneas to Venus",
>   "date": "c. 1700-1704",
>   "collection": "Louvre Museum"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-15T07:43:39+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology, this artwork depicts the mythological scene of **Apollo in the Forge of Vulcan**.
> 
> Here is a breakdown of the elements in the image that lead to this conclusion:
> 
> *   **The Setting:** The scene on the left is a dark, cavernous forge. Muscular, semi-nude figures are seen working with hammers, an anvil, and what appears to be bellows, indicating a blacksmith's workshop. This is the traditional representation of the forge of Vulcan (the Roman god of fire and metalworking, known as Hephaestus in Greek mythology).
> 
> *   **The Central Figures:**
>     *   **Vulcan (Hephaestus):** The seated, bearded, and muscular man in the center is Vulcan. He is surrounded by pieces of armor and weaponry that his forge produces. His posture, with arms crossed and looking up, suggests he is listening intently or reacting to news.
>     *   **Apollo:** The figure descending on a cloud is Apollo, the god of music, poetry, truth, and light. He is identifiable by his youthful, idealized appearance and the laurel wreath on his head. The radiance emanating from him further signifies his divine and solar nature. He is touching Vulcan's shoulder and gesturing with his other hand, indicating he is delivering a message.
> 
> *   **The Narrative:** The specific story being depicted is most likely from Ovid's *Metamorphoses*. In this tale, Apollo, the all-seeing sun god, discovers the adulterous affair between Vulcan's wife, Venus (goddess of love), and Mars (god of war). He then goes to Vulcan's forge to reveal the infidelity to the cuckolded husband.
> 
> *   **Supporting Details:**
>     *   **The Cyclopes:** The workers in the background are Vulcan's assistants, the Cyclopes.
>     *   **The Relief Sculpture:** In the upper right corner, on the balustrade of the classical building, there is a relief sculpture that appears to show an amorous couple (likely Venus and Mars), providing a visual clue to the subject of Apollo's revelation.
> 
> In summary, the image captures the dramatic moment when Apollo informs Vulcan of his wife's affair with Mars, set within the god's bustling forge.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-15T07:43:57+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of classical mythology, this painting depicts the mythological scene of **Apollo in the Forge of Vulcan**.
> 
> Here is a breakdown of the figures and elements in the scene:
> 
> *   **Vulcan (Hephaestus in Greek mythology):** The seated, bearded figure in the center is Vulcan, the Roman god of fire, metalworking, and the forge. He is surrounded by the tools of his trade and his creations.
> *   **The Cyclopes:** The muscular, semi-nude figures working in the background are the Cyclopes, the assistants to Vulcan in his forge, which was said to be under Mount Etna. They are shown hammering metal on an anvil.
> *   **Apollo:** The figure descending on a cloud is Apollo, the god of music, poetry, prophecy, and the sun. He is identifiable by the **laurel wreath** on his head, a traditional symbol of his, and the radiant light emanating from him. He is shown interacting with Vulcan, placing a hand on his shoulder and gesturing, as if giving a divine instruction or commission.
> *   **The Forge and Armor:** The setting is Vulcan's forge, indicated by the rocky cave, anvil

### Probe B-forced-choice — Closed identification

_Run: 2026-06-15T07:44:16+00:00_

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

> Apollo in Vulcan's forge revealing Venus' love-affair with Mars

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:48:05+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> *   Wait, let's look at the style again. It's very French, 18th century.
> *   Let's search for: "Apollo in the Forge of Vulcan" "drawing" "Louvre" or "Metropolitan Museum".
> *   Wait, could it be by *Charles-Joseph Natoire*?
>     *   Natoire did a drawing "Apollo in the Forge of Vulcan" (or "Apollo revealing the love of Mars and Venus to Vulcan").
>     *   Let's check *Jean-Baptiste Marie Pierre*: "Apollo in the Forge of Vulcan" (1748, drawing or painting).
>     *   Let's check *Louis de Boullogne*: "Apollo in the Forge of Vulcan" (1703).
>     *   Let's check *Antoine Coypel*: "Apollo in the Forge of Vulcan" (1700-1710).
>     *   Let's check *Charles de La Fosse*: "Apollo in the Forge of Vulcan" (1680s).
>     *   Let's check *Jean-Baptiste Jouvenet*: "Apollo in the Forge of Vulcan" (1700s).
>     *   Let's check *Michel Corneille the Younger*: "Apollo in the Forge of Vulcan" (1680s).
>     *   Let's check *Nicolas Bertin*: "Apollo in the Forge of Vulcan" (1700s).
>     *   Let's check *Jean-François de Troy*: "Apollo in the Forge of Vulcan" (1710s).
>     *   Let's check *François Lemoyne*: "Apollo in the Forge of Vulcan" (1720s).
>     *   Let's check *Charles-Antoine Coypel*: "Apollo in the Forge of Vulcan" (1730s).
>     *   Let's check *Charles-Joseph Natoire*: "Apollo in the Forge of Vulcan" (1737).
>     *   Let's check *Carle van Loo*: "Apollo in the Forge of Vulcan" (1740s).
>     *   Let's check *Jean-Baptiste Marie Pierre*: "Apollo in the Forge of Vulcan" (1748).
>     *   Let's check *Louis-Jean-François Lagrenée*: "Apollo in the Forge of Vulcan" (1760s).
>     *   Let's check *Jean-Simon Berthélemy*: "Apollo in the Forge of Vulcan" (1770s).
>     *   Let's check *Jean-Guillaume Moitte*: "Apollo in the Forge of Vulcan" (1780s).
>     *   Let's check *Pierre-Jacques Cazes*: "Apollo in the Forge of Vulcan" (1710s).
>     *   Let's check *Claude Audran III*: "Apollo in the Forge of Vulcan" (1700s).
>     *   Let's check *

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:09:23+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This image depicts the classical mythological scene of **Apollo revealing the infidelity of Venus and Mars to Vulcan in his forge** (a subject from Ovid's *Metamorphoses*). 
> 
> Here are the key elements shown in the artwork:
> 
> * **Vulcan (Hephaestus):** Seated in the center, looking back in shock and dismay as he receives the news. At his feet lie pieces of armor (greaves, breastplate, and helmet) that he and his helpers have been crafting.
> * **Apollo (Sol):** The sun god, who sees all deeds on Earth, arrives on a cloud from the right. He is surrounded by a radiant halo of light and points toward the upper right corner to expose the affair.
> * **Venus and Mars:** In the upper right background, on a draped balcony/alcove, the goddess of love (Venus, Vulcan's wife) and the god of war (Mars) are shown embracing in bed.
> * **The Cyclopes / Blacksmiths:** On the left, inside the dark, cavernous forge, Vulcan's assistants are busy hammering metal at the anvil and stoking the fire.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:09:31+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> This work depicts the mythological scene of **Apollo revealing the infidelity of Venus and Mars to Vulcan** (often titled *Apollo in the Forge of Vulcan*). 
> 
> ### **The Figures and Scene:**
> * **Apollo (the Sun God):** The radiant, youthful figure floating on a cloud with rays of light emanating from his head. He is pointing toward the upper right to reveal the affair.
> * **Vulcan (Hephaestus):** The muscular, bearded blacksmith god seated in the center. He looks dismayed and brooding as he receives the news of his wife's betrayal.
> * **Venus and Mars:** Visible in the upper right background, embracing in a bed on a balcony.
> * **The Cyclopes:** Vulcan's assistants, shown working at the anvil inside the cave/forge on the left, hammering out armor.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:09:39+00:00_

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

> Apollo in Vulcan's forge revealing Venus' love-affair with Mars

