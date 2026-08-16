---
title: "Unit 01: Foundations"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/01-foundations/
---

The on-ramp. Two weeks of getting fluent with Python, pandas, matplotlib, and
Bayesian thinking before the real ML work begins. By the end you'll be able to
load a messy CSV, clean it, plot it, and make a probabilistic argument about
what it shows.

Nothing here is machine learning yet. That's deliberate — every model we build
later this year sits on top of these four skills, and the students who struggle
in March are almost always the ones who stayed shaky on pandas in September.

## Concepts You'll Learn About

- **Python for data science** — NumPy arrays, pandas DataFrames, selecting and
  filtering rows and columns
- **Data exploration** — reading CSVs, handling missing values, summary statistics
- **Visualization** — matplotlib plots, interpreting distributions and trends
- **Bayes' theorem** — prior and posterior probability, updating beliefs with
  evidence; the probabilistic lens you'll use all year

---

## 1: Python Introduction

A fast tour of the Python you'll actually use this year. Not a complete language
course — we skip a lot — but enough that the rest of the units don't trip you up
on syntax.

### What you'll do

Work through the notebook cell by cell, running each one. Variables, data types,
lists and dictionaries, control flow, functions, and imports. Then a first look
at Matplotlib, which gets its own extended section at the end.

### Key ideas

- Cells run in the order *you* run them, not top to bottom — a common source of
  confusion later
- Python is dynamically typed; you don't declare types, but types still matter
- Lists and dictionaries cover most of what you'll need before pandas

*[Placeholder — expand with the specific gotchas that come up in class.]*

{% include nb.html local="Quick-Intro-To-Python.ipynb" %}

---

## 2: Pandas and Real Weather Data

First contact with a real, imperfect dataset: Leesburg airport weather records.
Real data has missing values, inconsistent labels, and columns whose names don't
mean what you'd guess.

### What you'll do

Load a CSV into a DataFrame and start asking it questions. How many rows? What
are the columns? How many days were clear? Does it rain more on weekends?

### Key ideas

- A DataFrame is a table; almost everything is selecting rows, selecting
  columns, or grouping
- `df.describe()` and `df.info()` before anything else — always look at your
  data before you analyze it
- Missing data is normal and you have to decide what to do about it

*[Placeholder — add the specific pandas idioms worth memorizing.]*

{% include nb.html local="weather.ipynb" %}

---

## 3: Weather Exercises

Eleven exercises in three tiers — Beginner, Intermediate, Advanced. Pick the tier
that matches where you are. The tiered structure reappears throughout the year.

### What you'll do

Answer questions about the weather dataset using pandas. The advanced tier
includes a chi-square investigation into whether weekend weather is measurably
different from weekday weather — your first hypothesis test, sneaking in during
week two.

### Going further

*[Placeholder — note which exercises are worth discussing as a group.]*

**[Open the exercises](./weather_exercises/)**

> **Assignment:** complete and submit your chosen tier.

---

## 4: Bayes' Theorem

The probabilistic lens you'll use all year. Introducing Bayes *before* any model
is deliberate — it primes you to think in terms of updating beliefs with
evidence, which is what every classifier we build is doing underneath.

### The formula

Conditional probability, inverted. The derivation is short and worth doing by
hand once, because the algebra makes the intuition stick in a way that memorizing
the formula doesn't.

### Why it matters here

The classic medical-test problem: a test that's 97% accurate, for a disease that
affects 1 in 1000 people. Most people's intuition about what a positive result
means is badly wrong, and the gap between intuition and arithmetic is the whole
lesson.

*[Placeholder — add the in-class worked example and the discussion that follows.]*

**[Notes (PDF)](../../notes/bayes-notes.pdf)**

{% include nb.html local="Bayes_Theorem_Student.ipynb" %}

---

## 5: London Weather Project

The unit's capstone. A 50-year climate dataset and one question: has London's
weather gotten worse?

### The task

You define "worse." That's the hard part and the point — part of the work is
deciding what to measure, then defending that choice in writing. Temperature?
Rainfall? Consecutive gray days? There's no answer key.

### What good work looks like

- A clearly stated claim
- Evidence from the data that actually supports it
- Honest acknowledgment of what the data can't tell you

*[Placeholder — add examples of strong student framings from past years.]*

**Data:** [london_weather.csv](../../data/london_weather.csv)
([original source](https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data))

> **Assignment:** submit your analysis notebook.

---

## What's Next

[Unit 02](../02-regression-correlation/) introduces the first actual model:
linear regression derived from scratch, before any library does it for you.
