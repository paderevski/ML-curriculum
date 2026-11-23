---
title: "Decision Trees"
layout: single
sidebar:
  nav: "ml"
---

## What a decision tree is

A **decision tree** makes a prediction by asking questions, one at a time. You
start at the top, answer the question, follow the branch that matches your
answer, and keep going until you reach a **leaf**. The leaf is the prediction.

Here is a tree that predicts whether we will play golf today:

![A decision tree for playing golf: Outlook, then Humidity or Wind]({{ '/notes/decision-trees-golf.svg' | relative_url }})

On a sunny day with normal humidity, we go left at Outlook, right at Humidity,
and land on **Yes**. On an overcast day we land on **Yes** right away, without
being asked anything else.

Some words we'll use:

- The **root** is the question at the top.
- Each box with a question in it is a **node**. The labels on the arrows are
  the possible **answers**, and each answer is a **branch**.
- A **leaf** is a box with no question. It holds the prediction.
- The **size** of a tree is how many questions it has. The golf tree has 3.
- The **depth** of a tree is the most questions you can be asked on one path
  from the root to a leaf. The golf tree has depth 2.

Two things to notice:

- **Not every path asks every question.** A sunny day never gets asked about
  the wind, and an overcast day is asked only one question.
- **A tree can ignore a feature completely.** Temperature isn't in this tree at
  all. Maybe it didn't help, or maybe the other questions already covered it.

You have used trees like this before, even if nobody called them that:

- **20 Questions.** "Is it alive? Is it bigger than a breadbox?" Every
  question cuts down the possibilities, and a good player asks the questions
  that cut the most.
- **Phone menus.** "Press 1 for billing, 2 for tech support." Each choice sends
  you down a branch until you reach a person who can help.
- **Medical checklists.** Emergency rooms use short yes/no checklists to decide,
  for example, whether an injured ankle needs an X-ray.

People wrote all of those trees by hand. Machine learning **builds the tree from
data**. We give it a table of examples with the right answers, and it decides
which questions to ask and in what order. Before we hand that job to a
computer, we'll do it ourselves.

## Your turn: will we wait for a table?

You show up at a restaurant and there's no free table. Do you wait, or leave?
The [WillWait? handout]({{ '/notebooks/05-classification/decision-tree-handout.pdf' | relative_url }})
has 12 times a diner made that choice, with 10 facts about each situation:
is there another restaurant nearby, are we hungry, how full is it, what kind of
food, and so on.

Your job is to build a tree that gets all 12 right.

**Do the handout before you read on.** The rest of these notes are about how to
choose questions well, and they make more sense once you've struggled to choose
some yourself.

## Guessing with no information

Here's a way to think about which question to ask first.

Suppose I pick one of the 12 diners at random and you have to guess whether they
waited, but you get to know **nothing** about the restaurant. What's your best
strategy?

Guess whatever happened most often. That's the **majority class**. In our data,
6 diners waited and 6 didn't, so it's a coin flip: you'll be right half the
time, 6 out of 12.

## Guessing with one answer

Now suppose you get to ask **one** question before you guess. Say you ask
"Were they hungry?"

![Splitting on Hungry: 5 Yes and 2 No if hungry, 1 Yes and 4 No if not]({{ '/notes/decision-trees-hungry.svg' | relative_url }})

- If they were hungry, 5 of those 7 diners waited. Guess **Yes**, and you're
  right 5 times out of 7.
- If they weren't hungry, only 1 of those 5 waited. Guess **No**, and you're
  right 4 times out of 5.

Altogether that's $5 + 4 = 9$ right out of 12, up from 6. One question made you
a much better guesser.

That gives us a way to compare questions. A question is useful if knowing the
answer changes your guess and makes it more likely to be right.

> **Try it.** Pick another column and work it out the same way. Split the 12
> rows by that column's answers, guess the majority in each group, and count
> how many you'd get right. **Which column makes your guess the most likely to be
> right?** That's a good candidate for the top of your tree.

## Some groups are better than others

As you try columns, you'll notice that some groups are more useful to land in
than others. Compare these three groups:

| Group | Waited | Didn't wait |
|:------|:------:|:-----------:|
| A | 4 | 0 |
| B | 3 | 1 |
| C | 2 | 2 |

Group A is perfect. If you land there, you know the answer for sure, and that
branch can stop and become a leaf. Group C is useless. You know nothing more
than you did before the question. Group B is somewhere in between.

Let's put a number on this. We want a score from 0 to 1 for how **mixed up** a
group is:

- A group that's all one class, like A, is as good as it gets. It should score **0**.
- A group that's a 50/50 split, like C, is as bad as it gets. It should score **1**.

Let $x$ be the fraction of the group that waited. Then we want a function with

$$f(0) = 0, \qquad f(1) = 0, \qquad f\left(\tfrac{1}{2}\right) = 1.$$

It should also be symmetric, since "mostly Yes" and "mostly No" are equally easy
to guess.

> **Try it.** Find a function with this behavior before reading on.

A parabola that's 0 at $x = 0$ and $x = 1$ has the form $c\,x(1-x)$, and making
the top equal 1 gives $c = 4$:

$$f(x) = 4x(1-x).$$

There are other functions that would also work, and we'll see a famous one next
class. For these notes, we'll drop the 4 and use

$$m(x) = x(1-x).$$

Multiplying every score by 4 doesn't change which group is better, so the 4 does
nothing for us except make the arithmetic messier. Now a pure group scores 0 and
a 50/50 group scores $\tfrac14$, the worst possible.

| Group | $x$ | $m(x) = x(1-x)$ |
|:------|:---:|:---------------:|
| A: 4 and 0 | 1 | 0 |
| B: 3 and 1 | 3/4 | 0.1875 |
| C: 2 and 2 | 1/2 | 0.25 |

Lower is better.

## Scoring a question

A question splits the data into groups, and each group gets a score. To give the
**question** one score, think about what happens when a new diner comes along.
You don't know in advance which branch they'll land in, so the question's score
is the **expected** score: each group's score, weighted by how often you land
in that group.

Back to Hungry:

- **Hungry = Yes** happens 7 times out of 12. That group has $x = 5/7$ waited,
  so its score is $\tfrac57 \cdot \tfrac27 = \tfrac{10}{49} \approx 0.204$.
- **Hungry = No** happens 5 times out of 12. That group has $x = 1/5$, so its
  score is $\tfrac15 \cdot \tfrac45 = \tfrac{4}{25} = 0.16$.

$$\text{score(Hungry)} = \tfrac{7}{12}(0.204) + \tfrac{5}{12}(0.16) \approx 0.119 + 0.067 = 0.186$$

Before asking anything, all 12 diners are one 50/50 group with a score of
$\tfrac14 = 0.25$. Asking about Hungry brings that down to 0.186. The best
question is the one that brings it down the most.

> **In class.** Each group gets one column and computes its expected score. Then
> we put all ten on the board and pick the winner.

Here's what you should find. The table lists the counts in each branch as
(waited, didn't wait).

| Column | Branches | Expected score |
|:-------|:---------|:--------------:|
| **Patrons** | None (0, 2) · Some (4, 0) · Full (2, 4) | **0.111** |
| Hungry | Yes (5, 2) · No (1, 4) | 0.186 |
| Est | 0–10 (4, 2) · 10–30 (1, 1) · 30–60 (1, 1) · >60 (0, 2) | 0.194 |
| Price | \$ (3, 4) · \$\$ (2, 0) · \$\$\$ (1, 2) | 0.198 |
| Fri | Yes (2, 3) · No (4, 3) | 0.243 |
| Rain | Yes (3, 2) · No (3, 4) | 0.243 |
| Res | Yes (3, 2) · No (3, 4) | 0.243 |
| Alt | Yes (3, 3) · No (3, 3) | 0.250 |
| Bar | Yes (3, 3) · No (3, 3) | 0.250 |
| Type | French (1, 1) · Italian (1, 1) · Thai (2, 2) · Burger (2, 2) | 0.250 |

**Patrons** wins easily:

![Splitting on Patrons: None is all No, Some is all Yes, Full is 2 Yes and 4 No]({{ '/notes/decision-trees-patrons.svg' | relative_url }})

Two of its three branches are already pure. The only work left is the Full branch.

Look at the bottom of the table, too. Alt, Bar and Type score exactly 0.25.
Every one of their branches is a perfect 50/50, so asking them first tells you
nothing at all. Type in particular feels like it should matter, but on its own
it's useless. Hold on to that, because it comes back later.

## Do it again on each branch

Once Patrons is at the root, each branch is a smaller version of the same
problem, and we solve it the same way.

- **None** (X7, X11): both didn't wait. The group is pure, so this branch is a
  **No** leaf.
- **Some** (X1, X3, X6, X8): all four waited. That's a **Yes** leaf.
- **Full** (X2, X4, X5, X9, X10, X12): 2 waited and 4 didn't. That's still
  mixed, so we need another question.

For the Full branch, we score every column again, but **only on these 6 rows**.
The group starts at $x = 2/6$, with a score of $\tfrac13 \cdot \tfrac23 \approx 0.222$.

| Column | Expected score on the Full rows |
|:-------|:------:|
| Hungry, Est, Price, Res, Type | 0.167 (tie) |
| Alt, Fri | 0.200 |
| Rain | 0.208 |
| Bar | 0.222 |

Five columns tie. Any of them is a fine choice, so we'll take **Hungry**:

- **Hungry = No** (X5, X9): both didn't wait. That's a **No** leaf.
- **Hungry = Yes** (X2, X4, X10, X12): 2 and 2. Still mixed.

Notice something here. Before this question, guessing No in the Full branch got
4 of 6 right. After it, we get 2 of 2 right on the No side and 2 of 4 on the Yes
side, which is still 4 of 6. If we judged questions by how many guesses they get
right, Hungry would look useless here. The score sees what the count misses:
we carved off a pure group, and that leaves less mess for the next question to
clean up.

Next comes the 4 rows that are Full and Hungry. Score the columns once more,
and **Type** wins with 0.125. Burger (X12) waited and Italian (X10) didn't, so
both become leaves. Thai has X2 and X4, one of each, and **Fri/Sat** splits them
perfectly. No French restaurant reaches this branch, so the tree has nothing to
go on there. We guess **No**, the same guess the textbook makes.

So Type, the column that was useless at the top, turns out to be the right
question deep in the tree. A question's value depends on which rows are left
when you ask it.

## The whole tree

![The full WillWait tree: Patrons, then Hungry, then Type, then Fri/Sat]({{ '/notes/decision-trees-willwait.svg' | relative_url }})

It has 4 questions and depth 4, and every one of the 12 diners lands on the
right answer. Seven of the ten columns never get used.

The method in one line: **at each node, ask the question with the lowest
expected score, and stop when a group is pure.** Then do the same thing to
every branch. That's the whole algorithm.

Some things to notice about it:

- **It's greedy.** It picks the best question *right now* and never looks ahead.
  Remember the five-way tie in the Full branch? If we had picked Est instead of
  Hungry, we'd get a different tree. It also has 4 questions, but its depth is
  only 3, so it's shallower than the one above. The greedy method found a good
  tree, but not necessarily the best one. Searching every possible tree to find
  the best one is far too slow on real data, so in practice we accept greedy.
- **It always gets the training data right if you let it keep going.** Keep
  asking questions and eventually every group is pure, even if that means
  asking a question just to tell two particular diners apart. That's
  memorizing, not learning. In the Est version of the tree, the last two
  questions can both be "Is there a bar?" (it ties with other columns at both
  spots). In one branch, having a bar means you *leave*,
  and in the other it means you *wait*. That doesn't sound like a real pattern
  about people. It sounds like a tree memorizing two rows. This is why real
  trees get a depth limit.

## What's next

The score $x(1-x)$ is a real one. Doubled, it's called the **Gini impurity**,
and it's the default way scikit-learn's `DecisionTreeClassifier` chooses splits.
Next class we'll meet the other popular score, **entropy**. It has the same
shape: 0 for a pure group, highest for a 50/50 split. It comes from information
theory, and it's what people mean when they say a split has "information gain."
