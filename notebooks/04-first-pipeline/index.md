---
title: "Unit 04: First End-to-End Pipeline"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/04-first-pipeline/
---

The "now do it yourself" hinge of the first quarter. Up through Unit 3 you've
been learning components — pandas, statistics, linear algebra. Here they
assemble into a complete machine learning workflow: load data, clean it, explore
it, encode it, split it, train a model, and evaluate the results. You'll see
the full pipeline once as a worked example, repeat it on a dataset you choose,
then finish with a theoretical look at the limits of what any classifier can
ever achieve.

## Concepts You'll Learn About

- **Data cleaning** — dropping constant features, handling missing values
  (dropping rows vs. imputing with the column mode)
- **Exploratory data analysis** — frequency plots, grouped bar charts,
  Cramér's V for categorical correlation
- **Categorical encoding** — `pd.get_dummies` (one-hot encoding) to turn
  string columns into numbers a model can use
- **Train / test split** — why you never evaluate a model on the data it
  trained on
- **Classification metrics** — accuracy, precision, recall, F1-score,
  confusion matrix; why the right metric depends on what mistakes cost
- **The sklearn API** — every classifier follows the same pattern:
  `clf.fit(X_train, y_train)` → `clf.predict(X_test)`
- **Bayes error** — the irreducible floor on classifier error when classes
  overlap; no model, however clever, can get below it

## Topics

- **Categorical classification pipeline** — a full end-to-end tour on ~26,000
  mushrooms (edible vs. poisonous): cleaning, EDA, encoding, splitting, and
  running seven classifiers back-to-back to see the sklearn API in action.
  The notebook is mostly read-and-run — the goal is to see every step before
  you do them yourself.
  {% include nb.html local="Mushroom_Student.ipynb" %}

- **Self-selected categorical dataset** — reproduce the Mushroom workflow on a
  dataset you find (UCI, Kaggle, data.gov). You choose the dataset and the
  question, handle whatever messiness it has, and write a markdown paragraph
  defending your conclusions.
  *Assignment: upload your completed notebook by end of class.*

- **Bayes error** — why even the best classifier can't beat the noise when
  class distributions overlap. You'll run experiments on synthetic Gaussian
  data, grid-search for the optimal decision boundary, then derive it
  analytically.
  {% include nb.html local="Bayes-Error-Student.ipynb" %}

## What's next

[Unit 05](/notebooks/05-regression-plus/) moves to continuous data — multilinear
regression, regularization, SVD, and PCA — and closes with the DIY Linear
Regression project, a more open-ended version of the same "find your own dataset"
pattern introduced here.
