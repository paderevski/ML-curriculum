---
title: "Unit 13: Transformers and Generative Models"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/13-transformers-generative/
---

The final unit. After eight months of building toward it, the Transformer
architecture arrives — and with it, everything from GPT-style text generation
to image captioning to variational autoencoders. The unit also marks a
framework switch: TensorFlow/Keras gives way to PyTorch, which is the right
tool for Transformer-scale work.

## Concepts You'll Learn About

- **Self-attention** — each token attends to every other token; the scaled
  dot-product attention mechanism; why √d_k matters
- **Multi-head attention** — running several attention functions in parallel
  and concatenating the results
- **Positional encoding** — injecting token order into an order-agnostic
  architecture
- **The Transformer block** — attention → add & norm → feed-forward → add & norm;
  encoder and decoder stacks
- **Autoregressive generation** — predicting one token at a time;
  temperature and sampling
- **Fine-tuning large language models** — adapting a pre-trained GPT-style
  model to a new corpus
- **Image captioning** — bridging vision (CNN encoder) and language (Transformer
  decoder)
- **Variational autoencoders** — encoder maps to a latent distribution, not
  a point; the reparameterization trick; generating new images by sampling
  the latent space

## Topics

- **PyTorch foundations** — tensors, autograd, and the training loop; switching to Pytorch for more complicated modern models.
  [Official PyTorch tutorial](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)
  {% include nb.html local="PytorchTutorial.ipynb" %}

- **Transformer Neural Machine Translation (NMT)** — building a full Transformer for English-to-Spanish
  translation.
    - [3Blue1Brown Ch6](https://www.3blue1brown.com/lessons/attention) ·
    - ["Attention Is All You Need" (Vaswani et al., 2017)](https://arxiv.org/pdf/1706.03762) ·
    - [Comprehension questions](../notebooks/13-transformers-generative/transformer_nmt_questions/)
    - {% include nb.html local="transformer_nmt_with_spanish.ipynb" %}

- **CharGPT** — a GPT-style Transformer generating Shakespeare character by
  character; tokenization and the autoregressive loop.
  - {% include nb.html local="charGPT_assignment.ipynb" %}

- **Class discussion + GPT-2 fine-tuning** — fishbowl discussion on the
  Transformer comprehension questions, then fine-tuning a GPT-2-style model on a
  corpus of your choice. Fair warning: most online tutorials are buggy;
  debugging is part of the exercise.

- **Image captioning** — a CNN encodes an image; a Transformer decoder generates
  a caption. Vision and language meeting in the middle.
  - {% include nb.html local="image_captioning_assignment.ipynb" %}

- **Variational Autoencoders on CelebA** — learning a latent space of faces;
  sampling new faces; interpolating between them.
  - [VAE notes](../../notes/vae_notes/) — theory behind the ELBO, the
  reparameterization trick, and the reconstruction vs. KL tradeoff.
  - {% include nb.html local="VAE_celeba_student.ipynb" %}

## Notes
- [VAE notes](../../notes/vae_notes/) — theory behind the ELBO, the
  reparameterization trick, and the reconstruction vs. KL tradeoff.
- [Transformer comprehension questions](../notebooks/13-transformers-generative/transformer_nmt_questions.md) —
  detailed questions to work through alongside the NMT notebook.
