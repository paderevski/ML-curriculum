---
title: "Unit 02: Linear Regression and Correlation"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/02-regression-correlation/
---

The first model — derived from scratch before scikit-learn enters the room.
Linear regression is introduced not as a black box but as the closed-form
solution to a least-squares minimization, so you understand what the library
is doing before you let it do it.

## Concepts You'll Learn About

- **Ordinary least squares** — minimizing the sum of squared residuals;
  deriving the slope and intercept analytically
- **Residuals and model fit** — what a good fit looks like vs. a poor one
- **R² (coefficient of determination)** — how much variance in y your model explains
- **Pearson correlation** — linear association between two variables; why
  correlation is not causation
- **Measures of spread** — variance, standard deviation in the context of regression

## Topics

- **Linear regression derivation** — the math behind least squares, then
  applied in NumPy without a library.
  {% include nb.html local="Least-Squares.ipynb" %}

- **Correlation and R²** — measuring how well a line fits and how strongly
  two variables are related.
  {% include nb.html local="Correlation.ipynb" %}

- **NumPy reference** — a supplementary notebook covering the array operations
  used throughout the unit.
  {% include nb.html local="Numpy-Intro.ipynb" %}

- **Custom regression assignment** — find your own dataset, fit a
  single-variable linear regression, and defend the fit in a markdown cell.
  Does the R² justify the model? What would a better one need?
  *Assignment: submit your notebook.*

## Notes

- [Linear regression derivation (notes)](/notes/Linear_regression_derivation/)
- [Correlation Coefficient (notes)](/notes/Correlation_Coefficient/)

## What's next

[Unit 03](/notebooks/03-linear-algebra/) is a focused two-day pause to build
the matrix vocabulary you'll need for SVD, PCA, and neural networks later in the year.
