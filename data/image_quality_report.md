# Image quality report

Generated: 2026-06-11

## Summary

| Metric | Value |
|--------|-------|
| Total images in dataset | 30 |
| Successfully downloaded | 30 |
| Failed | 0 |
| Low-res (< 1 Mpx) | 0 |
| Mid-res (1–10 Mpx) | 13 |
| Hi-res (≥ 10 Mpx) | 17 |
| Largest image | 42.54 Mpx (potiphar-wife, Hertziana, 7367×5774) |
| Assembled from tiles | 2 (feast-esther, gathering-manna — Frick via artresearch) |

## Failed downloads

None. The three previously failing sources were replaced on 2026-06-11:

| id | replacement | new source |
|----|-------------|-----------|
| finding-moses | replaces `moses-law-sinai` (Warburg 503) — **different subject**: The finding of Moses | hertziana |
| abraham-isaac | same subject, Warburg 503 → Zeri copy | zeri (via iiif.artresearch.net) |
| belshazzar-feast | same subject, MFA WAF-blocked → RKD copy | rkd |

The subject swap is propagated to `probes/probes.json` (subject list,
forced-choice prompt, B_enriched description key).

---

## Full image inventory

### Mythology (15 images)

| id | dimensions (px) | Mpx | file size | aspect ratio | tiled | source |
|----|----------------|-----|-----------|--------------|-------|--------|
| aeneas-anchises-troy ⚠ Tier A | 1878 × 1239 | 2.33 | 573.9 KB | 626:413 | no | rkd |
| apollo-pan-midas | 2164 × 1812 | 3.92 | 439 KB | 541:453 | no | rkd |
| marriage-cupid-psyche | 3079 × 2063 | 6.35 | 780.6 KB | 3079:2063 | no | rkd |
| triumph-bacchus | 2912 × 1367 | 3.98 | 584.9 KB | 2912:1367 | no | rkd |
| apollo-vulcan-forge | 2808 × 2132 | 5.99 | 664.3 KB | 54:41 | no | rkd |
| triumph-mars | 2506 × 1909 | 4.78 | 687.3 KB | 2506:1909 | no | rkd |
| meeting-dido-aeneas | 2520 × 1832 | 4.62 | 748.0 KB | 315:229 | no | rkd |
| sacrifice-iphigenia | 2374 × 1731 | 4.11 | 347.8 KB | 2374:1731 | no | rkd |
| prometheus-chained-vulcan | 3703 × 4096 | 15.17 | 3.4 MB | 3703:4096 | no | rkd |
| wedding-peleus-thetis | 4129 × 2848 | 11.76 | 2.4 MB | 4129:2848 | no | rkd |
| nausicaa-ulysses | 4552 × 2999 | 13.65 | 3.2 MB | 4552:2999 | no | rkd |
| sacrifice-venus-temple | 4122 × 3854 | 15.89 | 1.6 MB | 2061:1927 | no | rkd |
| abduction-amphitrite | 5507 × 4499 | 24.78 | 4.5 MB | 5507:4499 | no | rkd |
| dido-sacrifice-juno | 5521 × 3924 | 21.66 | 1.6 MB | 5521:3924 | no | rkd |
| athena-pegasus | 5698 × 4317 | 24.60 | 4.6 MB | 5698:4317 | no | rkd |

### Old Testament (15 images)

| id | dimensions (px) | Mpx | file size | aspect ratio | tiled | source |
|----|----------------|-----|-----------|--------------|-------|--------|
| balaam-ass | 2743 × 3735 | 10.24 | 1.7 MB | 2743:3735 | no | rkd |
| samson-pillars | 3072 × 2286 | 7.02 | 1.3 MB | 512:381 | no | zeri |
| drunkenness-noah | 2048 × 1584 | 3.24 | 547 KB | 128:99 | no | rkd |
| bathsheba-letter | 2104 × 1650 | 3.47 | 904.3 KB | 1052:825 | no | rkd |
| hagar-ishmael | 3072 × 2356 | 7.24 | 877.2 KB | 768:589 | no | zeri |
| prodigal-son-brothel | 3124 × 2421 | 7.56 | 1.1 MB | 3124:2421 | no | rkd |
| judah-tamar | 3308 × 2512 | 8.31 | 1.1 MB | 827:628 | no | rkd |
| isaac-blesses-jacob | 4888 × 3906 | 19.09 | 3.0 MB | 2444:1953 | no | rkd |
| gathering-manna | 5628 × 3578 | 20.14 | 3.2 MB | 2814:1789 | yes (3×2) | frick |
| feast-esther | 5821 × 3526 | 20.52 | 1.7 MB | 5821:3526 | yes (3×2) | frick |
| jephtha-daughter | 5782 × 4204 | 24.31 | 4.1 MB | 2891:2102 | no | rkd |
| potiphar-wife | 7367 × 5774 | 42.54 | 6.6 MB | 7367:5774 | no | hertziana |
| finding-moses | 7176 × 5659 | 40.61 | 7.7 MB | 7176:5659 | no | hertziana |
| abraham-isaac | 2365 × 3072 | 7.27 | 1.0 MB | 2365:3072 | no | zeri |
| belshazzar-feast | 2154 × 1474 | 3.17 | 0.5 MB | 1077:737 | no | rkd |

---

## Key findings

### Resolution history across runs

| | Run 1 | Run 2 | Run 3 | Run 4 (current) |
|---|---|---|---|---|
| Low-res (< 1 Mpx) | 10 | 4 | 1 | **0** |
| Mid-res (1–10 Mpx) | 10 | 10 | 10 | 11 |
| Hi-res (≥ 10 Mpx) | 7 | 13 | 16 | 16 |

### Remaining low-res images

None. All 30 downloaded images are above 1 Mpx.

### Tier A calibration image

`aeneas-anchises-troy` is now at 1878×1239 px (2.33 Mpx), up from 0.18 Mpx.
This is sufficient for all probe variants including Probe C detail questions.
The low-resolution confound noted in the previous report is resolved.

### Tiled assembly

Two Frick images served via `iiif.artresearch.net` enforced a `maxArea` cap
below their native size and were assembled from tiles automatically:

| id | native | tiles |
|----|--------|-------|
| feast-esther | 5821 × 3526 | 3×2 grid |
| gathering-manna | 5628 × 3578 | 3×2 grid |

Both are confirmed at full native resolution in the downloaded files.

---

## Remediation checklist

- [x] aeneas-anchises-troy — resolved (now 2.33 Mpx)
- [x] prometheus-chained-vulcan — resolved (now 15.17 Mpx)
- [x] abduction-amphitrite — resolved (now 24.78 Mpx)
- [x] wedding-peleus-thetis — resolved (now 11.76 Mpx)
- [x] nausicaa-ulysses — resolved (now 13.65 Mpx)
- [x] athena-pegasus — resolved (now 24.60 Mpx)
- [x] sacrifice-venus-temple — resolved (now 15.89 Mpx)
- [x] apollo-pan-midas — resolved (now 3.92 Mpx, 2164×1812)
- [x] balaam-ass — resolved (now 10.24 Mpx, 2743×3735)
- [x] samson-pillars — resolved (now 7.02 Mpx, 3072×2286, via Zeri)
- [x] drunkenness-noah — resolved (now 3.24 Mpx, 2048×1584)
- [x] moses-law-sinai — replaced by `finding-moses` (different subject, Hertziana, 40.61 Mpx)
- [x] abraham-isaac — resolved via Zeri copy (7.27 Mpx)
- [x] belshazzar-feast — resolved via RKD copy (3.17 Mpx)
