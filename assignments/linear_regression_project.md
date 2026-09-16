---
title: "Linear Regression Project Rubric (20 points)"
layout: single
sidebar:
  nav: "ml"
---

Your notebook must have these four `##` markdown headings, in this order: **Overview of Data**, **Processing Data**, **Linear Regression**, and **Analysis**. Each section should include explanatory markdown text, not just code.

> In the **Overview of Data** section, keep the writing in markdown only. No code cells or output should appear there.

### Format (2 pts)

| Criterion | Full credit | Partial | Pts |
|---|---|---|---|
| **Headings and exposition** | All four `##` headings are present with these names and in the correct order. Every section includes explanatory markdown. | A heading is missing, renamed, out of order, or a section is mostly code with little explanation. | 2 |

### 1. Overview of Data (3 pts)

| Criterion | Full credit | Partial | Pts |
|---|---|---|---|
| **Source and description** | States the dataset source with a link and explains, in general terms, what the dataset is about and what information it contains. | The source is given, but the dataset is only briefly or vaguely described. | 2 |
| **Origin and motivation** | Briefly explains where the data came from (for example: experiment, survey, public dataset, simulation, or news data) and why you chose it. | Either the origin or the motivation is missing. | 1 |

### 2. Processing Data (2 pts)

| Criterion | Full credit | Partial | Pts |
|---|---|---|---|
| **Loading and cleaning** | The data loads correctly in the notebook. If applicable, explains what cleaning was done, if any (for example: dropped missing values, removed rows, removed outliers, adjusted or binned data, or no cleaning was needed). | The data loads, but cleaning or filtering is done without any explanation. | 2 |

### 3. Linear Regression (5 pts)

| Criterion | Full credit | Partial | Pts |
|---|---|---|---|
| **Choice of variables** | Clearly names the variables used for x and y, explains why they may be related, and predicts the direction of the relationship (for example: positive or negative). | The variables are named, but the reason for the relationship is weak, missing, or unclear. | 3 |
| **Fit and equation** | A line is computed in code, and the equation is printed from the code output. | The equation is typed by hand, incomplete, or missing. | 2 |

### 4. Analysis (8 pts)

Please google how to add these features to a graph if you don't know how!

| Criterion | Full credit | Partial | Pts |
|---|---|---|---|
| **Graph** | Includes a scatter plot of the original data points with the fitted line, clearly labeled axes, and a title, and a legend. | The graph is incomplete, missing labels, missing a title, or does not clearly show the fitted line. | 2 |
| **Interpreting R²** | R² is printed from the code and explained in words using a sentence such as: "x explains about __% of the variation in y." The explanation matches the pattern shown in the plot. | R² is reported but not explained, or the explanation does not match the plot or the value of R². | 3 |
| **Conclusion** | Answers the question, "Is a line a reasonable model for this data?" using the R² and the plot as evidence. Gives at least one sensible idea for why the fit is not better or what a better model might use (for example: another variable, a curve, or splitting the data). | The conclusion is present but does not match the evidence, or it gives no idea for improving the model. | 3 |
