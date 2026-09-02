# Accessibility Audit Log

Tracking WCAG 2.1 AA spot-checks and fixes against the ADA Title II rule
(applies to this site as a public school resource; compliance deadline
April 24, 2026 for districts serving 50,000+ population).

Status values: `ok`, `fixed`, `needs-fix`, `not-checked`.

## File status

| File | Status | Notes |
|---|---|---|
| `notebook-viewer.html` | fixed | Added `lang="en"`, viewport meta tag, and `alt` text on generated plot images (previously bare `<img>` with no alt). |
| `_includes/nb.html` | ok | Disclosure widget already uses `aria-expanded`/`aria-haspopup` correctly. |
| `assets/js/notebook-links.js` | ok | Keyboard support (Escape to close, focus return), focusin/focusout handling all present. |
| `_includes/head/custom.html` | fixed | Added `loader: {load: ['a11y/explorer']}` to MathJax config for speech-text/keyboard math exploration. Should be spot-checked with a real screen reader. |
| `_includes/footer/custom.html` | ok | Static ad placement div only, nothing to check. |
| `index.md`, `notebooks/02-regression-correlation/index.md` | fixed | Linear regression derivation link now points to the accessible `.md`/HTML page as primary, with the PDF offered as a secondary `(PDF)` download. |
| `_data/navigation.yml` | ok | Structured data only, no markup to check directly (theme renders it). |
| `assets/css/main.scss` | ok | Only override is link color `#1a6bb0` on white — contrast ratio ~5.6:1, passes AA. |
| `patch.md`, `setup.md`, `bayes-practice.md` | ok | Plain markdown, no raw HTML/images/tables to check. |
| `statistics.html` | fixed | Decorative icon spans and redundant SVG charts marked `aria-hidden="true"`/`focusable="false"`; `.subtitle` color darkened from `#7f8c8d` to `#5f6c72` (now passes 4.5:1); added `scope="col"` to comparison table headers. |

## Not yet checked

- `_layouts/` (if any custom layouts exist beyond the theme defaults)
- Unit `index.md` pages for units 4–12 under `notebooks/*/`
- Sidebar nav markup rendered by the theme — keyboard nav and focus order
- Any custom Jekyll theme overrides under `_includes/`/`_layouts/` not listed above

## Unit index pages (1–3) + main calendar — fixed

| File | Status | Notes |
|---|---|---|
| `index.md` (main calendar) | fixed | Replaced blank-header `| | |` info table with a plain list (screen readers were announcing unlabeled table headers); reworded two ambiguous "here" links to descriptive link text (WCAG 2.4.4). |
| `notebooks/01-foundations/index.md` | fixed | Reworded a "here" link to descriptive text; fixed two stacked bold PDF links that ran together as one paragraph in Markdown, now a proper list with explicit `(PDF)` labels. Note: `bayes-notes.pdf` still has no accessible `.md`/HTML twin (see PDF section below) — labeling only clarifies link purpose, doesn't fix the underlying untagged PDF. `handout.pdf` has a pandoc source (`probability-warmup-handout.md`) but it isn't currently built as a Jekyll page, so no accessible twin exists yet either — flagged as a future task, out of scope for this pass (would require editing files beyond the index page). |
| `notebooks/02-regression-correlation/index.md` | ok | Already fixed in a previous pass (derivation notes link); Correlation Coefficient notes link already points to the accessible page directly. No further issues found. |
| `notebooks/03-first-pipeline/index.md` | ok | No tables, images, or PDF links; all notebook links use the accessible `nb.html` include; no ambiguous link text. |

## PDF authoring convention (going forward)

- Author content in `.md`, generate PDFs via pandoc as a print/download
  convenience copy — don't hand-edit the PDF after generation, or content
  will drift from the accessible source.
- Always link the `.md`/rendered HTML page as the **primary** link; offer
  the PDF as a secondary `(PDF)` link, never the only link.
- This only covers self-authored notes. It doesn't apply to third-party
  PDFs (see below).

**Linking to external/third-party research paper PDFs** (e.g. arXiv): no
extra obligation here — DOJ's Title II rule carves out an exception for
third-party content you don't control and aren't contractually responsible
for producing. You're not expected to fix or rehost someone else's paper.
Good practice, not a requirement: label the link clearly (e.g. `(PDF)` or
"external") so users know what they're clicking before they land on
content that may not be accessible, and link an HTML/abstract version
instead if the source happens to offer one (arXiv often does).

## `.ipynb` / rendered notebook HTML — needs-fix (large, not quick)

- Markdown cell headings convert to real `<h1>`/`<h2>` correctly — ok.
- Plot images in pre-rendered HTML exports (~20 files, 100+ images, e.g.
  `notebooks/09-cnns/CIFAR10_Training.html`, `notebooks/04-regression-plus/Life_Expectancy.html`)
  all carry nbconvert's boilerplate `alt="No description has been provided
  for this image"` — present but meaningless. Real fix requires writing a
  description per plot (ideally in the notebook markdown before export,
  since these HTML files are regenerated build artifacts).

## PDFs (LaTeX-generated) — needs-fix (large, not quick)

`pdflatex` output is typically untagged: no structure tree, no reading
order, math is pure vector glyphs with no semantic meaning. Retagging is a
real project (`tagpdf`/`axessibility` LaTeX packages + manual verification),
not a quick fix.

Files with an existing accessible `.md`/HTML twin (quick win = link to the
twin instead of/alongside the PDF):
- `notes/Linear_regression_derivation.pdf` → `/notes/Linear_regression_derivation/`
- `notes/Correlation_Coefficient.pdf` → has `.md`
- `notes/derivatives-crash-course.pdf` → has `.md`
- `notes/vae_notes.pdf` → has `.md`
- `notes/bayes-notes.pdf` → source `.md` reconstructed from the PDF (original
  was lost) and linked as primary from `notebooks/01-foundations/index.md`,
  PDF kept as secondary download.

PDF-only, no accessible alternative exists yet:
- `notes/d2l.ai-LeNet.pdf`
- `notes/lenet-min.pdf`
- `notebooks/01-foundations/handout.pdf` — pandoc source exists
  (`probability-warmup-handout.md`) but isn't built as a Jekyll page yet.

## MathJax config (`_includes/head/custom.html`) — quick fix available

No accessibility ("explorer") extension loaded, so screen reader users get
no speech-text/keyboard exploration of math expressions. Adding
`loader: {load: ['a11y/explorer']}` to the MathJax config is a one-line
change (should be spot-checked with an actual screen reader afterward).

## How to continue

Pick a batch from "Not yet checked", spot-check it, and add a row above with
status + a one-line note. Flag anything found as `needs-fix` until addressed.
