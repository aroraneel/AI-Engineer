# Probability Distributions — Cheat Sheet

A quick reference covering the 9 most commonly used probability
distributions in statistics and machine learning.

---

## 1. Bernoulli Distribution

**What it models:** a single trial with exactly two outcomes (success/failure).

**Formula:**
```
P(X=1) = p        (success)
P(X=0) = 1-p      (failure)
```

**Parameters:** `p` (probability of success)

**Mean:** `p`   **Variance:** `p(1-p)`

**Real examples:** one coin flip, one email being spam or not, one customer churning or not.

**scipy:** `stats.bernoulli(p)`

**ML relevance:** foundation of binary classification — every classifier prediction IS a Bernoulli random variable.

---

## 2. Binomial Distribution

**What it models:** a fixed number of independent Bernoulli trials, counting successes.

**Formula:**
```
P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
```

**Parameters:** `n` (number of trials), `p` (probability of success per trial)

**Mean:** `n×p`   **Variance:** `n×p×(1-p)`

**Real examples:** number of heads in 10 coin flips, number of defective items in a batch of 50 parts.

**scipy:** `stats.binom(n, p)`

**Requirements:** fixed n, independent trials, only 2 outcomes per trial, same p every trial.

---

## 3. Poisson Distribution

**What it models:** count of events over a fixed interval (time/space), given an average rate. No fixed "n."

**Formula:**
```
P(X=k) = (λ^k × e^(-λ)) / k!
```

**Parameters:** `λ` (lambda, average rate)

**Mean:** `λ`   **Variance:** `λ` (both equal — distinctive property)

**Real examples:** customers arriving per hour, emails received per day, typos per page.

**scipy:** `stats.poisson(lam)`

**Binomial vs Poisson:** Binomial has a fixed number of trials; Poisson counts occurrences over a continuous interval with no fixed n — both require independence, but that alone doesn't distinguish them.

---

## 4. Normal (Gaussian) Distribution

**What it models:** continuous, symmetric, bell-shaped data clustering around a mean.

**Formula:**
```
f(x) = (1 / (σ√(2π))) × e^(-(x-μ)² / (2σ²))
```

**Parameters:** `μ` (mean, location), `σ` (standard deviation, scale)

**Mean:** `μ`   **Median:** `μ`   **Mode:** `μ` (all equal)

**Real examples:** height, exam scores, measurement errors.

**scipy:** `stats.norm(mean, std)`

**Empirical Rule (68-95-99.7):**
```
68% within μ ± 1σ
95% within μ ± 2σ
99.7% within μ ± 3σ
```

**Z-score:** `z = (x-μ)/σ` — how many std devs a value is from the mean. Compare `|z|` to judge distance from average.

**ML relevance:** regression residual assumptions, Gaussian Naive Bayes, neural net weight initialization, anomaly detection (|z|>3 = outlier).

---

## 5. Uniform Distribution

**What it models:** every value in a range `[a,b]` is equally likely — flat, not bell-shaped.

**Formula (continuous):**
```
f(x) = 1/(b-a)    for a ≤ x ≤ b
```

**Parameters:** `a` (lower bound), `b` (upper bound)

**Mean:** `(a+b)/2`   **Variance:** `(b-a)²/12`

**Real examples:** random number generators, bus arrival time within a scheduled window, fair die (discrete case).

**scipy:** `stats.uniform(loc=a, scale=b-a)` — note: scipy uses `scale=width`, not `scale=b`.

**Normal vs Uniform:** does data cluster around a typical value (Normal), or is every outcome equally likely with no typical value (Uniform)?

---

## 6. Log-normal Distribution

**What it models:** data whose LOG is normally distributed. Occurs when a variable is the *product* of many independent factors (vs. Normal, which arises from *sums*).

**Shape:** sharp peak near low values, long right tail, never negative.

**Real examples:** income, stock prices, file sizes, blood pressure.

**Key insight:** take the log of the data — if that looks Normal, the original data is log-normal.

---

## 7. Power Law Distribution

**What it models:** frequency is inversely proportional to magnitude — few large events, many small ones, at every scale.

**Formula:**
```
y = x^(-a)
```

**Real examples:** word frequency in language, city population sizes, website traffic.

**How to spot one:** appears as a straight line on a log-log plot.

---

## 8. Pareto Distribution

**What it models:** a specific, well-known power law — the "80/20 rule."

**Real examples:** 80% of revenue from 20% of customers, 80% of bugs from 20% of code, original context: income/wealth distribution.

**How to check:** plot log(x) vs log(y) — a straight line indicates Pareto.

**Practical warning (applies to log-normal/power law/Pareto):** don't blindly apply mean/std to this kind of data — a few extreme values badly skew the "average," making it a misleading summary.

---

## 9. Student's t-distribution

**What it models:** similar to Normal, but with "fatter tails" — used when working with SMALL sample sizes or when the population standard deviation is unknown (must estimate it from the sample).

**Parameters:** degrees of freedom (df, related to sample size) — as df increases, t-distribution approaches Normal.

**Real examples:** used in the t-test, for comparing sample means when you don't know the true population std.

**scipy:** `stats.t(df)`

---

## Quick Decision Guide — Which Distribution?

| Question | Distribution |
|---|---|
| One trial, 2 outcomes? | Bernoulli |
| Fixed n trials, counting successes? | Binomial |
| Counting events over time/space, no fixed n? | Poisson |
| Continuous, symmetric, clusters around a mean? | Normal |
| Every value equally likely in a range? | Uniform |
| Log of the data looks Normal? Product of many factors? | Log-normal |
| Frequency inversely proportional to magnitude, straight line on log-log plot? | Power law |
| Specific "80/20" pattern? | Pareto |
| Small sample, unknown population std? | Student's t |

---

## Mean vs Variance Quick Reference

| Distribution | Mean | Variance |
|---|---|---|
| Bernoulli | p | p(1-p) |
| Binomial | np | np(1-p) |
| Poisson | λ | λ |
| Normal | μ | σ² |
| Uniform | (a+b)/2 | (b-a)²/12 |
