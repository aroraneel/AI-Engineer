# Day 10 — Correlation & Covariance

**Topics:** correlation & covariance; intuition for spotting outliers (revisited via correlation lens)

## What I Learned

- **Covariance** measures whether two variables move together. Positive = same direction, negative = opposite directions, near 0 = no consistent relationship.
- **Covariance's raw number is hard to interpret directly** — it's affected by the scale/units of the variables (e.g. height in cm vs meters gives wildly different covariance numbers for the same relationship).
- **Correlation (Pearson r)** standardizes covariance into a value always between -1 and 1, regardless of original units. This is what `df.corr()` and heatmaps have been showing since Day 5.
  - +1 = perfect positive relationship
  - 0 = no linear relationship
  - -1 = perfect negative relationship
  - Rough strength guide: 0.7–1.0 strong, 0.3–0.7 moderate, 0–0.3 weak
- **`np.cov()` and `np.corrcoef()` return symmetric 2x2 matrices** — `[0,1]` and `[1,0]` are always identical values, since "how related are A and B" is the same question either order. `[0,1]` is the common convention, purely for readability/consistency, not because `[1,0]` is wrong.
- **Correlation never proves causation on its own.** A strong correlation can come from one variable genuinely causing the other (cigarettes → lung disease), or from a hidden third factor independently driving both (e.g. hot weather driving both ice cream sales and drowning deaths, or fire size driving both firefighter count and damage).
- The key test for "is this correlation actually causation": ask whether a plausible hidden third factor could independently explain both variables moving together.

## Resources Used

- General statistics fundamentals (covariance, Pearson correlation, correlation vs causation)

## Mistakes I Made & Fixed

- Printed the full covariance/correlation matrix instead of extracting just the single value at `[0,1]` — fixed by indexing into the matrix (`cov_matrix[0, 1]`) rather than printing the whole thing.
- Misclassified "ice cream consumption vs drowning deaths" as direct causation — this is actually the classic textbook example of correlation driven by a hidden third factor (hot summer weather driving both variables independently), essentially identical in structure to the ice cream/shark attacks example covered in the lesson.
- Initially left the "firefighters vs fire damage" hidden factor unnamed — added the actual driver (fire size) after review.

## Exercises Completed

- [x] Task 1 — Covariance calculation and interpretation
- [x] Task 2 — Pearson correlation, strength/direction classification
- [x] Task 3 — Correlation matrix on a real DataFrame (3 variables, coherent story across all pairs)
- [x] Task 4 — Correlation vs causation reasoning across 4 real-world scenarios

## Milestone

This completes **Days 1–10: Data & Statistics Foundations** — NumPy, Pandas, reading data, Matplotlib, Seaborn/EDA, and core descriptive/inferential statistics groundwork. Probability begins Day 11.

## Next Up

Day 11 — Probability: addition & multiplication rules; PDF / PMF / CDF; types of distributions; Bernoulli distribution