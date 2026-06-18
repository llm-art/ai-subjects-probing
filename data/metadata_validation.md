# Ground-truth validation — SPARQL vs manual

Per-field check of the SPARQL auto-extraction against the PI's manual gold standard. `✓` agree · `≠` differ · `SPARQL∅` SPARQL missed it (manual has it) · `manual∅` manual blank (SPARQL has it) · `—` both blank.

data/metadata.json now uses **manual** for artist/title/date and SPARQL for collection + multilingual name variants.

| id | artist | manual artist | SPARQL artist | title | date | manual date | SPARQL date | collection |
|---|---|---|---|---|---|---|---|---|
| prometheus-chained-vulcan | SPARQL∅ | Baburen, Dirck van |  | SPARQL∅ | ✓ | 1623 | dated 1623 | ✓ |
| aeneas-anchises-troy | SPARQL∅ | Suavius, Lambert |  | SPARQL∅ | ✓ | 1550 | c. 1550 | ✓ |
| abduction-amphitrite | SPARQL∅ | Terwesten, Mattheus |  | SPARQL∅ | ✓ | 1685 - 1757 | 1685 - 1757 | manual∅ |
| wedding-peleus-thetis | SPARQL∅ | Cornelisz. van Haarlem, Cornelis |  | SPARQL∅ | ✓ | 1592-1593 | 1592-1593 | manual∅ |
| apollo-pan-midas | — |  |  | SPARQL∅ | ✓ | c. 1620 | c. 1620 | manual∅ |
| marriage-cupid-psyche | — |  |  | SPARQL∅ | ✓ | 19th century | 19th century | manual∅ |
| triumph-bacchus | SPARQL∅ | Mont, Deodat van der |  | SPARQL∅ | ≠ | first half 17th century | eerste helft 17de eeuw | — |
| apollo-vulcan-forge | SPARQL∅ | Maes, Godfried (II) |  | SPARQL∅ | ✓ | 1664 - 1700 | 1664 - 1700 | manual∅ |
| triumph-mars | SPARQL∅ | Nieulandt, Guilliam van (II) |  | SPARQL∅ | ✓ | 1627 (dated) | 1627 (dated) | manual∅ |
| nausicaa-ulysses | SPARQL∅ | Lastman, Pieter |  | SPARQL∅ | ≠ | dated 1619 | 1619 gedateerd | manual∅ |
| meeting-dido-aeneas | SPARQL∅ | Coignet, Michiel (II) |  | SPARQL∅ | ✓ | 1648 (dated) | 1648 (dated) | — |
| sacrifice-iphigenia | SPARQL∅ | Wet, Jacob de (I) |  | SPARQL∅ | ✓ | 1635 - 1672 | 1635 - 1672 | manual∅ |
| athena-pegasus | SPARQL∅ | Thulden, Theodoor van |  | SPARQL∅ | ✓ | 1644 (dated) | 1644 (dated) | manual∅ |
| dido-sacrifice-juno | SPARQL∅ | Romanelli, Giovanni Francesco |  | SPARQL∅ | ✓ | 1655 | 1655 | manual∅ |
| sacrifice-venus-temple | SPARQL∅ | Rubens, Peter Paul |  | SPARQL∅ | ≠ | c. 1630 | ca. 1630 | manual∅ |
| finding-moses | — |  |  | — | — |  |  | — |
| abraham-isaac | — |  |  | — | — |  |  | — |
| potiphar-wife | SPARQL∅ | Bilivert, Giovanni |  | ✓ | — |  |  | SPARQL∅ |
| balaam-ass | SPARQL∅ | Lastman, Pieter |  | SPARQL∅ | ✓ | dated 1622 | dated 1622 | manual∅ |
| isaac-blesses-jacob | SPARQL∅ | Horst, Gerrit Willemsz. |  | SPARQL∅ | ✓ | 1638 | 1638 | manual∅ |
| samson-pillars | SPARQL∅ | Rubens, Peter Paul [manner of/after] |  | SPARQL∅ | ✓ | first half 17th century | first half 17th century | manual∅ |
| drunkenness-noah | SPARQL∅ | Floris, Frans (I) [circle of] |  | SPARQL∅ | ✓ | c. 1550-1574 | c. 1550-1574 | — |
| feast-esther | ✓ | Cortona, Pietro da | Cortona, Pietro da | ✓ | ✓ | 1622-1678 | 1622-1678 | manual∅ |
| belshazzar-feast | — |  |  | — | — |  |  | — |
| bathsheba-letter | SPARQL∅ | Rubens, Peter Paul [free after] |  | SPARQL∅ | ✓ | after 1635 | after 1635 | — |
| gathering-manna | ✓ | Bramantino | Bramantino | ✓ | ✓ | 1503-1506 | 1503-1506 | manual∅ |
| hagar-ishmael | ✓ | Cortona, Pietro da | Cortona, Pietro da | SPARQL∅ | ✓ | 1637 - 1638 | 1637 - 1638 | manual∅ |
| prodigal-son-brothel | SPARQL∅ | Bredael, Peeter van |  | SPARQL∅ | ✓ | after 1658 | after 1658 | — |
| jephtha-daughter | SPARQL∅ | Francken, Hieronymus (III) |  | SPARQL∅ | ✓ | 1626 - 1661 | 1626 - 1661 | — |
| judah-tamar | SPARQL∅ | Hemessen, Jan Sanders van |  | SPARQL∅ | ≠ | second or third quarter 16th century | tweede of derde kwart 16de eeuw | manual∅ |
| diana-actaeon | ≠ | Titian | Titiaan | ✓ | ✓ | 1559 | 1559 | manual∅ |
| jupiter-mercury | ✓ | Dossi, Dosso | Dossi, Dosso | ✓ | ✓ | 1499-1542 | 1499-1542 | manual∅ |
| judgement-midas | ✓ | Cima da Conegliano, Giovanni Battista | Cima da Conegliano, Giovanni Battista | ✓ | ✓ | 1459-1518 | 1459-1518 | manual∅ |
| embassy-hippolyta | ✓ | Carpaccio, Vittore | Carpaccio, Vittore | ✓ | ✓ | 1475-1525 | 1475-1525 | manual∅ |
| jason-dragon | ✓ | Roberti, Ercole de' | Roberti, Ercole de' | ✓ | ✓ | 1460-1496 | 1460-1496 | manual∅ |
| circe-sorceress | ≠ | Vassallo, Anton Maria | Vassallo, Antonio Maria | ✓ | ✓ | 1577-1657 | 1577-1657 | manual∅ |
| apollo-muses | ✓ | Tintoretto | Tintoretto | ✓ | ✓ | 1532-1594 | 1532-1594 | manual∅ |
| rape-deianira | ✓ | Pollaiolo, Antonio | Pollaiolo, Antonio del | ✓ | ✓ | 1473 | 1473 | manual∅ |
| taking-athens-minos | ✓ | Master of the Campana Cassoni | Master of the Campana Cassoni | ✓ | ✓ | 1515-1519 | 1515-1519 | manual∅ |
| flood-deucalion | ✓ | Carpioni, Giulio | Carpioni, Giulio | ✓ | ✓ | 1633-1678 | 1633-1678 | manual∅ |
| abduction-helen | ✓ | Campana, Giacinto | Campana, Giacinto | ✓ | ✓ | 1600-1650 | 1600-1650 | manual∅ |
| lot-daughters | ✓ | Guercino | Guercino | ✓ | ✓ | 1611-1666 | 1611-1666 | manual∅ |
| joseph-cup-dream | ✓ | Carlone, Giovanni Battista | Carlone, Giovanni Battista | ✓ | ✓ | 1612-1677 | 1612-1677 | manual∅ |
| abraham-melchizedek | ✓ | Bleker, Gerrit Claesz | Bleker, Gerrit Claesz | ✓ | ✓ | 1625-1656 | 1625-1656 | manual∅ |
| abigail-david | ≠ | Cornelisz van Oostsanen, Jacob | Cornelisz, Jacob | ✓ | ✓ | 1453-1533 | 1453-1533 | manual∅ |
| saul-witch-endor | ≠ | Cornelisz van Oostsanen, Jacob | Cornelisz, Jacob | ✓ | ✓ | 1500 | 1500 | manual∅ |
| naaman-syrian | ≠ | Engelbrechtszoon, Cornelis | Engebrechtsz., Cornelis | ✓ | ✓ | 1488-1533 | 1488-1533 | manual∅ |
| abram-lot-divide | ✓ | Zanchi, Antonio | Zanchi, Antonio | ✓ | ✓ | 1651-1722 | 1651-1722 | manual∅ |
| jeremiah-baruch | ✓ | Allston, Washington | Allston, Washington | ✓ | ✓ | 1799-1843 | 1799-1843 | manual∅ |
| sennacherib-angel | ✓ | Tanzio da Varallo | Tanzio da Varallo | ✓ | ✓ | 1574-1635 | 1574-1635 | — |
| moses-crown-pharaoh | ✓ | Tiepolo, Giovanni Battista | Tiepolo, Giovanni Battista | ✓ | ✓ | 1716-1770 | 1716-1770 | manual∅ |
| sacrifice-jephthah | ✓ | Mazzoni, Sebastiano | Mazzoni, Sebastiano | ✓ | ✓ | 1631-1678 | 1631-1678 | manual∅ |
| judgement-solomon | ✓ | Cresti, Domenico | Cresti, Domenico | ✓ | ✓ | 1578-1638 | 1578-1638 | manual∅ |
| tobit-tobias | ✓ | Preti, Mattia | Preti, Mattia | ✓ | ✓ | 1633-1699 | 1633-1699 | manual∅ |
| jacob-esau-reconcile | ✓ | Cortona, Pietro da | Cortona, Pietro da | ✓ | ✓ | 1616-1669 | 1616-1669 | manual∅ |
| elisha-shunem-woman | ✓ | Mola, Pier Francesco | Mola, Pier Francesco | ✓ | ✓ | 1648-1650 | 1648-1650 | manual∅ |

---

**Field agreement tallies:**

- **artist**: SPARQL∅=22 · —=5 · ≠=5 · ✓=24
- **title**: SPARQL∅=24 · —=3 · ✓=29
- **date**: —=4 · ≠=4 · ✓=48
- **collection**: SPARQL∅=1 · manual∅=43 · —=10 · ✓=2
