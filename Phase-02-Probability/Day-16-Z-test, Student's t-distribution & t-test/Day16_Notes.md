# Day 16 — Z-test; Student's t-distribution and t-test; Z-test vs t-test — Notes

Topics covered: Z-test; Student's t-distribution; one-sample and two-sample
t-tests; Z-test vs t-test decision rule

---

## 1. The Z-test

### What it does

Tests whether a sample mean is significantly different from a known
population mean — using the Z-score concept from Day 13, now applied
formally as a hypothesis test.

### The formula

```
z = (x̄ - μ) / (σ/√n)
```

- `x̄` = sample mean
- `μ` = population mean (under H0)
- `σ` = population standard deviation (must be **known**)
- `n` = sample size
- `σ/√n` = standard error (Day 14)

This is the Z-score formula from Day 13, except the denominator now uses
standard error instead of raw σ, since we're testing a sample *mean*
(which itself has variability, per CLT) rather than a single raw value.

### The critical requirement

**Z-test requires knowing the true population standard deviation (σ).**
This is a major real-world limitation — you almost never actually know
the true population σ; you typically only have your sample.

### Worked example (Task 1 & 2)

Factory claims light bulbs last 1200 hours on average, population σ=80
hours (known). Sample of 40 bulbs averages 1180 hours.

```python
sample_mean, pop_mean, pop_std, n = 1180, 1200, 80, 40
z = (sample_mean - pop_mean) / (pop_std / np.sqrt(n))
# z ≈ -1.5811
```

Negative z makes sense — the sample mean (1180) is below the claimed
population mean (1200).

**Converting z to a p-value (two-tailed):**
```python
p_value = 2 * (1 - stats.norm.cdf(abs(z)))
# p_value ≈ 0.1138
```

Since 0.1138 > 0.05 → **fail to reject H0**. There isn't enough evidence
to conclude the factory's 1200-hour claim is wrong — a sample averaging
1180 could plausibly happen just from random sampling variation, even if
the true average really is 1200.

---

## 2. Student's t-distribution

### The problem Z-test can't handle

In real life, the population σ is rarely known. You usually only have
your **sample's** standard deviation — which is itself just an estimate,
and with a small sample, that estimate can be unreliable.

### Intuition — why "extra caution" is needed

Imagine estimating the average height of students in a city using only
12 randomly measured students. By chance, you might pick an unusually
tall or short group — your estimated spread (`s`) from those 12 could be
off from the true city-wide spread. With only a small sample, there's
more room for that estimate to be wrong.

The t-distribution builds in **extra caution** for this uncertainty — it
deliberately makes the range of "expected" outcomes wider than a true
Normal distribution would, by giving more probability to extreme values.

### Shape comparison (diagram)

Both Normal and t-distribution are symmetric bell shapes with the same
center. The t-distribution has a slightly lower peak and **fatter tails**
— more probability sits further from the center, reflecting the added
uncertainty of estimating spread from limited data.

```
Normal (thin tails):          t-distribution (fatter tails):
        /\                            /\
       /  \                          /  \
      /    \                        /    \
  ___/      \___                __/        \__
                              (wider, more area in tails)
```

### Degrees of freedom (df)

`df = n - 1` (same n-1 adjustment as Day 7's sample variance lesson).
As df increases (bigger sample), the t-distribution's tails shrink and
it converges toward Normal — this is why Z-test and t-test results
become very similar for large samples.

### The t-test formula

```
t = (x̄ - μ) / (s/√n)
```

Identical structure to the Z-test formula, but `s` (sample standard
deviation, estimated) replaces `σ` (population standard deviation,
known) — that's the entire difference in the formula itself. The
*distribution* used to interpret the result differs (t-distribution
instead of Normal), accounting for the extra uncertainty.

### One-sample t-test (Task 3)

Nutritionist claims average calorie count is 250. Sample of 10 bars,
population σ unknown.

```python
t_statistic, p_value = stats.ttest_1samp(sample_bars, popmean=250)
# t_statistic ≈ 0.3919, p_value ≈ 0.7043
```

Since 0.7043 > 0.05 → fail to reject H0. No evidence the 250-calorie
claim is wrong.

### Two-sample t-test (Task 4)

Comparing average time-on-page between two independent website designs.

```python
t_statistic, p_value = stats.ttest_ind(design_a, design_b)
# t_statistic ≈ -8.567, p_value ≈ 9.116e-08
```

**Reading scientific notation:** `9.116e-08` means move the decimal
point 8 places left: `0.00000009116` — an extremely tiny number, not
literally "9.1160" (which wouldn't even be a valid probability, since
p-values only range 0 to 1).

Since this p-value is far less than 0.05 → reject H0. Strong evidence
that Design A has a genuinely different average time-on-page than
Design B.

---

## 3. Z-test vs t-test — Decision Rule

| | Z-test | t-test |
|---|---|---|
| Population σ known? | Yes | No (estimated from sample) |
| Sample size | Large (typically n≥30) | Small (n<30) OR σ unknown |
| Distribution used | Normal | Student's t (fatter tails) |
| Formula | `(x̄-μ)/(σ/√n)` | `(x̄-μ)/(s/√n)` |

**The practical decision rule:** if you know the true population σ →
Z-test. If you don't know it (the common real-world case, since a
sample always has *some* calculable std, but that's not the same as
knowing the *population's* true std) → t-test, especially with small
samples.

**Scenarios worked through (Task 5):**
- n=500, population σ known from historical data → **Z-test**
- n=8, population σ unknown → **t-test**
- n=15, testing a new drug with no historical population variance data
  → **t-test** (unknown population σ, reinforced by small sample size)

**Key distinguishing detail:** the deciding factor is specifically
whether the *population's true* standard deviation is known — not
whether *any* standard deviation can be calculated (a sample always
produces its own std, but that's an estimate, not the true population
value).

---

## Mistakes I Made & Fixed Today

- In the Z-test manual calculation, mistakenly set `n = 1200` (actually
  the population mean) instead of `n = 40` (the real sample size) — a
  variable naming mix-up that would have completely broken the formula's
  denominator (`√1200` vs `√40` are very different numbers).
- In a t-test decision-rule check, wrote `if t_statistic <= p_value:`
  instead of the correct `if p_value <= alpha:` — an entirely wrong
  comparison, caught by manually checking the real printed numbers
  against what the decision *should* have been.
- Misread scipy's scientific notation output (`9.116e-08`) as literally
  "9.1160" in a written comment — actually represents an extremely small
  number (~0.0000000912). Learned to convert `e-XX` notation by moving
  the decimal point left by that many places.
- Used a hyphen in a variable name (`t-statistic`), which Python
  interprets as subtraction rather than a valid identifier — needed an
  underscore instead (`t_statistic`).
- Reasoned about Z-test vs t-test using vague language ("there is a std"
  / "no std") rather than the precise distinguishing factor — whether
  the population's TRUE standard deviation specifically is known,
  since a sample always has some calculable std regardless.

---

## Resources Used

- "Student t Distribution in Hindi Part 1 | Properties of t Distribution
  | When to use t test and z test" —
  https://www.youtube.com/watch?v=TIc9Sj5Mx4c
- "Z-Statistics vs. T-Statistics EXPLAINED in 4 Minutes" —
  https://www.youtube.com/watch?v=DEkPZv5ppHI