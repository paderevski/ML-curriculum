---
title: "DIY Linear Regression++ -- Project Rubric"
subtitle: "Unit 4 -- 40 points"
---

Your notebook needs a `#` title and an `##` author line at the top, and the
four sections below as `##` headings. All discussion goes in markdown cells,
not code comments. Every graph needs a title and axis labels, with a legend
where one is needed. Run all cells before submitting.

*Note*: +1 is possible for excellent work in each section. Punitive points may also apply for egregious errors or omissions.

**Note**: I am expecting you to copy/paste the code I gave you, with needed modifications and additions. Any deviation from this
expectation should be documented and explained.

## Presentation (3 pts)

| Criterion | Full credit | Partial | Pts |
|:----------|:------------|:--------|:---:|
| Title, author, structure | `#` title and `##` author at top; the four sections present as `##` headings, in order; discussion in markdown. | Missing title or author, sections renamed or out of order, or discussion left in code comments. | 2 |
| Notebook runs | Every cell has output, and the notebook runs top to bottom from a fresh runtime. | Cells unrun, or output inconsistent with the code that produced it. | 1 |

## 1. Data and Features (13 pts)

| Criterion | Full credit | Partial | Pts |
|:----------|:------------|:--------|:---:|
| Source and description | Cited with a link. What a row represents, how many rows and features, what the target variable is and why you chose it. | Source given but the data barely described, or no link. | 3 |
| Missing data and categoricals | Says what was missing and how much, what you did about it, and why. Categorical features encoded with the choice explained (or stated that there are none). | Handled in code without explanation, or a strategy named with no reasoning. | 3 |
| Normalization | Features normalized correctly. | Normalized incorrectly, or applied inconsistently. | 2 |
| Distributions | Distributions plotted for the features, with **selected** discussion of what they show -- skew, outliers, odd scales, suspicious values. (You don't have to describe every graph, just describe trends or interesting patterns.)  | Plots present with no discussion, or generic discussion that would fit any dataset. | 2 |
| Correlation and collinearity | Correlation structure shown (heatmap or matrix) and discussed. Identifies which features appear collinear. Also mention features which seem to provide little information to the model.| Correlations displayed but little or no discussion. | 3 |

## 2. Regression and Regularization (12 pts)

| Criterion | Full credit | Partial | Pts |
|:----------|:------------|:--------|:---:|
| Baseline model and fit | Multiple regression fit, goodness of fit $R^2$ reported and interpreted in plain language -- what the number means for this data, not just its value. | Metric reported without interpretation, or an interpretation that contradicts the evidence. | 3 |
| Coefficient plot (before) | Coefficients plotted and discussed. Which features matter, which directions, anything surprising. | Plot without discussion. | 2 |
| L1 and L2 with alpha selection | Both penalties applied, alpha swept across a range, results plotted, and your chosen alpha justified from the sweep. | One penalty only, no sweep, or an alpha chosen with no reasoning. | 4 |
| Coefficient plot (after) | Updated plot with a comparison to the baseline. Says which coefficients disappeared or shrank. | Updated plot with no comparison or no interpretation. | 3 |

## 3. Model Interpretation (6 pts)

| Criterion | Full credit | Partial | Pts |
|:----------|:------------|:--------|:---:|
| Coefficients in context | Specific coefficients read in the units of the problem, with attention to what normalization did to their meaning. | Coefficients described only as large or small. | 3 |
| True vs. predicted plot | Plotted with a reference line, and discussed -- where the model does well, where it fails, any structure in the misses. | Plot present without discussion, or discussion that ignores what the plot shows. | 3 |

## 4. PCA and Best Model (6 pts)

| Criterion | Full credit | Partial | Pts |
|:----------|:------------|:--------|:---:|
| PCA and explained variance | PCA performed, cumulative explained variance plotted, and read: how many components capture most of the variance, and what that says about the data's real dimensionality. | Plot present but not interpreted. | 3 |
| Accuracy across dimensions | Model accuracy evaluated across a range of component counts and plotted, with the tradeoff discussed. | A single dimension tried, or results not compared. | 3 |

## Final defense

Pick one model and describe it. (There may not be a clear 'best' -- but you can pick
one for your own, logical, reasons). For full credit
name the model and its settings, support the choice with specific numbers from
your own sweeps and plots, and describe the overall goodness of fit. Finally,
reflect on the appropriateness of a linear model for the problem, and suggest
possible ways to improve the result with a different analysis

Your analysis should be specific.
A reflection that would read the same for any dataset does not earn full credit,
even if everything in it is true.
