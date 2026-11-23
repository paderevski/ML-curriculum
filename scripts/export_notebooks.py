#!/usr/bin/env python3
"""Export Jupyter notebooks to adjacent HTML files."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from functools import cache
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
WIDGET_STATE_MIMETYPE = "application/vnd.jupyter.widget-state+json"


def iter_notebooks() -> list[Path]:
    # Skip hidden folders (.ipynb_checkpoints) and folders starting with "_"
    # (such as _orphans/): Jekyll doesn't publish those, so their HTML is
    # never used.
    return sorted(
        path
        for path in NOTEBOOKS_DIR.rglob("*.ipynb")
        if not any(
            part.startswith((".", "_"))
            for part in path.relative_to(NOTEBOOKS_DIR).parts[:-1]
        )
    )


@cache
def exporter() -> HTMLExporter:
    # One exporter for every notebook: starting `jupyter nbconvert` once per
    # notebook cost about a second each just in Python startup.
    return HTMLExporter(template_name="lab")


def read_notebook(notebook_path: Path) -> nbformat.NotebookNode:
    notebook = nbformat.read(notebook_path, as_version=4)

    # Some notebooks save widget metadata without a "state" key, which makes
    # nbconvert crash. Add an empty one (in memory only).
    widgets = notebook.metadata.get("widgets")
    if isinstance(widgets, dict):
        widget_state = widgets.get(WIDGET_STATE_MIMETYPE)
        if isinstance(widget_state, dict) and "state" not in widget_state:
            widget_state["state"] = {}

    return notebook


def output_html_path(notebook_path: Path) -> Path:
    return notebook_path.with_suffix(".html")


def needs_export(notebook_path: Path) -> bool:
    html_path = output_html_path(notebook_path)
    if not html_path.exists():
        return True
    return notebook_path.stat().st_mtime > html_path.stat().st_mtime


def export_notebook(notebook_path: Path, *, force: bool = False) -> bool:
    if not force and not needs_export(notebook_path):
        return False

    print(f"Converting {notebook_path.relative_to(REPO_ROOT)}")
    html, _ = exporter().from_notebook_node(
        read_notebook(notebook_path),
        resources={"metadata": {"name": notebook_path.stem}},  # page <title>
    )
    output_html_path(notebook_path).write_text(html, encoding="utf-8")
    return True


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export Jupyter notebooks to adjacent HTML files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="rebuild HTML even when the existing output is up to date",
    )
    parser.add_argument(
        "notebooks",
        nargs="*",
        help="optional notebook paths to export",
    )
    return parser.parse_args(argv)


def print_summary(*, converted: int, skipped: int, forced: bool) -> None:
    mode = "forced export" if forced else "incremental export"
    print(f"Export summary ({mode}): {converted} converted, {skipped} skipped")


def main() -> None:
    args = parse_args(sys.argv[1:])
    notebook_args = [Path(arg).resolve() for arg in args.notebooks]
    notebook_paths = notebook_args or iter_notebooks()
    converted = 0
    skipped = 0

    for notebook_path in notebook_paths:
        if notebook_path.suffix != ".ipynb":
            raise SystemExit(f"Expected a notebook path, got: {notebook_path}")
        if export_notebook(notebook_path, force=args.force):
            converted += 1
        else:
            skipped += 1

    print_summary(converted=converted, skipped=skipped, forced=args.force)


if __name__ == "__main__":
    main()
