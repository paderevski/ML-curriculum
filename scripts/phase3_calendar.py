#!/usr/bin/env python3
"""
Phase 3: Update calendar.md to reflect the new notebooks/<unit>/ structure.

Strategy:
1. Walk notebooks/ and build a mapping: basename -> new relative path.
2. Find link-like patterns in calendar.md and rewrite them.
3. Also fix the known-broken './lessons/Decision_Tree_Student.html' path.
4. Report any links that still point to non-existent files.
"""

import os
import re
import sys

NOTEBOOKS = "notebooks"
CALENDAR = "calendar.md"


def build_inverse_mapping():
    """Map basename -> path-from-repo-root, only for files inside unit folders."""
    mapping = {}
    for entry in sorted(os.listdir(NOTEBOOKS)):
        full = os.path.join(NOTEBOOKS, entry)
        if not os.path.isdir(full):
            continue
        # Skip _orphans (we don't want calendar pointing there)
        if entry == "_orphans":
            continue
        for fname in os.listdir(full):
            if fname.startswith("."):
                continue
            if os.path.isdir(os.path.join(full, fname)):
                continue
            # If a basename appears twice we have a problem — flag it
            if fname in mapping:
                print(
                    f"WARNING: '{fname}' appears in both "
                    f"{mapping[fname]} and {entry}/, ambiguous"
                )
            mapping[fname] = f"{NOTEBOOKS}/{entry}/{fname}"
    return mapping


def rewrite_calendar(mapping):
    with open(CALENDAR) as f:
        text = f.read()

    original = text
    replacements = 0

    # Sort by basename length (longest first) so longer names match before shorter ones
    for basename in sorted(mapping.keys(), key=len, reverse=True):
        new_path = mapping[basename]
        # Match (./notebooks/<basename>) or (notebooks/<basename>) in markdown link contexts.
        # We're conservative: only inside parentheses (markdown link target).
        for old_form in [
            f"./notebooks/{basename}",
            f"notebooks/{basename}",
        ]:
            # Only replace when followed by ) or end-of-link punctuation,
            # to avoid matching inside a longer path.
            # Pattern: old_form followed by ) or whitespace at end of line
            pattern = re.escape(old_form) + r"(?=[)\s])"
            new_form = (
                f"./{new_path}" if old_form.startswith("./") else new_path
            )
            new_text, n = re.subn(pattern, new_form, text)
            text = new_text
            replacements += n

    # Fix the known-broken './lessons/' reference
    lessons_pattern = re.escape("./lessons/Decision_Tree_Student.html")
    new_text, n = re.subn(
        lessons_pattern,
        "./notebooks/06-classification/Decision_Tree_Student.html",
        text,
    )
    text = new_text
    replacements += n

    if text == original:
        print("  No changes made to calendar.md")
        return

    with open(CALENDAR, "w") as f:
        f.write(text)
    print(f"  {replacements} replacements made in calendar.md")


def validate(mapping):
    """Find any links in calendar.md that still don't resolve."""
    with open(CALENDAR) as f:
        text = f.read()
    # Find every markdown link target
    link_re = re.compile(r"\]\(([^)]+)\)")
    broken = []
    for match in link_re.finditer(text):
        target = match.group(1)
        # Strip query strings or anchors
        target = target.split("#")[0].split("?")[0]
        # Skip URLs
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        # Skip relative parent paths beyond our repo
        if target.startswith("../"):
            continue
        # Resolve relative to repo root
        path = target.lstrip("./") if target.startswith("./") else target
        if not os.path.exists(path):
            broken.append(target)
    if broken:
        print(f"\nWARNING: {len(broken)} links in calendar.md still don't resolve:")
        for b in broken[:20]:
            print(f"  - {b}")
        if len(broken) > 20:
            print(f"  ... and {len(broken) - 20} more")
    else:
        print("\nAll relative links in calendar.md resolve to existing files.")


def main():
    mapping = build_inverse_mapping()
    print(f"Built mapping for {len(mapping)} files in unit folders")
    rewrite_calendar(mapping)
    validate(mapping)


if __name__ == "__main__":
    main()
