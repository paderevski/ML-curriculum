---
title: "How to Read a CSV File in Google Colab"
---

## 1. Get a CSV file

Either download one or make your own.

- **Download:** Find a dataset online (e.g., Kaggle, data.gov, a GitHub repo) and save the `.csv` file to your computer. On GitHub, click **Raw** first, then save the page.
- **Make one:** In Google Sheets, enter your data with column names in the first row, then choose **File → Download → Comma-separated values (.csv)**.

For this guide, the file is called `data.csv`.

## 2. Put it in your Google Drive

1. Go to [drive.google.com](https://drive.google.com).
2. Open the **Colab Notebooks** folder. (If it doesn't exist, create it with **New → New folder**.)
3. Inside **Colab Notebooks**, create a folder named `data` if you don't already have one.
4. Open `data` and upload `data.csv` with **New → File upload**.

Your file now lives at `My Drive/Colab Notebooks/data/data.csv`.

## 3. Create a new Colab notebook

Go to [colab.research.google.com](https://colab.research.google.com) and click **New notebook**. Give it a name by clicking the title at the top.

## 4. Mount Google Drive

Run this in the first cell:

```python
from google.colab import drive
drive.mount('/content/drive')
```

A pop-up will ask for permission to access your Drive. Allow it. When it finishes, you'll see `Mounted at /content/drive`.

Your Drive files are now available under `/content/drive/MyDrive/`.

## 5. Read the file with pandas

In a new cell:

```python
import pandas as pd

path = '/content/drive/MyDrive/Colab Notebooks/data/data.csv'
df = pd.read_csv(path)

df.head()
```

`df.head()` shows the first five rows. A couple of other quick checks:

```python
df.shape     # (number of rows, number of columns)
df.columns   # the column names
```

## Troubleshooting

- **`FileNotFoundError`:** The path is wrong. Check spelling and capitalization, and confirm the file is where you think it is:

  ```python
  !ls "/content/drive/MyDrive/Colab Notebooks/data"
  ```

- **Just uploaded the file but it isn't showing up?** Wait a few seconds and try again, or remount with `drive.mount('/content/drive', force_remount=True)`.
