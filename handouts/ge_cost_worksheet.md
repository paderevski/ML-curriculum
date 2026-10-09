---
title: "Gaussian Elimination and What It Costs"
geometry: margin=1in
header-includes:
  - \usepackage{amsmath}
  - \pagenumbering{gobble}
---

Name: \underline{\hspace{3in}} \hfill Date: \underline{\hspace{1.2in}}

## Part 1: Row operations

The goal of Gaussian elimination is to turn a system of equations into a staircase shape (everything below the diagonal is 0) using one move over and over: subtract a multiple of one row from another row. We write the system as an augmented matrix, where the bar separates the coefficients from the right-hand sides.

All the examples on this worksheet are chosen so that no row swaps are needed.

**Example.** Solve
$$
\begin{aligned}
x + 2y + z &= 8 \\
2x + 5y + 3z &= 21 \\
3x + 8y + 7z &= 40
\end{aligned}
\qquad\text{which is}\qquad
\left[\begin{array}{ccc|c} 1 & 2 & 1 & 8 \\ 2 & 5 & 3 & 21 \\ 3 & 8 & 7 & 40 \end{array}\right]
$$

*Step 1.* The pivot is the 1 in the top left. To clear the 2 below it, subtract 2 times row 1 from row 2. To clear the 3, subtract 3 times row 1 from row 3. Every number in the row changes, including the one after the bar:
$$
\left[\begin{array}{ccc|c} 1 & 2 & 1 & 8 \\ 0 & 1 & 1 & 5 \\ 0 & 2 & 4 & 16 \end{array}\right]
$$

a. Finish the job. Use the new pivot (the 1 in the middle) to clear the 2 below it, then solve from the bottom up. $x = $ ______, $y = $ ______, $z = $ ______.

\vspace{1.3in}

**On your own.** Solve the system below from scratch, writing out the augmented matrix after each step.
$$
\begin{aligned}
x + 2y + z &= 1 \\
3x + 7y + 6z &= 5 \\
2x + 8y + 16z &= 12
\end{aligned}
$$

\vspace{2.2in}

**Optional.** Keep going from your staircase. Divide each row by its pivot, then use the bottom row to clear the entries above the bottom pivot, then the middle row to clear the entry above the middle pivot, until the left side is the identity matrix and the right side is the answer. How does this compare to back substitution?

\vspace{1.5in}

## Part 2: Counting the work

A flop is one arithmetic operation on two numbers: a multiplication, division, addition, or subtraction each counts as 1. Here are the ground rules for counting.

- Count only the work done on the coefficient matrix (the left side of the bar). Ignore the right-hand side.
- In each step, you know the entries below the pivot become 0, so don't count work to produce them. Count only the entries you actually have to compute.
- For each row you fix, count 1 division to get the multiplier, then 1 multiplication and 1 subtraction for each entry that has to change.

For example, in Part 1's example, step 1 fixes 2 rows. Each row costs 1 division, plus 2 multiplications and 2 subtractions (the two entries to the right of the pivot). That is 5 flops per row, so 10 flops in step 1.

a. Fill in the table for the 3 by 3 case.

| Step | Rows to fix | Entries to update per row | Flops per row | Flops in step |
|:----:|:-----------:|:-------------------------:|:-------------:|:-------------:|
| 1    |             |                           |               |               |
| 2    |             |                           |               |               |

Total flops for 3 by 3: ______

b. Do the same for a 4 by 4 matrix.

| Step | Rows to fix | Entries to update per row | Flops per row | Flops in step |
|:----:|:-----------:|:-------------------------:|:-------------:|:-------------:|
| 1    |             |                           |               |               |
| 2    |             |                           |               |               |
| 3    |             |                           |               |               |

Total flops for 4 by 4: ______

c. Now an $n$ by $n$ matrix. In step $k$, how many rows have to be fixed? ______ How many entries to update in each of those rows? ______ How many flops per row? ______ So how many flops in step $k$? ______

d. It is easier to add things up if you let $j = n - k$, the number of rows below the pivot. Then $j$ runs through the values $1, 2, \ldots, n-1$ as the steps go along, and the work in a step looks like $j + 2j^2$. Write the total as a sum, and then use these two facts to simplify it:
$$
\sum_{i=1}^{m} i = \frac{m(m+1)}{2} \approx \frac{m^2}{2}
\qquad\qquad
\sum_{i=1}^{m} i^2 = \frac{m(m+1)(2m+1)}{6} \approx \frac{m^3}{3}
$$
For large $n$, only the highest power of $n$ matters. What is the total flop count in terms of $n$?

\vspace{1.3in}

e. Check your formula against your answers to a and b.

f. If you double $n$, how much longer does elimination take? If a computer does a billion flops per second, roughly how long does it take for $n = 1000$?

\vspace{0.8in}

## Part 3: The determinant, the slow way

You may know the cofactor formula for a determinant. Expanding along the first row,
$$
\det(A) = \sum_{j=1}^{n} (-1)^{1+j}\, a_{1j} \det(M_{1j}),
$$
where $M_{1j}$ is the $(n-1)$ by $(n-1)$ matrix left over after deleting row 1 and column $j$. Each of those smaller determinants is found the same way, by expanding again, until you hit $1$ by $1$ matrices, where the determinant is just the entry.

Let $D(n)$ be the number of flops to find the determinant of an $n$ by $n$ matrix this way. Count a multiplication or an addition or a subtraction as 1 flop, and treat the plus and minus signs as free.

a. $D(1) = 0$, since there is nothing to compute. For $n \geq 2$, there are $n$ smaller determinants, each costing $D(n-1)$. Then you need $n$ multiplications (each $a_{1j}$ times its smaller determinant) and $n - 1$ additions or subtractions to combine them. Write $D(n)$ in terms of $D(n-1)$.

\vspace{0.6in}

b. Use your formula to find $D(2)$, $D(3)$, and $D(4)$. Check $D(2)$ by hand: you know that the determinant of a 2 by 2 matrix is $ad - bc$.

\vspace{1.0in}

c. Compare to elimination. Fill in the table (the elimination flop counts come from Part 2).

| $n$ | Elimination flops | Cofactor flops |
|:---:|:-----------------:|:--------------:|
| 3   |                   |                |
| 4   |                   |                |

d. Each time $n$ goes up by one, the cofactor count gets multiplied by about what? Look at your recurrence. What kind of growth is that? Roughly how many flops would a 20 by 20 determinant take? (Hint: $20! \approx 2.4 \times 10^{18}$.) At a billion flops per second, how many years is that?

\vspace{1.0in}

e. There is a much faster way. After elimination with no row swaps, the determinant of $A$ is the product of the pivots (the numbers on the diagonal of the staircase). Try it on the example from Part 1: find the product of your pivots, then compute the determinant of that matrix with the cofactor formula and compare.

\vspace{1.4in}

## Part 4: A matrix where the numbers blow up

Here is a special 4 by 4 matrix.
$$
A = \begin{bmatrix} 1 & 0 & 0 & 1 \\ -1 & 1 & 0 & 1 \\ -1 & -1 & 1 & 1 \\ -1 & -1 & -1 & 1 \end{bmatrix}
$$

a. Do Gaussian elimination on $A$ (no right-hand side this time), writing out the matrix after each step. The pivots all tie in size with the entries below them, so there are no swaps.

\vspace{2.2in}

b. What is the largest entry in the original matrix? What is the largest entry you see anywhere during the elimination? Look at the last column as you go along. What pattern do you see?

\vspace{0.8in}

c. Now guess what happens for the same pattern of matrix in size $n$ by $n$ (1s on the diagonal, $-1$s below it, 1s in the last column). What would the bottom right entry of the staircase be? Check your guess on the 3 by 3 case.

\vspace{0.8in}

d. Use your formula to predict the bottom right entry for $n = 10$ and for $n = 60$. A computer stores about 16 significant digits for each number. What do you think might go wrong for $n = 60$?

\vspace{1.0in}

\newpage

# Answer Key

## Part 1

Example, step 2: subtract 2 times row 2 from row 3 to get $[\,0\ \ 0\ \ 2 \mid 6\,]$. So $z = 3$, $y = 5 - 3 = 2$, $x = 8 - 4 - 3 = 1$.

On your own: the multipliers are 3 and 2 for step 1, giving
$$
\left[\begin{array}{ccc|c} 1 & 2 & 1 & 1 \\ 0 & 1 & 3 & 2 \\ 0 & 4 & 14 & 10 \end{array}\right]
$$
then 4 in step 2, giving a last row of $[\,0\ \ 0\ \ 2 \mid 2\,]$. So $z = 1$, $y = -1$, $x = 2$.

Optional: divide the last row by 2 to get $[\,0\ \ 0\ \ 1 \mid 1\,]$. Subtract 3 times it from row 2 to get $[\,0\ \ 1\ \ 0 \mid -1\,]$, and subtract it from row 1 to get $[\,1\ \ 2\ \ 0 \mid 0\,]$. Then subtract 2 times row 2 from row 1 to get $[\,1\ \ 0\ \ 0 \mid 2\,]$. The right side now reads off the answer directly, with no back substitution needed, but it takes more work (about $n^3$ flops overall instead of about $2n^3/3$ plus a lower-order back substitution).

## Part 2

a. Step 1: 2 rows, 2 entries per row, 5 flops per row, 10 flops. Step 2: 1 row, 1 entry per row, 3 flops per row, 3 flops. Total: 13.

b. Step 1: 3 rows, 3 entries, 7 flops per row, 21 flops. Step 2: 2 rows, 2 entries, 5 flops per row, 10 flops. Step 3: 1 row, 1 entry, 3 flops, 3 flops. Total: 34.

c. In step $k$: $n - k$ rows, $n - k$ entries per row, $1 + 2(n-k)$ flops per row, $(n-k)(1 + 2(n-k))$ flops in the step.

d. With $j = n - k$, the total is $\sum_{j=1}^{n-1} (j + 2j^2)$. Using the facts with $m = n - 1$:
$$
\frac{(n-1)n}{2} + 2 \cdot \frac{(n-1)n(2n-1)}{6} = \frac{n(n-1)(4n+1)}{6} \approx \frac{2n^3}{3}.
$$

e. $n = 3$: $3 \cdot 2 \cdot 13 / 6 = 13$. $n = 4$: $4 \cdot 3 \cdot 17 / 6 = 34$. Both match.

f. Doubling $n$ multiplies the work by about 8. For $n = 1000$ it is about $\tfrac{2}{3} \times 10^9$ flops, so under a second.

## Part 3

a. $D(n) = n\,D(n-1) + n + (n-1) = n\,D(n-1) + 2n - 1$.

b. $D(2) = 2 \cdot 0 + 3 = 3$, which matches $ad - bc$ (2 multiplications and 1 subtraction). $D(3) = 3 \cdot 3 + 5 = 14$. $D(4) = 4 \cdot 14 + 7 = 63$.

c.

| $n$ | Elimination flops | Cofactor flops |
|:---:|:-----------------:|:--------------:|
| 3   | 13                | 14             |
| 4   | 34                | 63             |

(For reference, $n = 5$ gives 70 versus 324, and $n = 10$ gives 615 versus about 9.9 million.)

d. The count gets multiplied by roughly $n$ each time, so it grows like a factorial. In fact $D(n) \approx e \cdot n!$. For $n = 20$ that is about $6.6 \times 10^{18}$ flops, which at a billion flops per second is about 210 years.

e. The pivots from the Part 1 example are $1, 1, 2$, with product $2$. The cofactor expansion of that matrix is $1(35 - 24) - 2(14 - 9) + 1(16 - 15) = 11 - 10 + 1 = 2$. They match. So the determinant costs only about $2n^3/3$ flops through elimination, instead of factorial work.

## Part 4

a. Step 1 adds row 1 to rows 2, 3, 4, so the last column becomes $1, 2, 2, 2$ (rows 2 to 4 are now $[\,0\ \ 1\ \ 0\ \ 2\,]$, $[\,0\ \ {-1}\ \ 1\ \ 2\,]$, $[\,0\ \ {-1}\ \ {-1}\ \ 2\,]$). Step 2 adds row 2 to rows 3 and 4, giving last-column entries $4, 4$. Step 3 adds row 3 to row 4. The final matrix is
$$
U = \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & 0 & 8 \end{bmatrix}
$$

b. The largest entry in $A$ is 1. The largest entry during elimination is 8. The last column doubles at every step: 1, 2, 4, 8.

c. The bottom right entry is $2^{n-1}$. For $n = 3$ the last column goes $1, 2, 4$ and the bottom right entry is 4.

d. For $n = 10$ it is $2^9 = 512$. For $n = 60$ it is $2^{59} \approx 5.8 \times 10^{17}$, which is larger than the 16 or so digits a computer can hold. Rounding errors get magnified by this growth, and the answer to a linear system can lose all its accuracy. (In a test, solving a 60 by 60 system with this matrix in double precision gave an answer whose error was around 60 percent of the size of the answer itself.) This is the worst case for elimination with row swaps, and it almost never shows up in practice.
