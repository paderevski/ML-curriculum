"""
ml_utils — shared helpers for the ML curriculum.

Bootstrap this in a notebook with:

    try:
        import ml_utils
    except ImportError:
        import urllib.request
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/paderevski/ML-curriculum/main/ml_utils.py",
            "ml_utils.py")
        import ml_utils

Then load data by short name, never by path or URL:

    from ml_utils import load_data
    df = load_data("weather")
"""

import os
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# Hosting
# ---------------------------------------------------------------------------
# Notebooks run on Colab, which means downloads happen on Google's VM rather
# than on a school machine — so the district's web filter isn't a factor. The
# only things that must clear the school network are the browser loading the
# course site and Colab itself.
#
# That leaves ordinary criteria, and a separate public data repo wins: free,
# versioned, pandas reads raw URLs directly, keeps the curriculum repo small,
# and doesn't bloat the Jekyll/RTD build the way committing data here would.
#
# Per-file ceiling is 100MB (GitHub warns above 50MB). Only mnist.pk.gz (22MB)
# is anywhere near that.
#
# Changing this one string re-points every notebook in the course.
BASE_URL = "https://raw.githubusercontent.com/AET-CS/ML-datasets/main/"

# Where downloaded files are kept for the rest of the session.
CACHE_DIR = Path(os.environ.get("ML_DATA_CACHE", "./ml-data"))


# ---------------------------------------------------------------------------
# Registry: short name -> filename at BASE_URL
# ---------------------------------------------------------------------------
# Add an entry here when a notebook needs a new dataset. Notebooks reference
# the short name only, so a file can move or be renamed without touching them.
DATASETS = {
    # Unit 01 — Foundations
    "weather":          "weather-daylight.csv",
    "london_weather":   "london_weather.csv",
    # Unit 03 — First Pipeline
    "mushroom":         "mushroom.csv",
    # Unit 04 — Regression++
    "life_expectancy":  "Life_Expectancy_Data.csv",
    "test_scores":      "test-scores.csv",
    "gauss":            "gauss.jpg",
    # Unit 05 — Classification
    "cancer":           "Cancer_Data.csv",
    "cancer_clean":     "Cancer_Data_Cleaned.csv",
    "loans":            "loan_data.csv",
    # Unit 06 — SVM / CV / Ensembles
    "fake_news":        "Fake_News.csv",
    "twitter":          "twitter_training.csv",
    "airline_tweets":   "airline_tweets.csv",
    "mnist":            "mnist.pk.gz",
    # Unit 07 — Anomaly Detection
    "creditcard":       "creditcard.csv",
    # Unit 10 — Transfer & Time Series
    "aapl":             "AAPL.csv",
    "bird_songs":       "bird_songs_metadata.csv",
}

# Deliberately NOT in the registry — these already load from canonical
# upstream sources and should stay that way. Re-hosting them would add a
# maintenance burden and break the link to the original dataset:
#
#   adult.data        UCI ML repository        (05/Decision_Tree_Student)
#   tinyshakespeare   karpathy/char-rnn        (11/Shakespeare_Student)
#   spa-eng.zip       storage.googleapis.com   (11 & 12, NMT notebooks)
#   shakespeare.txt   storage.googleapis.com   (12/charGPT)
#
# Also excluded: the CelebA and image-captioning notebooks read from a
# mounted Google Drive (/content/drive/...). That's intentional — those are
# large files and training checkpoints that shouldn't live in a git repo.


def data_path(name):
    """Return a local path for `name`, downloading it if necessary.

    Resolution order:
      1. A file already in the working directory (brainy, or a repo checkout)
      2. The session cache (downloaded earlier in this session)
      3. Download from BASE_URL into the cache

    Returns a Path. Use this when a library wants a filename rather than a
    DataFrame — e.g. image loaders, gzip, or open().
    """
    if name not in DATASETS:
        raise KeyError(
            f"Unknown dataset {name!r}. Known names: {sorted(DATASETS)}"
        )
    filename = DATASETS[name]

    # 1. Already sitting next to the notebook?
    local = Path(filename)
    if local.exists():
        return local

    # 2. Already cached this session?
    cached = CACHE_DIR / filename
    if cached.exists():
        return cached

    # 3. Fetch it.
    url = BASE_URL + filename
    cached.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {filename} ...", end=" ", flush=True)
    try:
        urllib.request.urlretrieve(url, cached)
    except Exception as e:
        raise RuntimeError(
            f"Could not download {filename} from {url}\n"
            f"({type(e).__name__}: {e})\n"
            "Check that the file exists in the ML-data repo — "
            "let Dr. White know which dataset failed."
        ) from e
    print("done.")
    return cached


def load_data(name, **kwargs):
    """Load a dataset by short name and return a pandas DataFrame.

    Extra keyword arguments are passed through to the underlying pandas
    reader, so this works:

        df = load_data("weather", parse_dates=["DATE"])

    For non-tabular files (images, pickles, raw text), use data_path()
    instead and open the returned path yourself.
    """
    import pandas as pd

    path = data_path(name)
    suffix = "".join(path.suffixes).lower()

    if ".csv" in suffix:
        return pd.read_csv(path, **kwargs)
    if ".tsv" in suffix or ".txt" in suffix:
        kwargs.setdefault("sep", "\t")
        return pd.read_csv(path, **kwargs)
    if ".json" in suffix:
        return pd.read_json(path, **kwargs)
    if suffix.endswith((".xlsx", ".xls")):
        return pd.read_excel(path, **kwargs)

    raise ValueError(
        f"Don't know how to load {path.name} as a DataFrame. "
        "Use data_path() and open it directly."
    )


def available():
    """Print the datasets this module knows about."""
    width = max(len(k) for k in DATASETS)
    for key in sorted(DATASETS):
        print(f"  {key:<{width}}  {DATASETS[key]}")
