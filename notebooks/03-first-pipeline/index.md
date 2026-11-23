---
title: "Unit 03: First End-to-End Pipeline"
layout: unit
sidebar:
  nav: "ml"
permalink: /notebooks/03-first-pipeline/
---

The "now do it yourself" hinge of the first quarter. Up through Unit 2 you've
been learning components: pandas, statistics, linear algebra. Here they come
together into a complete machine learning workflow: load data, clean it,
explore it, encode it, split it, train a model, and evaluate the results.
You'll see the full pipeline once as a worked example, repeat it on a dataset
you choose, then finish with a theoretical look at the limits of what any
classifier can achieve.

## Categorical Classification Pipeline

A full end-to-end tour on about 26,000 mushrooms (edible vs. poisonous):
cleaning, EDA, encoding, splitting, and running seven classifiers back to back
to see the sklearn API in action. The notebook is mostly read-and-run; the goal
is to see every step before you do them yourself.

#### Key ideas

- **Data cleaning**: dropping constant features, handling missing values
  (dropping rows vs. imputing with the column mode)
- **EDA**: frequency plots, grouped bar charts, Cramér's V for categorical correlation
- **Encoding**: `pd.get_dummies` (one-hot) turns string columns into numbers a model can use
- **Train/test split**: never evaluate a model on the data it trained on
- **Metrics**: accuracy, precision, recall, F1, the confusion matrix, and why
  the right one depends on what mistakes cost
- **The sklearn API**: every classifier is `clf.fit(X_train, y_train)` then `clf.predict(X_test)`

#### Notebooks & materials

- **Warm-up** [Categorical data](../../notes/categorical_intro.md):
  Try to fit a linear regression to colors. What goes wrong?
- **Demo + HW** [Poisoned Mushroom Dataset](./Mushroom_Student_2026B.ipynb):
  We go through the pipeline in class; the analysis questions are homework.

## Your Own Categorical Dataset

Reproduce the mushroom workflow on a dataset you find (UCI, Kaggle, data.gov).
You choose the dataset and the question, handle whatever messiness it has, and
write a markdown paragraph defending your conclusions.

#### Notebooks & materials

- **Project** Self-selected categorical dataset: Upload your completed notebook
  by the end of class.

## Bayes Error

Why even the best classifier can't beat the noise when class distributions
overlap. You'll run experiments on synthetic Gaussian data, grid-search for the
optimal decision boundary, then derive it analytically.

#### Key ideas

- **Bayes error**: the irreducible floor on classifier error when classes overlap
- No model, however clever, can get below it

#### Notebooks & materials

- **Homework** [Bayes Error](./Bayes-Error-Student.ipynb):
  Find the best possible decision boundary for overlapping Gaussian classes.
