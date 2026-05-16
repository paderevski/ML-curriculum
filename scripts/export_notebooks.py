#!/usr/bin/env python3
"""Export Jupyter notebooks to adjacent HTML files."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"


def iter_notebooks() -> list[Path]:
    return sorted(
        path
        for path in NOTEBOOKS_DIR.rglob("*.ipynb")
        if "/." not in path.relative_to(REPO_ROOT).as_posix()
    )


def export_notebook(notebook_path: Path) -> None:
    subprocess.run(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "html",
            "--template",
            "lab",
            str(notebook_path),
            "--output-dir",
            str(notebook_path.parent),
        ],
        check=True,
    )


def main() -> None:
    notebook_args = [Path(arg).resolve() for arg in sys.argv[1:]]
    notebook_paths = notebook_args or iter_notebooks()

    for notebook_path in notebook_paths:
        if notebook_path.suffix != ".ipynb":
            raise SystemExit(f"Expected a notebook path, got: {notebook_path}")
        export_notebook(notebook_path)


if __name__ == "__main__":
    main()
