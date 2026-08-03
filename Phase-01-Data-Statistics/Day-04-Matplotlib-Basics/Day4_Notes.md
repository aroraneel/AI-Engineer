# Day 4 — Data Visualization with Matplotlib — Notes

Topics covered: line plots, bar plots, scatter plots, subplot layouts

---

## 1. Why Visualization Matters

Numbers in a table are hard to reason about at a glance. A chart lets you
*see* patterns — trends, outliers, comparisons — instantly. Matplotlib is the
foundational plotting library in Python; most other visualization tools
(Seaborn, Pandas' `.plot()`) are built on top of it.

---

## 2. The Basic Pattern

```python
import matplotlib.pyplot as plt

plt.plot(x, y)      # or plt.bar(), plt.scatter(), etc.
plt.show()           # actually renders the plot
```

Every plot follows this shape: **prepare data -> call a plotting function ->
customize -> plt.show()**.

> matplotlib.pyplot as plt. Every plot: call a plot function, then
> plt.show() to render it.

---

## 3. Line Plots — Trends Over an Ordered Sequence

```python
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 250, 180, 300, 280]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

`plt.plot(x, y)` draws a line connecting the points, in order. Best used when
there's a natural sequence (time, steps) where the connecting line tells a
meaningful "trend" story.

> plt.plot(x,y) = line chart, good for trends/sequences. Always add
> title/xlabel/ylabel.

---

## 4. Bar Plots — Comparing Categories

```python
products = ["Laptop", "Mouse", "Keyboard"]
revenue = [55000, 1200, 2500]

plt.bar(products, revenue)
plt.title("Revenue by Product")
plt.show()
```

`plt.bar(x, y)` draws a bar per category. Best for comparing **discrete
groups** that don't have an inherent order/continuity between them (unlike a
line plot).

> plt.bar(x,y) = bar chart, good for comparing categories. Line plot implies
> a sequence; bar plot doesn't.

---

## 5. Scatter Plots — Relationship Between Two Variables

```python
hours_studied = [1, 2, 3, 4, 5]
marks = [50, 55, 65, 70, 85]

plt.scatter(hours_studied, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.show()
```

`plt.scatter(x, y)` plots individual points with **no connecting lines** —
used to check correlation/relationship between two numeric variables, where
neither has an inherent "order."

> plt.scatter(x,y) = scatter plot, shows relationship/correlation between two
> variables. No connecting lines.

### Choosing between the three

| Situation | Chart |
|---|---|
| Ordered sequence (time, steps) where a trend matters | Line plot |
| Comparing two variables for a relationship, no inherent order | Scatter plot |
| Comparing distinct categories/groups | Bar plot |

> Line plot = trend over an ordered sequence. Scatter plot = relationship
> between two variables, no inherent order. Bar plot = comparing distinct
> categories.

---

## 6. Subplots — Multiple Charts in One Figure

### Older style: `plt.subplot()`

```python
plt.subplot(1, 2, 1)   # 1 row, 2 columns, this is plot #1 (left)
plt.plot(months, sales)
plt.title("Sales Trend")

plt.subplot(1, 2, 2)   # 1 row, 2 columns, this is plot #2 (right)
plt.bar(products, revenue)
plt.title("Revenue by Product")

plt.tight_layout()
plt.show()
```

`plt.subplot(rows, cols, position)` — position starts at **1**, not 0, and
counts left-to-right, top-to-bottom.

> plt.subplot(rows, cols, position) — position starts at 1, not 0. Counts
> left-to-right, top-to-bottom. Use plt.tight_layout() to avoid overlapping
> labels.

### Modern style: `plt.subplots()` (with an "s") — the one actually used in practice

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))  # 2 rows, 2 columns

axes[0, 0].plot(months, website_visitors)
axes[0, 0].set_title("Website Visitors Over 6 Months")

axes[0, 1].bar(languages, popularity_score)
axes[0, 1].set_title("Programming Language Popularity")

axes[1, 0].scatter(study_hours, exam_scores)
axes[1, 0].set_title("Study Hours vs Exam Scores")

axes[1, 1].plot(months, temperature_by_month)
axes[1, 1].set_title("Temperature Over 6 Months")

plt.tight_layout()
plt.show()
```

`fig` = the overall figure. `axes` = an array of individual plot "slots."

**Critical rule for indexing `axes`:**
- Grid with only 1 row OR only 1 column -> `axes` is 1D -> `axes[0]`, `axes[1]`, ...
- Grid with more than 1 row AND more than 1 column (e.g. 2x2) -> `axes` is 2D
  -> must use `axes[row, col]`, e.g. `axes[0,0]`, `axes[0,1]`, `axes[1,0]`,
  `axes[1,1]`

> plt.subplots(rows, cols) — creates fig + axes array upfront. axes[i] =
> individual subplot for 1D grids; axes[row,col] for 2D grids. More common in
> real code than plt.subplot() (no "s").

---

## 7. The X/Y Argument Order Rule (the big recurring bug today)

In `plot()`, `bar()`, and `scatter()`, **the first argument is always the
x-axis, the second is always the y-axis**:

```python
plt.plot(months, website_visitors)     # months = x, website_visitors = y
plt.bar(languages, popularity_score)   # languages = x, popularity_score = y
plt.scatter(study_hours, exam_scores)  # study_hours = x, exam_scores = y
```

**How to decide the order from the task wording:**
- "A over B" -> B is the x-axis (what you're plotting *against*), A is the
  y-axis (what's changing)
- "A vs B", when A is an outcome and B is an input -> B is usually the x-axis
  (the cause/input), A is the y-axis (the effect/outcome)

Whatever order you use in the function call **must match** what your
`xlabel`/`ylabel` claim — otherwise the chart tells a false story.

---

## Quick Reference Cheat Sheet

```python
import matplotlib.pyplot as plt

# Line plot
plt.plot(x, y)
plt.title("Title"); plt.xlabel("X"); plt.ylabel("Y")
plt.show()

# Bar plot
plt.bar(categories, values)
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.show()

# 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x1, y1); axes[0, 0].set_title("A")
axes[0, 1].bar(x2, y2);  axes[0, 1].set_title("B")
axes[1, 0].scatter(x3, y3); axes[1, 0].set_title("C")
axes[1, 1].plot(x4, y4); axes[1, 1].set_title("D")
plt.tight_layout()
plt.show()
```

---

## Mistakes I Made & Fixed Today

- Passed variable names as quoted strings (`plt.plot("website_visitors",
  "months")`) instead of the actual variables — quotes make it literal text,
  which can't be plotted as data.
- Repeatedly swapped x/y argument order across `plot()`, `bar()`, and
  `scatter()` calls — first argument is always x, second is always y, and it
  must match the axis labels.
- Used 1D indexing (`axes[0]`, `axes[1]`) on a 2x2 grid instead of 2D indexing
  (`axes[0,0]`, `axes[0,1]`, etc.) — grids with more than 1 row AND more than
  1 column need two indices.
- Called `.set_title(...)` on the wrong `axes[row,col]` — titles must be set
  on the exact same axes object that was just drawn on.
- Called `plt.show` without parentheses — only references the function
  without calling it; needs `plt.show()`.

---

## Resources Used

- [Matplotlib Pyplot Tutorial (official docs)](https://matplotlib.org/stable/tutorials/pyplot.html)