# Probe A — ground truth vs received (per model, per entry)

## Overview statistics

Probe A asks each model to name the **artist, title, date, and collection** as a JSON object. Each element is graded 0/1 by an LLM judge (`gemini-3.5-flash`) against the manually-verified ground truth in `data/metadata.json` (accepting name/translation variants and overlapping date ranges). Collection is **low-confidence** — its ground truth is often a historical owner rather than the current museum.

**Per-element accuracy (judged correct / judged):**

| element | gemini-2.5-pro | gemini-3.5-flash |
|---|---|---|
| artist | 13/51 (25%) | 14/50 (28%) |
| title | 33/53 (62%) | 34/52 (65%) |
| date | 36/52 (69%) | 30/51 (59%) |
| collection ⚠ | 10/46 (22%) | 9/45 (20%) |
| **overall (excl. collection)** | 82/156 (53%) | 78/153 (51%) |

**Recognition vs. title accuracy** (does claiming to recognise the work track with getting the subject right?):

| | gemini-2.5-pro | gemini-3.5-flash |
|---|---|---|
| claimed recognised | 55/56 | 54/56 |
| └ title correct when recognised | 33/55 (60%) | 34/54 (63%) |
| └ title correct when NOT recognised | 0/1 (0%) | 0/1 (0%) |

`·` in the tables below = not yet judged · blank received = model returned null / unparseable.

## Artist

| id | ground truth | gemini-2.5-pro | gemini-3.5-flash |
|---|---|---|---|
| prometheus-chained-vulcan | Baburen, Dirck van | ✓ Dirck van Baburen | ✓ Dirck van Baburen |
| aeneas-anchises-troy | Suavius, Lambert | ✗ El Greco (Doménikos Theotokópoulos) | ✗ Gillis van Valckenborch |
| abduction-amphitrite | Terwesten, Mattheus | ✗ Giorgio Vasari | ✗ Hendrick de Clerck |
| wedding-peleus-thetis | Cornelisz. van Haarlem, Cornelis | ✗ Joachim Wtewael | ✗ Frans Floris |
| triumph-bacchus | Mont, Deodat van der | ✗ Cornelis de Vos | ✗ Frans Francken the Younger |
| apollo-vulcan-forge | Maes, Godfried (II) | ✗ Antoine Coypel | · |
| triumph-mars | Nieulandt, Guilliam van (II) | ✓ Willem van Nieulandt II | ✓ Willem van Nieulandt II |
| nausicaa-ulysses | Lastman, Pieter | ✗ Hendrik van Balen the Elder and Jan Brueghel the Elder | ✗ Peter Paul Rubens |
| meeting-dido-aeneas | Coignet, Michiel (II) | ✗ Giovanni Battista Tiepolo | ✗ Peter Paul Rubens |
| sacrifice-iphigenia | Wet, Jacob de (I) | ✗ Jan Victors | ✗ Pieter Lastman |
| athena-pegasus | Thulden, Theodoor van | ✗ Cornelis Schut I | ✓ Theodoor van Thulden |
| dido-sacrifice-juno | Romanelli, Giovanni Francesco | ✗ Jacob Jordaens | ✗ Eustache Le Sueur |
| sacrifice-venus-temple | Rubens, Peter Paul | ✓ Peter Paul Rubens | ✓ Peter Paul Rubens |
| potiphar-wife | Bilivert, Giovanni | ✓ Giovanni Biliverti | ✓ Giovanni Bilivert |
| balaam-ass | Lastman, Pieter | ✗ Rembrandt van Rijn | ✗ Rembrandt van Rijn |
| isaac-blesses-jacob | Horst, Gerrit Willemsz. | ✗ Govert Flinck | ✗ Govert Flinck |
| samson-pillars | Rubens, Peter Paul [manner of/after] | ✓ Peter Paul Rubens | ✗ Valerio Castello |
| drunkenness-noah | Floris, Frans (I) [circle of] | ✗ Jacopo Tintoretto | ✗ Bernardo Strozzi |
| feast-esther | Cortona, Pietro da | ✗ Pietro della Vecchia | ✗ Pietro della Vecchia |
| bathsheba-letter | Rubens, Peter Paul [free after] | ✗ Hieronymus Francken the Younger | ✗ Jan Brueghel the Younger and Hendrick van Balen |
| gathering-manna | Bramantino | ✗ Ercole de' Roberti | ✗ Bernardino Luini |
| hagar-ishmael | Cortona, Pietro da | ✗ Pompeo Batoni | ✗ Carlo Maratta |
| prodigal-son-brothel | Bredael, Peeter van | ✗ Jan Miel | ✗ Jan Miel |
| jephtha-daughter | Francken, Hieronymus (III) | ✗ Frans Francken the Younger | ✗ Frans Francken II |
| judah-tamar | Hemessen, Jan Sanders van | ✗ Jan van Scorel | ✗ Jan Swart van Groningen |
| diana-actaeon | Titian | ✓ Titian | ✓ Titian |
| jupiter-mercury | Dossi, Dosso | ✓ Dosso Dossi (Giovanni di Niccolò de Luteri) | ✓ Dosso Dossi |
| judgement-midas | Cima da Conegliano, Giovanni Battista | ✓ Cima da Conegliano | ✓ Cima da Conegliano |
| embassy-hippolyta | Carpaccio, Vittore | ✗ Antonio Pisanello | ✗ Apollonio di Giovanni |
| jason-dragon | Roberti, Ercole de' | ✗ Stefano da Ferrara | ✗ Stefano da Ferrara |
| circe-sorceress | Vassallo, Anton Maria | ✗ Jacopo Bassano | ✗ Giovanni Benedetto Castiglione |
| apollo-muses | Tintoretto | ✗ Annibale Carracci | ✗ Hendrick Goltzius |
| rape-deianira | Pollaiolo, Antonio | ✓ Antonio del Pollaiuolo | ✓ Antonio del Pollaiuolo |
| taking-athens-minos | Master of the Campana Cassoni | ✗ Albrecht Altdorfer | ✗ |
| flood-deucalion | Carpioni, Giulio | ✗ José Aparicio Inglada | ✗ Jean-Baptiste Marie Pierre |
| abduction-helen | Campana, Giacinto | ✗ Tintoretto (Jacopo Robusti) | ✗ Guido Reni |
| lot-daughters | Guercino | ✗ Guido Reni | ✓ Guercino (Giovanni Francesco Barbieri) |
| joseph-cup-dream | Carlone, Giovanni Battista | ✗ Jan Cossiers | ✗ Jan Cossiers |
| abraham-melchizedek | Bleker, Gerrit Claesz | ✗ Peter Paul Rubens | ✗ Gaspar de Crayer |
| abigail-david | Cornelisz van Oostsanen, Jacob | ✗ Master of the von Groote Adoration | ✗ Lucas van Leyden |
| saul-witch-endor | Cornelisz van Oostsanen, Jacob | ✗ Follower of Hieronymus Bosch | ✗ Jan de Beer |
| naaman-syrian | Engelbrechtszoon, Cornelis | ✗ Hieronymus Bosch | ✗ Lucas van Leyden |
| abram-lot-divide | Zanchi, Antonio | ✓ Antonio Zanchi | ✓ Antonio Zanchi |
| jeremiah-baruch | Allston, Washington | ✓ Washington Allston | ✓ Washington Allston |
| sennacherib-angel | Tanzio da Varallo | ✗ Peter Paul Rubens | ✓ Tanzio da Varallo |
| moses-crown-pharaoh | Tiepolo, Giovanni Battista | ✓ Giovanni Battista Tiepolo | ✓ Giovanni Battista Tiepolo |
| sacrifice-jephthah | Mazzoni, Sebastiano | ✗ Peter Paul Rubens | ✗ Jean-Honoré Fragonard |
| judgement-solomon | Cresti, Domenico | ✗ Matthias Stom | ✗ Jusepe de Ribera |
| tobit-tobias | Preti, Mattia | ✗ Bernardo Strozzi | ✗ Matthias Stom |
| jacob-esau-reconcile | Cortona, Pietro da | ✓ Pietro da Cortona | ✗ Giovanni Maria Bottalla |
| elisha-shunem-woman | Mola, Pier Francesco | ✗ Gaspard Dughet | ✗ Francisque Millet |

## Title

| id | ground truth | gemini-2.5-pro | gemini-3.5-flash |
|---|---|---|---|
| prometheus-chained-vulcan | Prometheus chained by Vulcan | ✓ Prometheus Being Chained by Vulcan | ✓ Prometheus Being Chained by Vulcan |
| aeneas-anchises-troy | Aeneas rescues his father Anchises from the burning Troy | ✗ The Fall of Troy | ✗ The Burning of Troy |
| abduction-amphitrite | Abduction of Amphitrite by Poseidon | ✗ Perseus and Andromeda | ✗ The Triumph of Amphitrite |
| wedding-peleus-thetis | The wedding of Peleus and Thetis | ✓ The Wedding of Peleus and Thetis | ✓ The Feast of the Gods |
| apollo-pan-midas | The Competition of Apollo and Pan and the judgment of Midas | ✓ The Judgment of Midas | ✓ The Judgment of Midas |
| marriage-cupid-psyche | Marriage of Cupid and Psyche | ✓ The Marriage of Cupid and Psyche | ✓ The Marriage of Cupid and Psyche |
| triumph-bacchus | The triumph of Bacchus | ✓ The Triumph of Bacchus | ✓ The Triumph of Bacchus |
| apollo-vulcan-forge | Apollo in Vulcan's forge revealing Venus' love-affair with Mars | ✗ Vulcan Presenting the Arms of Aeneas to Venus | · |
| triumph-mars | The triumph of Mars: an Allegory of War | ✗ The Triumph of a Roman General | ✗ The Triumph of Scipio Africanus |
| nausicaa-ulysses | The meeting of Nausicaa and Ulysses | ✗ The Feast of the Gods | ✗ The Finding of Erichthonius |
| meeting-dido-aeneas | The meeting of Dido and Aeneas | ✓ The Meeting of Dido and Aeneas | ✓ The Meeting of Dido and Aeneas |
| sacrifice-iphigenia | The sacrifice of Iphigenia | ✓ The Sacrifice of Iphigenia | ✓ The Sacrifice of Iphigenia |
| athena-pegasus | The goddess Pallas Athena and the horse Pegasus | ✓ Minerva with Pegasus | ✓ Minerva and Pegasus |
| dido-sacrifice-juno | Dido's sacrifice to Juno | ✓ Dido's Sacrifice to Juno | ✓ Sacrifice to Juno |
| sacrifice-venus-temple | Sacrifice to Venus in a temple | ✓ The Worship of Venus | ✗ The Feast of Venus |
| potiphar-wife | Josephs Keuschheit | ✓ La castità di Giuseppe (The Chastity of Joseph) | ✓ The Chastity of Joseph |
| balaam-ass | Balaam and his ass | ✓ Balaam and the Ass | ✓ Balaam and the Ass |
| isaac-blesses-jacob | Isaac blessing Jacob | ✓ Isaac Blessing Jacob | ✓ Isaac Blessing Jacob |
| samson-pillars | Samson breaks the pillars; the temple of Dagon collapses, killing all that are in it (Judges 16:29-31) | ✓ The Death of Samson | ✓ Samson Destroying the Temple |
| drunkenness-noah | The drunkenness of Noah | ✓ The Drunkenness of Noah | ✓ The Drunkenness of Noah |
| feast-esther | Feast of Esther. | ✓ The Feast of Esther | ✓ Feast of Esther |
| bathsheba-letter | Bathsheba receives a letter from David (2 Samuel 11:4) | ✗ Bathsheba at her Fountain | ✓ Bathsheba at her Bath |
| gathering-manna | The Gathering of Manna. | ✓ The Israelites Gathering Manna | ✓ The Gathering of Manna |
| hagar-ishmael | Hagar, Ishmael and the Angel in the Wilderness. | ✓ Hagar and the Angel | ✓ Hagar and Ishmael in the Wilderness |
| prodigal-son-brothel | The Prodigal Son is being chased from the brotherl after spending all his money (Luke 15:13) | ✗ The Charlatan | ✗ The Interrupted Serenade |
| jephtha-daughter | Jephtha welcomed by his daughter (Judges 11:29-40) | ✓ The Meeting of Jephthah and His Daughter | ✓ The Meeting of Jephthah and his Daughter |
| judah-tamar | Judah's love-affair with Tamar; he gives her his signet-ring (Genesis 38:18) | ✗ Vertumnus and Pomona | ✓ Judah and Tamar |
| diana-actaeon | Diana and Actaeon. | ✓ Diana and Actaeon | ✓ Diana and Actaeon |
| jupiter-mercury | Jupiter and Mercury. | ✓ Jupiter, Mercury and Virtue | ✓ Jupiter, Mercury and Virtue |
| judgement-midas | The Judgement of Midas. | ✓ The Judgment of Midas (The Contest between Apollo and Marsyas) | ✓ The Judgment of Midas |
| embassy-hippolyta | The Embassy of Hippolyta, Queen of the Amazons, to Theseus, King of Athens. | ✗ The Tournament of Louvezerp | ✗ Penthesilea before Priam |
| jason-dragon | Episode from the Legend of the Argonauts: Jason Slaying the Sleepless Dragon. | ✗ Miracle of Saint Maurelius | ✗ Jason and the Golden Fleece |
| circe-sorceress | The Sorceress Circe. | ✓ The Sorceress Circe | ✓ The Sorceress Circe |
| apollo-muses | Apollo and the Muses. | ✗ An Allegory of Truth and Time | ✓ The Muses on Mount Helicon |
| rape-deianira | The Rape of Deianira. | ✓ The Rape of Deianira | ✓ Hercules and Deianira |
| taking-athens-minos | The Taking of Athens by Minos. | ✗ The Victory of Charlemagne over the Avars near Regensburg | ✗ |
| flood-deucalion | A Scene from Greek Mythology: The Flood of the Age of Deucalion. | ✓ The Flood (El Diluvio) | ✓ The Flood of Deucalion |
| abduction-helen | The Abduction of Helen. | ✓ The Rape of Helen | ✓ The Abduction of Helen |
| lot-daughters | Lot and His Daughters. | ✓ Lot and His Daughters | ✓ Lot and his Daughters |
| joseph-cup-dream | Two Scenes in the Life of Joseph: "The Discovery of Joseph's Cup in Benjamin's Sack" and "Joseph Interpreting Pharaoh's Dream". | ✗ The Discovery of the Stolen Cup in Benjamin's Sack | ✗ The Finding of the Cup in Benjamin's Sack |
| abraham-melchizedek | Abraham Meeting Melchizedek. | ✓ The Meeting of Abraham and Melchizedek | ✗ The Conversion of Saint Bavo |
| abigail-david | Abigail in Supplication before David. | ✓ The Meeting of David and Abigail | ✓ The Meeting of David and Abigail |
| saul-witch-endor | Saul Coming to Consult the Witch of Endor. | ✗ The Dream of the Doctor (Allegory of the Transience of Life) | ✗ The Sorceress |
| naaman-syrian | The Story of the Syrian Captain Naaman. | ✗ Triptych of the Baptism of Christ | ✗ Triptych with the Baptism of Christ |
| abram-lot-divide | Abram and Iot Dividing up the World between Them. | ✗ The Philosophers (Pythagoras and his pupils) | ✗ Archimedes |
| jeremiah-baruch | Jeremiah Dictating His Prophecy of the Destruction of Jerusalem to Baruch the Scribe. | ✓ Jeremiah Dictating His Prophecy of the Destruction of Jerusalem to Baruch the Scribe | ✓ Jeremiah Dictating his Prophecy of the Destruction of Jerusalem to Baruch the Scribe |
| sennacherib-angel | The Forces of Sennacherib put to Rout by the Angel. | ✓ The Defeat of Sennacherib | ✓ The Defeat of Sennacherib |
| moses-crown-pharaoh | The Child Moses Trampling on the Crown of the Pharoahs. | ✗ The Adoration of the Magi | ✗ The Presentation in the Temple |
| sacrifice-jephthah | Sacrifice of Jephthah. | ✗ The Massacre of the Innocents | ✗ Coresus Sacrificing Himself to Save Callirhoe |
| judgement-solomon | Judgement of Solomon. | ✓ The Judgment of Solomon | ✓ The Judgment of Solomon |
| tobit-tobias | Tobit Blessing Tobias. | ✓ Tobit Blessing his Son | ✗ The Departure of Tobias |
| jacob-esau-reconcile | Reconciliation of Jacob and Esau. | ✗ The Rape of the Sabine Women | ✓ The Meeting of Jacob and Esau |
| elisha-shunem-woman | The Prophet Elisha and the Rich Woman of Shunem. | ✗ Landscape with Elijah and the Angel | ✗ Landscape with Elijah and the Widow of Zarephath |

## Date

| id | ground truth | gemini-2.5-pro | gemini-3.5-flash |
|---|---|---|---|
| prometheus-chained-vulcan | 1623 | ✓ c. 1623 | ✓ 1623 |
| aeneas-anchises-troy | 1550 | ✗ c. 1596-1600 | ✗ c. 1600 |
| abduction-amphitrite | 1685 - 1757 | ✗ c. 1570-1572 | ✗ c. 1610 |
| wedding-peleus-thetis | 1592-1593 | ✗ c. 1612 | ✗ 1550 |
| apollo-pan-midas | c. 1620 | ✗ c. 1605 - c. 1608 | ✗ c. 1630 |
| marriage-cupid-psyche | 19th century | ✗ 1756 | ✗ c. 1645 |
| triumph-bacchus | first half 17th century | ✓ c. 1636 | ✓ c. 1620 |
| apollo-vulcan-forge | 1664 - 1700 | ✓ c. 1700-1704 | · |
| triumph-mars | 1627 (dated) | ✗ c. 1620 | ✗ 1615 |
| nausicaa-ulysses | dated 1619 | ✗ c. 1608-1610 | ✗ ca. 1632-1633 |
| meeting-dido-aeneas | 1648 (dated) | ✗ c. 1757 | ✗ c. 1630 |
| sacrifice-iphigenia | 1635 - 1672 | ✓ c. 1640-1650 | ✗ 1614 |
| athena-pegasus | 1644 (dated) | ✓ 1644 | ✗ 1654 |
| dido-sacrifice-juno | 1655 | ✓ c. 1650 | ✓ c. 1650 |
| sacrifice-venus-temple | c. 1630 | ✗ c. 1636-1637 | ✗ c. 1636-1637 |
| balaam-ass | dated 1622 | ✓ 1626 | ✓ 1626 |
| isaac-blesses-jacob | 1638 | ✓ c. 1638 | ✓ 1638 |
| samson-pillars | first half 17th century | ✓ c. 1605 | ✓ c. 1650 |
| drunkenness-noah | c. 1550-1574 | ✓ c. 1550-1560 | ✗ c. 1630 |
| feast-esther | 1622-1678 | ✓ c. 1645-1650 | ✓ ca. 1640 |
| bathsheba-letter | after 1635 | ✓ c. 1625-1635 | ✗ c. 1625-1630 |
| gathering-manna | 1503-1506 | ✗ c. 1490 | ✗ c. 1520-1523 |
| hagar-ishmael | 1637 - 1638 | ✗ 1776 | ✗ c. 1680 |
| prodigal-son-brothel | after 1658 | ✗ c. 1650 | ✗ c. 1640 |
| jephtha-daughter | 1626 - 1661 | ✓ c. 1630-1635 | ✓ c. 1620 |
| judah-tamar | second or third quarter 16th century | ✓ c. 1524 | ✓ ca. 1530 - 1540 |
| diana-actaeon | 1559 | ✓ 1556–1559 | ✓ 1556–1559 |
| jupiter-mercury | 1499-1542 | ✓ c. 1524 | ✓ c. 1524 |
| judgement-midas | 1459-1518 | ✓ c. 1505-1510 | ✓ c. 1507-1509 |
| embassy-hippolyta | 1475-1525 | ✗ c. 1447-1448 | ✗ c. 1450-1460 |
| jason-dragon | 1460-1496 | ✓ c. 1480 | ✓ c. 1490 |
| circe-sorceress | 1577-1657 | ✓ c. 1570s | ✓ c. 1650 |
| apollo-muses | 1532-1594 | ✗ c. 1600-1601 | ✓ 1592 |
| rape-deianira | 1473 | ✓ c. 1470-1475 | ✓ c. 1470 |
| taking-athens-minos | 1515-1519 | ✓ c. 1518 | ✗ |
| flood-deucalion | 1633-1678 | ✗ 1827 | ✗ 1746 |
| abduction-helen | 1600-1650 | ✗ c. 1578-1579 | ✓ 1631 |
| lot-daughters | 1611-1666 | ✓ c. 1615-1616 | ✓ 1650 |
| joseph-cup-dream | 1612-1677 | ✓ c. 1650s | ✓ c. 1650 |
| abraham-melchizedek | 1625-1656 | ✓ c. 1626 | ✓ c. 1630-1650 |
| abigail-david | 1453-1533 | ✓ c. 1515-1520 | ✓ c. 1515-1520 |
| saul-witch-endor | 1500 | ✓ c. 1500 | ✓ 1506 |
| naaman-syrian | 1488-1533 | ✓ c. 1500 | ✓ 1521 |
| abram-lot-divide | 1651-1722 | ✓ c. 1665 | ✓ ca. 1670 |
| jeremiah-baruch | 1799-1843 | ✓ 1820 | ✓ 1820 |
| sennacherib-angel | 1574-1635 | ✓ c. 1612-1614 | ✓ ca. 1627-1629 |
| moses-crown-pharaoh | 1716-1770 | ✓ ca. 1753 | ✓ c. 1735-1740 |
| sacrifice-jephthah | 1631-1678 | ✓ c. 1636-1638 | ✗ 1765 |
| judgement-solomon | 1578-1638 | ✓ c. 1640 | ✓ c. 1609-1610 |
| tobit-tobias | 1633-1699 | ✓ c. 1630-1635 | ✓ c. 1640 |
| jacob-esau-reconcile | 1616-1669 | ✓ c. 1629-1631 | ✓ c. 1640 |
| elisha-shunem-woman | 1648-1650 | ✓ c. 1650-1660 | ✗ c. 1670-1679 |

## Collection

| id | ground truth | gemini-2.5-pro | gemini-3.5-flash |
|---|---|---|---|
| prometheus-chained-vulcan | Rijksmuseum | ✓ Rijksmuseum | ✓ Rijksmuseum |
| aeneas-anchises-troy | Centraal Museum | ✗ National Gallery of Greece | ✗ |
| abduction-amphitrite | Instituut Collectie Nederland | ✗ Palazzo Vecchio, Florence | ✗ Museo del Prado |
| wedding-peleus-thetis | Frans Hals Museum | ✗ Alte Pinakothek, Munich | ✗ Royal Museum of Fine Arts Antwerp |
| apollo-pan-midas | Museum Schloss Wilhelmshöhe | ✗ Rijksmuseum | ✗ State Hermitage Museum |
| marriage-cupid-psyche | Private collection | ✗ Gemäldegalerie, Berlin | ✗ Musée du Louvre |
| apollo-vulcan-forge | Baulme Fine Arts, F. | ✗ Louvre Museum | · |
| triumph-mars | Portovano, Enrico baron | ✓ Herzog Anton Ulrich-Museum | ✓ Rijksmuseum, Amsterdam |
| nausicaa-ulysses | Alte Pinakothek | ✗ | ✗ Allen Memorial Art Museum |
| sacrifice-iphigenia | Mautner-Markhof | ✗ Rijksmuseum | ✗ Rijksmuseum, Amsterdam |
| athena-pegasus | J. Paul Getty Museum | ✗ | ✗ Royal Museum of Fine Arts Antwerp |
| dido-sacrifice-juno | Norton Simon Museum | ✗ | ✗ Musée du Louvre, Paris |
| sacrifice-venus-temple | Courtauld Gallery | ✗ Museo Nacional del Prado | ✗ Kunsthistorisches Museum, Vienna |
| potiphar-wife | Galleria Nazionale d'arte Antica | ✓ Galleria Barberini | ✓ Galleria Nazionale d'Arte Antica, Palazzo Barberini |
| balaam-ass | The Israel Museum | ✗ Musée Cognacq-Jay | ✗ Musée Cognacq-Jay |
| isaac-blesses-jacob | Dulwich Picture Gallery | ✗ Rijksmuseum | ✗ Rijksmuseum, Amsterdam |
| samson-pillars | J. Paul Getty Museum | ✓ J. Paul Getty Museum | ✗ Hermitage Museum, St. Petersburg |
| feast-esther | J .Paul Getty Museum, Malibu | ✓ J. Paul Getty Museum | ✓ J. Paul Getty Museum |
| gathering-manna | Samuel H. Kress Foundation, New York | ✗ The National Gallery, London | ✗ Pinacoteca di Brera |
| hagar-ishmael | John and Mable Ringling Museum of Art | ✗ Galleria Nazionale d'Arte Antica - Palazzo Corsini | ✗ Museo del Prado |
| judah-tamar | Private collection | ✗ Museum Boijmans Van Beuningen | ✗ Rijksmuseum, Amsterdam |
| diana-actaeon | Earl of Ellesmere, London | ✓ National Gallery, London and National Galleries of Scotland | ✓ National Gallery, London and National Galleries of Scotland |
| jupiter-mercury | Kunsthistorisches Museum Wien | ✓ Kunsthistorisches Museum, Vienna | ✗ Wawel Royal Castle, Kraków |
| judgement-midas | Pinacoteca di Parma, Parma | ✗ Statens Museum for Kunst, Copenhagen | ✗ Statens Museum for Kunst |
| embassy-hippolyta | Musée Jacquemart-André | ✗ Palazzo Ducale, Mantua | ✗ |
| jason-dragon | Phoebe Timpson | ✗ Pinacoteca Nazionale, Ferrara | ✗ |
| circe-sorceress | Uffizi Gallery | ✗ Kunsthistorisches Museum, Vienna | ✗ J. Paul Getty Museum |
| apollo-muses | Dr. G.H.A. Clowes, Indianapolis | ✗ Royal Collection Trust | ✗ Teylers Museum |
| rape-deianira | Yale University Art Gallery | ✓ Yale University Art Gallery | ✓ Yale University Art Gallery |
| taking-athens-minos | Musee du Petit Palais, Avignon | ✗ Gabinetto dei Disegni e delle Stampe, Uffizi Gallery | ✗ |
| flood-deucalion | Academy of fine Arts, Siena | ✗ Real Academia de Bellas Artes de San Fernando | ✗ Musée des Beaux-Arts de Nancy |
| abduction-helen | Palazzo spada, Roma | ✗ Museo Nacional del Prado | ✗ Louvre Museum |
| lot-daughters | Toledo Museum of Art, Toledo | ✗ National Gallery, London | ✗ Musée du Louvre, Paris |
| joseph-cup-dream | Finch College, New York | ✗ Royal Museums of Fine Arts of Belgium | ✗ Hermitage Museum, St. Petersburg |
| abraham-melchizedek | Private collection (Confidential File) | ✗ National Gallery of Art, Washington D.C. | ✗ Museum of Fine Arts, Ghent |
| abigail-david | kunstmuseum, København | ✗ Städel Museum, Frankfurt am Main | ✗ Detroit Institute of Arts |
| saul-witch-endor | Rijksmuseum | ✗ The Courtauld, London | ✗ British Museum |
| naaman-syrian | Kunsthistorisches Museum Wien | ✗ Royal Museums of Fine Arts of Belgium | ✗ Museo Nacional Thyssen-Bornemisza, Madrid |
| abram-lot-divide | Sta. Maria Zobenigo, Venezia | ✗ Accademia Carrara, Bergamo | ✗ |
| jeremiah-baruch | Yale University Art Gallery | ✓ Yale University Art Gallery | ✓ Yale University Art Gallery |
| moses-crown-pharaoh | Amherst College, Amherst | ✗ The Metropolitan Museum of Art | ✗ Gemäldegalerie Alte Meister, Dresden |
| sacrifice-jephthah | William Rockhill Nelson Gallery of Art, Kansas City | ✗ Alte Pinakothek, Munich | ✗ Musée du Louvre |
| judgement-solomon | Gallerie Borghese, Roma | ✗ Museum of Fine Arts, Houston | ✓ Galleria Borghese |
| tobit-tobias | Montreal Museum of Fine Arts | ✗ The State Hermitage Museum, St. Petersburg | ✗ |
| jacob-esau-reconcile | Palazzo dei Conservatori, Roma | ✓ Capitoline Museums, Rome | ✓ Capitoline Museums, Rome |
| elisha-shunem-woman | Ringling Museum, Sarasota | ✗ The National Gallery, London | ✗ National Gallery, London |
