# Probe A — per-element correctness (LLM-judge)

Judge: `gemini:gemini-3.5-flash`. Ground truth: `data/metadata.json`. Each element scored 0/1. **collection is low-confidence** (institutional keeper is often a historical owner, not the current museum).

## `gemini_gemini-2.5-pro`

| id | recognized | artist | title | date | collection ⚠ | total |
|---|---|---|---|---|---|---|
| abduction-amphitrite | True | ✗ | ✗ | ✗ | ✗ | 0/4 |
| abduction-helen | True | ✗ | ✓ | ✗ | ✗ | 1/4 |
| abigail-david | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| abraham-isaac | True | · | · | · | · | 0/0 |
| abraham-melchizedek | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| abram-lot-divide | True | ✓ | ✗ | ✓ | ✗ | 2/4 |
| aeneas-anchises-troy | True | ✗ | ✗ | ✗ | ✗ | 0/4 |
| apollo-muses | True | ✗ | ✗ | ✗ | ✗ | 0/4 |
| apollo-pan-midas | True | · | ✓ | ✗ | ✗ | 1/3 |
| apollo-vulcan-forge | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| athena-pegasus | True | ✗ | ✓ | ✓ | ✗ | 2/3 |
| balaam-ass | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| bathsheba-letter | True | ✗ | ✗ | ✓ | · | 1/3 |
| belshazzar-feast | True | · | · | · | · | 0/0 |
| circe-sorceress | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| diana-actaeon | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| dido-sacrifice-juno | True | ✗ | ✓ | ✓ | ✗ | 2/3 |
| drunkenness-noah | True | ✗ | ✓ | ✓ | · | 2/3 |
| elisha-shunem-woman | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| embassy-hippolyta | True | ✗ | ✗ | ✗ | ✗ | 0/4 |
| feast-esther | True | ✗ | ✓ | ✓ | ✓ | 3/4 |
| finding-moses | False | · | · | · | · | 0/0 |
| flood-deucalion | True | ✗ | ✓ | ✗ | ✗ | 1/4 |
| gathering-manna | True | ✗ | ✓ | ✗ | ✗ | 1/4 |
| hagar-ishmael | True | ✗ | ✓ | ✗ | ✗ | 1/4 |
| isaac-blesses-jacob | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| jacob-esau-reconcile | True | ✓ | ✗ | ✓ | ✓ | 3/4 |
| jason-dragon | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| jephtha-daughter | True | ✗ | ✓ | ✓ | · | 2/3 |
| jeremiah-baruch | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| joseph-cup-dream | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| judah-tamar | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| judgement-midas | True | ✓ | ✓ | ✓ | ✗ | 3/4 |
| judgement-solomon | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| jupiter-mercury | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| lot-daughters | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| marriage-cupid-psyche | True | · | ✓ | ✗ | ✗ | 1/3 |
| meeting-dido-aeneas | True | ✗ | ✓ | ✗ | · | 1/3 |
| moses-crown-pharaoh | True | ✓ | ✗ | ✓ | ✗ | 2/4 |
| naaman-syrian | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| nausicaa-ulysses | True | ✗ | ✗ | ✗ | ✗ | 0/3 |
| potiphar-wife | True | ✓ | ✓ | · | ✓ | 3/3 |
| prodigal-son-brothel | True | ✗ | ✗ | ✗ | · | 0/3 |
| prometheus-chained-vulcan | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| rape-deianira | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| sacrifice-iphigenia | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| sacrifice-jephthah | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| sacrifice-venus-temple | True | ✓ | ✓ | ✗ | ✗ | 2/4 |
| samson-pillars | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| saul-witch-endor | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| sennacherib-angel | True | ✗ | ✓ | ✓ | ✓ | 3/4 |
| taking-athens-minos | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| tobit-tobias | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| triumph-bacchus | True | ✗ | ✓ | ✓ | · | 2/3 |
| triumph-mars | True | ✓ | ✗ | ✗ | ✓ | 2/4 |
| wedding-peleus-thetis | True | ✗ | ✓ | ✗ | ✗ | 1/4 |

**Total: 93/200 elements correct**

## `gemini_gemini-3.5-flash`

| id | recognized | artist | title | date | collection ⚠ | total |
|---|---|---|---|---|---|---|
| abduction-amphitrite | True | ✗ | ✗ | ✗ | ✗ | 0/4 |
| abduction-helen | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| abigail-david | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| abraham-isaac | True | · | · | · | · | 0/0 |
| abraham-melchizedek | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| abram-lot-divide | True | ✓ | ✗ | ✓ | ✗ | 2/3 |
| aeneas-anchises-troy | True | ✗ | ✗ | ✗ | ✗ | 0/3 |
| apollo-muses | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| apollo-pan-midas | True | · | ✓ | ✗ | ✗ | 1/3 |
| apollo-vulcan-forge | — | — | — | — | — | _parse_error_ |
| athena-pegasus | True | ✓ | ✓ | ✗ | ✗ | 2/4 |
| balaam-ass | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| bathsheba-letter | True | ✗ | ✓ | ✗ | · | 1/3 |
| belshazzar-feast | True | · | · | · | · | 0/0 |
| circe-sorceress | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| diana-actaeon | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| dido-sacrifice-juno | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| drunkenness-noah | True | ✗ | ✓ | ✗ | · | 1/3 |
| elisha-shunem-woman | True | ✗ | ✗ | ✗ | ✗ | 0/4 |
| embassy-hippolyta | True | ✗ | ✗ | ✗ | ✗ | 0/3 |
| feast-esther | True | ✗ | ✓ | ✓ | ✓ | 3/4 |
| finding-moses | True | · | · | · | · | 0/0 |
| flood-deucalion | True | ✗ | ✓ | ✗ | ✗ | 1/4 |
| gathering-manna | True | ✗ | ✓ | ✗ | ✗ | 1/4 |
| hagar-ishmael | True | ✗ | ✓ | ✗ | ✗ | 1/4 |
| isaac-blesses-jacob | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| jacob-esau-reconcile | True | ✗ | ✓ | ✓ | ✓ | 3/4 |
| jason-dragon | True | ✗ | ✗ | ✓ | ✗ | 1/3 |
| jephtha-daughter | True | ✗ | ✓ | ✓ | · | 2/3 |
| jeremiah-baruch | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| joseph-cup-dream | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| judah-tamar | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| judgement-midas | True | ✓ | ✓ | ✓ | ✗ | 3/4 |
| judgement-solomon | True | ✗ | ✓ | ✓ | ✓ | 3/4 |
| jupiter-mercury | True | ✓ | ✓ | ✓ | ✗ | 3/4 |
| lot-daughters | True | ✓ | ✓ | ✓ | ✗ | 3/4 |
| marriage-cupid-psyche | True | · | ✓ | ✗ | ✗ | 1/3 |
| meeting-dido-aeneas | True | ✗ | ✓ | ✗ | · | 1/3 |
| moses-crown-pharaoh | True | ✓ | ✗ | ✓ | ✗ | 2/4 |
| naaman-syrian | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| nausicaa-ulysses | True | ✗ | ✗ | ✗ | ✗ | 0/4 |
| potiphar-wife | True | ✓ | ✓ | · | ✓ | 3/3 |
| prodigal-son-brothel | True | ✗ | ✗ | ✗ | · | 0/3 |
| prometheus-chained-vulcan | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| rape-deianira | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| sacrifice-iphigenia | True | ✗ | ✓ | ✗ | ✗ | 1/4 |
| sacrifice-jephthah | True | ✗ | ✗ | ✗ | ✗ | 0/4 |
| sacrifice-venus-temple | True | ✓ | ✗ | ✗ | ✗ | 1/4 |
| samson-pillars | True | ✗ | ✓ | ✓ | ✗ | 2/4 |
| saul-witch-endor | True | ✗ | ✗ | ✓ | ✗ | 1/4 |
| sennacherib-angel | True | ✓ | ✓ | ✓ | ✓ | 4/4 |
| taking-athens-minos | False | ✗ | ✗ | ✗ | ✗ | 0/0 |
| tobit-tobias | True | ✗ | ✗ | ✓ | ✗ | 1/3 |
| triumph-bacchus | True | ✗ | ✓ | ✓ | · | 2/3 |
| triumph-mars | True | ✓ | ✗ | ✗ | ✓ | 2/4 |
| wedding-peleus-thetis | True | ✗ | ✓ | ✗ | ✗ | 1/4 |

**Total: 88/190 elements correct**
