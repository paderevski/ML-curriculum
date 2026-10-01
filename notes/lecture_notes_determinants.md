---
title: "Lecture Notes: Linear Systems, Determinants, and Ill-Conditioning"
---

## 1. Solving Ax = b with the inverse

A linear system can be written $A\mathbf{x} = \mathbf{b}$. If $A$ has an inverse, multiply both sides by it:

$$\mathbf{x} = A^{-1}\mathbf{b}$$

This is the matrix version of dividing both sides of $ax = b$ by $a$. The warm-up system $x + y = 10,\ x - y = 2$ is $A = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, and $A^{-1}\mathbf{b}$ gives $(6, 4)$.

## 2. The determinant is what we divide by

Every formula for the inverse divides by $\det(A)$. For a 2x2,

$$A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

and Cramer's rule says $x_i = \det(A_i)/\det(A)$, where $A_i$ is $A$ with column $i$ replaced by $\mathbf{b}$. If $\det(A) = 0$ we are dividing by zero, so there is no inverse and no unique solution. Depending on $\mathbf{b}$, the system has either no solution (our $x + y = 10,\ x + y = 12$) or infinitely many (change the 12 to a 10).

## 3. When is the determinant zero?

The easy cases: two rows are identical, or one row is a constant multiple of another ($r_1 = c\, r_2$). In the warm-up, system 2 has two identical rows on the left, and in system 3 row 3 is exactly $2 \cdot r_1$. Geometrically, two of the equations describe the "same direction" and so the rows carry less information than it looks like.

## 4. Linear combinations of rows

Rows do not have to be copies of each other. Take

$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 5 & 7 & 9 \end{pmatrix}$$

Here $r_1 + r_2 = r_3$. Expanding along the first row,

$$\det(A) = 1(45 - 42) - 2(36 - 30) + 3(28 - 25) = 3 - 12 + 9 = 0.$$

The general principle: if some combination of the rows adds up to the zero row, that is $c_1 r_1 + c_2 r_2 + c_3 r_3 = \mathbf{0}$ with the $c_i$ not all zero, then $\det(A) = 0$. Here the combination is $r_1 + r_2 - r_3 = \mathbf{0}$. Section 3 is the special case where the combination involves only two rows.

## 5. The homogeneous test

The statement above can be read as an equation. A combination of rows is $\mathbf{x}^T A$, so "some nontrivial combination of rows is zero" says

$$\mathbf{x}^T A = \mathbf{0}^T \text{ has a nonzero solution } \mathbf{x}.$$

(For the example, $\mathbf{x} = (1, 1, -1)$.) The same is true for columns: if $A\mathbf{x} = \mathbf{0}$ has a nonzero solution (here $\mathbf{x} = (1, -2, 1)$), then $\det(A) = 0$. This is the cleanest way to think about it: the determinant is zero exactly when there is some nonzero input that the matrix sends to zero, and information is lost. A matrix that loses information cannot be undone.

## 6. Close to zero is also bad

A determinant that is zero is a disaster; a determinant that is merely very small is a quieter disaster. The inverse still exists, but we are dividing by a tiny number, so small errors in $\mathbf{b}$ (measurement noise, rounding) get blown up in $\mathbf{x}$. Such a system is called ill-conditioned. This is the subject of the ill-conditioning handout.

## 7. Why this matters in machine learning

Suppose we fit a linear model by solving the normal equations $(X^T X)\mathbf{w} = X^T \mathbf{y}$. Solving this means inverting $X^T X$. If two features (columns of $X$) are collinear, or nearly so (a very high Pearson $r$), then $X^T X$ is singular or nearly singular, and we are back in sections 4 through 6. The weights become huge, unstable, and swing wildly with small changes in the data.

A practical remedy is to drop one of the redundant features, since it carries almost no information the other does not already carry. Since $\det(A) = \det(A^T)$, everything above applies equally to rows and columns, so "dependent rows" and "dependent columns" are the same problem.
