#!/usr/bin/env python3
"""
Phase 1: Move notebooks into per-unit folders.

For each unit, we list the notebooks to place there. The script automatically
also moves matching .html and .md companion files (so e.g. moving
'knn-Student.ipynb' also moves 'knn-Student.html' if it exists).
"""

import os
import subprocess
import sys

NOTEBOOKS = "notebooks"

# Map: unit folder name -> list of files to move INTO it (relative to notebooks/)
mapping = {
    "01-foundations": [
        "Quick-Intro-To-Python.ipynb",
        "Quick-Intro-To-Python_Key.ipynb",
        "weather.ipynb",
        "weather_teacher.ipynb",
        "weather-daylight.csv",
        "Bayes_Theorem_Student.ipynb",
    ],
    "02-regression-correlation": [
        "Least-Squares.ipynb",
        "Numpy-Intro.ipynb",
        "Correlation.ipynb",
    ],
    "03-linear-algebra": [
        "Linear_Algebra_and_Python.ipynb",
        "Matrices_Index_Warmup-Student.ipynb",
        "Intro_to_Matrices_in_NumPy.ipynb",
    ],
    "04-first-pipeline": [
        "Mushroom_Student.ipynb",
        "Mushroom_Key.ipynb",
        "Bayes-Error-Student.ipynb",
    ],
    "05-regression-plus": [
        "Test_Scores.ipynb",
        "Life_Expectancy_Student.ipynb",
        "Life_Expectancy.ipynb",
        "Life_Part_2_Student.ipynb",
        "Life_Part_2.ipynb",
        "Visualizing_Transformation_Matrices.ipynb",
        "Low_Rank_Matrix_Approximations.ipynb",
        "Image-Compression.ipynb",
        "gauss.jpg",
        "PCA.ipynb",
    ],
    "06-classification": [
        "Cancer_Logistic_Student.ipynb",
        "Cancer_Logistic_Student_Key.ipynb",
        "Cancer_Data.csv",
        "Cancer_Data_Cleaned.csv",
        "knn-Student.ipynb",
        "knn-Key.ipynb",
        "digits-student.ipynb",
        "digits-key.ipynb",
        "Decision_Tree_Student.ipynb",
    ],
    "07-svm-cv-ensembles": [
        "Notes-SVM.ipynb",
        "SVM_Lab-Student.ipynb",
        "CrossValidation.ipynb",
        "mnist.pk.gz",
        "Twitter.ipynb",
        "Twitter-Airline.ipynb",
        "Ensemble_Methods.ipynb",
    ],
    # 08-anomaly is handled separately (rename existing anomaly/ folder)
    "09-dense-neural-networks": [
        "Softmax.ipynb",
        "Activation-Functions.ipynb",
    ],
    "10-cnns": [
        "CIFAR10_Training.ipynb",
        "ImageConvolutions.ipynb",
        "alexnet.ipynb",
    ],
    "11-transfer-and-time-series": [
        "Birds.ipynb",
        "AAPL.ipynb",
    ],
    "12-rnns-seq2seq": [
        "Shakespeare_Student.ipynb",
        "sentiment_analysis-student.ipynb",
        "Neural-Machine-Translation-Starter.ipynb",
        "seq2seq_nmt_reference.ipynb",
        "seq2seq_nmt_pytorch_hf_reference.ipynb",
    ],
    "13-transformers-generative": [
        "PytorchTutorial.ipynb",
        "transformer_nmt_with_spanish.ipynb",
        "charGPT_assignment.ipynb",
        "image_captioning_assignment.ipynb",
        "image_captioning_key.ipynb",
        "VAE_celeba_student.ipynb",
    ],
}

# Orphans: files we keep but with no clear unit home
orphans = [
    "bayes_error_assignment.ipynb",
    "bayes_error_assignment.py",
    "Distance.ipynb",
    "Studying_Logistic_Regression.ipynb",
]


def git_mv(src, dst):
    """Run git mv, raising on error."""
    print(f"  git mv {src} -> {dst}")
    subprocess.run(["git", "mv", src, dst], check=True)


def find_companions(stem):
    """For 'foo.ipynb', find 'foo.html' and 'foo.md' if they exist."""
    base = stem.rsplit(".", 1)[0]
    companions = []
    for ext in [".html", ".md"]:
        candidate = base + ext
        full = os.path.join(NOTEBOOKS, candidate)
        if os.path.exists(full):
            companions.append(candidate)
    return companions


def main():
    # Phase 1a: Make unit folders
    for unit in mapping:
        os.makedirs(os.path.join(NOTEBOOKS, unit), exist_ok=True)
    os.makedirs(os.path.join(NOTEBOOKS, "_orphans"), exist_ok=True)

    # Phase 1b: Rename anomaly/ -> 08-anomaly/
    if os.path.isdir(os.path.join(NOTEBOOKS, "anomaly")):
        git_mv(os.path.join(NOTEBOOKS, "anomaly"), os.path.join(NOTEBOOKS, "08-anomaly"))

    # Phase 1c: Move Gaussian-credit.ipynb out to orphans
    gaussian = os.path.join(NOTEBOOKS, "08-anomaly", "Gaussian-credit.ipynb")
    if os.path.exists(gaussian):
        git_mv(gaussian, os.path.join(NOTEBOOKS, "_orphans", "Gaussian-credit.ipynb"))

    # Phase 1d: Move all mapped notebooks (plus their companions) into unit folders
    for unit, files in mapping.items():
        for fname in files:
            src = os.path.join(NOTEBOOKS, fname)
            dst = os.path.join(NOTEBOOKS, unit, fname)
            if not os.path.exists(src):
                print(f"  WARNING: {src} not found, skipping")
                continue
            git_mv(src, dst)
            # Also move .html/.md companions if they exist
            if fname.endswith(".ipynb"):
                for companion in find_companions(fname):
                    csrc = os.path.join(NOTEBOOKS, companion)
                    cdst = os.path.join(NOTEBOOKS, unit, companion)
                    git_mv(csrc, cdst)

    # Phase 1e: Move orphans
    for fname in orphans:
        src = os.path.join(NOTEBOOKS, fname)
        if not os.path.exists(src):
            print(f"  WARNING: orphan {src} not found, skipping")
            continue
        git_mv(src, os.path.join(NOTEBOOKS, "_orphans", fname))

    print("\nDone with Phase 1 moves.")


if __name__ == "__main__":
    main()
