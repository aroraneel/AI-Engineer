# Day 7 — Central Tendency & Dispersion; Why n-1

**Topics:** central tendency & dispersion; why we divide by n-1 for sample variance

## What I Learned

- **Central tendency** = one number describing the "center" of data. Mean = average. Median = middle value when sorted. Mode = most frequent value.
- **Mean is sensitive to outliers; median resists them.** A single extreme value (e.g. one very high salary) can drag the mean far from what's "typical," while the median stays anchored near the actual middle of the data.
- **Dispersion** = how spread out data is around its center. Two datasets can share the same mean but look completely different once you check their spread.
- **Range** = max − min. **Variance** = average of squared differences from the mean. **Standard deviation** = √variance, back in the original units (variance alone is in "squared" units, harder to interpret directly).
- **Population variance** divides by N (total count). **Sample variance** divides by **N−1**, not N — this is Bessel's correction.
- **Why n−1:** a sample's own mean is always the value closest to that sample's own data points (that's what "mean" means mathematically), so measuring spread against a sample's own mean makes the data look slightly *more* clustered — and the calculated variance slightly *too small* — than it really is relative to the true population mean. Dividing by a smaller number (n−1) corrects that underestimation.
- Sample variance/std dev is always ≥ population variance/std dev on the same data — verified directly with real numbers (population variance 100.0 vs sample variance 116.67 on the same 7-value dataset).
- The n−1 correction matters proportionally more for small samples (the "−1" is a large % of a small n) and barely matters for large samples (the "−1" is a tiny % of a large n) — consistent with large samples already being more reliable estimates on their own.
- Pandas' `.std()` and `.var()` default to **sample** statistics (n−1) automatically; pass `ddof=0` to get the population version instead.
- When mean is noticeably higher than median, suspect a high-value outlier pulling the mean up; when mean is lower than median, suspect a low-value outlier pulling it down.

## Resources Used

- General statistics fundamentals (conceptual — mean/median/mode, variance, Bessel's correction)
- [NumPy `np.var` / `np.std` documentation](https://numpy.org/doc/stable/reference/generated/numpy.var.html) (for the `ddof` parameter)

## Mistakes I Made & Fixed

- Called `data2(90 - 10)` — tried to "call" an array like a function using `()`, and hardcoded values instead of using `.max()`/`.min()` on the actual array. Fixed to `data2.max() - data2.min()`.
- Tried `df["Age"].mean(ddof=0)` — `ddof` is a parameter for `.std()`/`.var()` only, since it controls sample vs population division; `.mean()` has no such distinction and doesn't accept it. Fixed to `df["Age"].std(ddof=0)`.
- Initially described comparison results as "right" or "wrong" between two differently-shaped datasets — refined to describe them accurately as "tightly clustered" vs "widely spread," since both were correct calculations of genuinely different data.

## Exercises Completed

- [x] Task 1 — Mean, median, mode (NumPy + Pandas)
- [x] Task 2 — Outlier sensitivity (mean vs median on salary data)
- [x] Task 3 — Dispersion (range, standard deviation)
- [x] Task 4 — Population vs sample variance (n vs n−1, proven with real numbers)
- [x] Task 5 — Applied to a real dataset; identified a likely outlier from the mean/median gap

## Next Up

Day 8 — Standard deviation; variables & random variables