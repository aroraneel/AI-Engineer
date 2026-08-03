# Day 5 — Seaborn + Full EDA Workflow

**Topics:** histplot, boxplot, scatterplot with hue, countplot, heatmap, pairplot, end-to-end EDA process

## What I Learned

- Seaborn is built on top of Matplotlib, designed for statistical visualization directly from DataFrames. It still needs `plt.show()` under the hood.
- Seaborn's calling style: `sns.plot_type(data=df, x="col1", y="col2")` — pass the whole DataFrame and name columns, instead of pulling out raw lists like Matplotlib.
- `sns.histplot(data=df, x="col", bins=N)` — shows the actual **shape** of a distribution (skew, bimodal patterns, etc.). A box plot only shows 5 summary numbers and can look identical for very differently-shaped data — histogram is the right tool when the goal is seeing "shape."
- `sns.boxplot(data=df, x="category", y="numeric")` — visual 5-number summary (min, Q1, median, Q3, max) per category, and shows outliers as individual points. Best for comparing spread/outliers *across groups*, not for seeing shape.
- `sns.scatterplot(data=df, x=, y=, hue="category")` — `hue` auto-colors points by a third category, letting you see relationships across 3 variables in one chart.
- `sns.countplot(data=df, x="col")` — auto-counts rows per category, no manual counting needed (unlike `plt.bar()`).
- `df.corr(numeric_only=True)` computes correlation (-1 to 1) between every pair of numeric columns; `sns.heatmap(corr_matrix, annot=True)` visualizes it as a color grid — a fast way to spot which variables move together, and to numerically confirm patterns already seen visually.
- `sns.pairplot(df)` auto-generates scatter plots for every pair of numeric columns plus histograms on the diagonal — the fastest first-look tool for a brand-new dataset.
- Full EDA workflow: load → first look (head/shape/info) → check missing values → summary stats → distributions → outliers → relationships → category breakdowns.

## Key Insight From the Dataset

`Study_Hours` and `Exam_Score` showed a strong positive correlation (0.88), confirmed both visually (scatter plot, pairplot) and numerically (heatmap). `Salary`, on the other hand, correlated weakly with every individual factor (age, study hours, exam score) but varied heavily by `Department` in the box plot — suggesting department, not personal metrics, is the main salary driver in this dataset.

## Resources Used

- [Seaborn official documentation](https://seaborn.pydata.org/)

## Exercises Completed

- [x] Task 1 — Load data & first look (head, shape, info)
- [x] Task 2 — Missing values & summary statistics
- [x] Task 3 — Histogram (distribution shape)
- [x] Task 4 — Box plot (outliers by category)
- [x] Task 5 — Scatter plot with hue (3-variable relationships)
- [x] Task 6 — Count plot (category counts)
- [x] Task 7 — Correlation heatmap
- [x] Task 8 — Pair plot (full dataset overview)

## Next Up

Day 6 — What is statistics; types of statistics; population vs sample