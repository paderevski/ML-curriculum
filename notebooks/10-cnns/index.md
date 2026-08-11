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

Convolutional neural networks are specifically designed to operate on 2D data. Before introducing this new model, let's first walk through a complete example of an image-processing workflow using the dense neural network layers you already know. The [CIFAR-10 dataset](https://www.cs.toronto.edu/~kriz/cifar.html) contains thousands of color images labeled with one of 10 categories. Work through {% include nb.html local="CIFAR10_Training.ipynb" %} to see how to load, train and improve the model using dense layers.

As a follow-up assignment, find a [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog) classification task and replicate the full pipeline in the example CIFAR notebook.

Next explore what an image convolution is  {% include nb.html local="ImageConvolutions.ipynb" %}

- **LeNet** — the foundational CNN architecture applied to MNIST/FashionMNIST.
  Following [d2l.ai chapter 7.6](https://d2l.ai/chapter_convolutional-neural-networks/lenet.html)
  ([local PDF](../../notes/d2l.ai-LeNet/)). A great
  [3D interactive visualization](https://adamharley.com/nn_vis/cnn/3d.html)
  accompanies this session.

- **Activation functions** — covered during Engineering Week; see
  [Unit 09](../09-dense-neural-networks/) for the notebook.

- **AlexNet on CIFAR-100** — scaling depth and applying dropout; training a
  historically significant architecture on a harder dataset.
  {% include nb.html local="alexnet.ipynb" %}

- **Presentations** — second round.

## What's next

[Unit 11](../11-transfer-and-time-series/) introduces transfer learning —
the insight that you don't have to train from scratch — and ends with a pivot
toward sequential data.
