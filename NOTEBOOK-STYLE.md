# Notebook Style Guide

House style for restyling notebooks in this repo — headers, structure, and the
constraints that keep a restyle from destroying real content. Worked examples
to refer back to when doing the next one:
`notebooks/01-foundations/Quick-Intro-To-Python.ipynb` (numbered topic tour)
and `notebooks/01-foundations/weather.ipynb` (unnumbered step-by-step
walkthrough).

This is a living document — update it as new edge cases turn up. It will.

---

## The one rule that matters most

**Never regenerate a code cell that already has real output.**

47 of the 61 notebooks in this repo (as of the last full scan) have stored
outputs — training curves, printed metrics, plotted figures, some of them
representing real GPU/compute time. If a code cell already has content in its
`outputs` field, restyling should never touch that cell's `source`,
`outputs`, `execution_count`, or `metadata` unless the actual code is
genuinely changing.

**What "restyling" is allowed to touch:**
- Markdown cells — reformat headers, add missing ones, fix header levels
- Splitting a code cell into two (e.g. to insert a header between two loosely
  related chunks) — fine, as long as neither half's *content* changes
- Whitespace at the end of a cell's source (see below)

**What it must never touch on an unrelated code cell:**
- `source` (the actual code)
- `outputs`
- `execution_count`
- `metadata` — especially `metadata.id` (Colab's auto-generated per-cell ID;
  13 notebooks currently have these) and `metadata.collapsed`

If you're scripting a restyle pass rather than hand-editing, read the
notebook, build a plan for which markdown cells to add/change, and apply only
those — never round-trip the whole cell list through a rebuild function that
defaults `outputs` to `[]`.

---

## Header conventions

Adapted from the Quick-Intro-To-Python pass. Four levels:

| Level | Pattern | Example |
|---|---|---|
| Title | `# Unit NN · Title` | `# Unit 01 · Introduction to JupyterLab and Python` |
| Top-level numbered section | `## N: Title` (colon, no period) | `## 1: Basic Data Types and Variables` |
| Subsection | `### N.M Title` (decimal, space, no colon) | `### 8.1 Line Plot` |
| Exercise | `#### Exercise N: Title` (own sequence, separate from main numbering) | `#### Exercise 1: Modified Line Plot` |
| Unnumbered section | Plain `## Title` | `## Practice Exercises` |

**Why colon, not period, after the number:** `## 1. Title` uses the exact
markdown syntax for an ordered-list item (`digit + period + space`). Some
renderers — Colab's sidebar table-of-contents among them — appear to strip a
leading token that looks like a list marker when building the TOC entry,
which silently drops the number from the sidebar even though the header
itself renders fine in the notebook body. `## 1: Title` doesn't match that
pattern and the number displays correctly. (This is inferred from observed
behavior, not documented — worth re-testing if a renderer's behavior ever
seems to have changed.)

**Numbering style can vary by notebook shape — don't force uniformity.**
Three patterns are established in this repo, each suited to a different kind
of notebook:

| Notebook shape | Pattern | Worked example |
|---|---|---|
| Topic tour — a set of distinct conceptual topics | `## N: Title` | `01-foundations/Quick-Intro-To-Python.ipynb` |
| Procedural pipeline — ordered stages of one workflow | `## Step N: Title` | `09-cnns/CIFAR10_Training.ipynb` |
| Step-by-step walkthrough — many short sequential actions | plain `## Title` (no number) | `01-foundations/weather.ipynb` |

Pick whichever fits the notebook. `Step N:` signals sequence in a way a bare
number doesn't; plain descriptive headers avoid absurdity when a notebook has
20+ short steps and numbering to `## 23:` would be pure noise. The
requirement is that *some* real header hierarchy exists and is internally
consistent within that notebook — not that every notebook in the repo uses
identical numbering text.

**Blurbs:** one short sentence under each top-level `##` header, same voice as
the site's "Topics" bullets on the unit index pages. Optional under `###`
subsections — often the code is self-explanatory at that level. Skip blurbs
entirely for notebooks where the code truly speaks for itself (a pure syntax
tour); keep them where the *why* matters (statistical reasoning, ML
decisions).

---

## Trailing newlines

A code cell's `source` array should not have a trailing `\n` on its *last*
line. Every line before the last should end with `\n`; the last should not.
This is how Jupyter's own UI writes cells natively. Cells built via
multi-line triple-quoted Python strings (the common pattern when scripting a
notebook rewrite) tend to violate this by default, since the string
conveniently ends right before the closing `"""` with a trailing newline —
that trailing `\n` shows up as an extra visible blank line at the bottom of
the cell in Jupyter/Colab's editor.

Quick check after any script-based edit:

```python
import json
with open('notebook.ipynb') as f:
    nb = json.load(f)
bad = [i for i, c in enumerate(nb['cells'])
       if c['cell_type'] == 'code' and c['source'] and c['source'][-1].endswith('\n')]
print(f"{len(bad)} cells with a trailing newline: {bad}")
```

---

## Known edge cases to check for before touching a notebook

From a repo-wide scan — not all of these will appear in every notebook, but
worth checking before starting:

- **ipywidgets output** (2 notebooks currently: `seq2seq_nmt_pytorch_hf_reference.ipynb`,
  `image_captioning_key.ipynb`). More fragile — widget output references a
  separate widget-state blob at the notebook-metadata level.
  `scripts/export_notebooks.py` already has sanitization logic for a known
  widget-state issue; be aware similar fragility can bite a manual edit too.
- **Baked-in error tracebacks** (6 notebooks currently). A cell crashed at
  some point and the traceback got saved as committed output. Usually
  unintentional — worth flagging separately as a content issue, not a
  styling one, rather than silently "fixing" by deleting the error output
  (that changes what was actually run).
- **Local machine paths leaked into stream output** (10 notebooks
  currently) — e.g. `/Users/pewhite/miniconda3/envs/...` sitting in a
  printed warning or log line. Cosmetic, low-risk to clean up, but changes
  committed output — flag rather than silently strip unless asked.
- **Zero headers on a real (non-orphaned) notebook.** `AAPL.ipynb` is the
  current known instance. `Untitled.ipynb` (in `_orphans/`) also has none,
  but that one's an orphan, not a real notebook — leave it alone.
- **No markdown-embedded images found repo-wide** as of the last scan — not
  a pattern that needs designing around yet, but re-check if that changes.

---

## Suggested workflow for restyling a notebook

1. Read the whole notebook first (`json.load` + dump cell contents) —
   don't start editing blind.
2. Check it against the edge-case list above.
3. Identify natural section breaks — usually already marked by inline
   numbered comments (`# 1. Topic`) in a not-yet-restyled notebook, or
   already-decent headers that just need convention alignment.
4. Draft markdown headers for each section (title, `##` sections, `###`
   subsections as needed, blurbs where they earn their place).
5. If scripting: edit cell `source` only for markdown cells and any
   never-yet-run code cells; leave every cell with real output untouched.
6. Check trailing newlines on any cell you did touch.
7. Confirm the file is still valid JSON with intact `nbformat`,
   `nbformat_minor`, and `metadata.kernelspec` before committing.
