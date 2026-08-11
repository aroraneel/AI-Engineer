# Day 15 — Estimation Theory; Hypothesis Testing Fundamentals; p-values — Notes

Topics covered: estimation theory (point vs interval estimates); hypothesis
testing fundamentals (H0/H1); p-values; decision rule; simulation

---

## 1. Estimation Theory

### The core problem it solves

You can rarely measure an entire population (every person's height, every
customer's satisfaction). Instead, you take a **sample** and use it to
estimate something about the population.

### Two types of estimates

**Point estimate** — a single number guess. Example: "the average
delivery time is 32 minutes" (calculated from a sample mean).

**Interval estimate** — a range, acknowledging uncertainty. Example: "the
true average delivery time is likely between 29-35 minutes." This is the
seed idea behind confidence intervals (formalized Day 17).

### Why a range is more honest

A sample mean is just one estimate — a different random sample would give
a slightly different mean. The **standard error** (σ/√n, from Day 14's
CLT lesson) tells you exactly how much an estimate might wobble. A point
estimate hides that uncertainty; an interval estimate shows it.

> Estimation theory = using sample data to estimate population
> parameters. Point estimate = single number. Interval estimate = range,
> accounts for uncertainty (built from standard error).

---

## 2. Hypothesis Testing Fundamentals

### The core idea

A formal way to answer: "is this difference/effect I'm seeing in my data
real, or could it just be random chance?"

### The two hypotheses

- **Null Hypothesis (H0)** — the default assumption of "no effect" or "no
  difference." What you assume is true unless the data proves otherwise.
- **Alternative Hypothesis (H1)** — the claim that there IS a real effect
  or difference.

**Worked example (Task 2) — drug trial:**
```
H0: the new drug does not lower blood pressure compared to placebo
    (no difference between the two groups)
H1: the new drug DOES lower blood pressure compared to placebo
    (a real, significant difference exists)
```

### The logic of the test

You don't try to prove H1 directly. Instead:
1. Assume H0 is true
2. Collect data
3. Ask: "if H0 really were true, how likely would it be to see data this
   extreme just by random chance?"
4. If that likelihood is very low, conclude H0 is probably wrong, and
   reject it in favor of H1

This calculated likelihood is exactly the **p-value**.

---

## 3. p-values

### The definition

The probability of obtaining test results at least as extreme as the
results actually observed, under the assumption that the null hypothesis
is correct.

**In plain English:** "assuming nothing special is happening (H0 true),
what's the chance I'd see a result this surprising just by random luck?"

- Small p-value → unlikely under H0 → strong evidence AGAINST H0 → reject
- Large p-value → ordinary/expected under H0 → not enough evidence to reject

### Diagram — visualizing the p-value

A bell curve represents the distribution of outcomes IF H0 were true,
centered on "no effect." The observed value from real data is marked to
the right of center. The **shaded area** beyond that point = the p-value
— the probability of getting a result this extreme or more, under H0.

```
         bell curve = outcomes under H0
              /\
             /  \
            /    \_______  <- shaded region = p-value
       ____/              \________
                    ^
              observed value
```

Further right the observed value sits → smaller shaded area → smaller
p-value → stronger evidence against H0.

### The significance level (alpha) — decision threshold

A common choice is α=0.05 — a 5% risk of a wrong decision.

**Decision rule:**
```
if p-value <= alpha:  reject H0        (statistically significant)
if p-value > alpha:   fail to reject H0 (not enough evidence)
```

**Boundary case (Task 3c):** p-value = 0.05 exactly, with α=0.05 →
**reject H0**. Since the rule uses `<=`, not strictly `<`, landing
exactly on alpha counts as reject by convention.

### Fisher's tea-tasting story

A colleague claimed she could tell whether milk was poured into a cup
before or after the tea, just by tasting. Fisher tested her, and
calculated the probability of her getting those results by random
guessing was about 1.4%. Because that probability was low, they leaned
toward believing she genuinely had the skill rather than it being
coincidence. Fisher's traditional p ≤ 0.05 threshold comes from this
reasoning.

### Important misconception to avoid

A p-value greater than alpha does NOT prove the null hypothesis is true
— it just means there isn't enough evidence to reject it based on the
current data. "Fail to reject H0" ≠ "H0 is proven true."

### Why this matters for ML

Comparing models (testing if a new model's accuracy is significantly
better than an old model's) and feature selection (testing if a
predictor variable has a statistically significant relationship with the
target).

---

## 4. Simulating a p-value (Task 4) — building real intuition

Instead of using a formula, estimated a p-value directly through
simulation — this makes the definition concrete rather than abstract.

**Scenario:** suspect a coin is biased toward heads. Flipped it 100
times, got 62 heads. H0: the coin is fair (p=0.5).

```python
# Simulate 10,000 experiments of flipping a FAIR coin 100 times each
simulations = np.random.binomial(n=100, p=0.5, size=10000)

# What fraction of those 10,000 fair-coin experiments produced 62+ heads?
p_value = np.mean(simulations >= 62)
# result: p_value ≈ 0.0099
```

**Interpretation:** if the coin were truly fair, getting 62 or more heads
out of 100 flips would only happen by random chance about 1% of the time
— rare enough that "fair coin" is no longer a convincing explanation.
Since 0.0099 ≤ 0.05, reject H0 — strong evidence the coin is biased
toward heads.

**This directly demonstrates what a p-value IS:** literally the fraction
of simulated fair-coin experiments that were as extreme as (or more
extreme than) what was actually observed. No formula needed to see the
concept — it's just counting outcomes.

---

## 5. Standard Error from Real Data (Task 5)

Connects directly to Day 14's CLT lesson. Given a sample of 40 customer
satisfaction scores:

```python
sample_size = 40
mean = scores.mean()                          # point estimate
sample_std = scores.std(ddof=1)                # ddof=1 = n-1, sample std
standard_error = sample_std / np.sqrt(sample_size)
```

`ddof=1` matters here — matches the Day 7 lesson on sample vs population
variance (using n-1 for sample statistics, since sample variance without
this correction tends to underestimate true population variance).

**Result:** mean ≈ 7.475, standard error ≈ 0.1717 — a small standard
error here suggests the sample mean is a fairly precise estimate of the
true population average satisfaction score.

---

## Mistakes I Made & Fixed Today

- Used `if (p_value <= alpha) is True:` instead of the simpler
  `if p_value <= alpha:` — a comparison already evaluates to True/False,
  making the extra `is True` redundant.
- Wrote a comment concluding "fail to reject H0" that directly
  contradicted the actual printed output ("reject H0") — caught by
  cross-checking the written conclusion against the real result.
- Left the plain-English interpretation blank after correctly deciding
  "reject H0" in the simulation task — code was right, but didn't yet
  explain what that meant about the coin (likely biased) or why (only
  ~1% chance of 62+ heads under a fair coin).
- Used `sqrt()` instead of `np.sqrt()` — caused a `NameError`, since
  `sqrt` isn't a built-in Python function without importing it (either
  from `math` or, as done throughout this project, via NumPy).
- Computed the point estimate (mean) but forgot to print it — only
  printed standard error initially, missing part of what the task asked
  for.

---

## Resources Used

- "Tutorial 14 - What Is Hypothesis Testing Explained In Hindi | Krish
  Naik" — https://www.youtube.com/watch?v=pZ1d32ar_iY
- "Hypothesis Testing Explained with Solved Numerical in Hindi | Machine
  Learning Course" — https://www.youtube.com/watch?v=tyoTXLdTpC4