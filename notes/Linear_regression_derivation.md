---
sidebar:
  nav: "ml"

title: "Linear Regression"
---

In a Linear Regression problem, we assume that a set of data points can be modeled accurately by a linear function. We further assume
that the observed data points contain some unavoidable, random, noise. In these notes we derive the formula for a best fit line under
these assumptions.

Given $n$ points $\left(x_{1}, y_{1}\right) \ldots\left(x_{n}, y_{n}\right)$
and an assumed relation $y=f(x)+\epsilon, \epsilon \sim N(\mu, \sigma)$
we want to find a model $f(x_i)=a x_i+b$
such that the root mean squared error

$$
\operatorname{RMSE}(a, b)=\sqrt{\frac 1n\sum_{i=1}^n \left(\tilde{y}_{i}-y_{i}\right)^{2}}
$$

is minimized. Here we define $\tilde{y}_{i} = f(x_i)$ and $\left(\tilde{y}_{i}-y_{i}\right)$ is the *residual* or the error between the
observed $y_i$ value and the estimate $\tilde{y}_i$.

First note that if we square the RMSE, the location of the minimum value does not change. Similarly, we can ignore the $\frac1n$ factor because it does
not affect the minimum either. So we can now worry about optimizing the **Residual Sum of Squares** instead.

$$
\operatorname{RSS}(a, b)=\sum_{i=1}^n \left(\tilde{y}_{i}-y_{i}\right)^{2}
$$

is minimized.

$RSS$ is a function of the line parameters $a$ and $b$ only. To minimize
it we need to take two partial derivatives and then set both partial derivatives to zero. (This could technically
find a maximum -- but it's reasonably clear this function has no maximum value because the error can always be increased.)

Take partial derivatives

$$
\begin{aligned}
\frac{\partial RSS}{\partial a} & =2 \sum_{i=1}^n\left(\tilde{y}_{i}-y_{i}\right) \frac{\partial}{\partial a}\left(\tilde{y}_{i}-y_{i}\right) \\
& =2 \sum_{i=1}^n\left(\tilde{y}_{i}-y_{i}\right) \frac{\partial}{\partial a} \left(a x_i + b - y_i\right) \\
& =2 \sum_{i=1}^n\left(\tilde{y}_{i}-y_{i}\right)\left(x_{i}\right) \\
\\
\frac{\partial RSS}{\partial b} & =2 \sum_{i=1}^n\left(\tilde{y}_{i}-y_{i}\right) \frac{\partial}{\partial b}\left(\tilde{y}_{i}-y_{i}\right) \\
& =2 \sum_{i=1}^n\left(\tilde{y}_{i}-y_{i}\right) \frac{\partial}{\partial b} \left(a x_i + b - y_i\right) \\
& =2 \sum_{i=1}^n\left(\tilde{y}_{i}-y_{i}\right)\left(1\right) \\
\end{aligned}
$$


And now we set both of the partials equal to zero.

$$\left\{\begin{array}{l}\dfrac{\partial RSS}{\partial a}=0 \\[20pt] \dfrac{\partial RSS}{\partial b}=0\end{array}\right. \Rightarrow\left\{\begin{array}{l}\sum_{i=1}^n\left(\tilde{y}_{i}-y_{i}\right) x_{i}=0 \\[10pt] \sum_{i=1}^n\left(\tilde{y}_{i}-y_{i}\right)=0\end{array}\right.$$

Since $\tilde{y}_{i} = ax_i+b$
$$\sum_{i=1}^n\left(a x_{i}+b-y_{i}\right) x_{i}=0 \Rightarrow a \sum_{i=1}^n x_{i}^{2}+b \sum_{i=1}^n x_{i}=\sum_{i=1}^n x_{i} y_{i}$$
and
$$\sum_{i=1}^n\left(a x_{i}+b-{y}_{i}\right)=0 \Rightarrow a \sum_{i=1}^n x_{i}+b \sum_{i=1}^n 1=\sum_{i=1}^n y_{i}$$

First note that $\sum_{i=1}^n 1=n$. This is simply a linear system of equations in two unknowns and the coefficients are these messy-looking sums. But they're just
numbers -- coefficients. We can solve this like any linear system.

The most straightforward way to solve any 2x2 system is using Cramer's rule.

$$
\begin{aligned}
a & =\dfrac{\left|\begin{array}{ll}
\displaystyle\sum_{i=1}^n x_{i} y_{i} & \displaystyle\sum_{i=1}^n x_{i} \\[8pt]
\displaystyle\sum_{i=1}^n y_{i} & n
\end{array}\right|}{\left|\begin{array}{ll}
\displaystyle\sum_{i=1}^n x_{i}^{2} & \displaystyle\sum_{i=1}^n x_{i} \\[8pt]
\displaystyle\sum_{i=1}^n x_{i} & n
\end{array}\right|} \\[16pt]
\end{aligned}
$$
and solving for $b$

$$
\begin{aligned}
b & =\dfrac{\left|\begin{array}{ll}
\displaystyle\sum_{i=1}^n x_{i}^{2} & \displaystyle\sum_{i=1}^n x_{i} y_{i} \\[8pt]
\displaystyle\sum_{i=1}^n x_{i} & \displaystyle\sum_{i=1}^n y_{i}
\end{array}\right|}{\left|\begin{array}{ll}
\displaystyle\sum_{i=1}^n x_{i}^{2} & \displaystyle\sum_{i=1}^n x_{i} \\[8pt]
\displaystyle\sum_{i=1}^n x_{i} & n
\end{array}\right|}
\end{aligned}
$$

This may look less foreboding if we replace all the sigmas with some new variable names. Let

$$
S_{x}=\sum_{i=1}^n x_{i}, \qquad S_{y}=\sum_{i=1}^n y_{i}, \qquad S_{xx}=\sum_{i=1}^n x_{i}^{2}, \qquad S_{xy}=\sum_{i=1}^n x_{i} y_{i}
$$

Taking determinants,
<a name="eq-a"></a>
$$a=\frac{n S_{xy}-S_{x} S_{y}}{n S_{xx}-S_{x}^{2}}\tag{a}$$

$$
b=\frac{S_{y} S_{xx}-S_{x} S_{xy}}{n S_{xx}-S_{x}^{2}}
$$

## Interpretation as a ratio of variances

Students of statistics may appreciate the following manipulations

*Definition* of covariance
$$E(x y)-E(x) E(y)=\operatorname{Cov}(x, y)$$

*Definition* of variance

$$\operatorname{Var}(x)=E\left[(x-\mu)^{2}\right]$$

*Lemma*

$$
\begin{aligned}
\operatorname{Var}(x)&=E\left[(x-\mu)^{2}\right] \\
&=E\left(x^{2}\right)-2 \mu E[x]+E[\mu]^{2} \\
&=E\left[x^{2}\right]-2 E[x]^{2}+\mu^{2} \\
&=E\left[x^{2}\right]-E[x]^{2}
\end{aligned}
$$


Manipulating the denominator of [equation ($a$)](#eq-a) above,
$$
\begin{aligned}
n \sum x_{i}^{2}-\left(\sum x_{i}\right)^{2} & =n^{2}\left(\frac{1}{n} \sum x_{i}^{2}-\left(\frac{\sum x_{i}}{n}\right)^{2}\right) \\
& =n^{2}\left(E\left[x^{2}\right]-E[x]^{2}\right) \\
& =n^{2} \operatorname{Var}(x)
\end{aligned}
$$

And the numerator
$$
\begin{aligned}
n \sum x_{i} y_{i}-\sum x_{i} \sum y_{i} \\
& =n^{2}\left(\frac{1}{n} \sum x_{i} y_{i}-\frac{1}{n} \sum x_{i} \cdot\frac1n \sum y_{i}\right) \\
& =n^{2}\left(E\left[x y\right]-E[x] E[y]\right) \\
& =n^{2}\left(E[x y]-\mu_{x} \mu_{y}\right) \\
& = n^2 \operatorname{Cov}(x,y)
\end{aligned}
$$

so

$$a=\frac{E[x y]-\mu_{x} \mu_{y}}{E\left[x^{2}\right]-\mu_{x}^{2}}=\frac{\operatorname{Cov}(x, y)}{\operatorname{Var}(x)}$$
