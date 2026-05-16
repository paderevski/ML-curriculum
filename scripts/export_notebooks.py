#!/usr/bin/env python3
"""Export Jupyter notebooks to adjacent HTML files."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
WIDGET_STATE_MIMETYPE = "application/vnd.jupyter.widget-state+json"


def iter_notebooks() -> list[Path]:
    return sorted(
        path
        for path in NOTEBOOKS_DIR.rglob("*.ipynb")
        if "/." not in path.relative_to(REPO_ROOT).as_posix()
    )


def sanitized_notebook_path(notebook_path: Path) -> Path:
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    metadata = notebook.setdefault("metadata", {})
    widgets = metadata.get("widgets")

    if isinstance(widgets, dict):
        widget_state = widgets.get(WIDGET_STATE_MIMETYPE)
        if isinstance(widget_state, dict) and "state" not in widget_state:
            widget_state["state"] = {}

    temp_file = tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".ipynb",
        delete=False,
        encoding="utf-8",
    )
    with temp_file:
        json.dump(notebook, temp_file)

    return Path(temp_file.name)


def output_html_path(notebook_path: Path) -> Path:
    return notebook_path.with_suffix(".html")


def needs_export(notebook_path: Path) -> bool:
    html_path = output_html_path(notebook_path)
    if not html_path.exists():
        return True
    return notebook_path.stat().st_mtime > html_path.stat().st_mtime


def export_notebook(notebook_path: Path) -> None:
    html_path = output_html_path(notebook_path)
    if not needs_export(notebook_path):
        print(f"Skipping {notebook_path} (up to date: {html_path})")
        return

    sanitized_path = sanitized_notebook_path(notebook_path)
    print("Converting " + str(sanitized_path) + "....")
    try:
        subprocess.run(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "html",
                "--template",
                "lab",
                str(sanitized_path),
                "--output-dir",
                str(notebook_path.parent),
                "--output",
                notebook_path.stem,
            ],
            check=True,
        )
    finally:
        sanitized_path.unlink(missing_ok=True)
    print("Finished")


def main() -> None:
    notebook_args = [Path(arg).resolve() for arg in sys.argv[1:]]
    notebook_paths = notebook_args or iter_notebooks()

    for notebook_path in notebook_paths:
        if notebook_path.suffix != ".ipynb":
            raise SystemExit(f"Expected a notebook path, got: {notebook_path}")
        export_notebook(notebook_path)


if __name__ == "__main__":
    main()
