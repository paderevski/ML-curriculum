---
title: "Unit 02: Regression, Correlation, and Linear Algebra"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/02-regression-correlation/
---

We spend time deriving the linear regression line-of-best-fit equation from scratch. Then we implement linear regression in python, learning how to use NumPy and work with
matrices on the way. We talk about goodness-of-fit measures, introduce some linear algebra and analyze some data along the way.

## 1: Linear Regression Derivation

The math behind least squares, then applied in NumPy from scratch.

### What you'll do

Derive the slope and intercept of the best-fit line analytically, minimizing
the sum of squared residuals. Then implement the result in NumPy and check it
against the closed-form solution.

### Key ideas

- **Ordinary least squares** — minimizing the sum of squared residuals;
  deriving the slope and intercept analytically
- **Residuals and model fit** — what a good fit looks like vs. a poor one
- [Derivation notes](../../notes/Linear_regression_derivation.pdf)

{% include nb.html local="Least-Squares.ipynb" %}

---

## 2: Correlation and R²

Measuring how well a line fits and how strongly two variables are related.

### What you'll do

Compute Pearson correlation and R² (coefficient of determination) for several
paired variables, and build intuition for what these numbers do and don't tell you.

### Key ideas

- **R² (coefficient of determination)** — how much variance in y your model explains
- **Pearson correlation** — linear association between two variables; why
  correlation is not causation
- **Measures of spread** — variance, standard deviation in the context of regression
- [Correlation Coefficient notes](../../notes/Correlation_Coefficient/)

{% include nb.html local="Correlation.ipynb" %}

---

## 3: NumPy Reference

A supplementary notebook covering the array operations used throughout the unit.

### What you'll do

Work through indexing, slicing, and basic array math as a refresher or
first exposure, depending on how comfortable you already are with NumPy.

{% include nb.html local="Numpy-Intro.ipynb" %}

---

## 4: Custom Regression Assignment

Find your own dataset, fit a single-variable linear regression, and defend
the fit in a markdown cell.

### What you'll do

Pick a dataset, fit the line, and report the R². Does it justify the model?
What would a better one need?

> **Assignment:** submit your notebook.

---

## 5: Linear Algebra in Python

A self-contained stretch to build the matrix foundation that later units
rely on heavily. The goal is fluency with NumPy matrix operations, not
proof-writing.

### What you'll do

Work through vectors, matrices, and the NumPy operations that manipulate
them — notation, shapes, and the difference between a row and a column vector.

### Key ideas

- **Vectors and matrices** — notation, shapes, the difference between a row
  and a column vector
- **Matrix multiplication** — how dot products chain together; why order matters
- **NumPy array operations** — indexing, slicing, broadcasting, `@` for matrix
  multiply

{% include nb.html local="Linear_Algebra_and_Python.ipynb" %}

---

## 6: Matrix Indexing Warmup

Practice selecting rows, columns, and submatrices; builds the indexing
fluency used everywhere else.

{% include nb.html local="Matrices_Index_Warmup-Student.ipynb" %}

---

## 7: Intro to Matrices in NumPy

Matrix multiply, transpose, inverse, and solving linear systems.

### Key ideas

- **Transpose and inverse** — what they do geometrically and when they exist

{% include nb.html local="Intro_to_Matrices_in_NumPy.ipynb" %}

---

## What's Next

[Unit 03](../03-first-pipeline/) is the first end-to-end ML project — you'll
use everything from Units 1–2 to clean, explore, and model a real dataset.
