---
title: "Unit 05: Classification Classics"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/05-classification/
unit_number: 5
math: true
toc: false   # the unit map at the top replaces the right-hand TOC

sections:
  - id: python-review
    title: "Python Review"
    summary: >-
      A two-part tune-up before the new algorithms. Neither part covers machine
      learning. They cover the list, loop, and array code that most ML bugs come from.
    ideas:
      - "Functions, lists, loops and dictionaries without any imports"
      - "NumPy arrays vs. lists: element-wise math, `shape`, broadcasting"
      - "A from-scratch Gaussian elimination solver"
    notes_draft: true
    notes_md: >-
      Each drill notebook checks itself: fill in the `# YOUR CODE HERE` cell, then
      run the test cell below it. A `FAIL` shows what was expected and what your
      code produced. Don't edit the tests.
    materials:
      - path: notebooks/05-classification/python-practice/python_drills_1_basics.ipynb
        role: hw
        label: "Python Drills, Part 1: Basics"
        blurb: "Functions, lists, loops, dictionaries. No imports allowed."
      - path: notebooks/05-classification/python-practice/python_drills_2_numpy.ipynb
        role: hw
        label: "Python Drills, Part 2: NumPy"
        blurb: "The same ideas with NumPy, ending in a Gaussian elimination solver."

  - id: logistic-regression
    title: "Logistic Regression"
    summary: >-
      Our first real classifier. We bend a linear model through a sigmoid so it
      outputs a probability, then fit it to tumor measurements where a false
      negative is the costly mistake.
    ideas:
      - "The sigmoid $$\\sigma(z) = 1/(1+e^{-z})$$ turns any score into a probability"
      - "Coefficients live in **log-odds**: each unit of $$x_j$$ multiplies the odds by $$e^{\\beta_j}$$"
      - "Fit by maximum likelihood, not least squares"
      - "The 0.5 threshold is a choice. Moving it trades precision for recall"
    notes_draft: true
    notes_md: >-
      Linear regression predicts any real number, but a class label needs a value
      between 0 and 1. Logistic regression keeps the linear score
      $$z = \beta_0 + \beta_1 x_1 + \dots$$ and passes it through the sigmoid, so
      $$P(y=1 \mid x) = \sigma(z)$$. Squared error on that output gives a bumpy loss,
      so we fit by maximizing the likelihood of the observed labels instead
      (equivalently, minimizing log-loss). When you read the classification report,
      look at recall for the malignant class first.
    materials:
      - local: Cancer_Logistic_Student.ipynb
        role: demo-hw
        label: "Cancer Data Logistic Regression"
        blurb: >-
          We work through the first half together on the Wisconsin breast-cancer
          data, and you finish the rest for homework.
      - kind: dataset
        role: hw
        label: "Loan Data: best-model challenge"
        url: /notebooks/05-classification/loan_data.csv
        blurb: >-
          Open-ended. Build the best logistic regression you can on `loan_data.csv`
          and defend your feature and threshold choices in markdown. Start your own notebook.

  - id: knn
    title: "k-Nearest Neighbors"
    summary: >-
      Classify a point by asking its neighbors. We come up with the algorithm on
      the board first, then you write it yourself before using sklearn's version.
    ideas:
      - "No training step: the model *is* the training data"
      - "Distance metrics, and why you must scale features first"
      - "Small $$k$$ overfits, large $$k$$ underfits"
      - "The curse of dimensionality: in high dimensions every point is far from every other"
    notes_draft: true
    notes_md: >-
      To classify $$q$$: compute its distance to every training point, take the $$k$$
      closest, and let them vote. That is the whole algorithm. The design choices
      are the distance metric (usually Euclidean), the value of $$k$$ (odd, to avoid
      ties, picked with a validation set), and feature scaling. A feature measured
      in thousands will swamp one measured in decimals unless you standardize.
      Further reading: a
      [survey of approximate nearest-neighbor algorithms](https://towardsdatascience.com/comprehensive-guide-to-approximate-nearest-neighbors-algorithms-8b94f057d6b6)
      used at Spotify and Netflix scale.
    materials:
      - local: knn-Student.ipynb
        role: classwork
        label: "k-NN from scratch"
        blurb: "Write your own k-NN classifier on a three-cluster Gaussian mixture."
      - local: digits-student.ipynb
        role: hw
        label: "Recognizing Digits with k-NN"
        blurb: "Apply k-NN to handwritten digits (sklearn's MNIST subset) and pick the best $$k$$."

  - id: kd-trees
    title: "k-d Trees"
    summary: >-
      Brute-force k-NN checks every point on every query. A k-d tree splits space
      on alternating axes, so a nearest-neighbor search can skip most of the data.
    ideas:
      - "Split at the median, alternating $$x$$, $$y$$, $$x$$, ... down the tree"
      - "Every node owns a rectangle, and the tree and the boxes hold the same information"
      - "Backtracking: the closest point isn't always in the leaf you land in"
      - "About $$\\log_2 n$$ levels, so search drops from $$O(n)$$ to roughly $$O(\\log n)$$"
    notes:
      url: /notes/kd-trees/
      label: "k-d Trees for Nearest-Neighbor Search"
    materials:
      - kind: interactive
        role: classwork
        label: "k-d Tree Explorer"
        url: /notebooks/05-classification/kdtree-explorer.html
        blurb: "Build a tree point by point and step through a search. Do this after the reading."
      - local: KDTree_Demo.ipynb
        role: demo
        label: "k-d Trees for Nearest Neighbors"
        blurb: "Build a 2D k-d tree in Python, query it, and count the distance checks it saves."
      - kind: worksheet
        role: hw
        label: "k-d tree packet"
        blurb: "Paper packet, handed out in class. Turn it in the same day."

  - id: decision-trees
    title: "Decision Trees"
    summary: >-
      Ask the most useful yes/no question first, then repeat. We classify a small
      restaurant dataset by hand to see why "most useful" means "most information
      gained", then run the lab on census income data.
    ideas:
      - "Recursive partitioning: greedy, one feature at a time"
      - "**Entropy** $$H = -\\sum p_i \\log_2 p_i$$ measures how mixed a node is"
      - "Information gain = parent entropy minus weighted child entropy"
      - "Deep trees memorize. Limit depth or prune them"
    notes_draft: true
    notes_md: >-
      In class we'll split the *WillWait?* restaurant data by hand. Try splitting on
      **Patrons** and then on **Type**, and compare how pure the children are. A
      split that leaves every child all-yes or all-no gains the full 1 bit, and a
      split that leaves every child 50/50 gains nothing. The tree picks the split
      with the highest gain, then repeats on each child.
    materials:
      - kind: worksheet
        role: classwork
        label: "WillWait? by hand"
        blurb: "Done on the board in groups. No notebook."
      - local: Decision_Tree_Student.ipynb
        role: hw
        label: "Decision Tree: Income Data"
        blurb: "Fit an entropy-based tree on UCI income data, then tune its depth."

  - id: entropy
    title: "Shannon Entropy"
    summary: >-
      Here entropy stands on its own, apart from decision trees: information as surprise,
      measured in bits. This sets up the compression ideas in Unit 06.
    ideas:
      - "A rare event carries more information: $$-\\log_2 p$$ bits"
      - "Entropy is the average surprise, and the fewest bits per symbol any code can use"
      - "Huffman coding gets close to that limit"
    notes_draft: true
    notes_md: >-
      If a source emits symbols with probabilities $$p_i$$, no encoding can average
      fewer than $$H = -\sum p_i \log_2 p_i$$ bits per symbol. A fair coin needs 1
      bit per flip, and a coin that lands heads 99% of the time needs about 0.08.
      We'll encode a few short strings by hand and compare them against this limit.
    materials:
      - kind: soon
        role: hw
        label: "Entropy & encoding notebook"
        blurb: "Coming soon."
---

Three algorithms over three weeks, each one introduced with a different dataset
and a different question. Every section follows the same pattern: we work out the
algorithm in class, you implement it yourself, and only then do you use the library
version. You earn the library.

Each section below has short **notes**, then its **notebooks**. Badges show how
each one is used:
<span class="role-badge role-badge--demo">Demo</span> we go through it together,
<span class="role-badge role-badge--classwork">In class</span> you work on it during class,
<span class="role-badge role-badge--hw">Homework</span> you finish and submit it.

{% include unit-sections.html %}

## What's next

[Unit 06](../06-svm-cv-ensembles/) finishes the classical-ML arc with SVMs,
cross-validation, word embeddings, and ensemble methods. These are the practices
professionals use on top of the algorithms you now know.
