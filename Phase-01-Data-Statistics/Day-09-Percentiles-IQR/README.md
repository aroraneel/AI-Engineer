# Day 9 — Percentiles, Quartiles, 5-Number Summary, IQR Outlier Detection

**Topics:** histograms (conceptual continuation from Day 5); percentiles & quartiles; the 5-number summary

## What I Learned

- **Nth percentile** = the value below which N% of the data falls. Tells relative standing, not a raw value — e.g. being at the 90th percentile means 90% of others scored lower (and 10% scored higher), placing you in roughly the top 10%.
- **Quartiles** are specific percentiles that split data into four equal parts: Q1 = 25th percentile, Q2 = median = 50th percentile, Q3 = 75th percentile.
- **IQR (Interquartile Range)** = Q3 − Q1 — measures the spread of the *middle 50%* of the data. This is exactly what a box plot's "box" represents.
- **5-number summary** = Minimum, Q1, Median, Q3, Maximum — this is literally what a box plot visualizes, and matches exactly what `.describe()` reports as min/25%/50%/75%/max.
- **Outlier detection rule (used by every box plot):**
  - Lower bound = Q1 − 1.5 × IQR
  - Upper bound = Q3 + 1.5 × IQR
  - Any value outside these bounds is flagged as an outlier.
- Verified this rule with real code: on a planted dataset, values `90` and `5` were correctly flagged as outliers against a tight cluster of 22-27, matching manual inspection exactly.

## Resources Used

- General statistics fundamentals (percentiles, quartiles, IQR, outlier detection)

## Mistakes I Made & Fixed

- Requested the 90th percentile but wrote `np.percentile(scores, 75)` — copy/typo error, fixed by matching the argument to the actual percentile asked for.
- Tried `np.percentile(min.scores)` to get the minimum — `min` is a Python built-in function, not an object with a `.scores` attribute, and percentile isn't the right tool for a plain minimum anyway. Fixed to `scores.min()` / `np.min(scores)`.
- Assigned `minimum = print(np.min(scores))` — `print()` returns `None`, not the printed value, so the variable ended up storing `None` instead of the actual number. Fixed by separating calculation from printing.
- Called `pd.Series(scores).describe` without parentheses — printed a reference to the method itself instead of running it (same class of bug as Day 4's `plt.show`). Fixed to `.describe()`.
- Wrote invalid chained comparison syntax (`lower_bound >= <= upper_bound`) for outlier detection, and initially forgot to actually reference the data array in the condition. Fixed using proper boolean indexing with `&`/`|` and parenthesized conditions, consistent with the pattern from Day 1.

## Exercises Completed

- [x] Task 1 — Percentiles (25th, 50th, 90th) with plain-English interpretation
- [x] Task 2 — Quartiles (Q1/Q2/Q3) and IQR
- [x] Task 3 — 5-number summary, cross-verified against `.describe()`
- [x] Task 4 — Real outlier detection using the IQR 1.5× rule

## Next Up

Day 10 — Correlation & covariance; intuition for spotting outliers