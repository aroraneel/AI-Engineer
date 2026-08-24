# Phase 2 — Formulas by Day

A day-by-day list of every formula covered in Phase 2 (Probability &
Inference), with what each symbol stands for and a short explanation.

---

## Day 11 — Probability Fundamentals

### Addition Rule (mutually exclusive)
```
P(A or B) = P(A) + P(B)
```
| Symbol | Stands for |
|---|---|
| P(A or B) | probability that A OR B happens |
| P(A) | probability of event A |
| P(B) | probability of event B |

**What it measures:** the probability of at least one of two events
happening, when they can't both happen at the same time.

---

### Addition Rule (overlapping)
```
P(A or B) = P(A) + P(B) - P(A and B)
```
| Symbol | Stands for |
|---|---|
| P(A and B) | probability that BOTH A and B happen |

**What it measures:** same as above, but subtracts the overlap so it
isn't counted twice.

---

### Multiplication Rule (independent)
```
P(A and B) = P(A) × P(B)
```
**What it measures:** the probability that two independent events both
happen.

---

### Multiplication Rule (dependent)
```
P(A and B) = P(A) × P(B|A)
```
| Symbol | Stands for |
|---|---|
| P(B\|A) | probability of B, given that A already happened |

**What it measures:** the probability both events happen, when the
first event affects the probability of the second.

---

### Bernoulli PMF
```
P(X=1) = p        (success)
P(X=0) = 1 - p     (failure)
```
| Symbol | Stands for |
|---|---|
| P(X=1) | probability of success |
| p | probability of success on one trial |
| P(X=0) | probability of failure |

**What it measures:** the probability of each outcome in a single
trial with exactly two possible results.

---

## Day 12 — Binomial & Poisson Distributions

### Binomial PMF
```
P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
```
| Symbol | Stands for |
|---|---|
| P(X=k) | probability of exactly k successes |
| C(n,k) | number of ways to arrange k successes among n trials ("n choose k") |
| n | total number of trials |
| k | number of successes being asked about |
| p | probability of success on one trial |

**What it measures:** the probability of getting exactly k successes
out of a fixed number of independent trials.

---

### Binomial Mean & Variance
```
Mean = n × p
Variance = n × p × (1-p)
```
**What it measures:** the expected number of successes, and how much
that count is expected to vary.

---

### Poisson PMF
```
P(X=k) = (λ^k × e^(-λ)) / k!
```
| Symbol | Stands for |
|---|---|
| P(X=k) | probability of exactly k events |
| λ (lambda) | the average/expected rate of events in the interval |
| k | exact number of events being asked about |
| e | Euler's number (≈2.71828), a fixed constant |
| k! | k factorial |

**What it measures:** the probability of a specific count of events
occurring over a fixed interval, given an average rate.

---

### Poisson Mean & Variance
```
Mean = λ
Variance = λ
```
**What it measures:** both equal the rate λ — a distinctive property
of the Poisson distribution.

---

## Day 13 — Normal, Z-score & Uniform Distribution

### Normal (Gaussian) PDF
```
f(x) = (1 / (σ√(2π))) × e^(-(x-μ)² / (2σ²))
```
| Symbol | Stands for |
|---|---|
| f(x) | the probability density at value x |
| σ (sigma) | standard deviation (controls width) |
| μ (mu) | the mean (controls center) |
| π (pi) | the constant ≈3.14159 |
| e | Euler's number, a fixed constant |

**What it measures:** the density of a symmetric, bell-shaped
distribution at any given value x.

---

### Empirical Rule (68-95-99.7)
```
68% within μ ± 1σ
95% within μ ± 2σ
99.7% within μ ± 3σ
```
**What it measures:** how much data falls within 1, 2, or 3 standard
deviations of the mean, for Normally distributed data.

---

### Z-score
```
z = (x - μ) / σ
```
| Symbol | Stands for |
|---|---|
| z | the z-score (number of std devs from the mean) |
| x | the specific value being checked |
| μ | the mean |
| σ | the standard deviation |

**What it measures:** how many standard deviations a value is from
the mean.

---

### Uniform PDF
```
f(x) = 1 / (b - a)     for a ≤ x ≤ b
```
| Symbol | Stands for |
|---|---|
| f(x) | the density at value x |
| a | lower bound of the range |
| b | upper bound of the range |

**What it measures:** the constant density across a range where every
value is equally likely.

---

### Uniform Mean & Variance
```
Mean = (a + b) / 2
Variance = (b - a)² / 12
```
**What it measures:** the midpoint of the range, and how spread out
the values are.

---

## Day 14 — Skewed Distributions & Central Limit Theorem

### Power Law
```
y = x^(-a)
```
| Symbol | Stands for |
|---|---|
| y | frequency/probability |
| x | magnitude of the event |
| a | the power/exponent controlling the decay rate |

**What it measures:** how frequency drops off as magnitude increases
— large events are rare, small events are common.

---

### Standard Error
```
SE = σ / √n
```
| Symbol | Stands for |
|---|---|
| SE | standard error (std dev of sample means) |
| σ | population standard deviation |
| n | sample size |

**What it measures:** how much sample means are expected to vary from
the true population mean — shrinks as sample size grows.

---

## Day 15 — Estimation, Hypothesis Testing & p-values

*(No new formulas — this day introduced the conceptual framework: H0/H1,
point vs interval estimates, and the decision rule below, reused every
day after.)*

### Decision Rule
```
if p-value <= alpha:  reject H0
if p-value > alpha:   fail to reject H0
```
| Symbol | Stands for |
|---|---|
| alpha (α) | the significance level (commonly 0.05) |

**What it measures:** the threshold for deciding whether observed data
provides enough evidence against H0.

---

## Day 16 — Z-test, Student's t-distribution & t-test

### Z-test Statistic
```
z = (x̄ - μ) / (σ / √n)
```
| Symbol | Stands for |
|---|---|
| z | the z-test statistic |
| x̄ | sample mean |
| μ | population mean (claimed value, under H0) |
| σ | population standard deviation (must be KNOWN) |
| n | sample size |

**What it measures:** how many standard errors the sample mean is from
the claimed population mean.

---

### t-test Statistic
```
t = (x̄ - μ) / (s / √n)
```
| Symbol | Stands for |
|---|---|
| t | the t-test statistic |
| s | sample standard deviation (used when population σ is UNKNOWN) |

**What it measures:** same idea as the Z-test, but uses the sample's
own estimated spread instead of a known population value.

---

### Degrees of Freedom (t-distribution)
```
df = n - 1
```
**What it measures:** how much the t-distribution's shape depends on
sample size — higher df makes it converge toward Normal.

---

## Day 17 — Type I/II Errors, Bayes' Theorem & Confidence Intervals

### Bayes' Theorem
```
P(A|B) = [P(B|A) × P(A)] / P(B)
```
| Symbol | Stands for |
|---|---|
| P(A\|B) | posterior — probability of A given B happened |
| P(B\|A) | likelihood — probability of B given A happened |
| P(A) | prior — probability of A before any evidence |
| P(B) | overall probability of B happening |

**What it measures:** how to update a probability based on new evidence.

---

### Confidence Interval (known σ)
```
CI = x̄ ± (z* × (σ/√n))
```
| Symbol | Stands for |
|---|---|
| CI | the confidence interval range |
| x̄ | sample mean |
| z* | critical z-value for the confidence level (1.96 for 95%) |
| σ/√n | standard error |

**What it measures:** a range likely to contain the true population
parameter, at a stated confidence level.

---

## Day 18 — Chi-square Test & Goodness-of-Fit

### Chi-square Statistic
```
χ² = Σ [(Observed - Expected)² / Expected]
```
| Symbol | Stands for |
|---|---|
| χ² (chi-squared) | the chi-square test statistic |
| Σ | "sum of" |
| Observed | the actual count measured in each category |
| Expected | the count expected if H0 were true |

**What it measures:** how far observed category counts are from
expected counts, across all categories.

---

### Degrees of Freedom (chi-square)
```
df = number of categories - 1
```
**What it measures:** how many categories are "free to vary" once the
total is fixed.

---

## Day 19 — ANOVA

### F-statistic
```
F = between-group variance / within-group variance
```
| Symbol | Stands for |
|---|---|
| F | the F-statistic |
| between-group variance | variation among the group means |
| within-group variance | variation of individual points inside each group |

**What it measures:** whether group means differ more than ordinary
random scatter would explain.

---

## Day 20 — Capstone

*(No new formulas — this day applied every formula above to real
scenarios, using the decision framework to choose the right one.)*

---

## Quick Reference — All Phase 2 Formulas

| Day | Formula | What it measures |
|---|---|---|
| 11 | P(A or B) = P(A)+P(B) [-P(A and B)] | Addition rule |
| 11 | P(A and B) = P(A)×P(B) [×P(B\|A)] | Multiplication rule |
| 11 | P(X=1)=p, P(X=0)=1-p | Bernoulli PMF |
| 12 | P(X=k)=C(n,k)×p^k×(1-p)^(n-k) | Binomial PMF |
| 12 | P(X=k)=(λ^k×e^-λ)/k! | Poisson PMF |
| 13 | f(x)=(1/σ√2π)×e^(-(x-μ)²/2σ²) | Normal PDF |
| 13 | z=(x-μ)/σ | Z-score |
| 13 | f(x)=1/(b-a) | Uniform PDF |
| 14 | y=x^(-a) | Power law |
| 14 | SE=σ/√n | Standard error |
| 15 | p<=alpha -> reject H0 | Decision rule |
| 16 | z=(x̄-μ)/(σ/√n) | Z-test statistic |
| 16 | t=(x̄-μ)/(s/√n) | t-test statistic |
| 16 | df=n-1 | Degrees of freedom (t) |
| 17 | P(A\|B)=[P(B\|A)×P(A)]/P(B) | Bayes' theorem |
| 17 | CI=x̄±(z*×SE) | Confidence interval |
| 18 | χ²=Σ[(O-E)²/E] | Chi-square statistic |
| 18 | df=categories-1 | Degrees of freedom (chi-square) |
| 19 | F=between-group var/within-group var | F-statistic |
