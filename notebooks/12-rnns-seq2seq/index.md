---
title: "Unit 12: RNNs and Sequence-to-Sequence"
layout: single
sidebar:
  nav: "ml"
permalink: /notebooks/12-rnns-seq2seq/
---

Where the course pivots fully into modern NLP. The progression mirrors the
historical arc that led to Transformers: character-level text generation →
sentiment classification → sequence-to-sequence translation → attention.
Each step reveals a limitation of the previous approach, motivating the next.

## Concepts You'll Learn About

- **Recurrent neural networks** — hidden state as memory; unrolling through time;
  the vanishing gradient problem
- **LSTMs** — gating mechanisms that let the network learn what to remember
  and what to forget
- **Sequence-to-sequence** — encoder compresses the input into a context vector;
  decoder generates the output token by token
- **Beam search** — keeping the top-k candidates at each decoding step instead
  of greedily picking one
- **Bahdanau attention** — letting the decoder look back at all encoder states,
  not just the final one; the idea that becomes Transformers
- **Embeddings** — learned dense representations of tokens; the input layer of
  every modern NLP model

## Topics

- **RNNs and character-level text generation** — Karpathy's "Unreasonable
  Effectiveness of RNNs" as context, then generating Shakespeare one character
  at a time.
  {% include nb.html local="Shakespeare_Student.ipynb" %}

- **Reading day** — working through assigned background reading on sequence models.

- **Sentiment analysis** — IMDB movie review classification with an LSTM;
  how a recurrent network reads a sentence and produces a label.
  {% include nb.html local="sentiment_analysis-student.ipynb" %}

- **Neural machine translation — starter** — build an LSTM seq2seq translator
  from scratch; train on an English/Spanish sentence pair dataset.
  {% include nb.html local="Neural-Machine-Translation-Starter.ipynb" %}

- **Improve + round-trip translation** — extend the starter with round-trip
  evaluation (English → Spanish → English); add attention and beam search from
  the reference notebook.
  {% include nb.html local="seq2seq_nmt_reference.ipynb" %}
  {% include nb.html local="seq2seq_nmt_pytorch_hf_reference.ipynb" %}
  *Assignment: implement attention, run round-trip tests, submit with
  analysis of where the model succeeds and fails.*

## Notes

- [Translation examples](/notes/translation_examples/) — reference input/output
  pairs for testing your translation model.

## What's next

[Unit 13](/notebooks/13-transformers-generative/) replaces the recurrence entirely
with self-attention — the Transformer — then uses it for translation, text
generation, image captioning, and generative modeling.
