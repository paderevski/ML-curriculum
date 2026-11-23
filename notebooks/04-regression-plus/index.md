---
title: "Unit 04: Regression++"
layout: unit
sidebar:
  nav: "ml"
permalink: /notebooks/04-regression-plus/
---

The longest unit, where regression grows into a real professional toolkit and
the linear algebra from Unit 2 finally pays off. You'll move from
single-variable models to multi-feature ones, learn why unregularized models
overfit, and discover that high-dimensional data often has hidden
low-dimensional structure you can exploit.

## Multilinear Regression

Introducing multiple features with a toy dataset, then scaling up to real
[WHO life-expectancy data](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/data).

#### Key ideas

- Fitting a model with many input features; the design matrix $X$
- Reading coefficients: each one is the effect of its feature *holding the others fixed*
- Always look at the data and its columns before you fit anything

#### Notes

> [Multilinear regression lecture notes](../../notes/Multilinear_regression.html)

#### Notebooks & materials

- **In class** [Test Scores](./Test_Scores.ipynb):
  A small toy dataset to see multiple regression end to end. Read the notebook
  carefully; you'll answer questions at the end of class.
- **Demo + HW** [Life Expectancy](./Life_Expectancy_Student.ipynb):
  We read through it together in class. For homework, do problems 1–3 at the
  end in a copy of the notebook.
- **Reference** [Life Expectancy column descriptions](./life-expectancy.md):
  What each of the WHO dataset's columns means.

## Solving Linear Systems

What's actually happening when we solve for regression coefficients: Gaussian
elimination, what it costs, and why some systems are fragile.

#### Key ideas

- Solving $A\mathbf{x} = \mathbf{b}$ by elimination, and why we don't compute $A^{-1}$
- Gaussian elimination takes about $n^3/3$ operations
- An ill-conditioned matrix turns tiny changes in $\mathbf{b}$ into big changes in $\mathbf{x}$

#### Notes

> [Solving linear systems and the condition number](../../notes/lecture_notes_determinants.md)
> ([PDF](../../notes/lecture_notes_determinants.pdf))

#### Notebooks & materials

- **Warm-up** [Linear systems](../../handouts/gaussian_warmup_handout.md):
  Solve some small systems by hand: one solution, none, or infinitely many?
- **Warm-up** [Ill-conditioned matrices](../../handouts/warmup_ax_b.pdf):
  Two nearly identical systems with very different answers.
- **Reference** [Gaussian elimination cost worksheet](../../handouts/ge_cost_worksheet.md):
  Practice based on the class notes on Gaussian elimination, with answers.

## Linear Dependence and Collinearity

When features carry the same information, regression can't tell them apart.
We see it by hand, then in code.

#### Key ideas

- Linearly dependent columns: one column is a combination of others
- Collinear features make coefficients unstable and hard to interpret
- The correlation matrix is the first place to look for it

#### Notebooks & materials

- **Warm-up** [Which equation fits best?](../../handouts/linear_dependence_worksheet.md):
  A warm-up on linear dependence with a small four-feature dataset.
- **Demo** [Exploring Collinearity](./collinearity.ipynb):
  Build a random dataset, make columns linearly dependent on purpose, and watch
  what happens to the correlation matrix.

## Normalization and Regularization

Continuing with the life-expectancy data: scaling features, adding L1/L2
penalties, and sweeping $\alpha$ to find the best model.

#### Key ideas

- Why scale matters before regularization
- **Ridge** (L2) shrinks coefficients; **Lasso** (L1) can set them to zero
- Choosing $\alpha$ with a sweep, and reading the sweep plot

#### Notebooks & materials

- **Homework** [Life Expectancy, Part 2](./Life_Part_2_Student.ipynb):
  Normalization, regularization, and feature selection on the WHO data.

## SVD

Matrix multiplication as a geometric transformation, then using the singular
value decomposition to compress an image of Gauss to a fraction of its size.

#### Key ideas

- Every matrix is a rotation, a stretch, and another rotation
- A rank-$k$ approximation keeps the $k$ largest singular values
- Image compression as a visual intuition for what "dimension" means in data

#### Notes

> [SVD notes](../../notes/svd_notes_ml.md)

#### Notebooks & materials

- **In class** [Visualizing Transformation Matrices](./Visualizing_Transformation_Matrices.ipynb):
  See what a $2 \times 2$ matrix does to the plane.
- **In class** [Low-Rank Matrix Approximations](./Low_Rank_Matrix_Approximations.ipynb):
  Build rank-$k$ approximations from the SVD.
- **Homework** [Image Compression](./Image-Compression.ipynb):
  Compress a photo of Gauss with the SVD. You'll need [the image](./gauss.jpg).

## PCA

Projecting data onto its principal components, then using PCA as a
preprocessing step before regression.

#### Key ideas

- Principal components are the directions of maximum variance
- Reducing features while keeping most of the information
- PCA before regression: fewer, uncorrelated features

#### Notebooks & materials

- **Demo** [PCA on Life Expectancy](./PCA.ipynb):
  A worked PCA of the life-expectancy data: vary the number of components and
  watch the regression score change. It's the model for the PCA pass of the
  [project](#project-diy-linear-regression).

## Project: DIY Linear Regression++

The major deliverable for the unit, built across several class days. Start
with a dataset you choose, then work through the full pipeline: feature
analysis (distributions, collinearity), normalization, L1/L2 $\alpha$
selection with a sweep plot, model interpretation, and a PCA dimension sweep.
Finish with a written defense of your "best model" choice.

#### Notebooks & materials

- **Project** [DIY Linear Regression++](../../notes/DIY-LinReg-Plus.md):
  The project requirements. Submitted in stages: draft, regularization pass,
  PCA pass, final.
- **Reference** [Grading rubric](../../assignments/LinRegPlusPlus_Rubric.md):
  How each section of your notebook is scored.
- **Reference** [Where to find data](../../handouts/data-sources-student.md):
  About 100 places to find a dataset, grouped by topic. You need at least 8
  numerical features.
