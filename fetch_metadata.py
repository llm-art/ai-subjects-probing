#!/usr/bin/env python3
"""
Fetch full ground-truth metadata (title, artist, date, collection) from the
artresearch.net SPARQL endpoint for every image in data/images.tsv.

Writes two files:
  - data/metadata.json       machine-readable ground truth keyed by image id
                             (consumed by score_probe_a.py)
  - data/metadata_check.md   human-readable title-vs-subject comparison

Subject-URI resolution:
  - Frick/Zeri/Pharos: the artresearch source_url is itself the RDF subject.
  - RKD: source_url is a proxy of the form
      https://artresearch.net/resource/?uri=https%3A%2F%2Fdata.rkd.nl%2Fimages%2F<id>
    The real RDF subject is the decoded `uri` param (https://data.rkd.nl/images/<id>);
    querying the proxy URL returns nothing.
"""

import csv
import json
import re
import time
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import requests

SPARQL = "https://artresearch.net/sparql"
HEADERS = {
    "Accept": "application/sparql-results+json",
    "User-Agent": "ai-subjects-probing/1.0",
}
TIMEOUT = 20
SLEEP = 0.3

CRM = "PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>"

TITLE_Q = CRM + """
SELECT ?title WHERE {{
  <{uri}> crm:P1_is_identified_by ?app .
  FILTER(CONTAINS(STR(?app), "title"))
  ?app crm:P190_has_symbolic_content ?title .
}} LIMIT 1
"""

ARTIST_ULAN_Q = CRM + """
SELECT ?artist WHERE {{
  <{uri}> crm:P108i_was_produced_by ?prod .
  ?prod crm:P14_carried_out_by ?artist .
}} LIMIT 1
"""

ARTIST_NAMES_Q = CRM + """
SELECT ?name WHERE {{
  <{uri}> crm:P1_is_identified_by ?ap .
  ?ap crm:P190_has_symbolic_content ?name .
}}
"""

DATE_Q = CRM + """
SELECT ?begin ?end ?label WHERE {{
  <{uri}> crm:P108i_was_produced_by ?prod .
  ?prod crm:P4_has_time-span ?ts .
  OPTIONAL {{ ?ts crm:P82a_begin_of_the_begin ?begin }}
  OPTIONAL {{ ?ts crm:P82b_end_of_the_end ?end }}
  OPTIONAL {{ ?ts crm:P1_is_identified_by ?ta . ?ta crm:P190_has_symbolic_content ?label }}
}} LIMIT 1
"""

COLLECTION_Q = CRM + """
SELECT ?keeper ?label WHERE {{
  <{uri}> crm:P50_has_current_keeper ?keeper .
  OPTIONAL {{ ?keeper crm:P1_is_identified_by ?ka . ?ka crm:P190_has_symbolic_content ?label }}
}} LIMIT 1
"""


def sparql(q):
    """Return list of binding dicts, or 'TIMEOUT'/'ERROR: ...' on failure."""
    try:
        r = requests.get(SPARQL, params={"query": q}, headers=HEADERS, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()["results"]["bindings"]
    except requests.exceptions.Timeout:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e}"


def first_value(bindings, var):
    if isinstance(bindings, list) and bindings:
        b = bindings[0]
        if var in b:
            return b[var]["value"]
    return None


def resolve_subject(source_url):
    """Map a TSV source_url to the RDF subject URI (or None)."""
    if not source_url:
        return None
    if "artresearch.net/resource/?uri=" in source_url:
        qs = parse_qs(urlparse(source_url).query)
        uri = qs.get("uri", [None])[0]
        return uri  # decoded data.rkd.nl/... subject
    if "artresearch.net/resource" in source_url:
        return source_url
    return None


def year_of(iso):
    if not iso:
        return None
    m = re.match(r"(-?\d{1,4})", iso)
    return m.group(1) if m else None


def fetch_one(subject):
    """Run all queries for one subject URI; return a metadata dict."""
    meta = {
        "subject_uri": subject,
        "title": None,
        "artist_ulan": None,
        "artist_names": [],
        "date_begin": None,
        "date_end": None,
        "date_label": None,
        "collection": None,
        "collection_uri": None,
        "status": "ok",
    }

    title_b = sparql(TITLE_Q.format(uri=subject))
    time.sleep(SLEEP)
    if isinstance(title_b, str):
        meta["status"] = title_b
        return meta
    meta["title"] = first_value(title_b, "title")

    ulan_b = sparql(ARTIST_ULAN_Q.format(uri=subject))
    time.sleep(SLEEP)
    if isinstance(ulan_b, list):
        ulan = first_value(ulan_b, "artist")
        meta["artist_ulan"] = ulan
        if ulan:
            names_b = sparql(ARTIST_NAMES_Q.format(uri=ulan))
            time.sleep(SLEEP)
            if isinstance(names_b, list):
                seen = []
                for b in names_b:
                    v = b.get("name", {}).get("value")
                    if v and v not in seen:
                        seen.append(v)
                meta["artist_names"] = seen

    date_b = sparql(DATE_Q.format(uri=subject))
    time.sleep(SLEEP)
    if isinstance(date_b, list):
        meta["date_begin"] = year_of(first_value(date_b, "begin"))
        meta["date_end"] = year_of(first_value(date_b, "end"))
        meta["date_label"] = first_value(date_b, "label")

    coll_b = sparql(COLLECTION_Q.format(uri=subject))
    time.sleep(SLEEP)
    if isinstance(coll_b, list):
        meta["collection_uri"] = first_value(coll_b, "keeper")
        meta["collection"] = first_value(coll_b, "label")

    if not any([meta["title"], meta["artist_ulan"], meta["date_begin"], meta["collection"]]):
        meta["status"] = "no_data"
    return meta


# ---- title-vs-subject comparison (for the human markdown report) ----

def normalise(s):
    return re.sub(r"\s+", " ", s.rstrip(".").strip().lower())


def match_label(our, theirs):
    if not theirs:
        return "NO_DATA"
    a, b = normalise(our), normalise(theirs)
    if a == b:
        return "MATCH"
    if a in b or b in a:
        return "PARTIAL"
    stop = {"the", "a", "an", "of", "and", "in", "to", "by", "his", "her", "its"}
    wa = set(a.split()) - stop
    wb = set(b.split()) - stop
    if wa and wb and len(wa & wb) / max(len(wa), len(wb)) >= 0.5:
        return "PARTIAL"
    return "MISMATCH"


def main():
    rows = []
    with open("data/images.tsv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    metadata = {}
    report = []
    for row in rows:
        img_id = row["id"]
        subject = row["subject"]
        rdf_subject = resolve_subject(row.get("source_url", "").strip())

        if not rdf_subject:
            metadata[img_id] = {"subject_uri": None, "status": "no_source"}
            report.append((img_id, subject, "N/A (no source URI)", "", "N/A"))
            print(f"SKIP {img_id}: no resolvable RDF subject")
            continue

        print(f"Querying {img_id} <{rdf_subject}> ...", end=" ", flush=True)
        meta = fetch_one(rdf_subject)
        metadata[img_id] = meta
        m = match_label(subject, meta.get("title"))
        artist = meta["artist_names"][0] if meta.get("artist_names") else (meta.get("artist_ulan") or "")
        report.append((img_id, subject, meta.get("title") or "", artist, m))
        print(f"{meta['status']} | title={meta.get('title')!r} artist={artist!r} "
              f"date={meta.get('date_label') or meta.get('date_begin')!r}")

    Path("data/metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGround truth written to data/metadata.json ({len(metadata)} images)")

    # human-readable comparison
    lines = [
        "# Metadata check",
        "",
        "Full ground truth from artresearch.net SPARQL (machine-readable copy in "
        "`data/metadata.json`). Title vs our subject label compared below.",
        "",
        "Match codes: **MATCH** · **PARTIAL** · **MISMATCH** · **NO_DATA** · **N/A** (no source URI)",
        "",
        "| id | our subject | institutional title | artist | match |",
        "|---|---|---|---|---|",
    ]
    for img_id, subject, title, artist, m in report:
        lines.append(f"| {img_id} | {subject} | {title} | {artist} | **{m}** |")

    counts = {}
    for *_, m in report:
        counts[m] = counts.get(m, 0) + 1
    lines += ["", "---", "",
              "**Summary:** " + " · ".join(f"{k}={v}" for k, v in sorted(counts.items())), ""]
    mismatches = [(i, s, t) for i, s, t, _, m in report if m == "MISMATCH"]
    if mismatches:
        lines += ["## Mismatches — review needed", ""]
        for i, s, t in mismatches:
            lines.append(f"- **{i}**: our `{s}` vs institutional `{t}`")
        lines.append("")
    Path("data/metadata_check.md").write_text("\n".join(lines), encoding="utf-8")
    print("Comparison written to data/metadata_check.md")


if __name__ == "__main__":
    main()
