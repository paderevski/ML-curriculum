---
title: "Unit 01: Foundations"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/01-foundations/
---
In this unit we introduce Python, Jupyter/Colab, and cover some fundamental concepts in
Machine Learning, Probability and Linear Algebra.

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

{% include nb.html local="Quick-Intro-To-Python.ipynb" %}

---

## 2: Pandas and Real Weather Data

First contact with a real, imperfect dataset: Leesburg airport weather records.
Real data has missing values, inconsistent labels, and columns whose names don't tell you
what they mean!

### What you'll do

Load a CSV into a DataFrame and start asking questions. How many rows? What
are the columns? How many days were clear? Does it rain more on weekends?

### Key ideas

- A DataFrame is a table; almost everything is selecting rows, selecting
  columns, or grouping
- `df.describe()` and `df.info()` before anything else — always look at your
  data before you analyze it
- Missing data is normal and you have to decide what to do about it
- The data format is described [here](./weather-columns.md)
- Notebook: {% include nb.html local="weather.ipynb" %}

---

## 3: Weather Exercises

Eleven exercises in three tiers — Beginner, Intermediate, Advanced. Pick the tier
that matches where you are.

### What you'll do

Answer questions about the weather dataset using pandas. The advanced tier
includes a chi-square investigation into whether weekend weather is measurably
different from weekday weather — your first hypothesis test, sneaking in during
week two.


**[Open the exercises](./weather_exercises/)**

> **Assignment:** complete and submit your chosen tier.

---

## 4: Bayes' Theorem

Introducing basic probability and one of its most fundamental theorems. We'll talk about
'reversing probability', which matters a lot more than you might think!

**[Intro to Probability](./handout.pdf)**
**[Bayes Theorem](../../notes/bayes-notes.pdf)**

Homework is to complete this notebook {% include nb.html local="Bayes_Theorem_Student.ipynb" %}

---

## 5: London Weather Project

A short capstone project for this unit. Determine if you think London's weather has
gotten worse over the last 50 years.

### The task

You define "worse." That's the fun part and the point — part of the work is
deciding what to measure, then defending that choice in writing. Temperature?
Rainfall? Consecutive gray days? You pick and back it up.

### What good work looks like

- A clearly stated claim with definitions
- Evidence from the data that actually supports it
- Some graph(s) or chart(s) to substantiate your claim

**Data:** [london_weather.csv](../../data/london_weather.csv)
([original source](https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data))

> **Assignment:** submit your analysis notebook.

---

## What's Next

[Unit 02](../02-regression-correlation/) introduces the first actual model:
linear regression derived from scratch, before we use built-in tools to do it for us.
