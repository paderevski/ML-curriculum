---
title: "Unit 09: Dense Neural Networks"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/09-dense-neural-networks/
---

The bridge between classical ML and deep learning. Before tackling convolutional
or recurrent networks, this unit builds intuition for how neural networks learn
at all — forward propagation, loss, and the chain rule applied layer by layer.
This unit is lighter on scheduled class time than others; some of the material
is woven into the CNNs unit that follows.

## Concepts You'll Learn About

- **Perceptrons** — the simplest neural unit; weighted sum + activation;
  the connection to logistic regression
- **Multi-layer perceptrons** — hidden layers; why depth matters;
  universal approximation (informally)
- **Forward propagation** — computing predictions from weights
- **Loss functions** — cross-entropy for classification; MSE for regression
- **Backpropagation** — the chain rule applied recursively; computing gradients
  layer by layer
- **Gradient descent** — updating weights in the direction that reduces loss;
  learning rate; local minima
- **Activation functions** — ReLU, sigmoid, tanh; why non-linearity is
  essential; vanishing gradients
- **Softmax** — turning raw scores into a probability distribution over classes

## Topics

- **Softmax and output layers** — converting network outputs into class
  probabilities; relationship to logistic regression.
  {% include nb.html local="Softmax.ipynb" %}

- **Activation functions** — why we need them, how they affect training dynamics,
  and how to choose between ReLU, sigmoid, and tanh.
  {% include nb.html local="Activation-Functions.ipynb" %}

## Notes

- [Backpropagation — worked example and theory](/notes/backprop/) — a
  fully worked 2-2-1 network with hand-traced forward and backward passes.

## What's next

[Unit 10](/notebooks/10-cnns/) applies these ideas to images — convolutional
networks replace the dense layers with learned spatial filters that are far
more efficient on image data.
