# Day 10 — Correlation & Covariance — Notes

Topics covered: correlation & covariance; outlier intuition revisited

---

## 1. Covariance

Measures whether two variables tend to increase/decrease TOGETHER.

```
Positive covariance -> when X goes up, Y tends to go up too (and vice versa)
Negative covariance -> when X goes up, Y tends to go DOWN (and vice versa)
Covariance near 0   -> no consistent relationship
```

**Example:** hours studied vs exam score -> as study hours increase, scores
tend to increase too -> positive covariance. Hours watching TV vs exam score
-> as TV hours increase, scores tend to decrease -> negative covariance.

> Covariance = whether two variables move together. Positive = move same
> direction. Negative = move opposite directions. Near 0 = no relationship.

```python
cov_matrix = np.cov(x, y)   # returns a 2x2 matrix
covariance = cov_matrix[0, 1]   # the actual cross-covariance value
```

The matrix also contains `[0,0]` (x's own variance) and `[1,1]` (y's own
variance) — the off-diagonal `[0,1]`/`[1,0]` (always identical, since the
matrix is symmetric) is the cross-covariance you actually want.

---

## 2. Why Covariance Alone Isn't Enough

Covariance's raw number is hard to interpret because it depends on the
UNITS and SCALE of the variables.

**Example:** covariance between height (cm) and weight (kg) will be a
totally different number than covariance between height (m) and weight (g)
— even describing the exact same relationship. The number tells you
direction, but not how STRONG the relationship is.

> Covariance's number is hard to interpret directly — it's affected by the
> scale/units of the variables. Tells you direction, not strength.

---

## 3. Correlation (Pearson r)

Correlation "standardizes" covariance into a value always between -1 and 1,
regardless of original units — this is the number `df.corr()` and every
heatmap since Day 5 has been showing.

```
+1  -> perfect positive relationship
 0  -> no linear relationship
-1  -> perfect negative relationship
```

**Rough strength guide:**
- 0.7 to 1.0 (or -0.7 to -1.0) -> strong
- 0.3 to 0.7 (or -0.3 to -0.7) -> moderate
- 0 to 0.3 (or 0 to -0.3)      -> weak/negligible

> Correlation = standardized covariance, always between -1 and 1. +1 =
> perfect positive, -1 = perfect negative, 0 = no linear relationship. This
> is what df.corr() and heatmaps show.

```python
corr_matrix = np.corrcoef(x, y)
correlation = corr_matrix[0, 1]   # convention: use [0,1]; [1,0] is identical
                                    # since the matrix is symmetric
```

**Full interpretation always includes direction AND strength:** e.g. r=0.85
between ice cream sales and temperature means a STRONG, POSITIVE
relationship — as temperature rises, sales rise too, fairly consistently.

---

## 4. Correlation vs Causation

**Correlation never proves causation on its own.** A strong correlation can
come from:
1. Genuine direct causation (A actually causes B)
2. A hidden THIRD factor independently driving both A and B, with no direct
   link between them

**Classic example:** ice cream sales and shark attacks (or drowning deaths)
are strongly positively correlated. Ice cream doesn't cause shark
attacks/drownings. The real driver is a hidden third factor: HOT SUMMER
WEATHER — more people swim (more risk) AND more people buy ice cream
(because it's hot), independently.

**Another example:** Nobel Prize winners per country correlates with
chocolate consumption per capita — the real hidden factor is likely
national wealth/economic development, which funds both research and
affordable chocolate.

> Correlation shows strength + direction of a relationship, but never
> proves causation on its own. Always describe both direction
> (positive/negative) and strength (weak/moderate/strong) when interpreting
> r.

**The test for spotting a hidden third factor:** ask "could some other
variable independently explain BOTH things moving together, without either
one directly causing the other?"

### Worked classification examples

| Pair | Type | Hidden factor (if applicable) |
|---|---|---|
| Firefighters at a scene vs damage caused | Hidden 3rd factor | Fire size (bigger fire -> more firefighters sent AND more damage) |
| Study hours vs exam score | Direct causation | (none needed) |
| Ice cream consumption vs drowning deaths | Hidden 3rd factor | Hot summer weather |
| Cigarettes smoked vs lung disease risk | Direct causation | (extensively proven medically) |

---

## Quick Reference Cheat Sheet

```python
import numpy as np
import pandas as pd

# Covariance
cov_matrix = np.cov(x, y)
covariance = cov_matrix[0, 1]

# Correlation
corr_matrix = np.corrcoef(x, y)
correlation = corr_matrix[0, 1]

# On a DataFrame
df.corr()                              # full correlation matrix
df.corr().loc["col1", "col2"]          # one specific pair
```

---

## Mistakes I Made & Fixed Today

- Printed the full 2x2 covariance/correlation matrix instead of extracting
  the single cross-value at `[0,1]` — fixed with proper indexing.
- Misclassified "ice cream consumption vs drowning deaths" as direct
  causation — this is structurally identical to the ice cream/shark attacks
  example from the lesson (hidden third factor: hot summer weather), not
  genuine causation.
- Initially left the hidden third factor for "firefighters vs fire damage"
  unnamed — added the actual driver (fire size) after review.

---

## Milestone

**Days 1-10 complete: Data & Statistics Foundations.** Covered NumPy,
Pandas, reading data from multiple sources, Matplotlib, Seaborn/EDA, and
core descriptive statistics (central tendency, dispersion, n-1 correction,
percentiles/IQR, correlation/covariance). Probability begins Day 11.

---

## Resources Used

- General statistics fundamentals (covariance, Pearson correlation,
  correlation vs causation)