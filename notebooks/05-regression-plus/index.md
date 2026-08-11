---
title: "Unit 05: Regression++"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/05-regression-plus/
---

The longest unit — where regression grows into a real professional toolkit and
where the linear algebra from Unit 3 finally pays off. You'll move from
single-variable models to multi-feature ones, learn why unregularized models
overfit, and discover that high-dimensional data often has hidden low-dimensional
structure you can exploit.

## Concepts You'll Learn About

- **Multiple linear regression** — fitting a model with many input features;
  the design matrix
- **Feature normalization** — why scale matters before regularization
- **L1 and L2 regularization** — Lasso and Ridge; shrinking coefficients to
  prevent overfitting; choosing alpha
- **Singular Value Decomposition (SVD)** — matrix factorization as coordinate
  transform; low-rank approximations
- **Image compression via SVD** — rank-k approximations as a visual intuition
  for what "dimension" means in data
- **Principal Component Analysis (PCA)** — finding the directions of maximum
  variance; reducing features while preserving information

## Topics

- **Multilinear regression** — introducing multiple features with a toy dataset,
  then scaling up to real [WHO life-expectancy data](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/data).
  [Lecture notes](../../notes/Multilinear_regression/)
  {% include nb.html local="Test_Scores.ipynb" %}
  {% include nb.html local="Life_Expectancy_Student.ipynb" %}

- **Normalization and regularization** — continuing with life-expectancy data;
  adding L1/L2 penalties and sweeping alpha to find the best model.
  {% include nb.html local="Life_Part_2_Student.ipynb" %}

- **Article research** — groups each find three articles on a chosen ML topic.
  An early dry-run for the spring research pitches.

- **SVD** — matrix multiplication as a geometric transformation; then using SVD
  to compress an image of Gauss to a fraction of its original size.
  [SVD notes](../../notes/svd_notes_ml/)
  {% include nb.html local="Visualizing_Transformation_Matrices.ipynb" %}
  {% include nb.html local="Low_Rank_Matrix_Approximations.ipynb" %}
  {% include nb.html local="Image-Compression.ipynb" %}

- **PCA** — projecting data onto its principal components; applying PCA as a
  preprocessing step before regression.
  {% include nb.html local="PCA.ipynb" %}

## Project: DIY Linear Regression++

The major deliverable for the unit, built across several class days.
Start with a dataset you choose, then work through the full pipeline:
feature analysis (distributions, collinearity), normalization, L1/L2 alpha
selection with a sweep plot, model interpretation, and a PCA dimension sweep.
Finish with a written defense of your "best model" choice.
*Iterative submission: draft → regularization pass → PCA pass → final.*

## Notes

- [Multilinear regression notes](../../notes/Multilinear_regression/)
- [SVD notes](../../notes/svd_notes_ml/)
- [DIY LinReg++ requirements](../../notes/DIY-LinReg-Plus/)

## What's next

[Unit 06](../06-classification/) introduces the classification algorithms
the course previewed in Unit 04 — this time with full explanations of how each one works.
