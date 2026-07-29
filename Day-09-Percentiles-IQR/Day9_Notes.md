# Day 9 — Percentiles, Quartiles, 5-Number Summary, IQR Outlier Detection — Notes

Topics covered: histograms (conceptual continuation); percentiles & quartiles; 5-number summary

---

## 1. Percentiles

**Nth percentile** = the value below which N% of the data falls.

**Example:** scoring in the 90th percentile on a test means 90% of
test-takers scored lower than you (and 10% scored higher). It tells
*relative standing*, not your raw score.

> Nth percentile = the value below which N% of the data falls. Tells
> relative standing, not raw value.

```python
np.percentile(scores, 25)   # 25th percentile
np.percentile(scores, 90)   # 90th percentile
```

---

## 2. Quartiles

Quartiles are specific, commonly-used percentiles that split data into four
equal parts:

- **Q1 (25th percentile)** — 25% of data falls below this
- **Q2 (50th percentile)** — this IS the median — 50% of data falls below
- **Q3 (75th percentile)** — 75% of data falls below this

**Worked example** (scores sorted, n=20): Q1=67.25, Q2=79.0, Q3=90.5.

**Interquartile Range (IQR)** = Q3 − Q1. Measures the spread of the MIDDLE
50% of the data — this is exactly what a box plot's "box" draws.

> Quartiles split data into 4 equal parts: Q1=25th percentile,
> Q2=median=50th, Q3=75th percentile. IQR = Q3-Q1 = spread of middle 50% of
> data.

---

## 3. The 5-Number Summary

Five numbers that summarize an entire dataset's spread — exactly what a box
plot visualizes:
```
Minimum, Q1, Median (Q2), Q3, Maximum
```

> 5-number summary = Min, Q1, Median, Q3, Max. This is literally what a box
> plot draws.

**Verified against Pandas:** manually calculated values (45, 67.25, 79.0,
90.5, 100) matched `pd.Series(scores).describe()`'s min/25%/50%/75%/max
exactly — confirming both the manual math and what `.describe()` has been
computing all along.

---

## 4. IQR Outlier Detection Rule

The exact formula behind every box plot's outlier dots:

```
Lower bound = Q1 - 1.5 x IQR
Upper bound = Q3 + 1.5 x IQR
```

Any value below the lower bound OR above the upper bound is flagged as an
outlier.

> Outlier rule: below Q1-1.5xIQR or above Q3+1.5xIQR = outlier. This is
> exactly what box plot dots represent.

**Worked example:** Q1=40, Q3=60, IQR=20
```
Lower bound = 40 - (1.5 x 20) = 40 - 30 = 10
Upper bound = 60 + (1.5 x 20) = 60 + 30 = 90
```
Lower bound anchors off Q1 (subtracting); upper bound anchors off Q3
(adding) — different reference points for each side.

**Verified with code** on a dataset clustered around 22-27 with two planted
outliers (90 and 5):
```python
Q1, Q3 = np.percentile(data, [25, 75])
IQR = Q3 - Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

outliers = data[(data < lower_bound) | (data > upper_bound)]
# -> [90, 5], exactly matching manual inspection
```

---

## Quick Reference Cheat Sheet

```python
import numpy as np
import pandas as pd

# Percentiles / quartiles
np.percentile(data, 25)      # Q1
np.percentile(data, 50)      # Q2 / median
np.percentile(data, 75)      # Q3
q1, q2, q3 = np.percentile(data, [25, 50, 75])   # all at once

# IQR
iqr = q3 - q1

# 5-number summary
data.min(), q1, q2, q3, data.max()
pd.Series(data).describe()   # gives the same 5 numbers + count/mean/std

# Outlier bounds
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = data[(data < lower_bound) | (data > upper_bound)]
```

---

## Mistakes I Made & Fixed Today

- Requested the 90th percentile but wrote `np.percentile(scores, 75)` —
  simple argument mismatch, fixed by matching the number to what was asked.
- Tried `np.percentile(min.scores)` — `min` is a Python built-in function,
  not an object with a `.scores` attribute; also percentile is the wrong
  tool for a plain minimum. Fixed to `scores.min()` / `np.min(scores)`.
- Assigned `minimum = print(np.min(scores))` — `print()` returns `None`, so
  the variable silently stored `None` instead of the actual number, even
  though the correct value appeared on screen. Fixed by separating
  calculation (`minimum = np.min(scores)`) from printing
  (`print(minimum)`).
- Called `pd.Series(scores).describe` without parentheses — this references
  the method itself rather than calling it (same bug class as Day 4's
  `plt.show`). Fixed to `.describe()`.
- Wrote invalid chained comparison syntax for outlier bounds
  (`lower_bound >= <= upper_bound`) and initially left the actual data array
  out of the condition entirely. Fixed using proper boolean indexing:
  `data[(data < lower_bound) | (data > upper_bound)]`.

---

## Resources Used

- General statistics fundamentals (percentiles, quartiles, IQR, outlier
  detection)