# Accessibility Audit Log

Tracking WCAG 2.1 AA spot-checks and fixes against the ADA Title II rule
(applies to this site as a public school resource; compliance deadline
April 24, 2026 for districts serving 50,000+ population).

Status values: `ok` (checked, no issue), `fixed` (issue found and repaired),
`needs-fix` (issue found, not yet repaired), `not-checked`.

---

## ✅ Done — fixed or confirmed ok

### Files checked

| File | Status | Notes |
|---|---|---|
| `notebook-viewer.html` | fixed | Added `lang="en"`, viewport meta tag, and `alt` text on generated plot images (previously bare `<img>` with no alt). |
| `_includes/nb.html` | ok | Disclosure widget already uses `aria-expanded`/`aria-haspopup` correctly. |
| `assets/js/notebook-links.js` | ok | Keyboard support (Escape to close, focus return), focusin/focusout handling all present. |
| `_includes/head/custom.html` | fixed | Added `loader: {load: ['a11y/explorer']}` to MathJax config for speech-text/keyboard math exploration. Should be spot-checked with a real screen reader. |
| `_includes/footer/custom.html` | ok | Static ad placement div only, nothing to check. |
| `_data/navigation.yml` | ok | Structured data only, no markup to check directly (theme renders it). |
| Sidebar nav markup (rendered from `navigation.yml`) | ok | Theme-default Minimal Mistakes `nav_list` include, no local override. Section headers ("Units"/"Notes"/"Reference") are static, always-expanded — flat, linear Tab order, no keyboard trap. Mobile toggle is a native `<input type="checkbox">` + `<label>`. See archived detail below. |
| `_layouts/` | n/a | No local `_layouts/` directory exists; all layouts come from the remote theme gem. |
| Custom `_includes/` overrides | ok | `_includes/` only contains `nb.html`, `head/custom.html`, `footer/custom.html` — all three checked above. |
| `assets/css/main.scss` | ok | Only override is link color `#1a6bb0` on white — contrast ratio ~5.6:1, passes AA. No focus outlines stripped; `.notebook-links__label:focus-visible` explicitly adds a visible focus ring. |
| `patch.md`, `setup.md`, `bayes-practice.md` | ok | Plain markdown, no raw HTML/images/tables to check. |
| `statistics.html` | fixed | Decorative icon spans and redundant SVG charts marked `aria-hidden="true"`/`focusable="false"`; `.subtitle` color darkened from `#7f8c8d` to `#5f6c72` (now passes 4.5:1); added `scope="col"` to comparison table headers. |
| `index.md` (main calendar) | fixed | Replaced blank-header `\| \| \|` info table with a plain list (screen readers were announcing unlabeled table headers); reworded two ambiguous "here" links to descriptive link text (WCAG 2.4.4); Linear Regression link points to the accessible `.md`/HTML page as primary, PDF as secondary. |
| `notebooks/01-foundations/index.md` | fixed | Reworded a "here" link to descriptive text; fixed two stacked bold PDF links that ran together as one paragraph in Markdown. Bayes Theorem and Intro to Probability links now point to their accessible `.md`/HTML pages as primary, with the PDF as a secondary `(PDF)` download. |
| `notebooks/02-regression-correlation/index.md` | fixed | Linear regression derivation link points to the accessible `.md`/HTML page as primary, PDF secondary. Correlation Coefficient notes link already pointed to the accessible page directly. No further issues found. |
| `notebooks/03-first-pipeline/index.md` | ok | No tables, images, or PDF links; all notebook links use the accessible `nb.html` include; no ambiguous link text. |

### PDFs repaired (self-authored notes)

- **`notes/bayes-notes.pdf`**: original `.md` source was lost. Reconstructed
  `notes/bayes-notes.md` by extracting text from the PDF (`pdftotext -layout`)
  and rewriting it as clean Markdown/MathJax (including the final derivation
  as an `aligned` block matching the PDF's multi-line layout). Now builds as
  an accessible page and is linked as primary from
  `notebooks/01-foundations/index.md`, PDF kept as secondary download.
- **`notebooks/01-foundations/handout.pdf`**: pandoc source
  `probability-warmup-handout.md` existed but had no Jekyll front matter
  (`title`/`layout`/`math`), so it wasn't building as a site page. Added
  front matter and removed a duplicate H1 (title already renders one via
  the theme). Now builds at
  `/notebooks/01-foundations/probability-warmup-handout/` and is linked as
  primary, with the PDF as secondary download.
- **`notes/Linear_regression_derivation.pdf`**: already had a `.md` twin;
  linked as primary from `index.md` and
  `notebooks/02-regression-correlation/index.md`, PDF secondary.

### Established convention: PDF authoring (going forward)

- Author content in `.md`, generate PDFs via pandoc as a print/download
  convenience copy — don't hand-edit the PDF after generation, or content
  will drift from the accessible source.
- Always link the `.md`/rendered HTML page as the **primary** link; offer
  the PDF as a secondary `(PDF)` link, never the only link.
- This only covers self-authored notes. It doesn't apply to third-party
  PDFs.

**Linking to external/third-party research paper PDFs** (e.g. arXiv): no
extra obligation here — DOJ's Title II rule carves out an exception for
third-party content you don't control and aren't contractually responsible
for producing. Good practice, not a requirement: label the link clearly
(e.g. `(PDF)` or "external"), and link an HTML/abstract version instead if
the source offers one (arXiv often does).

<details>
<summary>Archived detail: sidebar nav markup inspection</summary>

Inspected the built `_site/index.html` sidebar (Minimal Mistakes theme,
`_data/navigation.yml` rendered via the theme's stock `nav_list` include —
no local override exists in `_includes/`):

- "Units" / "Notes" / "Reference" section headers (no `url` in the data
  file) render as static `<span>` labels with their child `<ul>` always
  visible — not a collapsible accordion. Every link is reachable via a
  flat, linear Tab order with nothing hidden behind required interaction —
  no keyboard trap.
- The mobile sidebar toggle uses a real `<input type="checkbox">` +
  `<label for="ac-toc">Toggle menu</label>` — native, keyboard-operable,
  with a visible text label. It doesn't announce open/closed state via
  `aria-expanded`, but that's stock theme markup — patching it would mean
  forking the theme's `nav_list` include locally, not a quick or low-risk
  change.
- The top masthead's responsive toggle button already has a
  `visually-hidden` "Toggle menu" label.

</details>

---

## 🔲 Needs fixing or investigation

### Not yet checked

- Unit `index.md` pages for units 4–12 under `notebooks/*/`

### `.ipynb` / rendered notebook HTML — large, not quick

- Markdown cell headings convert to real `<h1>`/`<h2>` correctly — ok.
- Plot images in pre-rendered HTML exports (~20 files, 100+ images, e.g.
  `notebooks/09-cnns/CIFAR10_Training.html`, `notebooks/04-regression-plus/Life_Expectancy.html`)
  all carry nbconvert's boilerplate `alt="No description has been provided
  for this image"` — present but meaningless. Real fix requires writing a
  description per plot (ideally in the notebook markdown before export,
  since these HTML files are regenerated build artifacts).

### PDFs (LaTeX-generated) — large, not quick

`pdflatex` output is typically untagged: no structure tree, no reading
order, math is pure vector glyphs with no semantic meaning. Retagging is a
real project (`tagpdf`/`axessibility` LaTeX packages + manual verification),
not a quick fix.

Files with an existing accessible `.md`/HTML twin, not currently linked
from any checked page (low-effort fix whenever they're referenced):
- `notes/Correlation_Coefficient.pdf` → has `.md`
- `notes/derivatives-crash-course.pdf` → has `.md`
- `notes/vae_notes.pdf` → has `.md`

PDF-only, no accessible alternative exists yet (real fix needed):
- `notes/d2l.ai-LeNet.pdf`
- `notes/lenet-min.pdf`

---

## How to continue

Pick a batch from "Needs fixing or investigation", spot-check it, and move
it into the "Done" section with status + a one-line note.
