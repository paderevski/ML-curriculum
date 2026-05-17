---
title: "Unit 03: Linear Algebra"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/03-linear-algebra/
---

A self-contained two-day unit to build the matrix foundation that later units
rely on heavily — SVD, PCA, image compression, and neural network weight updates
all speak this language. The goal is fluency with NumPy matrix operations, not
proof-writing.

## Concepts You'll Learn About

- **Vectors and matrices** — notation, shapes, the difference between a row
  and a column vector
- **Matrix multiplication** — how dot products chain together; why order matters
- **Transpose and inverse** — what they do geometrically and when they exist
- **NumPy array operations** — indexing, slicing, broadcasting, `@` for matrix
  multiply

## Topics

- **Linear algebra in Python** — vectors, matrices, and the NumPy operations
  that manipulate them.
  {% include nb.html local="Linear_Algebra_and_Python.ipynb" %}

- **Matrix indexing warmup** — practice selecting rows, columns, and
  submatrices; builds the indexing fluency used everywhere else.
  {% include nb.html local="Matrices_Index_Warmup-Student.ipynb" %}

- **Intro to matrices in NumPy** — matrix multiply, transpose, inverse, and
  solving linear systems.
  {% include nb.html local="Intro_to_Matrices_in_NumPy.ipynb" %}

## What's next

[Unit 04](../notebooks/04-first-pipeline/) is the first end-to-end ML project —
you'll use everything from Units 1–3 to clean, explore, and model a real dataset.
