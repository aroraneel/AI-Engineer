# Day 13 — Normal/Gaussian Distribution; Standard Normal & Z-score; Uniform Distribution — Notes

Topics covered: Normal (Gaussian) distribution; empirical rule (68-95-99.7);
Z-scores; Uniform distribution

---

## 1. What Problem Does Normal Distribution Solve?

Previous distributions (Bernoulli, Binomial, Poisson) all deal with
**counting** discrete outcomes (0, 1, 2, 3...). Normal is the first
**continuous** distribution — for measurements that can take any value,
including decimals (height, weight, temperature, exam scores).

---

## 2. The Bell Shape

Plotting real-world continuous measurements (like heights) produces a
curve that:
- Peaks in the middle (most values cluster around the average)
- Drops off symmetrically on both sides (extreme values are rare, equally
  rare in both directions)
- Smooth, no sharp corners

Also called the **Gaussian distribution** (after Carl Gauss) or **bell
curve**.

**Key property:** mean = median = mode, all at the exact center. Zero
skewness — perfectly symmetric.

---

## 3. Two Parameters Define It Completely

- **μ (mu)** = mean = **location parameter** — shifts where the center sits
- **σ (sigma)** = standard deviation = **scale parameter** — controls how
  wide/narrow the bell is

```
Small σ  -> narrow, tall bell (data tightly clustered)
Large σ  -> wide, flat bell (data spread out)
```

Diagram (same mean, different σ):
```
        Dataset A (σ=5, narrow/tall)     Dataset B (σ=15, wide/flat)
              /\                              ___
             /  \                           _/   \_
            /    \                        _/       \_
        ___/      \___                  _/           \_
```
Both centered on the same mean, but A is tall & skinny, B is short & wide.

---

## 4. The Formula — Built Piece by Piece

```
f(x) = (1 / (σ√(2π))) × e^(-(x-μ)² / (2σ²))
```

**Piece 1 — `(x-μ)²`:** squared distance from the mean. Always positive
(squaring removes the sign). Punishes large distances harder than small
ones — e.g. distance 2 → 4, distance 4 → 16 (4x the distance-squared for
2x the distance). This is why the tails drop off fast.

**Piece 2 — `e^(-...)`:** exponential decay. At x=μ, the exponent is 0, so
`e^0 = 1` — this is the peak of the curve. As x moves away from μ, the
exponent grows more negative, and `e^(-big number)` shrinks toward 0.

**Piece 3 — `/(2σ²)`:** controls width. Large σ → division shrinks the
exponent's effect → curve doesn't drop as fast → wide/flat bell. Small σ →
division barely shrinks anything → curve drops fast → narrow/tall bell.

**Piece 4 — `1/(σ√2π)`:** normalizing constant. Doesn't shape the curve —
exists purely so the total area under the curve equals exactly 1 (the PDF
rule: total probability must sum to 1). Formal calculus proof of this
constant is available in the reference video linked below, but not
required for applied understanding.

**Sanity check — at x=μ exactly:**
```
(x-μ)² = 0² = 0
e^(-0/2σ²) = e^0 = 1   <- maximum possible value of the exponential piece
```
Confirms mathematically that the curve peaks exactly at the mean.

> Normal formula = shape (squared distance + exponential decay, controlled
> by σ) × normalizing constant (forces total area = 1).

---

## 5. The Empirical Rule (68-95-99.7)

For ANY Normal distribution, regardless of μ and σ:

```
68% of data falls within μ ± 1σ
95% of data falls within μ ± 2σ
99.7% of data falls within μ ± 3σ
```

**Worked example — exam scores, μ=70, σ=10:**
```
68% range: 70 ± 10  -> 60 to 80
95% range: 70 ± 20  -> 50 to 90
99.7% range: 70 ± 30 -> 40 to 100
```

**Common mistake made and caught:** initially used ±1σ (60-80) when asked
for the 95% range — mixed up which multiple of σ corresponds to which
percentage. The pattern to remember: 1σ→68%, 2σ→95%, 3σ→99.7% — each step
out captures noticeably more of the tail.

**Verified with scipy's exact CDF** (Task 3): the true value for ±1σ isn't
exactly 68%, it's **68.27%** — the "68-95-99.7" figures are commonly
rounded shorthand. Precise values: 68.27%, 95.45%, 99.73%.

```python
norm_dist = stats.norm(mean, std)
prob = norm_dist.cdf(upper) - norm_dist.cdf(lower)   # exact probability
```

**Practical use:** only ~0.3% of data lies beyond 3σ — this is why "3
sigma away" is a common outlier-flagging threshold in ML pipelines and
manufacturing quality control.

> Empirical rule = quick estimate tool. 1σ→68%, 2σ→95%, 3σ→99.7%. Exact
> values via CDF are close but not identical to these rounded figures.

---

## 6. Z-Scores

Answers: "how many standard deviations away from the mean is this value?"

```
z = (x - μ) / σ
```

**Worked example:** exam scores μ=70, σ=10, student scored x=85:
```
z = (85 - 70) / 10 = 1.5
```
Interpretation: 1.5 standard deviations above the mean.

**Comparing distance from average across two values:** compare `|z|`
(absolute value), not the raw z-score — sign only indicates direction
(above/below), not distance.

**Worked example (Task 4):** heights μ=170, σ=7.
```
184cm: z = (184-170)/7 = 2.0
159cm: z = (159-170)/7 = -1.5714
```
Comparing |2.0| vs |1.5714| → the 184cm person is further from average.

**Connection to empirical rule:** the empirical rule is literally
describing z-score ranges — z between -1 and +1 covers 68%, -2 to +2
covers 95%, -3 to +3 covers 99.7%.

**Why z-scores matter:** they let you compare values from completely
different distributions on the same standardized scale (e.g. comparing a
test scored out of 100 to one scored out of 800).

> z = (x-μ)/σ. Positive = above average, negative = below average.
> Compare |z| (not raw z) to determine which value is further from
> average, since sign only shows direction.

---

## 7. Uniform Distribution

Every value in a range `[a,b]` is **equally likely** — flat, not
bell-shaped. No value is more or less probable than another.

**Discrete Uniform example:** a fair die — each face has probability
exactly 1/6, all equal.

**Continuous Uniform formula:**
```
f(x) = 1 / (b - a)      for a <= x <= b
f(x) = 0                otherwise
```

**Why it looks like this:** the PDF rule requires total area = 1. A flat
rectangle's area = height × width. To make area = 1:
```
height × (b-a) = 1
height = 1/(b-a)
```

**Worked example (Task 5):** random number generator, uniform between 5
and 25.
```python
a, b = 5, 25
density = 1 / (b - a)   # 1/20 = 0.05
```
Verified against `scipy.stats.uniform(loc=a, scale=b-a).pdf(10)` →
matches exactly, 0.05.

**Mean and Variance:**
```
Mean = (a+b)/2       (just the midpoint)
Variance = (b-a)²/12
```
Confirmed manual mean (15.0) matches `uniform_dist.mean()` (15.0).

**scipy gotcha:** `stats.uniform` uses `loc` = starting point and `scale`
= width (not `loc=a, scale=b` directly) — must pass `scale=b-a`, not `b`.

> Uniform = every value in [a,b] equally likely. f(x) = 1/(b-a).
> Mean = midpoint (a+b)/2. Flat rectangle, not a bell — no "typical" value.

---

## 8. Normal vs Uniform — How to Tell Them Apart

The real distinguishing question: **does the data cluster around a
typical/average value (Normal), or is every outcome equally likely with
no typical value standing out (Uniform)?**

**Scenarios worked through (Task 6):**
- Bus arrival time within a fixed 20-minute unpredictable window →
  **Uniform** (any minute equally likely, no "typical" arrival minute)
- Adult human heights in a large population → **Normal** (heights cluster
  around a mean with a symmetric bell-shaped spread, most people close to
  average, extremes rare)
- Outcome of rolling a fair die → **Uniform** (each face equally likely,
  no "typical" face)

---

## 9. Why Normal Matters for ML

- **Regression** — assumes residuals (errors) are Normally distributed
  around 0; underlies valid confidence intervals and hypothesis tests on
  model coefficients
- **Gaussian Naive Bayes** — estimates μ and σ per feature per class, then
  plugs new data directly into the Normal PDF formula for likelihood
- **Neural network weight initialization** — weights often drawn from
  Normal(μ=0, small σ) (e.g. Xavier/He initialization) to prevent
  gradients from exploding or vanishing early in training
- **Anomaly detection** — flag data points with `|z| > 3` (beyond 3σ) as
  potential outliers — direct application of the empirical rule

---

## Mistakes I Made & Fixed Today

- Computed the 95% empirical rule range using ±1σ instead of ±2σ — gave
  60-80 (the 68% range) instead of the correct 50-90. Fixed by explicitly
  re-deriving each multiple of σ against its correct percentage.
- Verified the 68% approximation with `.cdf()` but didn't explicitly state
  the comparison the task asked for — printed the raw number (0.6827)
  without showing how it relates to 68%. Learned to make comparisons
  explicit (side-by-side print, computed difference, or a comment).
- Wrote the wrong z-score value (1.0 instead of 2.0) in an explanation
  comment despite the printed output being correct — a copy-paste slip.
  Also initially described each person's z-score separately instead of
  directly answering "who is further from average" via `|z|` comparison.
- Named a density variable generically as `x` in the Uniform task instead
  of `density` — not a bug, but reduces readability since `x` usually
  implies an input value, not a computed output.
- Left reasoning blank for why heights are Normal rather than Uniform —
  filled in by contrasting with the Uniform examples: heights cluster
  around a typical average, while Uniform scenarios have no typical value
  (every outcome equally likely).

---

## Resources Used

- "Normal Distribution Explained in Hindi | Statistics Series" —
  https://www.youtube.com/watch?v=2CGvLkj-V4Q — covered distribution
  shape/symmetry, mean=median=mode, and the location parameter (μ) vs
  scale parameter (σ) terminology
- "Normalization Constant for the Normal/Gaussian | Full Derivation with
  visualizations" — https://www.youtube.com/watch?v=u2q7YmwfcyU —
  optional calculus derivation of the `1/(σ√2π)` normalizing constant,
  kept as an advanced reference, not required for applied-level depth