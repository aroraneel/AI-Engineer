# Day 5 — Seaborn + Full EDA Workflow — Notes

Topics covered: histplot, boxplot, scatterplot with hue, countplot, heatmap,
pairplot, end-to-end EDA process

---

## 1. Why Seaborn, If We Already Have Matplotlib?

Matplotlib gives full control, but everything (colors, styling, statistical
calculations) is manual. Seaborn is built **on top of** Matplotlib, designed
specifically for **statistical visualization on DataFrames** — it works
directly with Pandas columns and adds automatic color grouping, statistical
summaries, and nicer default styling.

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

Seaborn plots still need `plt.show()` to render, since it draws using
Matplotlib underneath.

> Seaborn = built on Matplotlib, made for statistical plots directly from
> DataFrames. Still needs plt.show().

---

## 2. The Core Calling Pattern

Matplotlib: pass raw x/y lists.
```python
plt.bar(languages, popularity_score)
```

Seaborn: pass a **DataFrame** and name the **columns**.
```python
sns.barplot(data=df, x="Language", y="Popularity_Score")
```

Instead of manually pulling lists out, hand Seaborn the whole table and tell
it which columns to use. This matters a lot for real EDA on datasets with
many columns.

> sns.plot_type(data=df, x="col1", y="col2") — pass the whole DataFrame, name
> the columns.

---

## 3. Histograms — Seeing the Distribution (Shape) of One Variable

```python
sns.histplot(data=df, x="Exam_Score", bins=15)
plt.title("Exam Score Distribution")
plt.show()
```

Groups numeric values into "bins" (ranges) and shows how many values fall in
each — reveals skew, normal shape, multiple peaks (bimodal), outliers.

> sns.histplot(data=df, x="col", bins=N) — shows distribution/shape of one
> numeric column.

### Histogram vs Box Plot — an important distinction

A box plot only shows **5 summary numbers** (min, Q1, median, Q3, max) — it
does NOT show the actual shape in between. Two very differently-shaped
distributions (evenly spread, bimodal, tightly clustered with outliers) can
produce an **identical-looking box plot**, because box plots only care about
those five points.

- **Histogram** -> best for seeing actual distribution *shape*
- **Box plot** -> best for comparing spread/outliers *across categories*

> Histogram shows actual distribution shape (can reveal skew, bimodal
> patterns). Box plot only shows 5 summary numbers — two very
> differently-shaped datasets can produce an identical box plot.

---

## 4. Box Plots — Spread and Outliers Per Category

```python
sns.boxplot(data=df, x="Department", y="Salary")
plt.title("Salary by Department")
plt.show()
```

Shows median, the middle 50% of data (the box), and individual dots for
outliers — the visual version of the 5-number summary, split per category.
Connects directly to ANOVA (Day 2): visually checking whether a category
affects a numeric outcome.

> sns.boxplot(data=df, x="category_col", y="numeric_col") — shows median,
> spread, and outliers per category.

**Reading example:** in the employee dataset, Engineering had the widest
spread and highest median salary; Marketing had a tight box with several
outlier points — the tighter the box, the more strongly deviating values
stand out as outliers.

---

## 5. Scatter Plots With `hue` — Relationships Across 3 Variables

```python
sns.scatterplot(data=df, x="Study_Hours", y="Exam_Score", hue="Gender")
plt.title("Study Hours vs Exam Score by Gender")
plt.show()
```

Same idea as a Matplotlib scatter plot, but `hue` automatically color-codes
points by a third category — something that takes manual work in plain
Matplotlib.

> sns.scatterplot(data=df, x=, y=, hue=) — hue adds automatic color-coding by
> a category. Shows relationships across 3 variables at once.

**Reading example:** in the employee data, both genders followed the same
overall study-hours-to-exam-score trend, with no visible separation by
color — meaning gender didn't change that relationship much. A "no effect"
finding is still a valid, useful EDA result.

---

## 6. Count Plots — Counting Categories Automatically

```python
sns.countplot(data=df, x="Department")
plt.title("Employee Count by Department")
plt.show()
```

Automatically counts rows per category and draws bars — no manual counting
needed first (unlike `plt.bar()`, which requires pre-computed counts).

> sns.countplot(data=df, x="col") — auto-counts rows per category, no manual
> counting needed.

**Why this matters for other charts:** category sample sizes affect how much
to trust patterns seen elsewhere (e.g. a box plot for a category with only 16
rows is less reliable than one with 63 rows).

---

## 7. Heatmaps — Visualizing Correlation

```python
corr_matrix = df.corr(numeric_only=True)     # correlation between all numeric columns
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```

- `df.corr()` computes a correlation value (-1 to 1) between every pair of
  numeric columns
- `sns.heatmap()` turns that grid into a color-coded visualization
- `annot=True` prints the actual number inside each cell

**Reading correlation values:**
- Close to **1** -> strong positive relationship
- Close to **-1** -> strong negative relationship
- Close to **0** -> little/no relationship

> df.corr() computes correlation between numeric columns. sns.heatmap(...)
> visualizes it as a color grid — a fast way to spot which variables move
> together.

**Reading example:** `Study_Hours` and `Exam_Score` showed 0.88 correlation —
confirming, with an exact number, the pattern already visible in the scatter
plot. `Employee_ID` correlated near zero with everything, as expected since
it's an arbitrary sequential ID with no real meaning.

---

## 8. Pair Plots — The Full-Dataset Overview

```python
sns.pairplot(df)
plt.show()
```

Automatically creates a grid of scatter plots for every pair of numeric
columns, with histograms on the diagonal. Fastest way to get a first overall
look at a new dataset — one line of code shows every relationship at once.

> sns.pairplot(df) — auto-generates scatter plots for every pair of numeric
> columns + histograms on diagonal. Best first step when exploring a
> brand-new dataset.

---

## 9. The Full EDA Workflow

A repeatable process for exploring any new dataset:

1. **Load the data** -> `pd.read_csv()`
2. **First look** -> `df.head()`, `df.shape`, `df.info()`
3. **Check missing values** -> `df.isnull().sum()`
4. **Summary statistics** -> `df.describe()`
5. **Distribution of key numeric columns** -> `sns.histplot()`
6. **Spot outliers** -> `sns.boxplot()`
7. **Check relationships between variables** -> `sns.pairplot()` or `sns.heatmap()`
8. **Category breakdowns** -> `sns.countplot()`

> EDA workflow = load -> first look -> check missing values -> summary
> stats -> distributions -> outliers -> relationships -> category
> breakdowns.

---

## Quick Reference Cheat Sheet

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# 1. First look
df.head(); df.shape; df.info()

# 2. Missing values & stats
df.isnull().sum()
df.describe()

# 3. Distribution
sns.histplot(data=df, x="col", bins=15)
plt.show()

# 4. Outliers by category
sns.boxplot(data=df, x="category_col", y="numeric_col")
plt.show()

# 5. Relationships (3 variables)
sns.scatterplot(data=df, x="col1", y="col2", hue="category_col")
plt.show()

# 6. Category counts
sns.countplot(data=df, x="category_col")
plt.show()

# 7. Correlation
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# 8. Full overview
sns.pairplot(df)
plt.show()
```

---

## Notes on This Session

- Worked in a Jupyter Notebook (`.ipynb`) instead of a `.py` script for the
  first time — better suited for EDA since multiple outputs (tables, charts)
  can stay visible side by side, cell by cell, instead of popping up and
  disappearing one at a time like in a script.
- No major bugs today — all 8 tasks were completed correctly on the first or
  near-first attempt, applying patterns learned across Days 2-4 (boolean
  filtering, column selection, x/y ordering) correctly to new Seaborn syntax.

## Key Insight From the Dataset

`Study_Hours` and `Exam_Score` showed a strong positive correlation (0.88),
confirmed both visually (scatter plot, pairplot) and numerically (heatmap).
`Salary` correlated weakly with every individual factor (age, study hours,
exam score) but varied heavily by `Department` in the box plot — suggesting
department, not personal metrics, is the main salary driver in this dataset.

---

## Resources Used

- [Seaborn official documentation](https://seaborn.pydata.org/)