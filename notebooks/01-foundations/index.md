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

## Concepts You'll Learn About

- **Python for data science** — NumPy arrays, pandas DataFrames, selecting and
  filtering rows and columns
- **Data exploration** — reading CSVs, handling missing values, summary statistics
- **Visualization** — matplotlib plots, interpreting distributions and trends
- **Bayes' theorem** — prior and posterior probability, updating beliefs with
  evidence; the probabilistic lens you'll use all year

## Topics

- **Python introduction** — environment setup and a fast tour of the Python
  features you'll use most.
  {% include nb.html local="Quick-Intro-To-Python.ipynb" %}

- **Pandas with real weather data** — loading Leesburg airport weather records
  and answering questions about them. First contact with a real, imperfect dataset.
  {% include nb.html local="weather.ipynb" %}

- **[Weather exercises](./weather_exercises/)** — eleven exercises in three tiers
  (Beginner / Intermediate / Advanced). The tiered structure reappears throughout
  the year. Includes a chi-square investigation into whether weekend weather
  differs from weekday weather.
  *Assignment: complete and submit your chosen tier.*

- **Bayes' theorem** — [notes (PDF)](../../notes/bayes-notes.pdf) and a notebook working
  through the probability mechanics that underlie every classifier you'll build
  this year. The choice to introduce Bayes *before* any model is deliberate —
  it primes you to think probabilistically from the start.
  {% include nb.html local="Bayes_Theorem_Student.ipynb" %}

- **London Weather project** — take a 50-year climate dataset
  ([london_weather.csv](../../data/london_weather.csv),
  [original source](https://www.kaggle.com/datasets/emmanuelfwerr/london-weather-data))
  and defend a claim about how London weather has changed. You define "worse" —
  and you have to justify that choice in writing.
  *Assignment: submit your analysis notebook.*

## What's next

[Unit 02](../notebooks/02-regression-correlation/) introduces the first actual
model: linear regression derived from scratch, before any library does it for you.
