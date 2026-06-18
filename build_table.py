#!/usr/bin/env python3
"""
Build data/probe_a_gt_vs_received.md: a per-element, per-model table of
ground truth vs the model's Probe A answer, with LLM-judge ✓/✗ verdicts and a
statistics overview at the top.

Reads data/metadata.json (ground truth) + results/raw/<slug>/<id>/A.json.
"""

import csv
import json
import re
from pathlib import Path

MODELS = [("gemini-2.5-pro", "gemini_gemini-2.5-pro"),
          ("gemini-3.5-flash", "gemini_gemini-3.5-flash")]
ELEMENTS = ["artist", "title", "date", "collection"]


def parse_json_answer(text):
    if not text:
        return None
    t = re.sub(r"^```(?:json)?\s*", "", text.strip())
    t = re.sub(r"\s*```$", "", t)
    m = re.search(r"\{.*\}", t, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None


def load(slug, img_id):
    """Return (parsed_answer dict, {element: score}, recognized, status)."""
    p = Path("results/raw") / slug / img_id / "A.json"
    if not p.exists():
        return {}, {}, None, "missing"
    d = json.load(open(p))
    ans = next((t["text"] for t in d["transcript"] if t["role"] == "assistant"), "")
    parsed = parse_json_answer(ans) or {}
    scoring = d.get("scoring", {})
    scores = {}
    if scoring.get("status") == "scored_llm_judge":
        for el, v in scoring.get("elements", {}).items():
            scores[el] = v.get("score")
    recog = parsed.get("recognized", scoring.get("recognized"))
    return parsed, scores, recog, scoring.get("status")


def gt_for(m, el):
    if el == "artist":
        return m.get("artist") or ""
    if el == "title":
        return m.get("title") or ""
    if el == "date":
        return m.get("date") or m.get("date_label") or ""
    if el == "collection":
        return m.get("collection") or ""
    return ""


def mark(s):
    return "✓" if s == 1 else ("✗" if s == 0 else "·")


def pct(n, d):
    return f"{n}/{d} ({100*n/d:.0f}%)" if d else "—"


def main():
    meta = json.load(open("data/metadata.json"))
    rows = list(csv.DictReader(open("data/images.tsv", newline="", encoding="utf-8"),
                               delimiter="\t"))

    # ---- statistics ----
    stats = {}          # slug -> per-element {correct, judged}
    recog_xtab = {}     # slug -> {recog_title_ok, recog_n, unrecog_title_ok, unrecog_n}
    for label, slug in MODELS:
        st = {el: [0, 0] for el in ELEMENTS}  # [correct, judged]
        xt = {"rec_ok": 0, "rec_n": 0, "unrec_ok": 0, "unrec_n": 0}
        for row in rows:
            img_id = row["id"]
            m = meta.get(img_id, {})
            _, scores, recog, _ = load(slug, img_id)
            title_ok = scores.get("title") == 1
            if recog is True:
                xt["rec_n"] += 1
                xt["rec_ok"] += int(title_ok)
            elif recog is False:
                xt["unrec_n"] += 1
                xt["unrec_ok"] += int(title_ok)
            for el in ELEMENTS:
                if not gt_for(m, el):
                    continue
                s = scores.get(el)
                if s in (0, 1):
                    st[el][1] += 1
                    st[el][0] += s
        stats[slug] = st
        recog_xtab[slug] = xt

    out = ["# Probe A — ground truth vs received (per model, per entry)", ""]

    # overview
    out += ["## Overview statistics", "",
            "Probe A asks each model to name the **artist, title, date, and collection** as a "
            "JSON object. Each element is graded 0/1 by an LLM judge "
            "(`gemini-3.5-flash`) against the manually-verified ground truth in "
            "`data/metadata.json` (accepting name/translation variants and overlapping date "
            "ranges). Collection is **low-confidence** — its ground truth is often a historical "
            "owner rather than the current museum.", ""]

    out += ["**Per-element accuracy (judged correct / judged):**", "",
            "| element | " + " | ".join(l for l, _ in MODELS) + " |",
            "|---|" + "---|" * len(MODELS)]
    for el in ELEMENTS:
        flag = " ⚠" if el == "collection" else ""
        cells = [pct(stats[s][el][0], stats[s][el][1]) for _, s in MODELS]
        out.append(f"| {el}{flag} | " + " | ".join(cells) + " |")
    # overall excluding low-confidence collection
    ov = []
    for _, s in MODELS:
        c = sum(stats[s][el][0] for el in ELEMENTS if el != "collection")
        n = sum(stats[s][el][1] for el in ELEMENTS if el != "collection")
        ov.append(pct(c, n))
    out.append(f"| **overall (excl. collection)** | " + " | ".join(ov) + " |")
    out.append("")

    out += ["**Recognition vs. title accuracy** "
            "(does claiming to recognise the work track with getting the subject right?):", "",
            "| | " + " | ".join(l for l, _ in MODELS) + " |",
            "|---|" + "---|" * len(MODELS)]
    out.append("| claimed recognised | "
               + " | ".join(f"{recog_xtab[s]['rec_n']}/56" for _, s in MODELS) + " |")
    out.append("| └ title correct when recognised | "
               + " | ".join(pct(recog_xtab[s]['rec_ok'], recog_xtab[s]['rec_n']) for _, s in MODELS) + " |")
    out.append("| └ title correct when NOT recognised | "
               + " | ".join(pct(recog_xtab[s]['unrec_ok'], recog_xtab[s]['unrec_n']) for _, s in MODELS) + " |")
    out += ["",
            "`·` in the tables below = not yet judged · blank received = model returned "
            "null / unparseable.", ""]

    # ---- per-element tables ----
    for el in ELEMENTS:
        out += [f"## {el.capitalize()}", "",
                "| id | ground truth | gemini-2.5-pro | gemini-3.5-flash |",
                "|---|---|---|---|"]
        for row in rows:
            img_id = row["id"]
            m = meta.get(img_id, {})
            gt = gt_for(m, el)
            if not gt:
                continue
            cells = []
            for _, slug in MODELS:
                parsed, scores, _, _ = load(slug, img_id)
                recv = parsed.get(el)
                recv = "" if recv is None else str(recv)
                cells.append(f"{mark(scores.get(el))} {recv}".strip())
            out.append(f"| {img_id} | {gt} | {cells[0]} | {cells[1]} |")
        out.append("")

    Path("data/probe_a_gt_vs_received.md").write_text("\n".join(out), encoding="utf-8")
    print("Wrote data/probe_a_gt_vs_received.md")


if __name__ == "__main__":
    main()
