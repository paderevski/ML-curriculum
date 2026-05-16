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
then finish with a theoretical notebook on the limits of what any classifier can
ever achieve.

## Concepts

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

## Notebooks

- {% include nb.html local="Mushroom_Student.ipynb" %} — worked example of the
  full pipeline on ~26,000 mushrooms (edible vs. poisonous). Mostly read-and-run;
  the goal is to see every step before you have to do them yourself.

- {% include nb.html local="Bayes-Error-Student.ipynb" %} — synthetic Gaussian
  experiments showing why overlapping class distributions create a performance
  floor no classifier can beat. You'll grid-search for the optimal split point
  and derive the theoretical boundary.

- {% include nb.html local="Mushroom_Key.ipynb" label="Mushroom (key)" %} —
  instructor reference.

## Assignment

Between the two notebooks there's a hands-on project: find your own categorical
dataset (UCI, Kaggle, data.gov), reproduce the Mushroom workflow on it, and
write a markdown paragraph defending your conclusions. This is the first
deliverable where you choose both the dataset and the framing question.

## What's next

[Unit 05](/notebooks/05-regression-plus/) moves to continuous data — multilinear
regression, regularization, SVD, and PCA — and closes with the DIY Linear
Regression project, a more open-ended version of the same "find your own dataset"
pattern introduced here.
