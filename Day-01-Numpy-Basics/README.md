# Day 1 — NumPy Fundamentals

**Topics:** arrays, indexing, broadcasting, vectorized operations

## What I Learned

- NumPy arrays (`ndarray`) are fast, fixed-type, shape-aware containers — the foundation every ML library (Pandas, scikit-learn, PyTorch) is built on.
- `.shape`, `.ndim`, `.dtype` are the first things to check on any array — most ML bugs come from shape mismatches.
- `np.array()` is a function call — needs `()`, not `[]`. A plain Python list has no `.shape`/`.ndim`; you must wrap it with `np.array()` first.
- Slicing follows `[start:stop:step]`, and **stop is always exclusive**. Leaving a piece blank uses its default: start→0, stop→end, step→1.
- 2D indexing uses `grid[row, col]`; `:` means "everything along this axis." A single index like `grid[1]` defaults to "this row, all columns."
- Boolean indexing (`data[data > 4]`) filters an array using a condition directly — no loop needed. Same pattern reused later in Pandas (`df[df["col"] > x]`).
- Broadcasting lets NumPy apply an operation between differently-shaped arrays by automatically stretching the smaller one — no manual copying.
- Vectorized operations apply to a whole array at once and run in optimized C code internally, which is why they're dramatically faster than a Python `for` loop.

## Benchmark Result (my own machine)

Doubling 1,000,000 numbers:
- Python list comprehension: **0.0451 sec**
- NumPy vectorized (`np_array * 2`): **0.0017 sec**
- **NumPy was ~26x faster**

## Mistakes I Made & Fixed

- Forgot to wrap lists with `np.array()` — plain Python lists don't have `.shape`.
- Used `np.array[...]` (square brackets) instead of `np.array(...)` (parentheses) — brackets index into something, parentheses call a function.
- Used `array[1::2]` instead of `array[::2]` for "every 2nd element" — forgot that leaving `start` blank means "start from 0."
- Used `x * 10` instead of `x + 10` when the task asked to add — broadcasting works the same way for any operator, so the code ran fine, but it wasn't the right operation.
- Printed a boolean mask instead of the filtered values in one case — had to apply the mask as an index (`data[mask]`) to actually get the values out.

## Resources Used

- [NumPy Quickstart Guide (official docs)](https://numpy.org/doc/stable/user/quickstart.html)

## Exercises Completed

- [x] Task 1 — Creating arrays & checking shape
- [x] Task 2 — 1D indexing & slicing
- [x] Task 3 — 2D indexing & slicing
- [x] Task 4 — Boolean indexing
- [x] Task 5 — Broadcasting
- [x] Task 6 — Vectorized operations speed test

## Next Up

Day 2 — Pandas Series & DataFrame; data manipulation with Pandas & NumPy