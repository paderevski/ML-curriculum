---
title: "Unit 02: Regression, Correlation, and Linear Algebra"
layout: unit
sidebar:
  nav: "ml"
permalink: /notebooks/02-regression-correlation/
---

We derive the linear regression line of best fit from scratch, then implement
it in Python, learning NumPy and working with matrices along the way. We talk
about goodness-of-fit measures, introduce some linear algebra, and analyze
some data.

## Least Squares

The math behind least squares, then applied in NumPy from scratch.

#### Key ideas

- **Ordinary least squares**: minimize the sum of squared residuals; derive the
  slope and intercept analytically
- **Residuals and model fit**: what a good fit looks like vs. a poor one
- One idea from calculus does the work: the derivative is zero at a minimum

#### Notes

> [Linear regression derivation](../../notes/Linear_regression_derivation.md)
> ([PDF](../../notes/Linear_regression_derivation.pdf))
>
> New to derivatives? [Derivatives crash course](../../notes/derivatives-crash-course.md)
> ([PDF](../../notes/derivatives-crash-course.pdf))

#### Notebooks & materials

- **Homework** [Least Squares](./Least-Squares.ipynb):
  Implement the closed-form solution in NumPy and check it against the data.

## Correlation and R²

Measuring how well a line fits and how strongly two variables are related.

#### Key ideas

- **$R^2$** (coefficient of determination): how much of the variance in $y$ your model explains
- **Pearson correlation**: linear association between two variables; correlation is not causation
- **Measures of spread**: variance and standard deviation in the context of regression

#### Notes

> [Correlation coefficient](../../notes/Correlation_Coefficient.md)
> ([PDF](../../notes/Correlation_Coefficient.pdf))

#### Notebooks & materials

- **Homework** [Correlation](./Correlation.ipynb):
  Compute Pearson correlation and $R^2$ for several paired variables and build
  intuition for what these numbers do and don't tell you.

## NumPy

The array operations used throughout the unit: indexing, slicing, and basic
array math, as a refresher or first exposure.

#### Notebooks & materials

- **Homework** [Intro to NumPy](./Numpy-Intro.ipynb):
  Work through the notebook, then submit it.

## Linear Regression Project

Find your own dataset, fit a single-variable linear regression, and defend the
fit. You'll submit a draft, get feedback, then revise for a final grade.

#### Notebooks & materials

- **Project** Linear regression lab: Pick a dataset with numerical fields, fit
  the line, report $R^2$, and explain in markdown whether it justifies the model.
- **Reference** [Grading rubric](../../assignments/linear_regression_project.md):
  The four sections your notebook needs and how each is scored.
- **Reference** [Loading data files in Colab](../../notes/read_csv_in_colab.md):
  How to get your CSV into a Colab notebook.

## Linear Algebra in Python

Building the matrix foundation that later units rely on heavily. The goal is
fluency with NumPy matrix operations, not proof-writing.

#### Key ideas

- **Vectors and matrices**: notation, shapes, row vs. column vectors
- **Matrix multiplication**: how dot products chain together; why order matters
- **Transpose and inverse**: what they do and when they exist
- **NumPy**: indexing, slicing, broadcasting, `@` for matrix multiply

#### Notebooks & materials

- **Homework** [Linear Algebra and Python](./Linear_Algebra_and_Python.ipynb):
  Vectors, matrices, and the NumPy operations that manipulate them.
- **Homework** [Matrix Indexing Warm-up](./Matrices_Index_Warmup-Student.ipynb):
  Selecting rows, columns, and submatrices.
- **Homework** [Intro to Matrices in NumPy](./Intro_to_Matrices_in_NumPy.ipynb):
  Matrix multiply, transpose, inverse, and solving linear systems.

## Linearize

Linear regression on curvilinear data: transform the data so a straight line
fits, then transform back.

#### Notebooks & materials

- **Homework** [Linearize](./Linearize_Student.ipynb):
  Fit curved data by linearizing it first.
