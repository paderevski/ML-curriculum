---
title: "Unit 10: Transfer Learning and Time Series"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/10-transfer-and-time-series/
---

Two connected ideas. Transfer learning is the practical insight that a network
trained on millions of images already knows a lot about edges, textures, and
shapes — you can freeze those layers and just retrain the final classifier on
your own data in minutes. Time series is the first look at data where *order
matters*, setting up the sequence models that follow.

## Concepts You'll Learn About

- **Transfer learning** — pre-trained weights as a feature extractor;
  frozen vs. fine-tuned layers
- **Fine-tuning** — unfreezing the top layers and retraining at a low
  learning rate to adapt to a new domain
- **Audio as an image** — spectrograms; applying image CNNs to sound
- **Time series** — sequences where the past predicts the future;
  sliding windows; stationarity
- **Recurrent processing (preview)** — why feed-forward networks struggle
  with sequences; motivating the RNNs of Unit 11

## Topics

- **Bird call classification** — audio spectrograms treated as images;
  transfer learning applied to an unusual domain (a "snow day" notebook
  with a fun origin story).
  {% include nb.html local="Birds.ipynb" %}

- **Fine-tuning ResNet / MobileNet** — freeze all layers except the final
  classifier, retrain on a new task; measure what fine-tuning gains over
  pure feature extraction.

- **Collect-your-own-images project** — photograph objects around the school,
  label them, train a transfer-learning classifier on your own data.
  *Assignment: submit your trained model and a reflection on what worked.*

- **Guest speaker.**

- **AAPL stock price prediction** — a time-series regression: predict
  tomorrow's close from a window of recent prices
  ([AAPL.csv](../../data/AAPL.csv)). A deliberate setup for
  "what would an RNN do better?"
  ([reference prediction](../../data/apple-prediction.png))
  {% include nb.html local="AAPL.ipynb" %}

## What's next

[Unit 11](../11-rnns-seq2seq/) answers the time-series question properly
with recurrent neural networks — and takes them all the way to neural machine
translation with attention.
