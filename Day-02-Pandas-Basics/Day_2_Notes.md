# Day 2 — Pandas Series & DataFrame — Notes

Topics covered: Series, DataFrame, inspection, selection, filtering, adding/dropping columns

---

## 1. Why Pandas, If We Already Have NumPy?

NumPy is great for pure numbers in a grid. Real-world data isn't just numbers —
it has column names, row labels, mixed types (text, dates, numbers), and
missing values. Pandas is built on top of NumPy specifically to handle that
kind of messy, labeled, real-world data.

> Pandas = built on NumPy, adds labels, column names, mixed types. Used for
> real-world tabular data (like a spreadsheet).

---

## 2. Series vs DataFrame

**Series** = a single column of data, with labels (an "index") attached to
each value.

```
0    10
1    20
2    30
```

**DataFrame** = a full table — multiple Series stuck together side by side,
each with a column name.

```
   Name    Age
0  Asha    25
1  Raj     30
2  Meera   28
```

> Series = single labeled column. DataFrame = full table, made of multiple
> Series with column names.

---

## 3. Creating a Series

```python
import pandas as pd

s = pd.Series([10, 20, 30])
```
```
0    10
1    20
2    30
dtype: int64
```

The left column (0, 1, 2) is the **index** — auto-generated unless specified.

Custom index:
```python
s = pd.Series(data=[10, 20, 30], index=["a", "b", "c"])
```
```
a    10
b    20
c    30
```

> Series has two parts: index (labels) and values. Index defaults to 0,1,2...
> but can be custom.

**Syntax trap:** when passing multiple arguments to a function, all of them
must sit inside the *same* matching pair of parentheses:
```python
# WRONG — index= ends up outside the function call, causes a SyntaxError
s2 = pd.Series(data=[100,200,300]), index=["a","b","c"]

# RIGHT — both arguments inside one pair of parentheses
s2 = pd.Series(data=[100,200,300], index=["a","b","c"])
```

---

## 4. Creating a DataFrame

Usually built from a dictionary — keys become column names, values (lists)
become column data.

```python
data = {
    "Name": ["Asha", "Raj", "Meera"],
    "Age": [25, 30, 28]
}
df = pd.DataFrame(data)
```
```
    Name  Age
0   Asha   25
1   Raj    30
2   Meera  28
```

> DataFrame from a dict: keys -> column names, lists -> column values. Each
> list must be the same length.

**Get column names exactly right at creation time.** Every later reference
(`df["Population"]`) depends on matching the spelling and case precisely —
a typo in the key means a `KeyError` everywhere you try to use it later.

---

## 5. Inspecting a DataFrame

```python
df.shape        # (rows, columns)
df.columns      # list of column names
df.info()       # column names, dtypes, non-null counts, memory usage
df.describe()   # quick statistics — mean, std, min, max, etc.
```

**Important:** `describe()` only computes statistics for **numeric** columns
by default — text columns (like a "City" column) are automatically skipped,
since you can't average city names.

**Small gotcha:** `df.info()` prints its own output directly *and* returns
`None`. Wrapping it in `print(df.info())` will show the info, followed by a
stray `None` on its own line. In practice, just call `df.info()` on its own
line without `print()`.

> head/tail = peek at data. shape = size. info() = structure + missing
> values. describe() = quick stats summary (numeric columns only).

---

## 6. Selecting Columns and Rows

```python
df["Name"]           # one column -> returns a Series
df[["Name", "Age"]]  # list of columns (even just one) -> returns a DataFrame

df.loc[0]    # select row by label
df.iloc[0]   # select row by position (0-based, like a list/NumPy array)
```

**Key distinction:**
- `.loc` -> label-based (uses the actual index labels)
- `.iloc` -> position-based (uses integer position)

These usually give the same row when the index is the default 0,1,2..., but
they are conceptually different and can diverge once the index is customized
(e.g. after filtering or setting a custom index).

> df["col"] -> one column (Series). df[["col"]] -> DataFrame (double
> brackets). .loc = by label. .iloc = by position.

---

## 7. Filtering Rows With a Condition

Same boolean-masking idea as NumPy yesterday, applied to a whole table:

```python
df[df["Age"] > 26]
```

`df["Age"] > 26` creates a boolean Series (True/False per row); `df[...]`
keeps only the rows where it's True.

> df[df["col"] > value] filters rows. Same boolean-masking idea as NumPy,
> applied to a whole table.

---

## 8. Adding a New Column

```python
df["Age_in_5_years"] = df["Age"] + 5
```

Vectorized, just like NumPy — no loop needed. The operation is applied to the
entire column at once.

> df["new_col"] = expression -> adds a new column. Vectorized, works on the
> whole column at once.

---

## 9. Dropping a Column or Row

```python
df.drop("Age_in_5_years", axis=1)   # drop a column (axis=1 = columns)
df.drop(0, axis=0)                  # drop a row (axis=0 = rows)
```

**`axis=0` = rows, `axis=1` = columns** — this convention reappears constantly
in Pandas.

**Important:** `drop()` returns a **new** DataFrame by default; it does not
modify the original. To make the change stick:
```python
df = df.drop("col", axis=1)      # reassign, or:
df.drop("col", axis=1, inplace=True)   # modify in place
```

If you call `.drop(...)` without printing or reassigning the result, the
computed DataFrame is silently discarded — nothing visibly changes.

> drop(axis=0) = rows, drop(axis=1) = columns. Doesn't modify original unless
> you reassign or use inplace=True.

---

## Quick Reference Cheat Sheet

```python
import pandas as pd

# Create
s = pd.Series([1, 2, 3], index=["a", "b", "c"])
df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})

# Inspect
df.shape, df.columns
df.info()
df.describe()

# Select
df["col1"]              # Series
df[["col1", "col2"]]    # DataFrame
df.loc[0]                # row by label
df.iloc[0]                # row by position

# Filter
df[df["col1"] > 1]

# Add / drop
df["new_col"] = df["col1"] * 2
df.drop("new_col", axis=1)          # returns new df, doesn't modify original
df.drop("new_col", axis=1, inplace=True)   # modifies in place
```

---

## Mistakes I Made & Fixed Today

- Misplaced a closing parenthesis when creating a Series with a custom index
  — `index=` ended up outside the `pd.Series(...)` call, causing a syntax
  error. Fixed by keeping all arguments inside one matching pair of
  parentheses.
- Typed the wrong values into a Series multiple times — a reminder to
  double-check data against the task before running, since wrong values in
  otherwise-correct code are an easy bug to miss.
- Misspelled dictionary keys (case and typos) — column names must be exact
  since every later reference depends on matching them precisely.
- Called `df.drop(...)` without `print()` or reassignment — since `drop()`
  returns a new DataFrame instead of modifying in place, the result was
  silently discarded.

---

## Resources Used

- [Pandas documentation — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)