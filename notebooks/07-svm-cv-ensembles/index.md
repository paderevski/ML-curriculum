---
title: "Unit 07: SVM, Cross-Validation, and Ensembles"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/07-svm-cv-ensembles/
---

The last classical-ML push before deep learning. This unit adds the
professional-practice layer: how to evaluate a model honestly, how to tune
hyperparameters without overfitting to your test set, and how to combine many
weak models into a stronger one. It also introduces the first learned text
representations — word embeddings — as a bridge toward the sequence models
coming later.

## Concepts You'll Learn About

- **Arithmetic coding** — optimal prefix-free codes; connecting Shannon entropy
  to practical compression
- **Support Vector Machines** — maximum-margin classifiers; the kernel trick;
  soft-margin SVMs; C as a regularization parameter
- **Cross-validation** — k-fold CV; why a held-out test set is not enough for
  hyperparameter search
- **Grid search** — systematic hyperparameter sweep; combining with CV to avoid
  data leakage
- **Word embeddings** — learned dense representations; TF-IDF vs. embeddings;
  first exposure to representations that encode meaning
- **Ensemble methods** — bagging, random forests, gradient boosting; why
  combining models reduces variance

## Topics

- **Arithmetic codes** — lecture on optimal coding; connects directly to the
  Shannon entropy from Unit 06.

- **SVM theory and lab** — the margin, support vectors, and the kernel trick;
  then a lab applying SVM to a classification problem.
  {% include nb.html local="Notes-SVM.ipynb" %}
  {% include nb.html local="SVM_Lab-Student.ipynb" %}

- **Cross-validation and grid search** — applied to Twitter airline sentiment
  ([twitter_training.csv](../../data/twitter_training.csv)) with SVM + TF-IDF;
  includes the `mnist.pk.gz` dataset as a secondary target.
  {% include nb.html local="CrossValidation.ipynb" %}

- **Word embeddings and fake news** — moving from bag-of-words to dense
  representations; applying them to a fake-news classification task.
  [word2vec embeddings](../../data/word2vec/)
  {% include nb.html local="Twitter.ipynb" %}
  {% include nb.html local="Twitter-Airline.ipynb" %}

- **Ensemble methods** — bagging, random forests, gradient boosting, and
  stacking; applied to a dataset of your choice.
  {% include nb.html local="Ensemble_Methods.ipynb" %}
  *Assignment: apply ensemble methods to a previously-analyzed dataset and submit.*

- **AET Challenge Day** — end-of-semester competition event.

## What's next

[Unit 08](../notebooks/08-anomaly/) is a short focused unit on anomaly detection —
the second-quarter capstone, closing with an open-ended quarter project.
