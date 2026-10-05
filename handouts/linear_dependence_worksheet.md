---
geometry: margin=0.9in
fontsize: 11pt
---

```{=latex}
\begin{center}{\Large\bfseries Which Equation Fits Best?}\end{center}
\vspace{-0.05in}
Name: \underline{\hspace{3in}} \hfill Date: \underline{\hspace{1.5in}}
```

## The data

A small dataframe has four features, $x_1, x_2, x_3, x_4$, and a target $y$. We want an equation of the form

$$\hat{y} = b_1 x_1 + b_2 x_2 + b_3 x_3 + b_4 x_4$$

that predicts $y$ as accurately as possible.

| row | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $y$ |
|:---:|:-----:|:-----:|:-----:|:-----:|:---:|
| 0   | 1     | 2     | 3     | 1     | 9   |
| 1   | 2     | 1     | 3     | 0     | 7   |
| 2   | 3     | 3     | 6     | 2     | 17  |
| 3   | 4     | 1     | 5     | 0     | 11  |
| 4   | 5     | 2     | 7     | 1     | 17  |

Three people each fit a model to this data and report an equation:

- Equation A: $\hat{y} = 2x_1 + 3x_2 + 0x_3 + 1x_4$
- Equation B: $\hat{y} = 1x_1 + 2x_2 + 1x_3 + 1x_4$
- Equation C: $\hat{y} = 0x_1 + 1x_2 + 2x_3 + 1x_4$

## Part 1: Check the fits

**1.** Use each equation to predict $y$ for every row. Fill in the table, then compute the sum of squared errors for each equation, $\text{SSE} = \sum_i (y_i - \hat{y}_i)^2$, summing over all five rows.

```{=latex}
{\renewcommand{\arraystretch}{1.6}
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline
row & actual $y$ & A prediction & B prediction & C prediction \\ \hline
0 & 9 & \hspace{0.9in} & \hspace{0.9in} & \hspace{0.9in} \\ \hline
1 & 7 & & & \\ \hline
2 & 17 & & & \\ \hline
3 & 11 & & & \\ \hline
4 & 17 & & & \\ \hline
\textbf{SSE} & & & & \\ \hline
\end{tabular}
\end{center}}
```

\vspace{0.1in}

**2.** Which equation is the best fit?

\newpage

## Part 2: Make sense of it

**3.** Explain what you found? Use the numbers in the data table to support your answer.

\vspace{1.0in}

**4.** Compare the coefficient on $x_4$ across the three equations with the coefficients on $x_1$, $x_2$, and $x_3$. What do you notice? What is different about $x_4$?

\vspace{0.9in}

**5.** Is there a fourth equation that also fits this data perfectly? Write one down, and check it against at least two rows.

\vspace{0.9in}

**6.** What does this example imply about interpreting the relationship between features and the target variable in a regression problem?

\vspace{0.7in}

## Optional: check it in code

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "x1": [1, 2, 3, 4, 5],
    "x2": [2, 1, 3, 1, 2],
    "x3": [3, 3, 6, 5, 7],
    "x4": [1, 0, 2, 0, 1],
    "y":  [9, 7, 17, 11, 17],
})

X = df[["x1", "x2", "x3", "x4"]].to_numpy()
print(np.linalg.matrix_rank(X))      # how many independent columns?
print(np.linalg.cond(X))             # condition number
```

\newpage

# Answer key (facilitator copy)

**Question 1.** All three equations produce identical predictions: 9, 7, 17, 11, 17. Every error is 0, so $\text{SSE} = 0$ for A, B, and C.

**Question 2.** All of them. Each is a perfect fit, so there is no single best equation.

**Question 3.** The columns are linearly dependent: $x_3 = x_1 + x_2$ in every row ($3 = 1+2$, $3 = 2+1$, $6 = 3+3$, $5 = 4+1$, $7 = 5+2$). So $x_3$ carries no information that $x_1$ and $x_2$ do not already carry, and any weight placed on $x_3$ can be traded for weight on $x_1$ and $x_2$. For example, going from A to B moves 1 unit of weight onto $x_3$ and takes 1 unit off each of $x_1$ and $x_2$, which changes nothing because $x_3$ is exactly $x_1 + x_2$.

**Question 4.** The coefficient on $x_4$ is 1 in all three equations, while the coefficients on $x_1$, $x_2$, $x_3$ all change. The column $x_4$ is not a combination of the others, so nothing can be traded for it: any change to its weight makes the predictions worse. Only the dependent columns have freedom.

**Question 5.** Any equation of the form

$$\hat{y} = (2 + t)\,x_1 + (3 + t)\,x_2 - t\,x_3 + 1\,x_4$$

works. A is $t = 0$, B is $t = -1$, C is $t = -2$. A new one: $t = 1$ gives $\hat{y} = 3x_1 + 4x_2 - 1x_3 + 1x_4$. Check row 0: $3(1) + 4(2) - 3 + 1 = 9$. Check row 3: $3(4) + 4(1) - 5 + 0 = 11$. Both match. Students who change the $x_4$ coefficient should find the check fails.

**Question 6.** Infinitely many, one for every real value of $t$. The question "what are the coefficients?" has no unique answer when columns are linearly dependent. The data cannot distinguish between the solutions, so the choice among them comes from outside the data (a regularizer, a pseudoinverse convention, or dropping a column).

**Discussion points.**

- The design matrix $X$ has rank 3 but 4 columns, so $X^T X$ is singular and the normal equations have a whole line of solutions rather than one. The line runs in the direction $(1, 1, -1, 0)$, which is why $b_4$ is pinned down while $b_1, b_2, b_3$ are not.
- The smallest singular value of $X$ is exactly 0 in theory. In floating point it shows up as roughly $10^{-16}$, so `np.linalg.cond(X)` reports something like $10^{16}$ instead of infinity. This is the same "high condition number" warning that statsmodels prints.
- Dropping $x_3$ fixes it: the remaining columns $x_1, x_2, x_4$ have rank 3 and a condition number of about 16, and the unique best fit is $\hat{y} = 2x_1 + 3x_2 + 1x_4$.
- Real data is rarely this exact, but near-dependence behaves similarly: many coefficient vectors fit almost equally well, and the coefficients become unstable.
