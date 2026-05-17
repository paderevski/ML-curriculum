#!/usr/bin/env python3
"""Generate Jekyll notebook metadata for notebook link includes."""

from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
OUTPUT_PATH = REPO_ROOT / "_data" / "notebooks.json"
SNIPPETS_OUTPUT_PATH = (
    REPO_ROOT / ".vscode" / "generated-notebook-local-choices.code-snippets"
)
REPOSITORY = "paderevski/ML-curriculum"
DEFAULT_BRANCH = "main"


def prettify_stem(stem: str) -> str:
    return stem.replace("_", " ").replace("-", " ").strip()


def extract_title(notebook_path: Path) -> str:
    with notebook_path.open(encoding="utf-8") as handle:
        notebook = json.load(handle)

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue

        source = cell.get("source", [])
        if isinstance(source, list):
            lines = source
        else:
            lines = str(source).splitlines()

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#"):
                return stripped.lstrip("#").strip()

    return prettify_stem(notebook_path.stem)


def build_entry(notebook_path: Path) -> dict[str, str]:
    relative_path = notebook_path.relative_to(REPO_ROOT).as_posix()
    html_path = notebook_path.relative_to(REPO_ROOT).with_suffix(".html").as_posix()

    return {
        "title": extract_title(notebook_path),
        "ipynb_path": relative_path,
        "html_path": html_path,
        "github_url": f"https://github.com/{REPOSITORY}/blob/{DEFAULT_BRANCH}/{relative_path}",
        "colab_url": f"https://colab.research.google.com/github/{REPOSITORY}/blob/{DEFAULT_BRANCH}/{relative_path}",
    }


def dir_keys(relative_dir: str) -> list[str]:
    return [
        relative_dir,
        f"/{relative_dir}",
        f"{relative_dir}/",
        f"/{relative_dir}/",
    ]


def build_local_choice_snippets(
    by_file: dict[str, dict[str, str]],
) -> dict[str, dict[str, object]]:
    notebook_names = sorted(by_file.keys())
    choices = ",".join(notebook_names)

    return {
        "Notebook include local choice": {
            "scope": "markdown",
            "prefix": "nbloc",
            "body": ['{% include nb.html local="${1|' + choices + '|}" %}'],
            "description": "Insert a local notebook include from the global notebook list",
        },
        "Notebook include local choice with label": {
            "scope": "markdown",
            "prefix": "nblocl",
            "body": ['{% include nb.html local="${1|' + choices + '|}" label="$2" %}'],
            "description": "Insert a labeled local notebook include from the global notebook list",
        },
    }


def iter_notebooks() -> list[Path]:
    return sorted(
        path
        for path in NOTEBOOKS_DIR.rglob("*.ipynb")
        if "/." not in path.relative_to(REPO_ROOT).as_posix()
    )


def main() -> None:
    by_file: dict[str, dict[str, str]] = {}
    by_stem: dict[str, dict[str, str]] = {}
    by_dir: dict[str, dict[str, dict[str, str]]] = {}
    by_path: dict[str, dict[str, str]] = {}
    duplicate_files: list[str] = []
    duplicate_stems: list[str] = []

    for notebook_path in iter_notebooks():
        entry = build_entry(notebook_path)
        basename = notebook_path.name
        stem = notebook_path.stem
        relative_path = notebook_path.relative_to(REPO_ROOT).as_posix()
        parent_dir = notebook_path.parent.relative_to(REPO_ROOT).as_posix()

        if basename in by_file:
            duplicate_files.append(basename)
            continue

        if stem in by_stem:
            duplicate_stems.append(stem)
        else:
            by_stem[stem] = entry

        by_file[basename] = entry
        by_path[relative_path] = entry

        for dir_key in dir_keys(parent_dir):
            by_dir.setdefault(dir_key, {})[basename] = entry
            by_dir[dir_key][stem] = entry

    if duplicate_files:
        duplicates = ", ".join(sorted(set(duplicate_files)))
        raise SystemExit(f"Duplicate notebook basenames found: {duplicates}")

    if duplicate_stems:
        duplicates = ", ".join(sorted(set(duplicate_stems)))
        raise SystemExit(f"Duplicate notebook stems found: {duplicates}")

    OUTPUT_PATH.write_text(
        json.dumps(
            {
                "by_dir": by_dir,
                "by_file": by_file,
                "by_path": by_path,
                "by_stem": by_stem,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    SNIPPETS_OUTPUT_PATH.write_text(
        json.dumps(build_local_choice_snippets(by_file), indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
