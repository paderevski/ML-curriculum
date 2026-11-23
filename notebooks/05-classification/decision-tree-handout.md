---
title: "Decision Trees, Day 1: Will We Wait?"
geometry: margin=0.9in
header-includes:
  - \usepackage{amsmath}
  - \usepackage{forest}
  - \usepackage{booktabs}
  - \pagenumbering{gobble}
---

Name: \underline{\hspace{3in}} \hfill Date: \underline{\hspace{1.2in}}

## Part 1: A decision tree

A **decision tree** makes a prediction by asking a series of questions. You
start at the top, answer the question, follow the branch that matches your
answer, and keep going until you reach a **leaf**. The leaf is the prediction.

Here is a tree that predicts whether we will play golf today.

\begin{center}
\begin{forest}
for tree={
  draw, rounded corners, align=center, font=\sffamily\large,
  inner sep=6pt, l sep=1.9cm, s sep=1.6cm, edge={-latex, thick},
  parent anchor=south, child anchor=north
},
where level=1{s sep=2.6cm}{},
leaf/.style={fill=gray!20, font=\sffamily\large\bfseries, rounded corners=8pt},
lbl/.style={edge label={node[midway, fill=white, inner sep=2pt, font=\itshape]{#1}}}
[Outlook?
  [Humidity?, lbl=Sunny
    [No, leaf, lbl=High]
    [Yes, leaf, lbl=Normal]
  ]
  [Yes, leaf, lbl=Overcast]
  [Wind?, lbl=Rain
    [No, leaf, lbl=Strong]
    [Yes, leaf, lbl=Weak]
  ]
]
\end{forest}
\end{center}

The white boxes are **questions** about the weather. The labels on the
branches are the possible **answers**. The gray boxes are **leaves**:
Yes means play, No means don't.

**Use the tree.** For each day, trace a path from the top and write the prediction.

\renewcommand{\arraystretch}{1.5}
\begin{center}
\begin{tabular}{c l l l l c}
\toprule
Day & Outlook & Temperature & Humidity & Wind & Play? \\
\midrule
A & Sunny    & Hot  & Normal & Strong & \underline{\hspace{0.7in}} \\
B & Rain     & Mild & High   & Strong & \underline{\hspace{0.7in}} \\
C & Overcast & Cool & High   & Strong & \underline{\hspace{0.7in}} \\
D & Sunny    & Mild & High   & Weak   & \underline{\hspace{0.7in}} \\
\bottomrule
\end{tabular}
\end{center}

**1.** On Day A, which of the four weather facts did you never look at?

\vspace{0.6in}

**2.** The tree never asks about Temperature. Give one reason someone might
build a tree that leaves out a feature on purpose.

\vspace{0.8in}

\newpage

## Part 2: Will we wait for a table?

You show up at a restaurant and there is no free table. Do you wait, or leave?
Below are 12 times a diner made that choice. Each row lists what the diner knew
about the situation, and the last column says whether they waited.

| Column | Question it answers |
|:-------|:--------------------|
| **Alt** | Is there another good restaurant nearby? |
| **Bar** | Is there a comfy bar to wait in? |
| **Fri** | Is it Friday or Saturday? |
| **Hun** | Are we hungry right now? |
| **Patrons** | How many people are inside? (None, Some, Full) |
| **Price** | How expensive is it? (\$, \$\$, \$\$\$) |
| **Rain** | Is it raining outside? |
| **Res** | Did we make a reservation? |
| **Type** | What kind of food? |
| **Est** | How long does the host say the wait is, in minutes? |

\renewcommand{\arraystretch}{1.35}
\begin{center}
\small
\setlength{\tabcolsep}{4.5pt}
\begin{tabular}{c c c c c c c c c l c | c}
\toprule
 & Alt & Bar & Fri & Hun & Patrons & Price & Rain & Res & Type & Est & \textbf{WillWait?} \\
\midrule
X1  & Yes & No  & No  & Yes & Some & \$\$\$ & No  & Yes & French  & 0--10  & \textbf{Yes} \\
X2  & Yes & No  & No  & Yes & Full & \$     & No  & No  & Thai    & 30--60 & \textbf{No}  \\
X3  & No  & Yes & No  & No  & Some & \$     & No  & No  & Burger  & 0--10  & \textbf{Yes} \\
X4  & Yes & No  & Yes & Yes & Full & \$     & Yes & No  & Thai    & 10--30 & \textbf{Yes} \\
X5  & Yes & No  & Yes & No  & Full & \$\$\$ & No  & Yes & French  & $>$60  & \textbf{No}  \\
X6  & No  & Yes & No  & Yes & Some & \$\$   & Yes & Yes & Italian & 0--10  & \textbf{Yes} \\
X7  & No  & Yes & No  & No  & None & \$     & Yes & No  & Burger  & 0--10  & \textbf{No}  \\
X8  & No  & No  & No  & Yes & Some & \$\$   & Yes & Yes & Thai    & 0--10  & \textbf{Yes} \\
X9  & No  & Yes & Yes & No  & Full & \$     & Yes & No  & Burger  & $>$60  & \textbf{No}  \\
X10 & Yes & Yes & Yes & Yes & Full & \$\$\$ & No  & Yes & Italian & 10--30 & \textbf{No}  \\
X11 & No  & No  & No  & No  & None & \$     & No  & No  & Thai    & 0--10  & \textbf{No}  \\
X12 & Yes & Yes & Yes & Yes & Full & \$     & No  & No  & Burger  & 30--60 & \textbf{Yes} \\
\bottomrule
\end{tabular}
\end{center}

\small Data: the restaurant example from Russell \& Norvig, *Artificial Intelligence: A Modern Approach*.
\normalsize

**Your job:** build a decision tree that predicts **WillWait?** Your tree
should give the right answer for all 12 rows. Draw it on the next page.

**Tips**

- You choose which question goes at the top. Any column can be a question.
- After the first question, the rows split into groups. Treat each group as
  its own smaller problem.
- When every row in a group has the same answer, stop. That branch becomes a leaf.
- A question can have more than two branches (Patrons has three).

\newpage

## Part 3: Your tree

**3.** Draw your tree here. Label every branch with an answer, and make every
leaf say Yes or No.

\vspace{4.2in}

**4.** Check your tree. Run each of X1 through X12 down your tree. How many
does it get right? (It should be 12. If not, fix the tree.)

\vspace{0.4in}

**5.** How many question boxes does your tree have (its **size**)? What is the
most questions you ever ask on one path from the top to a leaf (its
**depth**)? Compare both numbers with a neighbor. Whose tree is smaller? Whose
is shallower?

\vspace{0.5in}

**6.** Which question did you put at the top, and why that one?

\vspace{0.8in}

**7.** A new restaurant, not in the table: Alt = No, Bar = Yes, Fri = No,
Hun = Yes, Patrons = Full, Price = \$\$, Rain = Yes, Res = No, Type = Italian,
Est = 30--60. What does your tree predict? Does your neighbor's tree predict
the same thing?

\vspace{0.6in}
