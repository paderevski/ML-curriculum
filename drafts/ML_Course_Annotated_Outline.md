# Machine Learning at the Academies of Loudoun
## An Annotated Outline of the 2025–2026 Course

*Compiled from the [course calendar](https://aet-cs.github.io/white/2025/ML/calendar/) and its linked notebooks, notes, and assignments.*

---

## Course at a Glance

A roughly chronological arc that begins with pandas-and-a-CSV and ends, nine months later, with a student-built Transformer translating Spanish to English. The trajectory is deliberately classical-to-modern: students see why the field needed each successive idea — why we moved past hand-coded features, why kernel methods gave way to neural networks, why RNNs gave way to attention. The course is project-driven throughout. Almost every unit closes with a "do this yourself on a dataset you choose" deliverable, and the final third of the year is structured around two research-pitch presentations.

Twelve loose units, by topic:

1. **Foundations** — pandas, Bayes, statistical thinking
2. **Linear Regression & Correlation** — least squares from scratch
3. **Linear Algebra Week** — matrix mechanics in NumPy
4. **First End-to-End Pipeline** — categorical classification on Mushrooms (and a dataset of your choice)
5. **Regression++** — multilinear, regularization, SVD, PCA, DIY LinReg++
6. **Classification Classics** — Logistic Regression, k-NN, Decision Trees
7. **Information Theory, SVM, Validation, Ensembles**
8. **Anomaly Detection** — fraud, GMMs, SMOTE
9. **CNNs** — convolutions, LeNet, AlexNet, activation theory
10. **Transfer Learning & Time Series** — fine-tuning ResNet, AAPL prediction
11. **RNNs & Sequence-to-Sequence** — Shakespeare, sentiment, NMT, Bahdanau attention
12. **Transformers, LLMs, and Generative Models** — from "Attention is All You Need" to VAEs

---

## Unit 1 — Foundations (Aug 21 – Sep 4)

The on-ramp. Two weeks of getting students fluent enough in pandas, matplotlib, and Bayesian thinking that the real ML can begin.

- **Aug 21 — Setup & Python intro.** [Quick-Intro-To-Python notebook](https://aet-cs.github.io/white/2025/ML/notebooks/Quick-Intro-To-Python.ipynb).
- **Aug 25 — Pandas with weather data.** First contact with real data: [weather notebook](https://aet-cs.github.io/white/2025/ML/notebooks/weather.ipynb) loading the Leesburg [airport CSV](https://aet-cs.github.io/white/2025/ML/notebooks/weather-daylight.csv).
- **Aug 27 — [Weather exercises](https://aet-cs.github.io/white/2025/ML/weather_exercises/).** Eleven exercises in three tiers (Beginner / Intermediate / Advanced) — the same scaffold-by-difficulty pattern that will reappear throughout the year. Includes the classic "is weekend weather measurably different from weekday weather?" investigation, which sneaks chi-square testing into Week 2.
- **Sep 2 — Bayes Theorem.** [Notes PDF](https://aet-cs.github.io/white/2025/ML/bayes-notes.pdf) plus a [student notebook](https://aet-cs.github.io/white/2025/ML/notebooks/Bayes_Theorem_Student.ipynb). Quick Python loops side-tutorial. The pedagogical choice to introduce Bayes *before* any actual ML model is a strong one — it primes students to think probabilistically about every classifier that follows.
- **Sep 4 — London Weather project.** First real deliverable: take a 50-year dataset, defend a claim about climate. The framing — *"You can define what makes weather 'worse' – part of this is definitely subjective"* — sets the tone that ML work is partly about justifying choices.

---

## Unit 2 — Linear Regression & Correlation (Sep 8 – Sep 12)

The first model. Derived from scratch before scikit-learn enters the room.

- **Sep 8 — Linear regression derivation.** [PDF notes](https://aet-cs.github.io/white/2025/ML/notes/Linear_regression_derivation.pdf) and the [Least-Squares notebook](https://aet-cs.github.io/white/2025/ML/notebooks/Least-Squares.ipynb). Also: the US AI Olympiad announcement.
- **Sep 10 — Coefficient of Determination.** [Notes on R²](https://aet-cs.github.io/white/2025/ML/notes/Correlation_Coefficient/) and the [Correlation notebook](https://aet-cs.github.io/white/2025/ML/notebooks/Correlation.ipynb).
- **Sep 12 — Measures of spread, custom regression assignment.** Find your own dataset, do a single-variable linear regression, defend the fit. London weather revisited with regression lines.

---

## Unit 3 — Linear Algebra Week (Sep 16 – Sep 18)

A self-contained pause to fix the mathematical foundation before things get matrix-heavy.

- **Sep 16 — Three NumPy notebooks back-to-back.** [Linear Algebra and Python](https://aet-cs.github.io/white/2025/ML/notebooks/Linear_Algebra_and_Python.ipynb), [Matrices Index Warmup](https://aet-cs.github.io/white/2025/ML/notebooks/Matrices_Index_Warmup-Student.ipynb), [Intro to Matrices in NumPy](https://aet-cs.github.io/white/2025/ML/notebooks/Intro_to_Matrices_in_NumPy.ipynb).
- **Sep 18 — Finish and submit.**

---

## Unit 4 — First End-to-End Pipeline (Sep 22 – Sep 26)

The "now do it yourself" hinge of the first quarter. Students see one worked categorical-classification pipeline, then build their own.

- **Sep 22 — [Mushroom exploration](https://aet-cs.github.io/white/2025/ML/notebooks/Mushroom_Student.ipynb).** Cleaning, encoding, EDA, modeling.
- **Sep 24 — Self-selected categorical analysis.** Same shape as Mushroom, your own dataset. First moment in the course where students are expected to choose the dataset *and* defend the conclusions in a markdown cell.
- **Sep 26 — [Bayes Error notebook](https://aet-cs.github.io/white/2025/ML/notebooks/Bayes-Error-Student.ipynb).** A theoretical capstone for the unit — the limit of what any classifier can achieve.

---

## Unit 5 — Regression++ (Sep 30 – Oct 27)

The longest unit. Where regression grows up into a real toolkit, and where linear algebra pays off.

- **Sep 30 — Multilinear regression begins.** [Lecture notes](https://aet-cs.github.io/white/2025/ML/notes/Multilinear_regression.html), [Test Scores](https://aet-cs.github.io/white/2025/ML/notebooks/Test_Scores.ipynb), [Life Expectancy](https://aet-cs.github.io/white/2025/ML/notebooks/Life_Expectancy_Student.ipynb) ([Kaggle source](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/data)).
- **Oct 3 — Normalization and regularization.** [Life Part 2](https://aet-cs.github.io/white/2025/ML/notebooks/Life_Part_2_Student.ipynb).
- **Oct 9 — Article research.** Groups find 3 articles each on a chosen topic. Hard to tell from the calendar entry alone, but this looks like an early dry-run for the spring research-pitch project.
- **Oct 14 — SVD notes.** Matrix multiplication as coordinate transform. [AI-generated SVD notes](https://aet-cs.github.io/white/2025/ML/notes/svd_notes_ml.md) (flagged as "OK-ish" — honest about provenance, a nice touch for students learning to evaluate sources).
- **Oct 16 — SVD applied.** [Visualizing Transformation Matrices](https://aet-cs.github.io/white/2025/ML/notebooks/Visualizing_Transformation_Matrices.ipynb) → [Low Rank Approximations](https://aet-cs.github.io/white/2025/ML/notebooks/Low_Rank_Matrix_Approximations.ipynb) → [Image Compression](https://aet-cs.github.io/white/2025/ML/notebooks/Image-Compression.ipynb) of Gauss. The "compress Gauss" moment is a high-payoff demo.
- **Oct 21 — [PCA](https://aet-cs.github.io/white/2025/ML/notebooks/PCA.ipynb).** Image Compression turned in. New homework: regression with PCA.
- **Oct 23 — Notebook viewer test, DIY LinReg draft due Friday night.**
- **Oct 27 — DIY LinReg++ due.** Per the [requirements](https://aet-cs.github.io/white/2025/ML/notes/DIY-LinReg-Plus.md): feature analysis (cleaning, distributions, collinearity), L1/L2 alpha selection, model interpretation, PCA dimension sweep, "best model" defense. This is the first major synthesis assignment of the year — and it asks for the same kind of judgment an actual data scientist would render.

---

## Unit 6 — Classification Classics (Nov 5 – Nov 21)

Three algorithms in three weeks. Each one introduced with a different dataset and a different motivating question.

- **Nov 5 — [Logistic Regression](https://aet-cs.github.io/white/2025/ML/notebooks/Cancer_Logistic_Student.ipynb).** Breast cancer classification.
- **Nov 7 — Logistic Regression on [loan data](https://aet-cs.github.io/white/2025/ML/data/loan_data.csv).** "Do the best LogReg you can." Open-ended, results-driven.
- **Nov 11 — k-Nearest Neighbors.** Devise the algorithm in class first, [then implement](https://aet-cs.github.io/white/2025/ML/notebooks/knn-Student.ipynb). The algorithm-before-library order is consistent throughout this course.
- **Nov 13 — k-NN on [Digits](https://aet-cs.github.io/white/2025/ML/notebooks/digits-student.ipynb).** Plus a [pointer](https://towardsdatascience.com/comprehensive-guide-to-approximate-nearest-neighbors-algorithms-8b94f057d6b6) to approximate-NN methods (Spotify, Netflix). Connects classroom algorithm to industrial scale.
- **Nov 17 — Decision Trees, hand-classifying.** WillWait? dataset done by hand. Entropy + Information Gain motivated.
- **Nov 19 — [Decision Tree Lab](https://aet-cs.github.io/white/2025/ML/notebooks/Decision_Tree_Student.ipynb)** on income data.
- **Nov 21 — Shannon entropy as information measure.** Encoding strings. *(The calendar entry trails off after "Ha" — likely a partial draft.)*

---

## Unit 7 — Information Theory, SVM, Validation, Ensembles (Dec 2 – Dec 16)

The last classical-ML push before deep learning. Arithmetic codes connect back to the Shannon material; SVM gets the full margin-and-kernel treatment; cross-validation and ensembles are the closing professional-practice topics.

- **Dec 2 — Arithmetic Codes.** *(Two-hour delay, so likely a compressed lecture session.)*
- **Dec 4 — [SVM notes](https://aet-cs.github.io/white/2025/ML/notebooks/Notes-SVM.ipynb) and [SVM Lab](https://aet-cs.github.io/white/2025/ML/notebooks/SVM_Lab-Student.ipynb).**
- **Dec 8 — [Cross Validation & Grid Search](https://aet-cs.github.io/white/2025/ML/notebooks/CrossValidation.ipynb).** Applied to [Twitter sentiment](https://aet-cs.github.io/white/2025/ML/data/twitter_training.csv) with SVM + TF-IDF.
- **Dec 10 — Fake news + [word embeddings](https://aet-cs.github.io/white/2025/ML/data/word2vec/).** First exposure to learned representations.
- **Dec 12 — Finish CV/GS notebooks.**
- **Dec 16 — [Ensemble Methods](https://aet-cs.github.io/white/2025/ML/notebooks/Ensemble_Methods.ipynb).**
- **Dec 18 — AET Challenge Day.**

---

## Unit 8 — Anomaly Detection (Jan 5 – Jan 9)

A short, focused unit that doubles as the second-quarter capstone.

- **Jan 5 — Ensembles applied** to a previously-analyzed dataset, submitted.
- **Jan 7 — Anomaly detection on [credit card fraud](https://aet-cs.github.io/white/2025/ML/notebooks/anomaly/CreditCard.ipynb).** Two approaches contrasted: [SMOTE oversampling](https://aet-cs.github.io/white/2025/ML/notebooks/anomaly/SMOTE-credit.ipynb) and a [Gaussian Mixture Model](https://aet-cs.github.io/white/2025/ML/notebooks/anomaly/GMM-credit.ipynb).
- **Jan 9 — Quarter project.** Find any [UCI dataset](http://archive.ics.uci.edu/datasets/) and model it. Classification, regression, or anomaly detection — student's choice.

---

## Unit 9 — CNNs (Jan 20 – Feb 26)

Deep learning enters. The unit unfolds across nearly six weeks because it's also when the spring research-pitch project is seeded.

- **Jan 20 — [CIFAR-10 baseline](https://aet-cs.github.io/white/2025/ML/notebooks/CIFAR10_Training.ipynb).** Modify the network, improve accuracy.
- **Feb 2 — Custom TF dataset.** Find a [tensorflow_datasets](https://www.tensorflow.org/datasets/catalog/) classification task and replicate the CIFAR sections: load → sample → build → train → curve → augment → improve → re-curve.
- **Feb 4–6 — Presentations.** *(Inferred from calendar: students present their TF-datasets work and earlier project results.)*
- **Feb 9 — [Research topic brainstorm](https://aet-cs.github.io/white/2025/ML/research-list/).** Three plausible ideas, slideshow due end of class. The framing — *"the best research projects start out as products"* — is good general advice that students rarely hear stated explicitly.
- **Feb 11 — [Image Convolutions](https://aet-cs.github.io/white/2025/ML/notebooks/ImageConvolutions.ipynb).** What a convolution actually is, before any "convolutional" *network*.
- **Feb 18 — LeNet from scratch.** Using [Dive into Deep Learning](https://d2l.ai) chapter 7.6 ([PDF excerpt](https://aet-cs.github.io/white/2025/ML/notes/d2l.ai-LeNet.pdf)). Also: the [MNIST 3D visualization](https://adamharley.com/nn_vis/cnn/3d.html) — a great hook. Quick research-idea pitches the next class: 2 minutes, no slides, problem/solution/who-cares.
- **Feb 20 — Presentations.**
- **Feb 24 — [Activation Functions](https://aet-cs.github.io/white/2025/ML/notebooks/Activation-Functions.ipynb)** during Engineering Week. The "why activations at all?" question deserves its own session.
- **Feb 26 — [AlexNet on CIFAR-100](https://aet-cs.github.io/white/2025/ML/notebooks/alexnet.ipynb).** Includes a [resize patch utility](https://aet-cs.github.io/white/2025/ML/patch/).

---

## Unit 10 — Transfer Learning & Time Series (Mar 2 – Mar 18)

The "you don't have to train from scratch" insight, and a pivot toward sequences.

- **Mar 2 — [Bird Calls](https://aet-cs.github.io/white/2025/ML/notebooks/Birds.ipynb).** Snow day notebook, audio classification.
- **Mar 10 — Fine-tuning ResNet / MobileNet.** Freeze all but the last layers, retrain.
- **Mar 12 — Collect-your-own-images project.** Students photograph things around the school and train a classifier. Real-world data collection plus transfer learning.
- **Mar 16 — Guest speaker.**
- **Mar 18 — Time series on [AAPL stock prices](https://aet-cs.github.io/white/2025/ML/data/AAPL.csv).** The [Apple prediction reference](../data/apple-prediction.png) shows what 64-step history + a single hidden node can do — a nice setup for "now let's see what an actual RNN buys us."

---

## Unit 11 — RNNs & Sequence-to-Sequence (Mar 24 – Apr 17)

Where the course pivots fully into modern NLP. The progression — char-level Shakespeare → sentiment → seq2seq translation → attention — mirrors the historical sequence of papers that led to Transformers.

- **Mar 24 — RNNs introduced.** [Karpathy's "Unreasonable Effectiveness"](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) plus [Shakespeare generation](https://aet-cs.github.io/white/2025/ML/notebooks/Shakespeare_Student.ipynb).
- **Apr 6 — Reading day.**
- **Apr 8 — [Sentiment Analysis](https://aet-cs.github.io/white/2025/ML/notebooks/sentiment_analysis-student.ipynb).** IMDB classification with RNNs.
- **Apr 13 — [NMT starter](https://aet-cs.github.io/white/2025/ML/notebooks/Neural-Machine-Translation-Starter.ipynb).** Build an LSTM seq2seq translator.
- **Apr 15 — Improve and add round-trip (eng→span→eng).** [Test cases](https://aet-cs.github.io/white/2025/ML/notes/translation_examples/) and a [reference notebook](https://aet-cs.github.io/white/2025/ML/notebooks/seq2seq_nmt_reference.ipynb) with Attention and Beam Search.
- **Apr 17 — Attention layer + Beam Search.** Implement Bahdanau-style attention. The note that this is *"a pain to get right in tensorflow"* is the kind of honesty students need to hear.

---

## Unit 12 — Transformers, LLMs, and Generative Models (Apr 23 – May 11)

The final unit. After eight months of building toward it, Transformers get four classes; LLMs and generative models close out the year.

- **Apr 23 — [PyTorch foundations](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)** and 3Blue1Brown's [Chapter 5 video](https://www.3blue1brown.com/?topic=neural-networks). Switching frameworks at exactly the right moment — Transformers in TF/Keras would have been needless suffering.
- **Apr 27 — [Transformer NMT with Spanish](https://aet-cs.github.io/white/2025/ML/notebooks/transformer_nmt_with_spanish.ipynb).** 3b1b Ch6, the [original paper](https://arxiv.org/pdf/1706.03762), and [comprehension questions](https://aet-cs.github.io/white/2025/ML/notebooks/transformer_nmt_questions/). The questions are extraordinarily good — they probe specifically the places students gloss over (why √d_k, why register_buffer vs Parameter, what changes when QKV are the same vs different, why the embedding-times-√d_model trick). This is the closest thing the year has to a final exam disguised as homework.
- **Apr 29 — [CharGPT](https://aet-cs.github.io/white/2025/ML/notebooks/charGPT_assignment.ipynb).** Transformers for Shakespeare, with [tokenization hints](https://aet-cs.github.io/white/2025/ML/notebooks/tokens.txt).
- **May 1 — Discussion + fine-tune GPT-2.** Class fishbowl on Transformer questions (leader + scribe + collective answer doc), then fine-tune a GPT-2-style model on a text corpus of choice. The honest preamble — *"There are many tutorials online, most of them are buggy so you'll need to debug"* — is exactly the right framing for what fine-tuning actually feels like.
- **May 5 — [Image captioning](https://aet-cs.github.io/white/2025/ML/notebooks/image_captioning_assignment.ipynb).** Vision-language at the seam between Units 9 and 11.
- **May 7 — Catch-up day.**
- **May 11 — [Variational Autoencoders](https://aet-cs.github.io/white/2025/ML/notebooks/VAE_celeba_student.ipynb)** on CelebA, with [VAE notes](https://aet-cs.github.io/white/2025/ML/notes/vae_notes.pdf). Generative modeling as the year's closing topic — a nice rhyme with the autoregressive generation that started the RNN unit.

---

## Pedagogical Themes That Run Through the Year

A few patterns that aren't visible from any single calendar entry but become obvious from a year-end view:

- **Algorithm-before-library.** k-NN, linear regression, the SVD, and decision-tree entropy are all derived or implemented from first principles before scikit-learn or PyTorch is invoked. Students *earn* the libraries.
- **Real datasets from day one.** Leesburg airport weather, London weather, breast cancer, loan defaults, credit card fraud, CelebA, Apple stock. Almost nothing toy.
- **Tiered exercises.** Beginner / Intermediate / Advanced, repeatedly — the weather exercises set the template that recurs in many later assignments.
- **Markdown-cell discussion required.** Conclusions live in prose, not just code output. This is the single most consistent assignment requirement across the year.
- **Iterative deliverables.** DIY Linear Regression is built across three classes: draft → with regularization → with PCA. Many other projects follow the same "submit something incomplete, then improve it" pattern.
- **Honesty about resource quality.** The "OK-ish AI-generated notes" on SVD, the "tutorials are buggy" warning before GPT-2 fine-tuning — students are taught to triangulate sources rather than trust any single one.
- **Two presentation cycles per year.** February (research idea pitches) and at least one other window in the spring. Presenting before researching, not after.

---

## Gaps & Opportunities

Things the calendar suggests would benefit from filling in. None of these are essential — the course is whole as it stands — but each is a low-effort, high-payoff edit.

**Calendar entries that need finishing:**
- **11/21** ends mid-word ("Ha"). Probably the Huffman coding or Hamming code lecture, given the Shannon-entropy context.
- **5/7** is just "Continue work on previous notebooks and assignments" — a real holding pattern. If you taught something specific that day, worth recording.
- **5/11** appears to be the last entry. If there's anything between then and the end of the AP exam window / end of year, it's not on the calendar.

**Small editorial fixes:**
- "September 26, 2026 (Friday)" — typo, should be 2025.
- "4/6 (monday)" — lowercase m.
- "**Attention* Layer**" on 4/17 has a stray asterisk that breaks markdown emphasis.
- "12/4/2025 (Thursday)" — December 4, 2025 was actually a Thursday, fine. But the inconsistent date formats across the year (some "MM/DD", some "Month DD, YYYY") could be normalized.

**Dates with notebooks but no description:**
- **3/16 (Guest speaker)** — worth a sentence about who and what they spoke on, for posterity.
- **4/6 reading assignment** — the [bit.ly link](https://bit.ly/4bVoiGP) is opaque. Naming the source would help future-you.

**Potential additions:**
- The course has a clear *arc* but no explicit **syllabus** linked from the calendar. A short "what this course is" preamble at the top of the calendar (one paragraph) would help new students and parents.
- The transformer comprehension questions are the strongest assessment artifact of the year. Earlier units could benefit from a similar question set (especially SVD/PCA, where the math leaves students with more rote understanding than conceptual).
- An **alumni / next-year-students FAQ** linking final projects would be a great way to memorialize student work alongside the materials.
- The two presentation cycles in spring don't seem to have written deliverables on the calendar — would be nice to capture *what the students presented* in some form (titles, abstracts, project repos).

---

## Resource Inventory

For reference. Pulled from the calendar links, deduplicated.

**Standalone notes / writeups:**
- [Bayes notes (PDF)](https://aet-cs.github.io/white/2025/ML/bayes-notes.pdf)
- [Linear regression derivation (PDF)](https://aet-cs.github.io/white/2025/ML/notes/Linear_regression_derivation.pdf)
- [Correlation Coefficient notes](https://aet-cs.github.io/white/2025/ML/notes/Correlation_Coefficient/)
- [Statistics notes (AI-generated)](https://aet-cs.github.io/white/2025/ML/statistics.html)
- [Multilinear regression notes](https://aet-cs.github.io/white/2025/ML/notes/Multilinear_regression.html)
- [SVD notes (AI-generated)](https://aet-cs.github.io/white/2025/ML/notes/svd_notes_ml.md)
- [DIY LinReg++ requirements](https://aet-cs.github.io/white/2025/ML/notes/DIY-LinReg-Plus.md)
- [VAE notes (PDF)](https://aet-cs.github.io/white/2025/ML/notes/vae_notes.pdf)
- [Translation examples](https://aet-cs.github.io/white/2025/ML/notes/translation_examples/)
- [LeNet from D2L (PDF excerpt)](https://aet-cs.github.io/white/2025/ML/notes/d2l.ai-LeNet.pdf)

**Notebooks, roughly by unit:**

| Unit | Notebooks |
|------|-----------|
| Foundations | Quick-Intro-To-Python, weather, Bayes_Theorem_Student |
| Regression | Least-Squares, Correlation |
| Linear Algebra | Linear_Algebra_and_Python, Matrices_Index_Warmup, Intro_to_Matrices_in_NumPy |
| First pipeline | Mushroom_Student, Bayes-Error-Student |
| Regression++ | Test_Scores, Life_Expectancy_Student, Life_Part_2_Student, Visualizing_Transformation_Matrices, Low_Rank_Matrix_Approximations, Image-Compression, PCA |
| Classification | Cancer_Logistic_Student, knn-Student, digits-student, Decision_Tree_Student |
| Info theory / SVM / CV / Ensembles | Notes-SVM, SVM_Lab-Student, CrossValidation, Ensemble_Methods |
| Anomaly | CreditCard, SMOTE-credit, GMM-credit |
| CNNs | CIFAR10_Training, ImageConvolutions, Activation-Functions, alexnet |
| Transfer / Time series | Birds |
| RNNs | Shakespeare_Student, sentiment_analysis-student, Neural-Machine-Translation-Starter, seq2seq_nmt_reference |
| Transformers / LLMs | transformer_nmt_with_spanish, charGPT_assignment, image_captioning_assignment, VAE_celeba_student |

**External resources cited:**
- 3Blue1Brown Neural Networks series (Ch 5, Ch 6)
- Karpathy, "The Unreasonable Effectiveness of RNNs" (2015)
- Vaswani et al., "Attention is All You Need" (2017)
- *Dive into Deep Learning* (d2l.ai)
- PyTorch official tutorials
- UCI ML Repository
- TensorFlow Datasets catalog

---

*Outline compiled May 15, 2026. Worth treating as a v1 — your call on whether to publish it as a course page, fold pieces into the syllabus, or just keep it as an end-of-year retrospective.*
