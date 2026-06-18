# Probe A vs institutional metadata — Frick/artresearch images

Cross-check: did Gemini-2.5-Pro's Probe A (recognition) correctly identify the institutional title?

| id | ground-truth subject | institutional title | A recognised? | B_plain correct? |
|---|---|---|---|---|
| potiphar-wife | Potiphar's wife catches Joseph by his robe; Joseph escapes l | Josephs Keuschheit | **NO** | **NO** |
| feast-esther | Feast of Esther | Feast of Esther. | **YES** | **YES** |
| gathering-manna | The Gathering of Manna | The Gathering of Manna. | **YES** | **YES** |
| diana-actaeon | Diana and Actaeon | Diana and Actaeon. | **YES** | **YES** |
| jupiter-mercury | Jupiter and Mercury | Jupiter and Mercury. | **YES** | **YES** |
| judgement-midas | The Judgement of Midas | The Judgement of Midas. | **PARTIAL** | **PARTIAL** |
| embassy-hippolyta | The Embassy of Hippolyta Queen of the Amazons to Theseus Kin | The Embassy of Hippolyta, Queen of the Amazons, to Theseus,  | **NO** | **NO** |
| jason-dragon | Episode from the Legend of the Argonauts: Jason Slaying the  | Episode from the Legend of the Argonauts: Jason Slaying the  | **NO** | **NO** |
| circe-sorceress | The Sorceress Circe | The Sorceress Circe. | **YES** | **YES** |
| apollo-muses | Apollo and the Muses | Apollo and the Muses. | **YES** | **YES** |
| rape-deianira | The Rape of Deianira | The Rape of Deianira. | **YES** | **YES** |
| taking-athens-minos | The Taking of Athens by Minos | The Taking of Athens by Minos. | **NO** | **NO** |
| flood-deucalion | A Scene from Greek Mythology: The Flood of the Age of Deucal | A Scene from Greek Mythology: The Flood of the Age of Deucal | **YES** | **YES** |
| abduction-helen | The Abduction of Helen | The Abduction of Helen. | **YES** | **YES** |
| lot-daughters | Lot and His Daughters | Lot and His Daughters. | **YES** | **YES** |
| joseph-cup-dream | Two Scenes in the Life of Joseph: The Discovery of Joseph's  | Two Scenes in the Life of Joseph: "The Discovery of Joseph's | **PARTIAL** | **NO** |
| abraham-melchizedek | Abraham Meeting Melchizedek | Abraham Meeting Melchizedek. | **YES** | **YES** |
| abigail-david | Abigail in Supplication before David | Abigail in Supplication before David. | **PARTIAL** | **PARTIAL** |
| saul-witch-endor | Saul Coming to Consult the Witch of Endor | Saul Coming to Consult the Witch of Endor. | **YES** | **NO** |
| naaman-syrian | The Story of the Syrian Captain Naaman | The Story of the Syrian Captain Naaman. | **NO** | **NO** |
| abram-lot-divide | Abram and Lot Dividing up the World between Them | Abram and Iot Dividing up the World between Them. | **NO** | **NO** |
| jeremiah-baruch | Jeremiah Dictating His Prophecy of the Destruction of Jerusa | Jeremiah Dictating His Prophecy of the Destruction of Jerusa | **YES** | **NO** |
| sennacherib-angel | The Forces of Sennacherib put to Rout by the Angel | The Forces of Sennacherib put to Rout by the Angel. | **NO** | **PARTIAL** |
| moses-crown-pharaoh | The Child Moses Trampling on the Crown of the Pharaohs | The Child Moses Trampling on the Crown of the Pharoahs. | **NO** | **NO** |
| sacrifice-jephthah | Sacrifice of Jephthah | Sacrifice of Jephthah. | **NO** | **NO** |
| judgement-solomon | Judgement of Solomon | Judgement of Solomon. | **PARTIAL** | **PARTIAL** |
| tobit-tobias | Tobit Blessing Tobias | Tobit Blessing Tobias. | **PARTIAL** | **YES** |
| jacob-esau-reconcile | Reconciliation of Jacob and Esau | Reconciliation of Jacob and Esau. | **NO** | **NO** |
| elisha-shunem-woman | The Prophet Elisha and the Rich Woman of Shunem | The Prophet Elisha and the Rich Woman of Shunem. | **NO** | **NO** |

---

**A recognised** = Probe A response mentions the institutional title (contamination indicator).
**B_plain correct** = B_plain response mentions key words of the ground-truth subject.