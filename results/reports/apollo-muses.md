# Probe report — `apollo-muses`

[![apollo-muses](https://iiif.artresearch.net/iiif/3/frick/4107100328032_0001.jp2/full/!800,800/0/default.jpg)](https://iiif.artresearch.net/iiif/3/frick/4107100328032_0001.jp2/full/max/0/default.jpg)

_Image served from IIIF (click for full resolution) — [info.json](https://iiif.artresearch.net/iiif/3/frick/4107100328032_0001.jp2/info.json)_

- **Ground-truth subject:** Apollo and the Muses
- **Category:** mythology
- **Institution:** frick
- **Image:** `data/images/apollo-muses.jpg` — native 11383×6718 px, sent 2048×1209 px
- **SHA-256:** `34da5590a07dccdcf705d31aa41abc85fffaff25352feb77e5523ecf1177f956`
- **Probe battery version:** 1.2
- **System instruction (all sessions):** You are looking at a single image. Answer only from what is visible in the image and your own internal knowledge. Do not use web search, retrieval, external tools, or any internet resources to answer.

_Each probe ran in a separate stateless session. Probe A returns structured JSON and is scored per element (artist/title/date/collection) by an LLM judge against institutional ground truth; the collection element is low-confidence. Probe C is expert-scored with semantic matching (e.g. "a burning building", "fire and smoke" and "Troy in flames" all match a burning-city reference)._

## Model: `gemini:gemini-2.5-pro`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:46:10+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Annibale Carracci",
>   "title": "An Allegory of Truth and Time",
>   "date": "c. 1600-1601",
>   "collection": "Royal Collection Trust"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T08:00:53+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> Based on the visual evidence in the image and general knowledge of art history and mythology, this is a depiction of a classical mythological scene, most likely **Apollo and the Muses**, with the inclusion of **Cupid**.
> 
> Here is a breakdown of the elements in the image:
> 
> *   **The Muses:** The group of women gathered in the landscape are the Muses, the nine goddesses of the arts, literature, and sciences in Greek mythology. They are shown in various poses of leisure and artistic engagement, gathered around a keyboard instrument that resembles a harpsichord or spinet.
> *   **Apollo:** The male figure flying in the upper left, holding a stringed instrument (like a viola da gamba or a lyre) and a bow to play it, is likely Apollo. As the god of music, poetry, and the arts, he was the leader of the Muses.
> *   **Cupid (Eros):** The winged figure flying near the top center, holding a bow and aiming an arrow, is Cupid, the god of love. His presence introduces the theme of love as a source of artistic inspiration or as a disruptive force among the gods.
> *   **Other Figures:** There are other figures, including a tumbling putto (a winged infant) in the upper left and other attendants, some winged, contributing to the lively and divine atmosphere of the scene.
> *   **Setting and Style:** The scene is set in a pastoral, idyllic landscape, a common setting for such mythological gatherings (like Mount Parnassus). The artwork is executed in a monochrome palette of brown and sepia tones (a technique known as brunaille or grisaille). The style is characteristic of the **Baroque period**, with its dynamic composition, dramatic use of light and shadow (chiaroscuro), and the depiction of full-bodied, fleshy figures in complex, energetic poses.
> 
> In summary, the image portrays a gathering of the Muses making music, presided over by their leader Apollo, while Cupid, the god of love, hovers above, creating a rich allegorical scene about the relationship between art, inspiration, and love.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T08:01:14+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the visual evidence in the image and knowledge of art history, this painting depicts a mythological scene, most likely **The Realm of Venus** or **The Court of Venus**.
> 
> Here is a breakdown of the scene and its figures:
> 
> *   **Subject:** The painting portrays an allegorical gathering in an idyllic, pastoral landscape, which is characteristic of depictions of the domain of Venus, the Roman goddess of love, beauty, and pleasure. The central activities are music and leisure, which were considered essential components of her court.
> 
> *   **Key Figures:**
>     *   **Cupid (or Eros):** The winged, nude youth flying in the upper left with a bow is unmistakably Cupid, the son and attendant of Venus. His presence is the strongest indicator that the scene is related to the theme of love.
>     *   **Venus:** While not definitively identifiable without specific attributes like doves or the golden apple, the central woman standing by the keyboard instrument, holding a music book, is likely Venus herself. She presides over the gathering, directing the music.
>     *   **Attendants (Nymphs or Graces):** The other women surrounding Venus are her attendants. They could be nymphs, mortals, or the Three Graces (Charites), who were often depicted in Venus's retinue. They are shown listening, singing, or relaxing, embodying beauty and harmony.
>     *   **Musicians and Personifications:** The figures are gathered around a keyboard instrument, likely a harpsichord or a virginal. Another figure flies above holding a stringed instrument, possibly a viola da gamba. These elements emphasize that music is the food of love and a central art in Venus's realm.
> 
> *   **Episode/Meaning:** This is not a depiction of a specific narrative myth (like the *Judgment of Paris*). Instead, it is a thematic and allegorical representation of Venus's world—a place of perpetual beauty, harmony, and sensual pleasure, where the arts, particularly music, flourish under the influence of love.
> 
> *   **Artistic Style:**
>     *   The painting is executed in a monochromatic palette of brown and white tones, a technique known as *en brunaille* (a variant of *grisaille*). This suggests it might be a preparatory oil sketch (*modello*) for a larger, full-color painting, or a finished work intended to emulate classical sculpture or drawing.
>     *   The style is characteristic of the **Baroque** period (c. 1600-1750). This is evident in the dynamic, swirling composition, the fleshy and muscular figures, the dramatic use of light and shadow (chiaroscuro), and the overall sense of energy and movement. The style is reminiscent of the work of artists like Peter Paul Rubens or Italian masters influenced by Titian.

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T08:01:36+00:00_

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

> The wedding of Peleus and Thetis

## Model: `gemini:gemini-3.5-flash`

### Probe A — Recognition (structured JSON; per-element LLM-judge scored)

_Run: 2026-06-18T13:50:38+00:00_

**Prompt:**

> What artwork is this? Answer with a SINGLE JSON object and nothing else (no markdown fences), with these keys: "recognized" (true or false — do you recognise this specific work), "artist", "title", "date", "collection". Give your best value for each field as a string, or null if unknown. Answer only from the image and your own knowledge.

**Response (verbatim):**

> ```json
> {
>   "recognized": true,
>   "artist": "Hendrick Goltzius",
>   "title": "The Muses on Mount Helicon",
>   "date": "1592",
>   "collection": "Teylers Museum"
> }
> ```

### Probe B-plain — Open identification, no context

_Run: 2026-06-18T13:15:36+00:00_

**Prompt:**

> What is depicted in this image?

**Response (verbatim):**

> This image depicts **Apollo and the Muses** (also known simply as *The Muses*), based on the famous painting by the Italian Renaissance master **Jacopo Tintoretto** (circa 1578, currently in the Royal Collection). 
> 
> This particular image is a monochrome chiaroscuro drawing or print (likely wash with white heightening on toned paper) after Tintoretto's composition.
> 
> ### Key Elements Depicted:
> * **Apollo:** The male figure flying in the upper left, holding a bow in one hand and a stringed instrument (a viol or lyre) in the other, symbolizing his role as the leader of the Muses and god of music and poetry.
> * **The Nine Muses:** The companion goddesses of the arts and sciences are shown in various poses:
>   * One muse is shown diving/flying horizontally on the left.
>   * Another sits in the bottom-left corner playing a lute.
>   * In the center, a muse sits holding an open book or tablet.
>   * On the right, several muses are gathered around a keyboard instrument (a virginal or spinet).
>   * Two standing muses are positioned on the far right.
> * **Pegasus:** In the far-left background, the winged horse Pegasus can be seen atop Mount Helicon near the Hippocrene fountain, which was struck open by his hoof and became sacred to the Muses.

### Probe B-framed — Open identification, cultural framing

_Run: 2026-06-18T13:15:50+00:00_

**Prompt:**

> This is a European oil painting. What scene or subject is depicted? Name the episode and the figures if you can.

**Response (verbatim):**

> Based on the composition, this work depicts **Apollo and the Muses** (specifically, it is a drawing or grisaille study after Jacopo Tintoretto's famous painting *The Muses*, c. 1578). 
> 
> ### **Subject and Episode**
> The scene depicts **Apollo and the Nine Muses on Mount Parnassus** (or Mount Helicon), celebrating music, poetry, and the arts. 
> 
> ### **Figures Depicted**
> * **Apollo:** The god of music, light, and poetry, shown flying in the upper left-center. He is surrounded by a radiant light, holding a bow in one hand and a stringed instrument (a viol or *lira da braccio*) in the other.
> * **The Nine Muses:** The sister goddesses of the arts and sciences, arranged in various poses:
>   * **In the foreground and center:** They are shown playing musical instruments (including a lute on the bottom left and a virginal/spinet keyboard instrument in the center-right) and holding books or sheets of music.
>   * **Flying on the left:** Another Muse floats downward, mirroring Apollo's movement.
> * **Pegasus:** The winged horse can be seen in the far-left background, standing near a fountain (representing the Hippocrene spring, which was struck open by Pegasus's hoof and became sacred to the Muses).

### Probe B-forced-choice — Closed identification

_Run: 2026-06-18T13:16:07+00:00_

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

> The goddess Pallas Athena and the horse Pegasus

