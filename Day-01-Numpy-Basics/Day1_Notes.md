# Day 1 — NumPy Fundamentals — Notes

Topics covered: arrays, indexing, broadcasting, vectorized operations

---

## 1. Why NumPy Exists

A normal Python list is flexible but slow — it stores numbers as generic Python
objects. NumPy gives you the `ndarray`: a fast, fixed-type, shape-aware grid of
numbers built for math.

> NumPy = fast, shape-aware number containers. It's the foundation every ML
> library (Pandas, scikit-learn, PyTorch, TensorFlow) is built on top of.

---

## 2. Arrays Have a Shape — and Shape Is Everything

An array can be 1D (a list of numbers), 2D (a table/grid), or more dimensions.

```python
a = np.array([1, 2, 3, 4, 5])          # shape (5,)   -> 1D, 5 elements
b = np.array([[1, 2, 3], [4, 5, 6]])   # shape (2, 3) -> 2D, 2 rows, 3 columns
```

**How to read shape fast:** count the outer brackets = rows, count items inside
one bracket = columns.

| Attribute | What it tells you       | Example (`b`) |
|-----------|--------------------------|---------------|
| `.shape`  | rows x columns (or more) | `(2, 3)`      |
| `.ndim`   | how many dimensions      | `2`           |
| `.dtype`  | what type the numbers are | `int64`     |

> Shape = (rows, columns). Always check shape first when debugging — most ML
> bugs are shape mismatches.

---

## 3. Indexing — 1D Arrays

1D arrays work like Python lists:

```python
arr = np.array([10, 20, 30, 40, 50])
#      index:    0   1   2   3   4

arr[0]     # 10   -> first element
arr[-1]    # 50   -> last element
arr[1:4]   # [20, 30, 40]  -> slice
arr[::2]   # [10, 30, 50]  -> every 2nd element
```

### Understanding `start:stop:step`

The numbers in a slice are **index positions, not values**.

```
Index:  0    1    2    3    4
Value: 10   20   30   40   50
```

`array[1:4]` means:
- **start = 1** -> begin at index 1 (value `20`)
- **stop = 4** -> stop *before* index 4 (index 3 is the last one included)
- **step** defaults to 1 -> move one index at a time

Result: `[20, 30, 40]` — **not** `50`, because `stop` is always excluded.

**Why is stop exclusive?** It makes the length of the slice easy to calculate:
`stop - start` = `4 - 1` = `3` elements. If stop were inclusive, every slice
calculation across the language would need `+1`, which is messier.

### Defaults when a piece is left blank

| Piece | Default if left blank |
|-------|------------------------|
| start | 0 (the very beginning) |
| stop  | the end of the array   |
| step  | 1                      |

```python
arr[::2]   # start=0, stop=end, step=2  -> [10, 30, 50]
arr[1:]    # start=1, stop=end, step=1  -> [20, 30, 40, 50]
arr[:3]    # start=0, stop=3, step=1    -> [10, 20, 30]
arr[:]     # everything, unchanged      -> [10, 20, 30, 40, 50]
```

> Numbers in a slice are index positions, not values. Stop index is always
> excluded. Length of slice = stop - start.

---

## 4. Indexing — 2D Arrays

2D arrays need two indices — row and column: `grid[row, col]`

```python
grid = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

grid[1, 2]     # 6        -> row 1, column 2
grid[0, :]     # [1 2 3]  -> ":" means "everything on this axis"
grid[:, 1]     # [2 5 8]  -> all rows, just column 1
grid[0:2, 0:2] # [[1 2],[4 5]]  -> top-left 2x2 block
```

> grid[row, col]. ":" means "all of this axis." This exact idea reappears in
> Pandas later as `df.loc[:, "col"]`.

### Grabbing a specific block (worked example: top-right 2x2)

```
        col0  col1  col2
row0  [   1     2     3  ]
row1  [   4     5     6  ]
row2  [   7     8     9  ]
```

"Top-right 2x2" = first 2 rows, **last 2 columns**:

```python
grid[0:2, 1:3]     # rows 0-1, cols 1-2
grid[:2, 1:3]      # shorthand, same result
grid[:2, -2:]      # using negative indexing — works regardless of grid size
```

Result: `[[2, 3], [5, 6]]`

**Tip:** negative indexing (`-2:`) is useful for "last N columns/rows" without
needing to know or count the exact size of the array.

---

## 5. Boolean (Conditional) Indexing

```python
data = np.array([3, 7, 1, 9, 4, 2, 8])

data > 4          # [False True False True False False True]  <- a "mask"
data[data > 4]    # [7 9 8]  -> only values where the mask is True
```

Instead of a `for` loop with an `if`, you write `data[condition]` and NumPy
filters instantly.

> Boolean indexing = data[condition] filters values automatically. Same
> pattern is reused later in Pandas as `df[df["col"] > value]`.

---

## 6. Broadcasting

```python
x = np.array([1, 2, 3])
x + 10   # [11, 12, 13]   -> the 10 is "stretched" across every element
```

It also works between a small array and a bigger one:

```python
matrix = np.array([[1, 2, 3],
                    [4, 5, 6]])
row = np.array([10, 20, 30])

matrix + row
# [[11, 22, 33],
#  [14, 25, 36]]
```

Here `row` is applied to *every row* of `matrix` automatically — no loop.

> Broadcasting = NumPy auto-stretches a smaller array to match a bigger one's
> shape, without copying data. Rule: works if dimensions match, or one of them
> is 1.

---

## 7. Vectorized Operations — Why NumPy Is Fast

"Vectorized" means applying an operation to the **whole array at once**,
instead of looping element by element.

```python
# Slow way — Python loop
result = [i * 2 for i in my_list]

# Fast way — vectorized
result = my_array * 2
```

Both give the same answer, but the vectorized version runs in optimized C
code internally instead of slow Python, element by element.

### My Benchmark (1,000,000 numbers, doubled)

| Method                  | Time        |
|-------------------------|-------------|
| Python list comprehension | 0.0451 sec |
| NumPy vectorized (`* 2`)   | 0.0017 sec |
| **Speedup**                | **~26x faster** |

> Vectorized = apply operation to whole array at once, no explicit loop. Runs
> in C internally -> much faster than a Python for-loop. This is why
> NumPy/Pandas/ML libraries are fast.

---

## Quick Reference Cheat Sheet

```python
import numpy as np

# Create
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])

# Inspect
a.shape, a.ndim, a.dtype

# Slice (1D): [start:stop:step], stop excluded
a[1:4]
a[::2]

# Index (2D): [row, col], ":" = everything on that axis
b[1, 0]
b[:, 0]
b[0:2, 0:2]

# Filter with a condition
a[a > 1]

# Broadcast an operation across shapes
a + 10
b + np.array([10, 20])

# Vectorize instead of looping
a * 2          # fast
[i * 2 for i in a]   # slow, avoid for large data
```

---

## Mistakes I Made & Fixed Today

- Forgot to wrap plain Python lists with `np.array()` — lists don't have `.shape`.
- Used `np.array[...]` (square brackets) instead of `np.array(...)` — `()`
  calls a function, `[]` indexes into something.
- Used `array[1::2]` instead of `array[::2]` for "every 2nd element" — forgot
  that leaving `start` blank means "start from index 0."
- Used `x * 10` instead of `x + 10` when the task asked to add — broadcasting
  works with any operator, so it ran fine, but wasn't the operation asked for.
- Printed a boolean mask instead of the filtered values in one case — had to
  apply the mask as an index (`data[mask]`) to actually pull the values out.

---

## Resources Used

- [NumPy Quickstart Guide (official docs)](https://numpy.org/doc/stable/user/quickstart.html)