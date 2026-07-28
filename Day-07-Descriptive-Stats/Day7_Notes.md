# Day 7 — Central Tendency & Dispersion; Why n-1 — Notes

Topics covered: central tendency & dispersion; why we divide by n-1 for sample variance

---

## 1. Central Tendency — "Where's the Center of My Data?"

Three main measures, each answering "if I described this data with ONE
number, what would it be?"

**Mean** — the average.
```python
data = [10, 20, 30, 40, 50]
mean = (10+20+30+40+50) / 5 = 30
```

**Median** — the middle value when sorted (average the two middle values if
the count is even).
```python
[10, 20, 30, 40, 50]  -> median = 30
[10, 20, 30, 40]      -> median = (20+30)/2 = 25
```

**Mode** — the most frequently occurring value.
```python
[10, 20, 20, 30, 40]  -> mode = 20
```

> Central tendency = one number describing the "center." Mean = average.
> Median = middle value (sorted). Mode = most frequent value.

---

## 2. Mean vs Median — Outlier Sensitivity

**Mean is sensitive to outliers. Median resists them.**

```python
salaries = [40000, 42000, 45000, 48000, 500000]
mean   = 135000   # pulled way up by the outlier
median = 45000     # unaffected, still represents "typical"
```

One extreme value distorts the mean badly, making it look like the "typical"
salary is 135k — misleading. The median (45k) is a much more honest
representation of what a typical value actually is.

> Mean is pulled toward outliers. Median resists outliers, better represents
> "typical" value in skewed data.

**Reading the gap:** if mean is noticeably HIGHER than median, suspect a
high-value outlier pulling the mean up. If mean is LOWER than median,
suspect a low-value outlier pulling it down. Close together = fairly
symmetric data, no major outliers.

---

## 3. Dispersion — "How Spread Out Is My Data?"

Two datasets can have the SAME mean and look completely different:
```python
Data A: [48, 49, 50, 51, 52]   -> mean = 50, tightly clustered
Data B: [10, 30, 50, 70, 90]   -> mean = 50, wildly spread out
```

**Range** — simplest measure: max minus min.
```python
Data B: 90 - 10 = 80
```

**Variance** — the average of the SQUARED differences from the mean.
Squaring does two things: makes every deviation positive (so spread in
either direction counts equally), and punishes larger deviations more
heavily.

**Standard deviation** — the square root of variance, bringing it back to
the same units as the original data (variance alone is in "squared" units,
harder to interpret directly).

> Dispersion = how spread out data is. Range = max-min. Variance = avg of
> squared differences from mean. Std dev = sqrt(variance), back in original
> units.

### Worked by hand: variance and std dev for [2, 4, 6]

```
Step 1 - mean:            (2+4+6)/3 = 4
Step 2 - distance from mean:  2-4=-2,  4-4=0,  6-4=2
Step 3 - square each:         (-2)^2=4,  0^2=0,  2^2=4
Step 4 - average the squares (this IS variance): (4+0+4)/3 = 2.67
Step 5 - std dev = sqrt(variance):              sqrt(2.67) = 1.63
```

---

## 4. Why Divide by n-1 for Sample Variance (Bessel's Correction)

**Population variance:**
```
population variance = sum((x - mean)^2) / N
```
N = total population size. Straightforward.

**Sample variance:**
```
sample variance = sum((x - sample_mean)^2) / (n - 1)
```

### The intuition, step by step

1. To calculate a sample's variance, you need "the mean" — but you don't
   know the TRUE population mean (would need the whole population for
   that). So you use the SAMPLE's own mean instead.
2. A sample's own mean is, by definition, the value closest to that
   sample's own data points (that's mathematically what "mean" means — it
   minimizes distance to its own points).
3. This means measuring "how far is each point from the mean" using the
   sample's own mean will always make the points look a LITTLE closer
   together than they'd look measured against the true population mean.
4. This makes the calculated variance a bit too SMALL — it underestimates
   the real spread.
5. Dividing by a SMALLER number (n-1 instead of n) makes the result a bit
   BIGGER, correcting for that underestimation.

> Sample variance divides by n-1, not n, because using the sample's own mean
> makes the calculated variance a bit too small (biased). Dividing by a
> smaller number (n-1) corrects this bias. Called Bessel's correction.

**Proven with real numbers** (scores = [55,60,65,70,75,80,85], N=7):
```python
np.var(scores)            # population variance -> 100.0
np.var(scores, ddof=1)    # sample variance     -> 116.67
```
Sample variance IS bigger, exactly as predicted. This will ALWAYS be true —
sample variance/std dev is always >= population variance/std dev on the same
data.

### Why the correction matters more for small samples

The "-1" is always just one unit subtracted, but its RELATIVE size compared
to n matters:
- n=5: dividing by 4 instead of 5 -> a 20% difference (big relative jump)
- n=500: dividing by 499 instead of 500 -> a 0.2% difference (tiny)

Bigger samples are naturally more reliable already, so they need less
correction — the "-1" becomes proportionally negligible as n grows.

### Pandas default behavior

`.std()` and `.var()` in Pandas default to SAMPLE statistics (divide by
n-1) automatically. Pass `ddof=0` to get the population version instead.
`.mean()` has NO `ddof` parameter — there's no sample/population distinction
for a simple average the way there is for variance.

---

## Quick Reference Cheat Sheet

```python
import numpy as np
import pandas as pd

data = np.array([...])

# Central tendency
np.mean(data)
np.median(data)
pd.Series(data).mode()          # returns a Series (possibly multiple modes)

# Dispersion
data.max() - data.min()         # range
np.var(data)                    # population variance (divides by N)
np.var(data, ddof=1)            # sample variance (divides by N-1)
np.std(data)                    # population std dev
np.std(data, ddof=1)            # sample std dev

# Pandas (defaults to SAMPLE stats already)
df["col"].mean()
df["col"].median()
df["col"].std()                 # sample std dev (ddof=1 default)
df["col"].std(ddof=0)           # population std dev
```

---

## Mistakes I Made & Fixed Today

- Called `data2(90 - 10)` — tried to "call" an array like a function using
  `()`, and hardcoded values instead of computing them from the array.
  Fixed to `data2.max() - data2.min()`.
- Tried `df["Age"].mean(ddof=0)` — `ddof` only applies to `.std()`/`.var()`,
  since those involve a sample/population division choice; `.mean()` has no
  such distinction. Fixed to `df["Age"].std(ddof=0)`.
- Initially framed differently-spread datasets as one being "right" and the
  other "wrong" in a comparison — refined to describe them accurately as
  differing in spread (tightly clustered vs widely spread), since both were
  correct calculations of genuinely different data.

---

## Resources Used

- General statistics fundamentals (conceptual — mean/median/mode, variance,
  Bessel's correction)
- [NumPy var/std documentation](https://numpy.org/doc/stable/reference/generated/numpy.var.html)