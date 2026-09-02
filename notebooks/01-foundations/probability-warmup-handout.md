---
title: "Probability Warm-Up: Intersection, Union, and Conditional"
layout: single
math: true
geometry: margin=1in
---

Name: ______________________  Date: ______________


## 0. Basic Terms

An **experiment** is anything with an uncertain outcome: rolling a die, testing a patient, drawing a card.

The **sample space** $S$ is the set of all possible outcomes. For one die roll, $S = \{1,2,3,4,5,6\}$.

An **event** is a subset of the sample space — something that either happens or doesn't. "The roll is even" is the event $A = \{2,4,6\}$.

When every outcome is equally likely:

$$P(A) = \frac{\text{number of outcomes in } A}{\text{number of outcomes in } S}$$

So $P(\text{even}) = 3/6 = 0.5$.

Two properties of probability functions:

- $0 \le P(A) \le 1$ always.
- $P(\bar{A}) = 1 - P(A)$, where $\bar{A}$ ("not $A$") is the **complement** of $A$.

> **Quick check.** A single fair die is rolled. Write out the **event** $B$ = "the roll is greater than 4" and compute $P(B)$ and $P(\bar{B})$.
>
> $B = \{\rule{2.5cm}{0.15pt}\}$   $P(B) = \rule{1.5cm}{0.15pt}$   $P(\bar{B}) = \rule{1.5cm}{0.15pt}$


## 1. Intersection — "**and**"

$A \cap B$ is the event that **both** $A$ and $B$ happen. Read the symbol as "and."

**Example.** Draw one card from a standard 52-card deck. Let

- $A$ = the card is a heart
- $B$ = the card is a face card — J, Q, K

$A \cap B$ = the card is a *heart face card*. There are exactly 3 of those (J♥, Q♥, K♥), so

$$P(A \cap B) = \frac{3}{52} \approx 0.058$$

Notice that $P(A \cap B)$ is smaller than both $P(A) = 13/52$ and $P(B) = 12/52$.

If $A \cap B$ is empty — the two events cannot co-occur — we call them **mutually exclusive** and $P(A \cap B) = 0$. "The card is a heart" and "the card is a spade" are mutually exclusive.

> **Exercise 1.** One card is drawn. Let $A$ = "the card is red" and $B$ = "the card is an ace."
>
> (a) How many cards are in $A \cap B$? _______
> (b) $P(A \cap B)=$ _______
> (c) Name two events in this deck that are mutually exclusive.


## 2. Union — "**or**"

$A \cup B$ is the event that $A$ happens, or $B$ happens, or both. Read the symbol as "or."

It is sometimes, but **usually not true** that $P(A \cup B) = P(A) + P(B)$. That is wrong whenever the events overlap, because everything in the overlap gets counted twice — once in $P(A)$ and again in $P(B)$. The Principle of Inclusion-Exclusion gives the proper formula:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

**Example.** Same deck, $A$ = heart, $B$ = face card. What is $P(A \cup B)$?

$$P(A \cup B) = \frac{13}{52} + \frac{12}{52} - \frac{3}{52} = \frac{22}{52} \approx 0.423$$

Check by counting directly: 13 hearts, plus the 9 face cards that aren't hearts, is 22 cards. ✓

> **Exercise 2.** In a class of 40 students, 22 have written Python before, 15 have taken a statistics course, and 9 have done both.
>
> (a) How many have done Python *or* statistics (or both)? _______
> (b) $P(\text{Python} \cup \text{Stats})=$ _______
> (c) How many have done *neither*? _______
> (d) Sketch a Venn diagram and label all four regions with counts.


## 3. Conditional probability — "**given**"

$P(A \mid B)$ is the probability that $A$ happens **given that we already know $B$ happened**. Read the bar as "given."

Conditioning on $B$ means throwing away every outcome where $B$ didn't happen. $B$ becomes the new sample space. So we count the outcomes where both happened, and divide by the outcomes where $B$ happened:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

**Example.** Draw a card. What is $P(\text{face card} \mid \text{heart})$?

$$P(B \mid A) = \frac{P(A \cap B)}{P(A)} = \frac{3/52}{13/52} = \frac{3}{13} \approx 0.231$$

Or just reason it out: we know it's a heart, so there are 13 possibilities, and 3 of them are face cards. Same answer, and the formula is only bookkeeping for that intuition.

### Two things to notice

**Order matters.** $P(A \mid B)$ and $P(B \mid A)$ are different questions with different denominators. Above, $P(\text{face} \mid \text{heart}) = 3/13$, but $P(\text{heart} \mid \text{face}) = \frac{3/52}{12/52} = 3/12 = 1/4$. Same numerator, different denominator, different answer. Computing $P(A|B)$ if you know $P(B|A)$ is the heart of the problem we're looking at today, and arguably a big part of machine learning!
t.

> **Exercise 3.** Roll two fair dice. Let $A$ = "the sum is 8" and $B$ = "the first die shows 5."
>
> (a) $P(A)=$ _______ (there are 36 equally likely outcomes)
> (b) $P(A \cap B)=$ _______
> (c) $P(A \mid B)=$ _______
> (d) Is $P(A \mid B)$ bigger or smaller than $P(A)$? What does that tell you?
> (e) Compute $P(B \mid A)$ and confirm it differs from $P(A \mid B)$.


## 4. Putting it together: the two-way table

Most real problems arrive as counts in a table, and every quantity above can be read straight off it.

Out of **1,000 people**, 1% carry an infection. A test is applied to all of them; among the infected it comes back positive 97% of the time, and among the healthy it also comes back positive 3% of the time.

|                  | Test **+** | Test **−** | **Total** |
| ---------------- | ---------: | ---------: | --------: |
| **Infected**     |        9.7 |        0.3 |        10 |
| **Not infected** |       29.7 |      960.3 |       990 |
| **Total**        |       39.4 |      960.6 |     1,000 |

(Decimal people are fine — these are expected counts, not a headcount.)

Reading the table:

- **Intersection:** $P(I \cap +) = 9.7/1000 = 0.0097$ — one cell, over the grand total.
- **Marginal:** $P(+) = 39.4/1000 = 0.0394$ — a row or column total, over the grand total.
- **Conditional:** $P(+ \mid I) = 9.7/10 = 0.97$ — one cell, over its *row* total. Conditioning on $I$ means the "Infected" row is now the whole world.
- **The other conditional:** $P(I \mid +) = 9.7/39.4 \approx 0.246$ — the same cell, over its *column* total.

> **Exercise 4.** Using the table above:
>
> (a) $P(\bar{I} \cap +)=$ _______
> (b) $P(- \mid \bar{I})=$ _______
> (c) $P(I \cup +)=$ _______ *(use the union formula, then verify by counting cells)*
> (d) Are $I$ and $+$ independent? Justify with numbers.

> **Exercise 5 — the punchline.** Compare your answers for $P(+ \mid I) = 0.97$ and $P(I \mid +) \approx 0.246$.
>
> Both describe "the test and the infection agreeing." In one sentence, explain to a classmate why they are so far apart. Which of the two would a patient actually want to know?


## Answer Key

**Quick check.** $B = \{5,6\}$, $P(B) = 2/6 = 1/3$, $P(\bar{B}) = 2/3$.

**Exercise 1.** (a) 2 (A♥, A♦). (b) $2/52 = 1/26 \approx 0.038$. (c) e.g. "heart" and "spade," or "ace" and "king" — any two that can't hold at once.

**Exercise 2.** (a) $22 + 15 - 9 = 28$. (b) $28/40 = 0.70$. (c) $40 - 28 = 12$. (d) Python only 13, both 9, Stats only 6, neither 12 — the four must sum to 40.

**Exercise 3.** (a) $5/36$ — the sum-8 outcomes are (2,6),(3,5),(4,4),(5,3),(6,2). (b) $1/36$ — only (5,3). (c) $\frac{1/36}{6/36} = 1/6$. (d) $1/6 > 5/36$, so learning the first die is a 5 makes a sum of 8 *more* likely; the events are not independent. (e) $P(B \mid A) = \frac{1/36}{5/36} = 1/5$, which is not $1/6$.

**Exercise 4.** (a) $29.7/1000 = 0.0297$. (b) $960.3/990 \approx 0.970$. (c) $P(I) + P(+) - P(I \cap +) = 0.01 + 0.0394 - 0.0097 = 0.0397$; by cells, $(9.7 + 0.3 + 29.7)/1000 = 0.0397$. ✓ (d) No. $P(+ \mid I) = 0.97$ but $P(+) = 0.0394$ — wildly different, so the test result depends heavily on infection status. (Good! An independent test would be worthless.)

**Exercise 5.** The infection is rare, so the 990 healthy people vastly outnumber the 10 infected ones — and 3% of a large group (29.7 false positives) beats 97% of a tiny group (9.7 true positives). A positive result is therefore most often a false alarm. The patient wants $P(I \mid +)$, but the test's advertised "97% accuracy" reports $P(+ \mid I)$. **Bayes' Theorem is the tool that converts the number we are given into the number we want.**
