# Day 2 — Pandas Series & DataFrame

**Topics:** Series, DataFrame, inspection, selection, filtering, adding/dropping columns

## What I Learned

- Pandas is built on top of NumPy, adding labels, column names, and support for mixed data types — built for real-world tabular data (like a spreadsheet).
- **Series** = a single labeled column of data (index + values). **DataFrame** = a full table, made of multiple Series with column names.
- A DataFrame is usually built from a dictionary: keys become column names, lists become column values (all lists must be the same length).
- Core inspection tools: `.shape` (size), `.columns` (names), `.info()` (types + missing values), `.describe()` (quick stats — numeric columns only).
- `df["col"]` (single column) returns a **Series**; `df[["col1","col2"]]` (list of columns) returns a **DataFrame** — the double brackets make the difference.
- `.loc` = select by label. `.iloc` = select by position. Same underlying idea as NumPy indexing, but for labeled data.
- Filtering rows uses the same boolean-masking idea from NumPy: `df[df["col"] > value]`.
- Adding a column: `df["new_col"] = expression` — vectorized, no loop needed.
- `df.drop("col", axis=1)` drops a column; `axis=0` drops rows. `drop()` returns a **new** DataFrame by default — it does not modify the original unless reassigned or called with `inplace=True`.

## Resources Used

- [Pandas documentation — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

## Mistakes I Made & Fixed

- Misplaced a closing parenthesis when creating a Series with a custom index — `index=` ended up outside the `pd.Series(...)` call, causing a syntax error. Fixed by keeping all arguments inside one matching pair of parentheses.
- Typed the wrong values into a Series multiple times (`20` instead of `25`) — a reminder to double-check data against the task before running, since wrong values in otherwise-correct code are an easy bug to miss.
- Misspelled dictionary keys (`"city"` instead of `"City"`, `"Populatiom"` instead of `"Population"`) — column names need to be exact since every later reference (`df["Population"]`) depends on matching them precisely.
- Called `df.drop(...)` without `print()` — since `drop()` returns a new DataFrame instead of modifying in place, forgetting to print or store the result means the output is silently discarded.

## Exercises Completed

- [x] Task 1 — Creating a Series (default + custom index)
- [x] Task 2 — Creating a DataFrame from a dictionary
- [x] Task 3 — Inspecting a DataFrame (shape, columns, info, describe)
- [x] Task 4 — Selecting columns and rows (`.loc` / `.iloc`)
- [x] Task 5 — Filtering rows with a condition
- [x] Task 6 — Adding and dropping columns

## Next Up

Day 3 — Reading data from multiple sources: CSV, JSON, SQL databases, REST APIs