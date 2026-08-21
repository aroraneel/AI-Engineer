# Matplotlib & Seaborn — Cheat Sheet

Quick reference for common plot types, syntax patterns, and when to use each.

---

## Setup

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

Seaborn is built **on top of** Matplotlib — it still needs `plt.show()` to
render, and `plt.title()`, `plt.xlabel()`, `plt.ylabel()` still work on
Seaborn plots.

---

## The Core Calling Pattern Difference

**Matplotlib** — pass raw x/y lists directly:
```python
plt.plot(months, website_visitors)
plt.bar(languages, popularity_score)
plt.scatter(study_hours, exam_scores)
```

**Seaborn** — pass a DataFrame and name the columns:
```python
sns.barplot(data=df, x="Language", y="Popularity_Score")
```

Seaborn works directly on Pandas DataFrames — hand it the whole table and
tell it which columns to use, instead of manually pulling out lists.
Matters a lot on real datasets with many columns.

---

## Matplotlib — Plot Types

### Line Plot — trend over time/sequence
```python
plt.plot(months, website_visitors)
plt.title("Website Visitors Over 6 Months")
plt.xlabel("Month")
plt.ylabel("Visitors")
plt.show()
```
**Use for:** continuous trends, time series.

### Bar Plot — comparing categories
```python
plt.bar(languages, popularity_score)
plt.title("Programming Language Popularity")
plt.xlabel("Language")
plt.ylabel("Popularity Score")
plt.show()
```
**Use for:** comparing a numeric value across discrete categories.

### Scatter Plot — relationship between two numeric variables
```python
plt.scatter(study_hours, exam_scores)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()
```
**Use for:** spotting correlation/relationships between two continuous variables.

### Subplots — multiple plots in a grid
```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0,0].plot(months, website_visitors)
axes[0,0].set_title("Website Visitors")

axes[0,1].bar(languages, popularity_score)
axes[0,1].set_title("Language Popularity")

axes[1,0].scatter(study_hours, exam_scores)
axes[1,0].set_title("Study Hours vs Exam Scores")

axes[1,1].plot(months, temperature_by_month)
axes[1,1].set_title("Temperature Over 6 Months")

plt.tight_layout()   # prevents overlapping labels/titles
plt.show()
```
**Key syntax notes:**
- `axes[row, col]` — index into the grid position
- Use `.set_title()` on subplots, not `plt.title()` (that only affects the last-drawn plot)
- Always call `plt.tight_layout()` before `plt.show()` with subplots

---

## Seaborn — Plot Types

### Histogram — distribution shape of ONE numeric variable
```python
sns.histplot(data=df, x="Exam_Score", bins=15)
plt.title("Exam Score Distribution")
plt.show()
```
**Use for:** seeing skew, normal shape, bimodal patterns, outliers in one column.

### Box Plot — spread & outliers per category
```python
sns.boxplot(data=df, x="Department", y="Salary")
plt.title("Salary by Department")
plt.show()
```
**Use for:** comparing spread/median/outliers of a numeric variable across categories. Shows the 5-number summary (min, Q1, median, Q3, max) visually.

**⚠️ Histogram vs Box Plot:** a box plot only shows 5 summary numbers — two very differently-shaped distributions (evenly spread vs bimodal) can produce an *identical-looking* box plot. Use histogram for actual shape, box plot for spread/outlier comparison across categories.

### Scatter Plot with `hue` — relationships across 3 variables
```python
sns.scatterplot(data=df, x="Study_Hours", y="Exam_Score", hue="Gender")
plt.title("Study Hours vs Exam Score by Gender")
plt.show()
```
**Use for:** same as a regular scatter plot, but `hue` auto-color-codes by a third categorical variable — reveals whether a relationship differs across groups.

### Count Plot — auto-counting categories
```python
sns.countplot(data=df, x="Department")
plt.title("Employee Count by Department")
plt.show()
```
**Use for:** counting rows per category automatically (no manual counting needed first, unlike `plt.bar()` which requires pre-computed counts). Also useful for checking sample size per category before trusting patterns in other charts.

### Heatmap — visualizing correlation
```python
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```
**Key syntax notes:**
- `df.corr()` computes correlation (-1 to 1) between every pair of numeric columns
- `annot=True` prints the actual number inside each cell
- `cmap="coolwarm"` — color scheme (red=positive, blue=negative, typically)

**Reading correlation values:**
```
Close to  1  -> strong positive relationship
Close to -1  -> strong negative relationship
Close to  0  -> little/no relationship
```

### Pair Plot — full-dataset overview in one line
```python
sns.pairplot(df)
plt.show()
```
**Use for:** the fastest first look at a brand-new dataset — auto-generates scatter plots for every pair of numeric columns, with histograms on the diagonal.

---

## Which Plot Do I Need? Quick Decision Guide

| Question | Plot |
|---|---|
| How does one numeric value change over time/sequence? | Line plot |
| How do numeric values compare across categories? | Bar plot |
| Is there a relationship between two numeric variables? | Scatter plot |
| Does that relationship differ by a 3rd category? | Scatter plot + `hue` |
| What's the shape/distribution of one numeric column? | Histogram |
| How does spread/outliers compare across categories? | Box plot |
| How many rows per category? | Count plot |
| Which variables move together? | Heatmap (correlation) |
| First overview of a brand-new dataset? | Pair plot |
| Need to compare multiple plots side by side? | Subplots (`plt.subplots`) |

---

## The Full EDA (Exploratory Data Analysis) Workflow

A repeatable process for exploring any new dataset, start to finish:

```python
# 1. Load the data
df = pd.read_csv("data.csv")

# 2. First look
df.head()
df.shape
df.info()

# 3. Check missing values
df.isnull().sum()

# 4. Summary statistics
df.describe()

# 5. Distribution of key numeric columns
sns.histplot(data=df, x="column_name")

# 6. Spot outliers
sns.boxplot(data=df, x="category_col", y="numeric_col")

# 7. Check relationships between variables
sns.scatterplot(data=df, x="col1", y="col2", hue="category_col")
sns.heatmap(df.corr(numeric_only=True), annot=True)

# 8. Full overview
sns.pairplot(df)
```

---

## Common Gotchas

- Seaborn plots still need `plt.show()` — it draws using Matplotlib underneath.
- With `plt.subplots()`, use `axes[row,col].set_title()`, not `plt.title()` — the latter only labels the very last plot drawn.
- `df.corr()` only works on numeric columns — use `numeric_only=True` to avoid errors on datasets with text columns.
- `plt.bar()` needs pre-counted values; `sns.countplot()` counts automatically from raw rows.
- Always call `plt.tight_layout()` before `plt.show()` when using subplots, or titles/labels can overlap.
