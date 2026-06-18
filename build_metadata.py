#!/usr/bin/env python3
"""
Adopt the PI's manually-verified ground truth as the authoritative metadata.

- Writes data/ground_truth_manual.tsv (the manual gold standard, tracked).
- Merges it with the SPARQL-extracted data/metadata.json:
    title, artist, date  -> MANUAL is authoritative
    artist_names         -> manual forms + SPARQL multilingual variants (for judge matching)
    collection           -> manual if present, else SPARQL keeper (SPARQL is richer here)
    collection_uri, subject_uri -> from SPARQL
  Rewrites data/metadata.json with the merged ground truth.
- Writes data/metadata_validation.md: per-field comparison SPARQL vs manual ("the check").
"""

import json
import re
from pathlib import Path

# id, artist, title, date, collection  (manual gold; "" = blank in source)
MANUAL = [
    ("prometheus-chained-vulcan", "Baburen, Dirck van", "Prometheus chained by Vulcan", "1623", "Rijksmuseum"),
    ("aeneas-anchises-troy", "Suavius, Lambert", "Aeneas rescues his father Anchises from the burning Troy", "1550", "Centraal Museum"),
    ("abduction-amphitrite", "Terwesten, Mattheus", "Abduction of Amphitrite by Poseidon", "1685 - 1757", ""),
    ("wedding-peleus-thetis", "Cornelisz. van Haarlem, Cornelis", "The wedding of Peleus and Thetis", "1592-1593", ""),
    ("apollo-pan-midas", "", "The Competition of Apollo and Pan and the judgment of Midas", "c. 1620", ""),
    ("marriage-cupid-psyche", "", "Marriage of Cupid and Psyche", "19th century", ""),
    ("triumph-bacchus", "Mont, Deodat van der", "The triumph of Bacchus", "first half 17th century", ""),
    ("apollo-vulcan-forge", "Maes, Godfried (II)", "Apollo in Vulcan's forge revealing Venus' love-affair with Mars", "1664 - 1700", ""),
    ("triumph-mars", "Nieulandt, Guilliam van (II)", "The triumph of Mars: an Allegory of War", "1627 (dated)", ""),
    ("nausicaa-ulysses", "Lastman, Pieter", "The meeting of Nausicaa and Ulysses", "dated 1619", ""),
    ("meeting-dido-aeneas", "Coignet, Michiel (II)", "The meeting of Dido and Aeneas", "1648 (dated)", ""),
    ("sacrifice-iphigenia", "Wet, Jacob de (I)", "The sacrifice of Iphigenia", "1635 - 1672", ""),
    ("athena-pegasus", "Thulden, Theodoor van", "The goddess Pallas Athena and the horse Pegasus", "1644 (dated)", ""),
    ("dido-sacrifice-juno", "Romanelli, Giovanni Francesco", "Dido's sacrifice to Juno", "1655", ""),
    ("sacrifice-venus-temple", "Rubens, Peter Paul", "Sacrifice to Venus in a temple", "c. 1630", ""),
    ("finding-moses", "", "", "", ""),
    ("abraham-isaac", "", "", "", ""),
    ("potiphar-wife", "Bilivert, Giovanni", "Josephs Keuschheit", "", "Galleria Nazionale d'arte Antica"),
    ("balaam-ass", "Lastman, Pieter", "Balaam and his ass", "dated 1622", ""),
    ("isaac-blesses-jacob", "Horst, Gerrit Willemsz.", "Isaac blessing Jacob", "1638", ""),
    ("samson-pillars", "Rubens, Peter Paul [manner of/after]", "Samson breaks the pillars; the temple of Dagon collapses, killing all that are in it (Judges 16:29-31)", "first half 17th century", ""),
    ("drunkenness-noah", "Floris, Frans (I) [circle of]", "The drunkenness of Noah", "c. 1550-1574", ""),
    ("feast-esther", "Cortona, Pietro da", "Feast of Esther.", "1622-1678", ""),
    ("belshazzar-feast", "", "", "", ""),
    ("bathsheba-letter", "Rubens, Peter Paul [free after]", "Bathsheba receives a letter from David (2 Samuel 11:4)", "after 1635", ""),
    ("gathering-manna", "Bramantino", "The Gathering of Manna.", "1503-1506", ""),
    ("hagar-ishmael", "Cortona, Pietro da", "Hagar, Ishmael and the Angel in the Wilderness.", "1637 - 1638", ""),
    ("prodigal-son-brothel", "Bredael, Peeter van", "The Prodigal Son is being chased from the brotherl after spending all his money (Luke 15:13)", "after 1658", ""),
    ("jephtha-daughter", "Francken, Hieronymus (III)", "Jephtha welcomed by his daughter (Judges 11:29-40)", "1626 - 1661", ""),
    ("judah-tamar", "Hemessen, Jan Sanders van", "Judah's love-affair with Tamar; he gives her his signet-ring (Genesis 38:18)", "second or third quarter 16th century", ""),
    ("diana-actaeon", "Titian", "Diana and Actaeon.", "1559", ""),
    ("jupiter-mercury", "Dossi, Dosso", "Jupiter and Mercury.", "1499-1542", ""),
    ("judgement-midas", "Cima da Conegliano, Giovanni Battista", "The Judgement of Midas.", "1459-1518", ""),
    ("embassy-hippolyta", "Carpaccio, Vittore", "The Embassy of Hippolyta, Queen of the Amazons, to Theseus, King of Athens.", "1475-1525", ""),
    ("jason-dragon", "Roberti, Ercole de'", "Episode from the Legend of the Argonauts: Jason Slaying the Sleepless Dragon.", "1460-1496", ""),
    ("circe-sorceress", "Vassallo, Anton Maria", "The Sorceress Circe.", "1577-1657", ""),
    ("apollo-muses", "Tintoretto", "Apollo and the Muses.", "1532-1594", ""),
    ("rape-deianira", "Pollaiolo, Antonio", "The Rape of Deianira.", "1473", ""),
    ("taking-athens-minos", "Master of the Campana Cassoni", "The Taking of Athens by Minos.", "1515-1519", ""),
    ("flood-deucalion", "Carpioni, Giulio", "A Scene from Greek Mythology: The Flood of the Age of Deucalion.", "1633-1678", ""),
    ("abduction-helen", "Campana, Giacinto", "The Abduction of Helen.", "1600-1650", ""),
    ("lot-daughters", "Guercino", "Lot and His Daughters.", "1611-1666", ""),
    ("joseph-cup-dream", "Carlone, Giovanni Battista", 'Two Scenes in the Life of Joseph: "The Discovery of Joseph\'s Cup in Benjamin\'s Sack" and "Joseph Interpreting Pharaoh\'s Dream".', "1612-1677", ""),
    ("abraham-melchizedek", "Bleker, Gerrit Claesz", "Abraham Meeting Melchizedek.", "1625-1656", ""),
    ("abigail-david", "Cornelisz van Oostsanen, Jacob", "Abigail in Supplication before David.", "1453-1533", ""),
    ("saul-witch-endor", "Cornelisz van Oostsanen, Jacob", "Saul Coming to Consult the Witch of Endor.", "1500", ""),
    ("naaman-syrian", "Engelbrechtszoon, Cornelis", "The Story of the Syrian Captain Naaman.", "1488-1533", ""),
    ("abram-lot-divide", "Zanchi, Antonio", "Abram and Iot Dividing up the World between Them.", "1651-1722", ""),
    ("jeremiah-baruch", "Allston, Washington", "Jeremiah Dictating His Prophecy of the Destruction of Jerusalem to Baruch the Scribe.", "1799-1843", ""),
    ("sennacherib-angel", "Tanzio da Varallo", "The Forces of Sennacherib put to Rout by the Angel.", "1574-1635", ""),
    ("moses-crown-pharaoh", "Tiepolo, Giovanni Battista", "The Child Moses Trampling on the Crown of the Pharoahs.", "1716-1770", ""),
    ("sacrifice-jephthah", "Mazzoni, Sebastiano", "Sacrifice of Jephthah.", "1631-1678", ""),
    ("judgement-solomon", "Cresti, Domenico", "Judgement of Solomon.", "1578-1638", ""),
    ("tobit-tobias", "Preti, Mattia", "Tobit Blessing Tobias.", "1633-1699", ""),
    ("jacob-esau-reconcile", "Cortona, Pietro da", "Reconciliation of Jacob and Esau.", "1616-1669", ""),
    ("elisha-shunem-woman", "Mola, Pier Francesco", "The Prophet Elisha and the Rich Woman of Shunem.", "1648-1650", ""),
]


def artist_variants(raw):
    """From 'Lastname, First [qualifier]' produce useful forms for matching."""
    if not raw:
        return []
    out = [raw]
    base = re.sub(r"\s*\[.*?\]\s*", "", raw).strip()  # drop [manner of/after] etc.
    if base and base not in out:
        out.append(base)
    if "," in base:
        last, first = base.split(",", 1)
        reordered = f"{first.strip()} {last.strip()}".strip()
        if reordered and reordered not in out:
            out.append(reordered)
    return out


def parse_years(date_str):
    """Return (begin, end) 4-digit year strings parsed from a free-text date, or (None, None)."""
    if not date_str:
        return None, None
    yrs = re.findall(r"\b(\d{4})\b", date_str)
    if not yrs:
        return None, None
    return yrs[0], yrs[-1]


def norm(s):
    return re.sub(r"\s+", " ", (s or "").rstrip(".").strip().lower())


def main():
    sparql = json.loads(Path("data/metadata.json").read_text(encoding="utf-8"))

    # 1) tracked manual TSV
    tsv = ["id\tartist\ttitle\tdate\tcollection"]
    for img_id, artist, title, date, coll in MANUAL:
        tsv.append("\t".join([img_id, artist, title, date, coll]))
    Path("data/ground_truth_manual.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")

    # 2) merged ground truth
    merged = {}
    validation = []
    for img_id, m_artist, m_title, m_date, m_coll in MANUAL:
        sp = sparql.get(img_id, {})
        sp_names = sp.get("artist_names") or []
        names = artist_variants(m_artist)
        for n in sp_names:
            if n not in names:
                names.append(n)

        m_begin, m_end = parse_years(m_date)
        date_begin = m_begin or sp.get("date_begin")
        date_end = m_end or sp.get("date_end")

        collection = m_coll or sp.get("collection")

        has_any = any([m_title, names, m_date, collection])
        merged[img_id] = {
            "subject_uri": sp.get("subject_uri"),
            "title": m_title or None,
            "artist": m_artist or None,
            "artist_names": names,
            "date": m_date or None,
            "date_begin": date_begin,
            "date_end": date_end,
            "date_label": m_date or sp.get("date_label"),
            "collection": collection,
            "collection_uri": sp.get("collection_uri"),
            "collection_source": "manual" if m_coll else ("sparql" if sp.get("collection") else None),
            "status": "ok" if has_any else "no_source",
            "ground_truth_source": "manual (artist/title/date) + sparql (collection/variants)",
        }

        # 3) validation: SPARQL vs manual per field
        sp_artist = sp_names[0] if sp_names else ""
        sp_title = sp.get("title") or ""
        sp_date = sp.get("date_label") or (sp.get("date_begin") or "")
        sp_coll = sp.get("collection") or ""

        def cmp(manual, sparql_v):
            if not manual and not sparql_v:
                return "—"
            if not sparql_v:
                return "SPARQL∅"
            if not manual:
                return "manual∅"
            return "✓" if (norm(manual) in norm(sparql_v) or norm(sparql_v) in norm(manual)
                           or norm(manual) == norm(sparql_v)) else "≠"

        validation.append((
            img_id,
            cmp(m_artist, sp_artist), m_artist, sp_artist,
            cmp(m_title, sp_title),
            cmp(m_date, sp_date), m_date, sp_date,
            cmp(m_coll, sp_coll),
        ))

    Path("data/metadata.json").write_text(
        json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")

    # 4) validation report
    lines = [
        "# Ground-truth validation — SPARQL vs manual",
        "",
        "Per-field check of the SPARQL auto-extraction against the PI's manual gold standard. "
        "`✓` agree · `≠` differ · `SPARQL∅` SPARQL missed it (manual has it) · "
        "`manual∅` manual blank (SPARQL has it) · `—` both blank.",
        "",
        "data/metadata.json now uses **manual** for artist/title/date and SPARQL for "
        "collection + multilingual name variants.",
        "",
        "| id | artist | manual artist | SPARQL artist | title | date | manual date | SPARQL date | collection |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    counts = {"artist": {}, "title": {}, "date": {}, "collection": {}}
    for (img_id, a_c, m_a, sp_a, t_c, d_c, m_d, sp_d, c_c) in validation:
        counts["artist"][a_c] = counts["artist"].get(a_c, 0) + 1
        counts["title"][t_c] = counts["title"].get(t_c, 0) + 1
        counts["date"][d_c] = counts["date"].get(d_c, 0) + 1
        counts["collection"][c_c] = counts["collection"].get(c_c, 0) + 1
        lines.append(f"| {img_id} | {a_c} | {m_a} | {sp_a} | {t_c} | {d_c} | {m_d} | {sp_d} | {c_c} |")
    lines += ["", "---", "", "**Field agreement tallies:**", ""]
    for fld in ("artist", "title", "date", "collection"):
        tally = " · ".join(f"{k}={v}" for k, v in sorted(counts[fld].items()))
        lines.append(f"- **{fld}**: {tally}")
    lines.append("")
    Path("data/metadata_validation.md").write_text("\n".join(lines), encoding="utf-8")

    n_ok = sum(1 for v in merged.values() if v["status"] == "ok")
    print(f"Wrote data/ground_truth_manual.tsv ({len(MANUAL)} rows)")
    print(f"Rewrote data/metadata.json (merged; {n_ok}/{len(merged)} with ground truth)")
    print("Wrote data/metadata_validation.md")


if __name__ == "__main__":
    main()
