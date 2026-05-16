---
title: "Unit 08: Anomaly Detection"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/08-anomaly/
---

A short, focused unit that doubles as the second-quarter capstone. The central
problem: credit card fraud is rare — less than 0.2% of transactions — so a
classifier that always predicts "not fraud" gets 99.8% accuracy and catches
nothing. This unit explores how to handle severe class imbalance and how to
detect anomalies without a clean supervised signal.

## Concepts You'll Learn About

- **Class imbalance** — why accuracy is a misleading metric when one class
  dominates; precision, recall, and F1 revisited
- **SMOTE** — Synthetic Minority Oversampling Technique; generating synthetic
  examples of the rare class
- **Gaussian Mixture Models** — unsupervised density estimation; flagging
  points in low-probability regions as anomalies
- **Supervised vs. unsupervised anomaly detection** — when you have labeled
  fraud examples vs. when you don't

## Topics

- **Credit card fraud — baseline and SMOTE** — the raw imbalance problem, then
  oversampling the fraud class and measuring the impact on recall.
  {% include nb.html local="CreditCard.ipynb" %}
  {% include nb.html local="SMOTE-credit.ipynb" %}

- **Gaussian Mixture Model approach** — fitting a GMM to the transaction data
  and flagging low-likelihood points as anomalies; comparing to the supervised approach.
  {% include nb.html local="GMM-credit.ipynb" %}

## Quarter Project

Find any dataset from the [UCI Repository](http://archive.ics.uci.edu/datasets/)
and model it using techniques from Units 1–8. Classification, regression, or
anomaly detection — your choice. The deliverable is a notebook with a clear
question, a defensible modeling approach, and a written interpretation of results.

## What's next

[Unit 09](/notebooks/09-dense-neural-networks/) introduces dense neural networks —
perceptrons, backpropagation, and the foundational ideas that make everything in
Units 10–13 possible.
