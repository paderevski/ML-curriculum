---
title: "Unit 06: Classification Classics"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/06-classification/
---

Three algorithms in three weeks, each introduced with a different dataset and a
different motivating question. The consistent pattern throughout: devise or
derive the algorithm in class first, then implement it, then reach for the
library. You earn the library.

## Concepts You'll Learn About

- **Logistic regression** — the sigmoid function; log-odds; maximum likelihood
  vs. least squares; interpreting coefficients
- **k-Nearest Neighbors** — distance metrics; the curse of dimensionality; why
  k matters; approximate NN at scale
- **Decision trees** — recursive partitioning; information gain; entropy as an
  impurity measure
- **Shannon entropy** — bits as a measure of uncertainty; encoding strings;
  connection to Huffman coding

## Topics

- **Logistic Regression on cancer data** — binary classification on the
  Wisconsin breast cancer dataset; reading the classification report carefully
  because false negatives cost lives.
  {% include nb.html local="Cancer_Logistic_Student.ipynb" %}

- **Logistic Regression on loan data** — open-ended: do the best logistic
  regression you can on [loan_data.csv](../../data/loan_data.csv) and defend your choices.
  *Assignment: submit your notebook.*

- **k-Nearest Neighbors** — devise the algorithm on the board first, then
  implement it. Applied to handwritten digit recognition.
  A [survey of approximate NN algorithms](https://towardsdatascience.com/comprehensive-guide-to-approximate-nearest-neighbors-algorithms-8b94f057d6b6)
  connects the classroom version to Spotify- and Netflix-scale systems.
  {% include nb.html local="knn-Student.ipynb" %}
  {% include nb.html local="digits-student.ipynb" %}

- **Decision Trees** — hand-classify the WillWait? restaurant dataset to
  motivate entropy and information gain, then run the lab on income data.
  {% include nb.html local="Decision_Tree_Student.ipynb" %}

- **Shannon entropy** — information as surprise; encoding strings efficiently;
  connection to the compression ideas coming in Unit 07.

## What's next

[Unit 07](../07-svm-cv-ensembles/) closes out the classical-ML arc with
SVMs, proper cross-validation, word embeddings, and ensemble methods — the
professional-practice layer on top of the algorithms you now know.
