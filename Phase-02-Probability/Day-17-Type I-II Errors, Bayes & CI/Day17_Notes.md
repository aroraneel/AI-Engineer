# Day 17 — Type I/II Errors; Bayes' Theorem; Confidence Intervals — Notes

Topics covered: Type I and Type II errors; Bayes' theorem; confidence intervals
(manual formula, scipy, t-distribution for unknown population std)

---

## 1. Type I and Type II Errors

Every hypothesis test can go wrong in two different ways, since the truth is
never actually known — every decision is made under uncertainty.

### Definitions

- **Type I error** — a false positive: rejecting H0 when it is actually TRUE.
- **Type II error** — a false negative: failing to reject H0 when it is
  actually FALSE.

### Diagram — the 2x2 decision grid

```
                    H0 actually TRUE     H0 actually FALSE
Fail to reject H0   Correct (no error)   Type II error (missed detection)
Reject H0           Type I error         Correct (no error)
                     (false alarm)
```

### Real-world examples worked through (Task 1)

- Spam filter marks a legitimate email as spam → **Type I error**
  (H0 = "not spam" was true, wrongly rejected — false alarm)
- Spam filter lets real spam through → **Type II error**
  (H0 = "not spam" was false, failed to reject it — missed detection)
- Court finds an innocent person guilty → **Type I error**
  (H0 = "innocent" was true, wrongly rejected — false alarm)

### Connection to alpha

The probability of a Type I error is controlled by α (the significance
level from Day 15). Lowering α (e.g. 0.05 → 0.01) reduces Type I error
risk, but as a tradeoff, increases Type II error risk (more likely to
miss real effects) — a fundamental tradeoff in hypothesis testing.

> Type I = false positive = rejecting a TRUE H0. Type II = false negative
> = failing to reject a FALSE H0. α controls Type I error rate; lowering
> it raises Type II risk.

---

## 2. Bayes' Theorem

### The core idea

Updates a probability based on new evidence — connects two directions of
conditional probability that are easy to confuse: P(A|B) vs P(B|A).

### The formula

```
P(A|B) = [P(B|A) × P(A)] / P(B)
```

- `P(A|B)` = posterior — probability of A given B happened (what we want)
- `P(B|A)` = likelihood — probability of B given A happened
- `P(A)` = prior — probability of A before any evidence
- `P(B)` = overall probability of B happening

### Worked example — rare disease test (Task 2)

```
P(Disease) = 0.02              (2% prevalence -- the prior)
P(Positive|Disease) = 0.90     (90% test accuracy for sick people)
P(Positive|No Disease) = 0.05  (5% false positive rate)
```

**Step 1 — P(Positive), the overall probability of testing positive:**
```python
p_positive = (p_positive_given_disease * p_disease) + \
             (p_positive_given_no_disease * p_no_disease)
# = (0.90 * 0.02) + (0.05 * 0.98) = 0.018 + 0.049 = 0.067
```

**Step 2 — Apply Bayes' theorem:**
```python
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_positive
# = 0.018 / 0.067 ≈ 0.2687
```

### Why this is surprising — the 100,000-person breakdown

Imagining 100,000 people with these same percentages:
```
2,000 people actually sick (2%)
98,000 people healthy (98%)

Of the 2,000 sick: 90% test positive -> 1,800 TRUE positives
Of the 98,000 healthy: 5% test positive -> 4,900 FALSE positives

Total positives = 1,800 + 4,900 = 6,700
Fraction actually sick = 1,800 / 6,700 ≈ 0.2687  <- matches the formula exactly
```

**The insight:** even with "90% accuracy," the disease's rarity means the
healthy population is enormous — even a small 5% false-positive rate
applied to that huge group produces MORE false positives (4,900) than
true positives from the small sick group (1,800). A test's accuracy
percentage alone doesn't determine how trustworthy a single result is —
the base rate (prior) matters enormously.

### Connection to ML

Foundation of the **Naive Bayes classifier** — calculates the probability
of a class (e.g. "spam") given observed features (specific words), by
combining the prior probability of that class with the likelihood of
seeing those features within it.

> Bayes' theorem = P(A|B) = [P(B|A)×P(A)]/P(B). Test/evidence accuracy
> alone isn't enough to interpret a result — the prior (how common
> something actually is) matters enormously, especially for rare events.

---

## 3. Confidence Intervals

### What it is

A range of values, calculated from sample data, likely to contain the
true population parameter, stated with a confidence level (commonly 95%).

### What "95% confident" actually means

**NOT:** "95% chance the true value is in THIS interval" — the true
population mean is a fixed number, already either in or out once
calculated.

**Actually means:** if you repeated the sampling process many times and
built a CI each time, 95% of those intervals would contain the true
mean. A statement about the reliability of the METHOD, not a probability
about any single interval.

### The formula (known population std)

```
CI = x̄ ± (z* × (σ/√n))
```

- `x̄` = sample mean
- `z*` = critical z-value for confidence level (1.96 for 95%)
- `σ/√n` = standard error (Day 14)
- `z* × (σ/√n)` = margin of error

### Worked example — manual calculation (Task 3)

Sample of 60 packages, mean=2.5kg, population σ=0.4kg (known), 95% CI:

```python
n, std, sample_mean, z = 60, 0.4, 2.5, 1.96
standard_error = std / np.sqrt(n)          # ≈ 0.0516
margin_of_error = z * standard_error       # ≈ 0.1012
lower_bound = sample_mean - margin_of_error  # ≈ 2.399
upper_bound = sample_mean + margin_of_error  # ≈ 2.601
```

**Interpretation:** "we're 95% confident the true average weight of all
packages falls between 2.399kg and 2.601kg."

### With scipy (Task 4)

```python
CI_95 = stats.norm.interval(confidence=0.95, loc=sample_mean, scale=standard_error)
# (2.399, 2.601) -- matches manual calculation exactly

CI_99 = stats.norm.interval(confidence=0.99, loc=sample_mean, scale=standard_error)
# (2.367, 2.633) -- noticeably WIDER
```

**Width comparison:** 95% CI width ≈ 0.202. 99% CI width ≈ 0.266. Higher
confidence level requires a wider interval to be more certain of
capturing the true value — confirmed directly with real numbers.

### From raw sample data with unknown population std (Task 5)

When population σ is unknown (the realistic case) AND sample size is
small, use the t-distribution instead (connects directly to Day 16).

```python
reaction_times = np.array([0.42, 0.39, 0.45, 0.41, 0.38, 0.44, 0.40, 0.43])
n = 8
sample_mean = np.mean(reaction_times)
sample_std = np.std(reaction_times, ddof=1)   # ddof=1 for sample std, Day 7
standard_error = sample_std / np.sqrt(n)

CI_95 = stats.t.interval(confidence=0.95, df=n-1, loc=sample_mean, scale=standard_error)
```

**Why t-distribution here:** population variance is unknown AND sample
size is small (n=8 < 30) — both conditions from Day 16's Z-test vs
t-test decision rule point directly to using the t-distribution.

### Connection to hypothesis testing

A confidence interval and a hypothesis test are two views of the same
underlying math. If a CI does NOT include the H0 value, that's
equivalent to rejecting H0 at the corresponding significance level
(e.g., a 95% CI not containing 0, for a "no difference" test, matches
rejecting H0 at α=0.05).

> CI = range likely to contain the true population parameter, at a
> stated confidence level. CI = x̄ ± (z*×SE). 95% confident means the
> METHOD captures the true value 95% of the time across repeated
> sampling — not "95% chance for this one interval." Higher confidence
> = wider interval. Larger sample = narrower interval.

---

## Mistakes I Made & Fixed Today

- In the Bayes' theorem calculation, wrapped the result in square
  brackets (`[...]`), accidentally creating a one-item list instead of a
  plain number — `round()` failed since it expects a single number.
- In the confidence interval manual calculation, mistakenly used
  `confidence_interval = 95` (meant to represent "95%") in place of the
  actual sample mean (2.5) — produced nonsensical bounds around 95
  instead of around 2.5. Also had lower/upper bound formulas swapped
  (adding margin for lower bound, subtracting for upper, instead of the
  reverse).
- Used `z = 1.90` instead of the specified `z* = 1.96` — small precision
  typo, but would meaningfully shift the calculated interval.
- Left some written interpretation comments too generic (e.g. stating
  the general CI definition instead of the actual calculated numbers) —
  working on always including specific values when a task asks for a
  plain-English interpretation.

---

## Resources Used

- "Tutorial 19 - Type 1 And Type 2 Error In Statistics - Krish Naik" —
  https://www.youtube.com/watch?v=8BxVMGn3c3o
- "Naive Bayes Classifier Algorithm Theorem Explained in Detail in
  Hindi" — https://www.youtube.com/watch?v=HUlOkr16ZCc
- "How To Perform Hypothesis Testing - Confidence Interval | Z-test..."
  — https://www.youtube.com/watch?v=Ib5UUBYzvPw