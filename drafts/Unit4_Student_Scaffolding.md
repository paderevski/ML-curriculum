# Unit 4: Your First End-to-End ML Project

Welcome to the unit where everything starts to click. Up to now you've been learning components — pandas, plotting, Bayes' theorem, statistics, linear algebra. This week you put them together into a real machine learning pipeline.

By the end of three classes you'll be able to take a raw dataset (with missing values, weird types, no documentation), turn it into something a model can use, try several classifiers, compare them, and understand why no classifier can ever drive error to exactly zero.

---

## Before you start

You should already be comfortable with:

- Loading data into a pandas DataFrame, filtering rows, selecting columns
- Making basic plots with matplotlib
- The Bayes' theorem ideas from [Unit 1](https://aet-cs.github.io/white/2025/ML/bayes-notes.pdf) — you'll lean on the underlying probability intuition

> ⚠️ **GAP:** No single "readiness check" page exists. A short quiz or self-check list — "if these five things look familiar, you're ready" — would help self-learners gauge whether to jump in or review.

**Time budget:** roughly three 90-minute class sessions, or about 5 focused hours on your own.

---

## Day 1 — Mushroom Exploration

**Open:** [`Mushroom_Student.ipynb`](https://aet-cs.github.io/white/2025/ML/notebooks/Mushroom_Student.ipynb)
**Dataset:** ~26,000 mushrooms, each described by 22 categorical features (cap color, odor, gill spacing, habitat, etc.). Target: edible (`e`) or poisonous (`p`).

This notebook is a full tour of the ML workflow. Your job today is to **read carefully and run every cell.** You won't write much code yourself — that's Day 2. Focus on understanding what each step does and why.

### Key concepts to watch for

**Data cleaning (cells 7–19).** Real data is messy. You'll see two strategies for dealing with missing values: *dropping rows* (you lose data) and *imputation* (you fill in something reasonable, here the mode of each column). Both are valid; the choice depends on how much data you have and why values are missing.

> ⚠️ **GAP:** No standalone notes on missing-data strategies. A 1-page lesson covering `dropna` vs. mean/median/mode imputation vs. more sophisticated approaches would help. Currently students see one technique and the alternative is named in passing.

**Exploratory Data Analysis (cells 22–34).** The point isn't pretty plots — it's *finding patterns.* The cap-color vs. class plot is unsurprising. The odor vs. class plot is the moment the dataset gives up most of its secret.

**Cramér's V correlation matrix (cells 36–40).** You can't compute Pearson correlation on strings. Cramér's V is the equivalent measure for categorical data — it ranges 0 to 1 and tells you how strongly two categorical features are associated.

> ⚠️ **GAP:** The notebook says "treat as a black box for now," which is reasonable. But a half-page explainer — "Cramér's V is built from a chi-squared test of independence, normalized so it ranges 0 to 1" — would let curious students close the loop.

**One-hot encoding (cell 43).** `pd.get_dummies(X)` turns every categorical column into a set of 0/1 columns. This is how categorical data becomes the numerical data scikit-learn needs.

> ⚠️ **GAP:** No standalone notes on encoding strategies. One-hot is the right tool here, but ordinal, target, and embedding encodings come up later. A short reference page naming the alternatives would help.

**Train/test split (cell 46).** *Never* evaluate a model on the same data it was trained on. The 20% test set is data the model has never seen — your real measure of generalization.

**Classification metrics (cells 47–52).** Accuracy alone is misleading when classes matter unequally. With mushrooms, a false negative (a poisonous mushroom labeled edible) is *much* worse than a false positive. Read the classification report carefully:

- **Precision** of "p": of the mushrooms you *called* poisonous, what fraction actually were?
- **Recall** of "p": of the mushrooms that actually *were* poisonous, what fraction did you catch?
- **F1**: a balance between precision and recall (their harmonic mean).
- The **confusion matrix** shows you exactly which mistakes the model is making.

> ⚠️ **GAP — biggest gap in the unit:** No standalone notes on classification metrics. This is one of the most important conceptual pieces in the whole course, and right now it lives in a single markdown cell. A 1-page explainer with worked examples (and the F1 formula) would pay off all year long.

**The sklearn API (cells 55–68).** *Every* scikit-learn classifier follows the same pattern: `clf = SomeClassifier(); clf.fit(X_train, y_train); clf.predict(X_test)`. The notebook runs seven different models with nearly identical code to make the point. You don't need to understand *how* each model works yet — that's the rest of the year. Just see that the workflow is the same for all of them.

### Checkpoint

Before moving on, make sure you can answer:

1. Why drop `veil-type` from the data?
2. What does "mode imputation" mean and when would you choose it over dropping rows?
3. Why is recall on "poisonous" more important than overall accuracy here?
4. What does `pd.get_dummies` do, and why is it needed before training?
5. Did all seven classifiers do equally well? Which would you trust most, and why?

---

## Day 2 — Your Own Dataset

Today you apply the workflow to a dataset you choose.

### The assignment

Pick a dataset from anywhere online — Kaggle, the [UCI Repository](http://archive.ics.uci.edu/datasets/), data.gov, wherever — and do a similar analysis to the one you just did with mushrooms.

**Required:**

- Restrict to *categorical* features only
- Clean the data; explain in markdown what you did about missing values and why
- Make at least three plots that reveal something about the data; at least one must use `groupby`
- Train at least three different classifiers and compare them
- End with a markdown cell discussing what you found — what's the target, what predicts it, which model worked best, and what you'd do next

**Turn in:** Your notebook, with a title cell and the markdown discussion. Upload via the class form by end of class.

> ⚠️ **GAP:** This assignment lives only as a paragraph in the calendar. A standalone page (e.g., `/notes/categorical-analysis-assignment.md`, paralleling `DIY-LinReg-Plus.md`) would let students reference the requirements without scrolling. The required bullet list above is my proposal — your call on whether to make it that specific.

### Choosing a dataset

The hardest part isn't the modeling — it's picking a dataset where you actually have a clear question. Good signs to look for:

- The target column is obvious (something like "result", "outcome", "class", "winner")
- Most features are categorical, or could be bucketed into categories
- The dataset is under ~100,000 rows so things run fast
- You actually find it interesting (this matters more than you'd think)

> ⚠️ **GAP:** A short "Dataset Picker" page with 5–10 vetted datasets known to work well here would help students who freeze at the selection step. Mushroom-like targets, Titanic, wine quality (bucketed), Pokémon types, etc.

---

## Day 3 — Bayes Error

**Open:** [`Bayes-Error-Student.ipynb`](https://aet-cs.github.io/white/2025/ML/notebooks/Bayes-Error-Student.ipynb)

Today's question: **is it always possible to drive classifier error to zero?**

Spoiler: no. And there's a name for the floor — **Bayes error.** Knowing this floor exists, and learning to recognize when you've hit it, will keep you from chasing impossible goals for the rest of the course.

### What you'll do

The notebook walks through five experiments with synthetic 2D Gaussian data:

1. **Well-separated groups.** Two Gaussians far apart. Error is essentially zero.
2. **Overlapping groups.** Same distributions, moved closer. Error appears even with the optimal boundary.
3. **Find the optimal split.** Scan over 41 candidate split points and find the one that minimizes error.
4. **Different variances.** When the two distributions have different spreads, the optimal boundary isn't the midpoint anymore. Find it empirically.
5. **Theory.** Derive the optimal boundary for equal-variance Gaussians, then for unequal-variance.

### Key concepts

**Irreducible error.** When two classes' distributions overlap, *any* classifier — no matter how clever — will make mistakes on the overlapping region. That overlap *is* the Bayes error.

**Bayes-optimal classifier.** The classifier that assigns each point to the class that's most likely given the data. By definition this is the best you can do.

> ⚠️ **GAP:** The bridge from Bayes' theorem (Unit 1) to the Bayes-optimal classifier (this unit) is never spelled out. A short paragraph — "the Bayes-optimal classifier *uses* Bayes' theorem to choose the most likely class for each input; the Bayes error is what's left over when classes genuinely overlap" — would tie the units together. This connection is the conceptual heart of the unit.

**The grid-search pattern.** In Part 3, you scan over many candidate split points and pick the best. This same pattern — *try many hyperparameter values, plot the curve, pick the best* — will reappear constantly: `k` in k-NN, `C` in SVM, depth in Decision Trees, learning rate in neural networks. This notebook is where the pattern starts.

### Heads-up on bugs

- **Cell 13** references `errors_close` and `error_rate_close` before they're defined. You're meant to compute these above the print statement; if you run the cell as-is you'll get a `NameError`. Define them first.
- **Cells 7 and 8** are nearly duplicate (same plot, second one adds the decision boundary). Run both; the duplication is intentional even if it reads redundantly.

### Checkpoint

After working through the notebook, you should be able to:

1. Explain in plain English why a classifier on overlapping classes can't reach 0% error.
2. Derive the optimal boundary between two 1D Gaussians with equal variance and means μ₁ and μ₂. (Hint: it's where the two probability densities are equal.)
3. Predict what happens to the optimal boundary when one distribution has much higher variance than the other.

> ⚠️ **GAP:** Part 5's questions are open-ended with no hints in the notebook itself. The "where the densities are equal" hint above isn't currently anywhere in the materials. A brief note (or a separate `bayes-error-derivation.pdf` working through the equal-variance case) would scaffold less-mathematical students through the derivation.

---

## What you've learned, and what's next

By the end of Unit 4 you have the *complete loop* of an ML project: load → clean → encode → split → train → evaluate → interpret. Everything else this year is variations on this loop with different models and different data types.

**Unit 5** starts the deep dive into multilinear regression, regularization, the SVD, and PCA — the tools for working with continuous data and understanding the *structure* hidden inside it. The workflow you just learned won't change. The models do.

---

## Summary: where the materials are too thin

For Patrick — the gaps I flagged above, consolidated, in rough order of payoff:

1. **A standalone lesson on classification metrics** (precision, recall, F1, confusion matrices). Highest payoff — used all year, currently only one markdown cell.
2. **A bridging paragraph or page connecting Bayes' theorem → Bayes-optimal classifier → Bayes error.** Conceptually central, never made explicit.
3. **A standalone Day-2 assignment page with rubric**, paralleling `DIY-LinReg-Plus.md`.
4. **Notes on missing-data strategies** (dropna vs. various imputations).
5. **Notes on categorical encoding** (one-hot vs. ordinal vs. target).
6. **A short Cramér's V explainer** so the "black box" doesn't have to stay black.
7. **A Dataset Picker page** with 5–10 vetted datasets for the Day-2 assignment.
8. **A worked-derivation hint or PDF** for the Part-5 boundary questions in Bayes Error.
9. **A readiness-check page** at the start of the unit listing prerequisites from Units 1–3.

Items 1, 2, and 3 would do the most work. Items 4–6 are 30-minute writes each. Item 7 is mostly curation. Items 8 and 9 are quick wins.
