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

## 3. Where your notebooks live

Your notebook already saved itself to Google Drive, in a folder Colab creates
automatically called **Colab Notebooks**.

Open **[drive.google.com](https://drive.google.com)**, go to **My Drive**, and
you'll see it. Your notebook is inside.

**That's where everything you make in Colab goes.** Colab always saves there and
doesn't give you a choice of folder, so don't fight it — just know where to
look. You'll be back in Drive regularly to rename things (Step 5).

### Name things so you can find them later

By May you'll have forty-odd notebooks in that one folder. The fix isn't
subfolders — it's names that sort themselves.

Start each notebook's name with its unit number:

```
u01-python-intro.ipynb
u01-weather.ipynb
u04-mushroom.ipynb
u10-cifar-cnn.ipynb
```

Drive sorts alphabetically, so this groups everything by unit for free. And
when you can't remember where something is, just search Drive for a word from
the name — that's faster than clicking through folders anyway.

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
the one you work in — the original tab is still the unsaved read-only version,
so close it so you don't mix them up.

Quick way to tell which one you're in: your saved copy has a normal Drive title
at the top-left and autosaves as you type. The read-only original doesn't.

### Then go rename it

Colab drops the copy into **Colab Notebooks** with that clumsy `Copy of` name
and no way to change either at save time. Fixing it takes ten seconds:

1. Open **[drive.google.com](https://drive.google.com)** → **My Drive** →
   **Colab Notebooks**
2. Find the file (it'll be at the top if you sort by *Last modified*)
3. Right-click → **Rename**
4. Give it a name like `u04-mushroom.ipynb` — unit number first, per Step 3

Do this right after you save the copy, while you still remember what the
notebook was. A folder full of `Copy of Copy of Untitled3.ipynb` in April is a
self-inflicted problem.

---

## Troubleshooting

**"My notebook disappeared."**
You probably worked in the version opened from the course site without saving a
copy. Unfortunately it's gone. Save the copy *first* from now on.

**"I can't find the file I saved."**
Check that you were on your `@lcps.org` account (Step 1). Then look in
**My Drive → Colab Notebooks** — everything Colab saves goes there. Sort by
*Last modified* and it'll be at the top.

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
5. Rename it in Drive when you're done — unit number first,
   like `u04-mushroom.ipynb`
