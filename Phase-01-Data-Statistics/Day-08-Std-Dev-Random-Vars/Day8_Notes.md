# Day 8 — Standard Deviation Deep Dive; Variables & Random Variables — Notes

Topics covered: interpreting standard deviation (empirical rule), coefficient
of variation, variable types, random variables

---

## 1. The Empirical Rule (68-95-99.7 Rule)

For data that's roughly bell-shaped (normal distribution), standard
deviation tells you how data clusters around the mean:

- **~68%** of data falls within **1 standard deviation** of the mean
- **~95%** of data falls within **2 standard deviations** of the mean
- **~99.7%** of data falls within **3 standard deviations** of the mean

**Example:** test scores with mean = 70, std dev = 10.
```
68% of students scored between 60 and 80   (70 +/- 10)
95% of students scored between 50 and 90   (70 +/- 20)
99.7% of students scored between 40 and 100 (70 +/- 30)
```

If a student scored 95, that's more than 2 std devs above the mean — roughly
top 2.5% of the class, known instantly just from mean and std dev.

> Empirical rule: ~68% of data within 1 std dev of mean, ~95% within 2,
> ~99.7% within 3 (for roughly bell-shaped data). Lets you judge "how
> unusual" a value is just from mean and std dev.

**Verified on real data:** scores with mean=70.3, std=3.69 -> 68% range =
[66.61, 73.99] -> 13 of 20 actual scores (65%) fell inside, closely matching
the predicted ~68%.

---

## 2. Coefficient of Variation (CV)

Is a std dev of 10 "big" or "small"? Depends entirely on scale — 10 is huge
for heights in cm, tiny for salaries in dollars.

**CV solves this by expressing std dev as a percentage of the mean:**
```
CV = (std dev / mean) x 100%
```

This makes spread comparable across datasets with very different scales.

> CV = (std dev / mean) x 100%. Lets you compare "relative spread" across
> datasets with very different scales/units.

**Worked example:**
```
Class A: mean=50, std=5   -> CV = (5/50)*100  = 10%
Class B: mean=90, std=8   -> CV = (8/90)*100  = 8.89%
```
Class A has MORE relative variability, even though its raw std dev (5) is
smaller than Class B's (8) — because Class A's mean is also much smaller, so
the same spread represents a bigger fraction of the average.

---

## 3. Variable Types

**First question to always ask: is this a number I can do math with, or a
label/category?**

### Quantitative (numeric) variables
- **Discrete** — countable, specific values, can't be a fraction (number of
  children, number of emails, goals scored)
- **Continuous** — any value within a range, infinitely divisible (height,
  weight, temperature, exact time)

### Qualitative (categorical) variables
- **Nominal** — no natural order (colors, blood type, movie genre)
- **Ordinal** — has a natural order (t-shirt size, satisfaction rating,
  education level)

> Variables: Quantitative (discrete=countable whole numbers,
> continuous=any value in a range) vs Qualitative (nominal=no order,
> ordinal=has order).

**Common trap:** any variable that's a COUNT (emails per day, goals scored)
is discrete, NOT ordinal or nominal — it's easy to forget discrete/continuous
are even options and jump straight to nominal/ordinal for anything that
looks list-like. Always check "is this actually a number?" first.

**Worked classification set:**
```
Number of emails per day              -> Discrete   (countable number)
Exact temperature in Celsius          -> Continuous (any decimal value)
Movie genre                           -> Nominal    (no order)
Education level                       -> Ordinal    (High School<Bachelor's<Master's<PhD)
Number of goals scored                -> Discrete   (countable number)
```

---

## 4. Random Variables

A **random variable** is a variable whose value is the *numerical outcome*
of a random process — the exact value isn't known in advance, but the
possible values and their probabilities can be described.

**Key distinction from a regular variable:** a regular variable is just "a
thing that varies." A random variable specifically maps outcomes of
randomness to numbers.

**Example:** flip a coin 3 times, X = "number of heads." X can only be 0, 1,
2, or 3, each with a specific probability — X is the random variable.

### Discrete random variable
Countable set of specific values.
- Number of heads in 3 coin flips (0, 1, 2, or 3 only)
- Number of customers entering a store in an hour
- A die roll (1-6 only, nothing in between)

### Continuous random variable
Any value within a range, often infinitely many possible values.
- Exact website load time
- A person's exact height

> Random variable = numerical outcome of a random process, with values and
> probabilities attached. Discrete random variable = countable specific
> values. Continuous random variable = any value in a range.

**Important nuance:** "has a range" does NOT make something continuous. The
real test: can every possible value be listed out one by one (even if there
are several), or can it be absolutely anything (including infinite decimal
precision) within that range? A die roll has a range (1-6) but is still
DISCRETE, because only 6 exact values are possible — nothing in between.

**Simulated with code:** `np.random.randint(1, 7, size=10000)` simulating
10,000 fair die rolls -> observed mean 3.5048, essentially identical to the
theoretical mean of 3.5 ((1+2+3+4+5+6)/6). A hands-on preview of the Law of
Large Numbers: with enough random trials, the observed average converges
toward the true theoretical average.

---

## Quick Reference Cheat Sheet

```python
import numpy as np
import pandas as pd

# Empirical rule
mean, std = data.mean(), data.std()
range_68 = (mean - std, mean + std)
range_95 = (mean - 2*std, mean + 2*std)
range_997 = (mean - 3*std, mean + 3*std)

# Coefficient of variation
cv = (std / mean) * 100

# Simulating a discrete random variable (die roll)
rolls = np.random.randint(1, 7, size=10000)
pd.Series(rolls).value_counts()
```

---

## Mistakes I Made & Fixed Today

- Wrote `np.mean(scores, ddof=0)` — `ddof` only applies to `.std()`/`.var()`,
  not `.mean()`, since mean has no sample/population division distinction.
- Copy-paste bug: `np.mean(class_b)` instead of `np.std(class_b)` when
  computing standard deviation, producing a meaningless CV of exactly 100.0
  (mean divided by itself). Caught because the result didn't make sense
  given the context, then fixed and re-verified the conclusion.
- Forgot discrete/continuous were valid classification options at all,
  initially mislabeling count-based numeric variables (emails per day, goals
  scored) as ordinal/nominal. Fixed by applying a "number vs category" first
  check before choosing a specific subtype.

---

## Resources Used

- General statistics fundamentals (empirical rule, coefficient of variation,
  variable classification, random variables)