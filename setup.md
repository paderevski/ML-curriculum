---
title: "Getting Started with Google Colab"
layout: single
sidebar:
  nav: "ml"
permalink: /setup/
---

Everything we do this year runs in **Google Colab** — a free service that runs
Python notebooks in your browser. Nothing to install, nothing to download. You
just need your LCPS Google account.

Work through this once on the first day. It takes about fifteen minutes.

---

## 1. Open Colab and check which account you're using

Go to **[colab.research.google.com](https://colab.research.google.com)**.

Now the important part. Look at the **circle in the top-right corner** — that's
your account avatar. Click it and confirm it shows your **LCPS school account**
(the one ending in `@lcps.org`).

> **Why this matters more than it sounds.** If you're also signed into a
> personal Gmail, Colab quietly picks whichever account your browser considers
> the default — and that's often the personal one. Everything will *look*
> like it's working, but your files save to the wrong Drive and you won't find
> them later. If the avatar shows the wrong account, click it and switch, or
> sign out of the other account entirely for the school day.

Get in the habit of glancing at that avatar every time you open Colab.

---

## 2. Make your first notebook

From the Colab home screen, click **New notebook** (bottom-right of the dialog,
or **File → New notebook**).

You'll get a page with one empty box. That box is a **cell** — that's where code
goes. Click into it and type:

```python
print("Hello from Colab!")
2 + 2
```

Now press **Shift+Enter** to run it. (Or click the ▶ button on the left of the
cell.)

The first time you run anything, Colab takes ten or twenty seconds to connect to
a machine. After that it's fast. You should see `Hello from Colab!` and `4`
appear below the cell.

**Try a couple more things** — add a new cell with the **+ Code** button and run:

```python
import math
print(math.pi)

name = "your name here"
print("Hi, " + name)
```

Nothing you do here can break anything. Experiment.

### Rename it

Click the title at the top-left — it says **Untitled0.ipynb** — and rename it to
something like `first-notebook.ipynb`. Colab saves automatically as you work.

---

## 3. Make a folder for this class

Your notebook already saved itself to Google Drive, in a folder Colab makes
automatically called **Colab Notebooks**.

Open **[drive.google.com](https://drive.google.com)** and you'll see it in
**My Drive**. Inside is the notebook you just made.

Make a folder for this course:

1. In Drive, open **My Drive**
2. Click **New → New folder**
3. Name it **ML** (or `Machine Learning`, whatever you'll recognize)
4. Drag `first-notebook.ipynb` from **Colab Notebooks** into it

> **Heads up:** Colab always saves new notebooks into **Colab Notebooks**,
> not into your `ML` folder. You can move a notebook afterward — either drag it
> in Drive, or from inside Colab use **File → Move**. Do a cleanup sweep every
> week or two so things don't pile up.

---

## 4. Open a course notebook from this site

Every notebook on this site has three links next to it: **view**, **download**,
and **colab**. Try it now — go to
[Unit 01: Foundations]({{ '/notebooks/01-foundations/' | relative_url }}) and
click the **colab** link next to *Introduction to JupyterLab and Python*.

It should open straight in Colab, ready to run. You may need to click **Run
anyway** on a warning about the notebook not being authored by Google — that's
expected, it just means the file came from outside Google.

**Read this next part carefully, because it's the mistake everyone makes once.**

---

## 5. Always "Save a copy in Drive" before you work

When you open a notebook from this site, Colab loads it straight from the course
repository. You can run it and edit it — but **it is not your copy, and your
changes are not being saved.** Close the tab and everything you typed is gone.

So the very first thing you do, every time:

**File → Save a copy in Drive**

A new tab opens with your own copy, named `Copy of <whatever>.ipynb`. *That's*
the one you work in. Rename it (drop the "Copy of") and move it to your `ML`
folder.

Quick way to tell which one you're in: your saved copy has a normal Drive title
at the top-left and autosaves as you type. The read-only original doesn't.

---

## Troubleshooting

**"My notebook disappeared."**
You probably worked in the version opened from the course site without saving a
copy. Unfortunately it's gone. Save the copy *first* from now on.

**"I can't find the file I saved."**
Check that you were on your `@lcps.org` account (Step 1). Then look in
**My Drive → Colab Notebooks** — that's where new notebooks land by default,
even if you meant to put them elsewhere.

**"It says I need to sign in."**
Your browser isn't signed into a Google account. Sign in with your LCPS account
and reload.

**"It's asking me to allow access to my Google Drive."**
Some notebooks later in the year mount your Drive so they can read data files.
Say yes — but only for notebooks from this course site.

**"The cell is taking forever / says 'Connecting'."**
Normal on the first run of a session while Colab assigns you a machine. If it
hangs for more than a minute, **Runtime → Restart session** usually fixes it.

**"I get a warning that the notebook wasn't authored by Google."**
Expected for any notebook from outside Google, including all of ours. Click
**Run anyway**.

---

## The short version

Once you've done this a few times, the whole routine is:

1. Check the avatar is your school account
2. Click **colab** on the course site
3. **File → Save a copy in Drive** — before anything else
4. Work in your copy
5. Move it into your `ML` folder when you're done
