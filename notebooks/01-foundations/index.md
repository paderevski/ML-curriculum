---
title: "Unit 01: Foundations"
layout: unit
sidebar:
  nav: "ml"
permalink: /notebooks/01-foundations/
---

In this unit we introduce Python, Jupyter/Colab, and cover some fundamental
concepts in Machine Learning, Probability and Linear Algebra.

## Python Introduction

A fast tour of the Python you'll actually use this year. Not a complete
language course (we skip a lot), but enough that the rest of the units don't
trip you up on syntax.

#### Key ideas

- Cells run in the order *you* run them, not top to bottom: a common source of
  confusion later
- Python is dynamically typed; you don't declare types, but types still matter
- Lists and dictionaries cover most of what you'll need before pandas

#### Notebooks & materials

- **Homework** [Introduction to JupyterLab and Python](./Quick-Intro-To-Python.ipynb):
  Work through the notebook cell by cell, running each one: variables, data
  types, lists and dictionaries, control flow, functions, and imports, then a
  first look at Matplotlib.

## Pandas and Real Weather Data

First contact with a real, imperfect dataset: Leesburg airport weather
records. Real data has missing values, inconsistent labels, and columns whose
names don't tell you what they mean!

#### Key ideas

- A DataFrame is a table; almost everything is selecting rows, selecting
  columns, or grouping
- `df.describe()` and `df.info()` before anything else: always look at your
  data before you analyze it
- Missing data is normal, and you have to decide what to do about it

#### Notebooks & materials

- **Demo + HW** [Cloudy Days in Leesburg](./weather.ipynb):
  We look at it together in class; you complete it for homework. Load the CSV
  into a DataFrame and start asking questions: how many days were clear? Does it
  rain more on weekends?
- **Reference** [Weather column reference](./weather-columns.md):
  What each column in the weather data means. Use it to define a "good" and a
  "bad" weather day.

## Weather Exercises

Eleven exercises in three tiers (Beginner, Intermediate, Advanced). Pick the
tier that matches where you are. The advanced tier includes a chi-square
investigation into whether weekend weather is measurably different from
weekday weather: your first hypothesis test, sneaking in during week two.

#### Notebooks & materials

- **Homework** [Leesburg Weather Exercises](./weather_exercises.md):
  Complete and submit your chosen tier.

## Bayes' Theorem

Basic probability and one of its most fundamental theorems. We'll talk about
"reversing" a probability, which matters a lot more than you might think!

#### Key ideas

- Conditional probability $P(A \mid B)$, and why it isn't $P(B \mid A)$
- Bayes' theorem lets you turn one into the other
- Contingency tables (confusion matrices) organize the counts

#### Notes

> [Bayes' Theorem](../../notes/bayes-notes.md) ([PDF](../../notes/bayes-notes.pdf))

#### Notebooks & materials

- **In class** [Intro to Probability](./probability-warmup-handout.md):
  Intersection, union, and conditional probability. Also as a [PDF](./handout.pdf).
- **In class** Confusion matrices worksheet: Contingency tables, handed out in class.
- **Homework** [Bayes' Theorem](./Bayes_Theorem_Student.ipynb):
  Practice with conditional probability and Bayes' theorem.

## London Weather Project

A short capstone project for this unit. Has London's weather gotten worse over
the last 50 years?

You define "worse." That's the fun part and the point: part of the work is
deciding what to measure, then defending that choice in writing. Temperature?
Rainfall? Consecutive gray days? You pick and back it up.

#### What good work looks like

- A clearly stated claim with definitions
- Evidence from the data that actually supports it
- Some graph(s) or chart(s) to substantiate your claim

#### Notebooks & materials

- **Project** London weather analysis: Submit your analysis notebook.
- **Reference** [london_weather.csv](../../data/london_weather.csv):
  The data ([original source](https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data)).
