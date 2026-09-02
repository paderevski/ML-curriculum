---
title: "A Ridiculously Short Introduction to Derivatives"
subtitle: "Now you'll be bored in math class for 2 years"
header-includes:
  - |
    \usepackage{fullpage}
---

## Purpose

We want to find the line that best fits a scatterplot. In this context, "best" means the line that makes the total squared error as small as possible. Finding the smallest value of a function requires one main idea from calculus: the derivative.

This handout introduces the four derivative rules used in the least-squares derivation.

---

## 1. What a derivative is

The **derivative** of a function is another function that gives the slope of the original function at each point.

If $f(x)$ is a function, its derivative can be written as $f'(x)$ or $\dfrac{df}{dx}$. These are two notations for the same quantity.

At a local minimum, the graph is flat, so its slope is zero. Therefore, one way to find an input that minimizes $f$ is to solve $f'(x)=0$.

---

## 2. The power rule

$$\frac{d}{dx}\,x^n = n\,x^{n-1}$$

To apply the power rule, multiply by the exponent and then reduce the exponent by one.

| $f(x)$ | $f'(x)$ |
|---|---|
| $x^2$ | $2x$ |
| $x^3$ | $3x^2$ |
| $x$ | $1$ |
| $7$ (a constant) | $0$ |

A constant has a horizontal graph, so its slope is $0$ everywhere.

---

## 3. Constants out front, and sums

$$\frac{d}{dx}\big[c\cdot f(x)\big] = c\cdot f'(x) \qquad\qquad \frac{d}{dx}\big[f(x)+g(x)\big] = f'(x)+g'(x)$$

A constant factor remains in front when differentiating. A sum can be differentiated term by term. The sum rule also applies to longer sums, including those written with $\sum_{i=1}^{n}$.

**Example.** $f(x) = 3x^2 - 7x + 4 \;\Longrightarrow\; f'(x) = 6x - 7$.

---

## 4. The chain rule

The least-squares derivation frequently involves expressions in which another expression is raised to a power. For these functions, we use the chain rule:

$$\frac{d}{dx}\big[g(x)\big]^n = n\big[g(x)\big]^{n-1}\cdot g'(x)$$

First apply the power rule to the outer expression, and then multiply by the derivative of the inner expression. The second factor, $g'(x)$, is an important part of the rule.

**Examples.**

- $\dfrac{d}{dx}(3x+2)^5 = 5(3x+2)^4\cdot 3 = 15(3x+2)^4$
- $\dfrac{d}{dx}(7-2x)^2 = 2(7-2x)\cdot(-2) = -4(7-2x)$

---

## 5. Using derivatives to find a minimum

**Example.** Minimize $f(x) = (x-4)^2 + 1$.

$$f'(x) = 2(x-4)\cdot 1 = 2(x-4) \qquad\Longrightarrow\qquad 2(x-4)=0 \qquad\Longrightarrow\qquad x = 4$$

Solving $f'(x)=0$ identifies a point where the graph is flat. Such a point could be a minimum, a maximum, or neither. However, the functions used in this unit are sums of squares with upward-opening graphs, so their flat points are minima. For these functions, a second-derivative check is not necessary.

---

## 6. Partial derivatives

The best-fit line has two unknowns: the slope $m$ and the intercept $b$. Its error function therefore has two inputs, $f(m,b)$, and we need to determine how the function changes with respect to each input.

To take the partial derivative with respect to $m$, treat $b$ as a constant. Similarly, when taking the partial derivative with respect to $b$, treat $m$ as a constant.

Partial derivatives use the symbol $\partial$ rather than $d$ to indicate that the function has other variables that are being held constant:

$$\frac{\partial f}{\partial m} \qquad\text{and}\qquad \frac{\partial f}{\partial b}$$

**Example.** $f(m,b) = (7 - 3m - b)^2$

Apply the chain rule in both cases. The derivative of the inner expression depends on which variable we are differentiating with respect to.

- With respect to $m$, treat $b$ as a constant. The derivative of $7 - 3m - b$ is $-3$.
  $$\frac{\partial f}{\partial m} = 2(7-3m-b)\cdot(-3) = -6(7-3m-b)$$
- With respect to $b$, treat $m$ as a constant. The derivative of the inner expression is $-1$.
  $$\frac{\partial f}{\partial b} = 2(7-3m-b)\cdot(-1) = -2(7-3m-b)$$

To minimize a function of two variables, set both partial derivatives equal to zero and solve the resulting system of equations.

---

## 7. A least-squares example

Consider the two data points $(1,2)$ and $(3,5)$. The residual sum of squares for a line $y = mx+b$ is

$$\mathrm{RSS}(m,b) = (2 - m - b)^2 + (5 - 3m - b)^2$$

Use the sum rule, followed by the chain rule on each term, to find both partial derivatives:

$$\frac{\partial \mathrm{RSS}}{\partial m} = -2(2-m-b) - 6(5-3m-b) \qquad\qquad \frac{\partial \mathrm{RSS}}{\partial b} = -2(2-m-b) - 2(5-3m-b)$$

Set both derivatives equal to zero and simplify by dividing each equation by $-2$:

$$17 - 10m - 4b = 0 \qquad\qquad 7 - 4m - 2b = 0$$

Solving the system gives $m = 1.5$ and $b = 0.5$. This agrees with the slope and intercept of the line through $(1,2)$ and $(3,5)$. With only two data points, the best-fit line passes through both points, so the residual sum of squares is zero.

For $n$ data points, the same rules apply, with the terms collected in a sum:

$$\frac{\partial}{\partial m}\sum_{i=1}^{n}\big(y_i - mx_i - b\big)^2 = \sum_{i=1}^{n} 2\big(y_i - mx_i - b\big)\cdot(-x_i)$$

This expression uses the chain rule; the derivative of the inner expression with respect to $m$ is $-x_i$.

---

## Practice

1. $f(x) = 5x^3 - 2x + 11$. Find $f'(x)$.
2. $f(x) = (4x - 9)^2$. Find $f'(x)$.
3. Minimize $f(x) = (x - 6)^2 + (x - 2)^2$.
4. $f(m,b) = (10 - 2m - b)^2$. Find $\partial f/\partial m$ and $\partial f/\partial b$.
5. $f(m,b) = 4m^2b + b^3 - m$. Find both partial derivatives.

### Answers

1. $15x^2 - 2$
2. $2(4x-9)\cdot 4 = 8(4x-9) = 32x - 72$
3. $f'(x) = 2(x-6) + 2(x-2) = 4x - 16$; setting this equal to zero gives $x = 4$, the mean of 6 and 2.
4. $\partial f/\partial m = -4(10-2m-b)$; $\;\partial f/\partial b = -2(10-2m-b)$
5. $\partial f/\partial m = 8mb - 1$; $\;\partial f/\partial b = 4m^2 + 3b^2$
