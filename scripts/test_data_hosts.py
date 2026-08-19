#!/usr/bin/env python3
"""
Which data hosts are reachable from a school machine?

Run this from a school computer (or paste into a Colab cell on a school
account) to settle where course datasets should live. Whichever host passes
becomes BASE_URL in ml_utils.py.

    python3 scripts/test_data_hosts.py

Each test fetches a small, known-good file and reports success, failure, or
timeout. A block usually shows up as a timeout, a connection reset, or an
HTML login/filter page instead of the expected content.
"""

import socket
import urllib.error
import urllib.request

TIMEOUT = 10

# Each entry: (label, url-of-something-small-and-real)
HOSTS = [
    (
        "readthedocs (course site)",
        "https://ml-curriculum.readthedocs.io/en/latest/index.html",
    ),
    (
        "raw.githubusercontent.com",
        "https://raw.githubusercontent.com/paderevski/ML-curriculum/main/README.md",
    ),
    (
        "github.com",
        "https://github.com/paderevski/ML-curriculum",
    ),
    (
        "Google Drive (direct download)",
        "https://drive.google.com/uc?export=download&id=0B0Uz0z0z0z0z",
    ),
    (
        "GitHub Pages",
        "https://paderevski.github.io/ML-curriculum/",
    ),
    (
        "Hugging Face",
        "https://huggingface.co/datasets",
    ),
]


def check(label, url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            body = resp.read(2048)
            ctype = resp.headers.get("Content-Type", "")
            # A filter page often returns 200 with HTML where we expected
            # something else, so flag HTML on non-HTML URLs as suspicious.
            suspicious = (
                b"<html" in body[:200].lower()
                and not url.endswith((".html", "/"))
            )
            note = "  (got HTML — possible filter page?)" if suspicious else ""
            return f"OK    {resp.status}  {label}{note}"
    except urllib.error.HTTPError as e:
        # A 404 still proves the host is reachable.
        verdict = "REACHABLE" if e.code in (401, 403, 404) else "HTTP ERR "
        return f"{verdict} {e.code}  {label}"
    except urllib.error.URLError as e:
        return f"BLOCKED?    {label}  ({e.reason})"
    except socket.timeout:
        return f"TIMEOUT     {label}"
    except Exception as e:
        return f"ERROR       {label}  ({type(e).__name__}: {e})"


def main():
    print(f"Testing {len(HOSTS)} hosts, {TIMEOUT}s timeout each.\n")
    for label, url in HOSTS:
        print(check(label, url))
    print(
        "\nAnything marked OK or REACHABLE can host course data.\n"
        "Prefer the first reachable option in this order:\n"
        "  readthedocs > raw.githubusercontent > GitHub Pages > Drive"
    )


if __name__ == "__main__":
    main()
