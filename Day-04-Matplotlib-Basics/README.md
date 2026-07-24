# Day 4 — Data Visualization with Matplotlib

**Topics:** line plots, bar plots, scatter plots, subplot layouts

## What I Learned

- Every plot follows the same pattern: prepare data → call a plot function (`plt.plot()`, `plt.bar()`, `plt.scatter()`) → customize (title, labels) → `plt.show()` to render.
- **Line plot** (`plt.plot(x, y)`) — best for trends over an ordered sequence (time, steps). Connecting points implies continuity.
- **Bar plot** (`plt.bar(x, y)`) — best for comparing distinct categories against each other. No implied order/continuity between bars.
- **Scatter plot** (`plt.scatter(x, y)`) — best for showing the relationship between two independent variables. No connecting lines, no implied order.
- In every one of these functions, **the first argument is the x-axis, the second is the y-axis** — and whatever the title/labels claim, the actual argument order must match that story.
- **Subplots**: `plt.subplots(rows, cols, figsize=(w,h))` creates a figure (`fig`) and a grid of individual plot slots (`axes`) upfront.
  - For a grid with more than 1 row and more than 1 column, `axes` is 2D — access slots with `axes[row, col]`, not `axes[i]`.
  - Each subplot needs its own `.set_title(...)` call, made on the exact same `axes[row, col]` that was just drawn on.
  - `plt.tight_layout()` prevents titles/labels from overlapping between subplots.

## Resources Used

- [Matplotlib Pyplot Tutorial (official docs)](https://matplotlib.org/stable/tutorials/pyplot.html)

## Mistakes I Made & Fixed

- Passed variable names as quoted strings (`plt.plot("website_visitors", "months")`) instead of the actual variables — quotes turn a variable name into literal text, which Matplotlib can't plot as data.
- Repeatedly swapped x/y argument order across plot(), bar(), and scatter() calls — the first argument is always x-axis, second is always y-axis, and it must match the story told by the axis labels/title (e.g. "A vs B" or "A over B" implies B is the x-axis).
- Used 1D indexing (`axes[0]`, `axes[1]`) on a 2×2 grid instead of 2D indexing (`axes[0,0]`, `axes[0,1]`, etc.) — a grid with more than one row AND more than one column requires two indices.
- Called `.set_title(...)` on the wrong `axes[row,col]`, disconnected from the subplot it was meant to label — titles must be set on the exact same axes object that was just drawn on.
- Called `plt.show` without parentheses — this only references the function without calling it; needs `plt.show()`.
- Minor: label text capitalization not matching the task exactly (e.g. "months" vs "Month") — small, but worth being precise about since labels are user-facing.

## Exercises Completed

- [x] Task 1 — Line plot (website visitors over months)
- [x] Task 2 — Bar plot (language popularity)
- [x] Task 3 — Scatter plot (study hours vs exam scores)
- [x] Task 4 — 2x2 subplot grid combining all chart types

## Next Up

Day 5 — Data visualization with Seaborn; building a first end-to-end EDA workflow

**Test day** — Days 1-5 review test before moving to Day 6.