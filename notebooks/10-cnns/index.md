---
title: "Unit 10: Convolutional Neural Networks"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/10-cnns/
---

Deep learning arrives for images. CNNs replace densely connected layers with
learned spatial filters — convolutions that detect edges, textures, and shapes
regardless of where they appear in the image. This unit unfolds over several
weeks and is also when the spring research project gets seeded: you'll pitch
an idea, refine it, and present progress.

## Concepts You'll Learn About

- **Convolution** — sliding a filter across an image; detecting local patterns;
  feature maps
- **Pooling** — downsampling feature maps; translation invariance
- **CNN architecture** — conv → activation → pool → flatten → dense; stacking
  layers to build hierarchy
- **Data augmentation** — flipping, cropping, and rotating training images to
  reduce overfitting
- **Transfer learning (first look)** — how networks trained on one dataset can
  be repurposed; previews Unit 11
- **AlexNet** — the 2012 architecture that started the deep learning era;
  depth, ReLU, and dropout

## Topics

- **CIFAR-10 baseline** — load the dataset, build a baseline CNN, plot the
  training curve, modify the architecture to improve accuracy.
  {% include nb.html local="CIFAR10_Training.ipynb" %}
  *Assignment: find a TensorFlow Datasets classification task and replicate the
  full CIFAR pipeline (load → sample → build → train → curve → augment → improve).*

- **Presentations** — first round of project progress presentations.

- **Research topic brainstorm** — each student develops three plausible research
  ideas and pitches them in a two-minute, no-slides format: problem, solution,
  who cares.

- **What is a convolution?** — building spatial intuition for filters before
  applying them in a network.
  {% include nb.html local="ImageConvolutions.ipynb" %}

- **LeNet** — the foundational CNN architecture applied to MNIST/FashionMNIST,
  following the [d2l.ai chapter 7.6 treatment](https://d2l.ai). A great
  [3D interactive visualization](https://adamharley.com/nn_vis/cnn/3d.html)
  accompanies this session.

- **Activation functions** — covered during Engineering Week; see
  [Unit 09](/notebooks/09-dense-neural-networks/) for the notebook.

- **AlexNet on CIFAR-100** — scaling depth and applying dropout; training a
  historically significant architecture on a harder dataset.
  {% include nb.html local="alexnet.ipynb" %}

- **Presentations** — second round.

## What's next

[Unit 11](/notebooks/11-transfer-and-time-series/) introduces transfer learning —
the insight that you don't have to train from scratch — and ends with a pivot
toward sequential data.
