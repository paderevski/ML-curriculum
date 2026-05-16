# Unit 4 — First End-to-End Pipeline
**Sep 22 – Sep 26 (3 class days)**

The pivot point of the first quarter. Up through Linear Algebra Week, students have been learning *components* — pandas, plotting, regression, matrix mechanics. Unit 4 is the first time the components assemble into a recognizable ML workflow: load → clean → explore → encode → split → fit → evaluate → interpret. Three days, two scaffolded notebooks bracketing one open-ended assignment.

**Unit arc:**
1. **Sep 22 — Mushroom Exploration:** a fully worked example, the teacher driving. Students mostly read and run.
2. **Sep 24 — Self-selected categorical analysis:** students reproduce the workflow on a dataset they choose. The hinge.
3. **Sep 26 — Bayes Error:** a theoretical capstone — what's the *floor* of error rate, and why can't classifiers reach 0% on overlapping classes?

The two notebooks bracket the unit deliberately: Mushroom shows what classifiers *do*, Bayes Error shows what they *can't*. The student project in the middle is where they internalize the workflow by repeating it.

---

## Day 1 — Mushroom Exploration (Sep 22)

[`Mushroom_Student.ipynb`](https://aet-cs.github.io/white/2025/ML/notebooks/Mushroom_Student.ipynb) — 71 cells (37 markdown, 34 code) — dataset: [`mushroom.csv`](https://aet-cs.github.io/white/2025/ML/data/mushroom.csv), ~26,000 mushrooms × 22 categorical features, target: edible/poisonous.

A complete EDA-to-modeling tour on one dataset, end to end. Strikingly, this is almost entirely a **read-and-run** notebook — there are no `# YOUR CODE HERE` markers. The active work happens the next class. The point of Day 1 is *exposure to the workflow*, not practice.

### Pedagogical moves worth flagging

- **The motivating stakes are real.** The introduction frames false negatives as "deadly" — a poisonous mushroom labeled edible kills you. This is set up early so that when precision/recall/F1 arrive in cell 47, students already know why "accuracy" alone is insufficient. The dataset choice does pedagogical work the teacher didn't have to do.
- **Two paths through missing data, both demonstrated.** Cell 17 shows `df.dropna().shape` — students see what *would* happen if they just dropped rows. Cell 19 then chooses mode imputation instead. This is rare; most teaching materials demonstrate only the chosen path. Showing both makes the choice visible.
- **The `veil-type` drop in cell 8** is a quiet lesson in feature evaluation. The column has one unique value across all 26,000 rows — students learn that *constant features carry no information* and can be discarded. No fanfare; just done.
- **Seaborn is introduced explicitly as a new library** (cell 24): *"We'll introduce a new plotting library — 'seaborn', which has some advantages over matplotlib."* That meta-framing — naming the tool, saying why — is a small move that helps students build mental indices.
- **Cramér's V as a black box.** Cell 36: *"You can treat `cramers_v` as a black box for now."* Explicit permission to use without understanding is a deliberate technique here — students need a heatmap of categorical correlations *now*, not a chi-squared digression. The function is short enough that curious students can read it.
- **The cell-43 reload.** *"In this cell we import some methods we'll use, reload the data frame (just to be safe), re-pre-process-it..."* The "just to be safe" is the teaching moment — it normalizes the habit of restarting from a known state when you're about to do something different (modeling vs. exploration).
- **`classifier_tryout` (cell 55) is taught as a pattern, not just utility code.** The framing is explicit: *"note how the scikit-learn API makes dealing with each of the models very similar."* The helper function exists to *demonstrate* the uniformity of the sklearn fit/predict interface. That's the actual lesson, not the helper.
- **Seven classifiers in a row** (Decision Tree, Random Forest, SVM, Logistic Regression, k-NN, GradientBoost, MLP). Students recognize roughly zero of these in detail at this point in the course. That's intentional — every one of them will be unpacked properly later in the year. The point here is "all of these exist, all of them work, and `clf.fit(X, y); clf.predict(X_test)` is the entire interface."
- **The closing prompt is interpretive, not auto-graded.** *"Which model above do you think is the best? Which one would you start with to try to get even better results?"* This is the kind of question that distinguishes ML from algorithm courses — there isn't a single answer and the student has to defend a choice.

### What the student actually does

Reads, runs, observes. The "active" task is the Sep 24 follow-up, where they're told: *"As an application, find your own dataset and try to mirror the process we took here."* Day 1 is a guided walkthrough; Day 2 is the test.

### Notes & small issues

- The mushroom CSV has a column header typo: `ruises` instead of `bruises`. This is in the source data file, not introduced by the notebook — and it's actually fine pedagogically (students learn that real data has spelling errors and you don't fix them silently).
- Cells 27 and 28 are nearly duplicate plots (cap-color frequency, then cap-color × class). Could be consolidated into one cell with two subplots, but the separation arguably helps students see "raw distribution" vs. "distribution by target."
- The `Mushroom_Key.ipynb` in the repo (50 cells vs. 71) is a working-teacher version with a local file path (`/home/pewhite/github/aet-cs/ML-datasets/`) and explores `LabelEncoder` + scipy's `chi2` directly, plus a `class_weight={'e':100, 'p':1}` trick that biases Random Forest toward catching poisonous mushrooms. None of that made it into the student version. The class-weight idea would be a great optional extension to surface — it's a one-line change with a dramatic recall shift.
- The MLP at the end has `hidden_layer_sizes=(1000,10,)` which is a curious shape — narrow bottleneck after a wide first layer. Worth a footnote either way (intentional? leftover from experimentation?). On categorical mushroom data it's overkill but it does run.

### Forward connections

Almost every classifier in the cell-by-cell sklearn parade gets its proper introduction later:
- Decision Trees → Unit 6, Nov 17
- k-NN → Unit 6, Nov 11
- Logistic Regression → Unit 6, Nov 5
- SVM → Unit 7, Dec 4
- Random Forest / GradientBoost (ensembles) → Unit 7, Dec 16
- Neural Networks (MLP) → Unit 9 onward, Jan 20+

You could argue this notebook is a *map* of the rest of the year — every model the students will study, demonstrated working, on day 22 of class.

---

## Day 2 — Self-Selected Categorical Analysis (Sep 24)

No new notebook. The assignment per the calendar:
> *Pick a dataset from any online source, restrict it to categorical features only, and perform a similar analysis to the one I modeled with "Mushroom Exploration". Load the data, clean it (fill in any NaN or missing data), make some graphs, look for correlations between features and outcomes, then perform several ML algorithms. Add an analysis paragraph at the end where you discuss the dataset and the goodness of fit of the models. Upload by end of class.*

This is **the hinge of the unit** and arguably one of the most important assignments of the first quarter. Students reproduce the Mushroom workflow on a dataset they choose, in one class period.

### Why this assignment matters in the year's arc

It's the first time students have to make *all* the decisions themselves: which dataset, how to handle missing data, which plots are worth making, which models to try, what counts as "good enough." This is also the first deliverable with a required prose discussion cell — a pattern that will recur all year (DIY Linear Regression++, London Weather, the quarter projects).

The "categorical features only" constraint is a clever scope-limiter. It keeps the assignment tractable in one class period and forces students to confront the discrete-variable side of ML rather than retreating to comfortable continuous-data territory.

### Potential gaps

- **No assignment-specific page.** The instructions live only in the calendar entry. A small `/notes/categorical-analysis-assignment.md` page (paralleling `DIY-LinReg-Plus.md`) would help — especially since this is referenced and reused as a workflow template later.
- **No grading rubric is linked.** What does "good enough" mean here? Some sense of what the markdown discussion paragraph should cover would help students who aren't sure what to write.
- **No archive of past student submissions.** This is the kind of assignment where seeing 2–3 prior students' choices would catalyze the slow ones in a 90-minute window. Could be an opt-in showcase.

---

## Day 3 — Bayes Error (Sep 26)

[`Bayes-Error-Student.ipynb`](https://aet-cs.github.io/white/2025/ML/notebooks/Bayes-Error-Student.ipynb) — 26 cells (11 markdown, 15 code) — synthetic 2D Gaussian clusters, no external dataset.

The theoretical counterpoint to Mushroom. Where Mushroom showed how to build classifiers, Bayes Error shows the *irreducible floor* on classifier performance when classes genuinely overlap. This is the conceptual idea most students will keep returning to all year — every time a model plateaus, they should be asking "is this Bayes error or is my model bad?"

### Structure (five parts)

1. **Well-separated Gaussians.** Means at [-3, 0] and [3, 0], identity covariance. Students see ~0% error with a sensible boundary.
2. **Overlapping Gaussians.** Same covariance, means moved to [-1, 0] and [1, 0]. Error rate jumps. The lesson: no matter how clever your classifier, you can't do better than the overlap allows.
3. **Grid search for optimal split.** Students fill in a loop over 41 candidate split points, plot error vs. split, find the minimum. This is also their first "scan a hyperparameter, plot the curve" experience — a workflow they'll use constantly later (k in k-NN, C in SVM, depth in trees).
4. **Different variances.** `cov_A = [[0.05, 0], [0, 0.05]]` (tight cluster) vs. `cov_B = [[2.0, 0], [0, 2.0]]` (loose cluster). The optimal boundary is no longer the midpoint. Students discover this empirically.
5. **Theoretical wrap-up.** Two markdown questions: what's the optimal boundary for equal-variance Gaussians? For unequal-variance? (Expected answers: perpendicular bisector — i.e., midpoint in 1D — and then the quadratic boundary of Gaussian discriminant analysis, though that name isn't given.)

### Pedagogical moves worth flagging

- **The arc itself is the lesson.** Part 1 (no error) → Part 2 (error appears) → Part 3 (optimize) → Part 4 (the optimum moves around) → Part 5 (derive). This is a textbook scaffold: phenomenon, problem, solution, complication, theory. Each part is short enough to fit in 10–15 minutes.
- **Synthetic data is the right choice.** Real data muddies the lesson — here you *know* the optimal boundary because you constructed the distributions. The student can verify their empirically-found split against the theoretical answer.
- **Part 5 sneaks in Gaussian discriminant analysis** without saying so. The "educated guess" framing is generous — the actual answer (quadratic boundary when variances differ) is a real result and rewards students who reason carefully. This unnamed pre-introduction will pay off when LDA/QDA come up later in any further study.

### What the student actually does

- Fills in: scatter plot in cell 12, error-counting in cell 13, the loop body in cell 15, plotting in cells 16 and 17, the entire variance-difference exploration in cell 19.
- Writes: theoretical answers in cells 22 and 24.

So ~half the cells require student work. Substantially more active than Mushroom.

### Notes & small issues

- **Cells 7 and 8 are duplicates** except cell 8 adds the decision boundary. The duplication might be intentional (show base plot, then enhance) but reads as redundant. Easy consolidation if you want a cleaner notebook.
- **Cell 13 references `errors_close` and `error_rate_close` before they're defined** — the student is supposed to define them above the print statement, but if they run the cell as-is they get a `NameError`. A `# YOUR CODE HERE: define errors_close, error_rate_close` placeholder above the print would prevent the confusion.
- **Cell 12 has a `# %%#` comment** that looks like a stray cell-magic marker (probably from a Jupytext / VS Code conversion). Harmless but distracting.
- **Part 5's questions are open-ended without checkpoints.** A nudge like "if you set the derivative of the difference of log-densities to zero, what equation do you get?" would help the less-mathematically-comfortable students reach the answer.
- **No graded check or autograder hooks.** This is fine — the notebook is genuinely exploratory. But it does make the assignment fully effort-graded.

### Forward connections

- The "grid search over a single parameter, plot error curve, find the min" pattern in Part 3 will recur for k-NN (k), Decision Trees (depth), SVM (C and gamma), and basically every model that follows. This notebook is where that workflow is established.
- The "irreducible error" framing is *the* mental model students need for the rest of the year. When CIFAR-10 plateaus at 92% in Unit 9, when sentiment analysis caps out at 88% in Unit 11 — Bayes error is the explanation, and they'll recognize it because of this lab.
- The quadratic boundary from Part 5 anticipates the kernel trick in SVM (Unit 7).

---

## Unit-Level Notes & Opportunities

### What's working really well

- The progression is tight: workflow tour → individual practice → theoretical bound. Three days, three modes (read, do, prove).
- Both notebooks are self-contained — students don't need anything from outside the calendar to complete them.
- The seven-classifier parade in Mushroom is a quietly brilliant device. It demonstrates the rest of the year on day one of the unit.

### Where the unit could grow without major changes

- **A short standalone assignment page for Sep 24**, paralleling `DIY-LinReg-Plus.md`. Even a 10-line checklist would help (dataset chosen and cited; missing data handled with justification; ≥3 plots including one groupby; ≥3 classifiers tried; conclusion paragraph in markdown).
- **An optional "deepening" extension on Mushroom** surfacing the class-weight idea from the Key notebook. *"Given how deadly false negatives are, modify the Random Forest to penalize them more heavily and report what changes."* Five-minute addition, very high payoff for the precision/recall framing.
- **A pointer from Bayes Error forward** — a one-line note at the end like *"You'll come back to this idea every time a model 'tops out' for the rest of the year. When you see a confusion matrix that won't budge, ask: is this Bayes error or is my model bad?"* Helps students recognize the concept's recurrence.
- **Showcase past student datasets from Sep 24.** A simple page listing 5–10 datasets students have chosen in past years (with one-line takeaways) would seed the slower starters.

### Connections to fix or strengthen

- **Backward to Bayes Theorem (Sep 2):** Bayes Error and Bayes Theorem aren't the same idea, but they're related — the Bayes-optimal classifier *uses* Bayes' theorem to assign each point to its most-likely class. One markdown cell at the top of Bayes-Error-Student making this connection explicit would help students see the through-line.
- **Forward to confusion-matrix metrics:** Mushroom introduces precision/recall/F1 via the deadly-poisoning framing, but doesn't return to them with the same intensity later. The framing deserves a callback when students are doing fraud detection (Unit 8) and the same asymmetry reappears.

---

## Format Check

This is a format proposal — if it feels too long or too short or off-balance, easier to tune now than after eleven more units. Some specific knobs:

- **Length per notebook** — currently ~6 paragraphs of annotation plus notes. Could be tighter (3–4 paragraphs) if scaling to 12 units feels heavy.
- **"Pedagogical moves" sections** — these are the most novel content here. Worth keeping prominent, or fold into prose?
- **"Notes & small issues"** — useful for a real revision pass but could be split out into a separate "issues to fix" document if it muddies the celebratory tone.
- **Forward/backward connections** — these create a web across units. Worth the bookkeeping?
- **Cell-by-cell granularity** — currently I cite specific cell numbers. Helpful for revision; possibly too granular if this becomes a public document.

Let me know what to keep and what to cut and I'll apply it to the rest.
