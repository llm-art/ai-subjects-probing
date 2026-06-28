# Probe A metadata evaluation site

Static, front-end-only viewer (GitHub Pages) for human assessment of **Probe A**
recognition metadata — `title`, `artist`, `date`, `collection` — per image per
model. Ground truth is shown on the left; each model's answers field-by-field on
the right, so a human can eyeball correctness at single-field granularity.

It is **one self-contained HTML page per image** (all data inlined — no
`fetch`), so it works opened directly from disk (`file://`) *and* on GitHub
Pages. A sticky header on every page (‹ prev / jump dropdown / next ›) links the
pages together; `index.html` is a thumbnail contact sheet.

The site does **not** record verdicts. Verdicts go into a Google Sheet imported
from the prefilled CSV (see below).

## Files

- `index.html` — contact-sheet landing page (generated).
- `<image_id>.html` — one self-contained page per image (generated).
- `style.css` — shared styles (authored; not generated).
- `probe_a_verdicts_prefilled.csv` — one row per image × model × field, every
  `verdict` prefilled `correct` (generated).

The HTML pages and the CSV are **generated** — do not hand-edit. Regenerate with:

```bash
python build_eval_site.py          # reads data/ + results/raw/, writes docs/
```

(`results/raw/**` is gitignored, so the build inlines those answers into the
committed pages. Rerun the build whenever new probe results land.)

## View it

- **Locally:** open `docs/index.html` in a browser, or
  `python -m http.server -d docs 8000` → http://localhost:8000.
- **GitHub Pages:** repo **Settings → Pages → Source: Deploy from a branch**,
  branch `main`, folder `/docs`. Served at `https://<user>.github.io/<repo>/`.

## Verdict workflow

1. Open the CSV in a Google Sheet (**File → Import → Upload →
   `probe_a_verdicts_prefilled.csv`**, "Replace spreadsheet").
2. Use the site to compare each model answer against ground truth.
3. Every row starts `correct`; change the `verdict` cell to `incorrect` (or
   whatever scale you adopt) only for wrong answers, and add `notes` as needed.
