#!/usr/bin/env python3
"""
Phase 1b: Move supplementary files (data, models, images, source docs)
that are at notebooks/ root but belong with specific units.
"""

import os
import subprocess

NOTEBOOKS = "notebooks"

# Supplementary files: source file -> destination unit folder
supplementary = {
    # Shakespeare training data and supporting files for RNN unit
    "shakespeare.txt": "12-rnns-seq2seq",
    "TextVecLayer-IMBD.keras": "12-rnns-seq2seq",
    # Transformer & generative unit
    "tokens.txt": "13-transformers-generative",
    "transformer_nmt_questions.docx": "13-transformers-generative",
    "transformer_nmt_questions.md": "13-transformers-generative",
    "simple_ddpm.py": "13-transformers-generative",
}

# Uncertain — put in orphans
orphans = [
    "acl.png",
    "model.pth",
]


def git_mv(src, dst):
    print(f"  git mv {src} -> {dst}")
    subprocess.run(["git", "mv", src, dst], check=True)


def main():
    for fname, unit in supplementary.items():
        src = os.path.join(NOTEBOOKS, fname)
        if os.path.exists(src):
            dst = os.path.join(NOTEBOOKS, unit, fname)
            git_mv(src, dst)
        else:
            print(f"  WARNING: {src} not found, skipping")

    for fname in orphans:
        src = os.path.join(NOTEBOOKS, fname)
        if os.path.exists(src):
            dst = os.path.join(NOTEBOOKS, "_orphans", fname)
            git_mv(src, dst)
        else:
            print(f"  WARNING: orphan {src} not found, skipping")

    # The images/ subdir with circle_boundary.png — leave it for now,
    # decide after we see what notebooks reference it.

    print("\nDone with Phase 1b.")


if __name__ == "__main__":
    main()
