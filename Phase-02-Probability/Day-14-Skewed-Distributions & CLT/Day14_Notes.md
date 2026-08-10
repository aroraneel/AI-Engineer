# Day 14 — Log-normal, Power law, Pareto Distributions; Central Limit Theorem — Notes

Topics covered: Log-normal distribution; Power law distribution; Pareto distribution;
Central Limit Theorem (standard error, sample mean simulation)

---

## Part 1: Skewed Distributions (light touch — recognize the shape)

### 1. Log-normal Distribution

If you take the **log** of a dataset and the result looks Normal (bell-shaped),
the original data is log-normal.

**Why it happens:** occurs when a variable is the *product* of many
independent factors — multiplication, not addition. (Sums of many things →
Normal, via CLT. Products of many things → Log-normal.)

**Real examples:** income distribution, stock prices, file sizes, blood
pressure, length of chess games, word counts in sentences.

**Shape:** sharp peak near low values, long tail stretching right. Can
never go negative (unlike Normal).

### 2. Power Law Distribution

```
y = x^(-a)
```

Frequency/probability is inversely proportional to magnitude — big events
are rare, small events are common.

**Real examples:** word frequency in language, city population sizes,
website traffic, earthquake magnitudes.

**How to spot one:** plot on a **log-log plot** (both axes logarithmic) —
a true power law shows up as a straight line.

### 3. Pareto Distribution

A specific, well-known type of power law — the **80/20 rule**: 80% of
effects come from 20% of causes.

**Real examples:** 80% of company revenue from 20% of customers, 20% of
code causing 80% of bugs, income/wealth distribution (where Pareto
originally found this pattern).

**How to check:** take log(x) and log(y), plot them against each other —
a straight line indicates Pareto.

### Diagram — comparing shapes

```
Normal (symmetric bell):        Log-normal (peak near low, long tail):
        /\                           /\
       /  \                         /  \_
      /    \                      _/     \___
  ___/      \___                _/           \______

Power law / Pareto (steep drop, long thin tail):
|\
| \
|  \___
|      \________________
```

### Practical takeaway

If you see a huge spike near zero with a long thin tail (income, city
sizes, followers, file sizes) — that's a signal for log-normal, power
law, or Pareto, NOT Normal. Applying mean/std blindly to this kind of
data gives misleading summaries, since a few extreme values dominate and
distort the "average."

**Worked example (Task 1):**
- File sizes on a computer → skewed (most tiny, a few huge) — Log-normal/
  Power law
- Adult resting heart rate → Normal (clusters symmetrically around a
  central value)
- Social media followers → Power law/Pareto (most users have few, a
  handful have millions — classic "few dominate" pattern)

---

## Part 2: Central Limit Theorem (CLT) — full depth

### The setup

Take any population — any shape at all (Uniform, Log-normal, Poisson,
even something chaotic). Then:
1. Take a random sample of size n (commonly n≥30) from that population
2. Calculate the mean of that sample
3. Repeat many times — sample again, calculate the mean again
4. Plot all the sample means

### The result

**The distribution of sample means always trends toward Normal,
regardless of the original population's shape, as long as the sample
size is reasonably large.**

### Dice example (makes it concrete)

Roll a single die many times: flat, Uniform — every number 1-6 equally
likely.

Roll 2 dice and add them: getting a 2 or 12 is rare (only 1 way each:
1+1, 6+6), but a 7 is common (many ways: 1+6, 2+5, 3+4...). The sum's
distribution is already curving toward bell-shaped.

Roll 3+ dice: even closer to Normal. Each additional die pushes the sum's
distribution closer to a bell curve — CLT happening visibly.

### The formula

For a population with mean `μ` and standard deviation `σ`, sample size `n`:

```
Mean of sample means = μ                    (same as population mean)
Standard deviation of sample means = σ/√n   ("standard error")
```

**Key insight:** as `n` grows, `σ/√n` shrinks — sample means cluster
tighter around the true population mean. Bigger samples give more
reliable estimates, mathematically guaranteed by CLT.

### Worked example — Task 2 (standard error)

Population: mean=50, std=30.
```python
se_36 = 30 / np.sqrt(36)    # = 5.0
se_100 = 30 / np.sqrt(100)  # = 3.0
```
As n increased from 36 to 100, standard error dropped from 5.0 to 3.0 —
confirms CLT: larger samples → smaller standard error → more precise
estimate of the population mean.

### Full simulation — Tasks 3, 4, 5

**Step 1 (Task 3):** built a deliberately skewed, non-Normal population
using an exponential distribution:
```python
population = np.random.exponential(scale=5, size=100000)
# mean ≈ 5.01, std ≈ 5.03
```
(Note: for exponential distributions, mean always equals std — a
distinctive property, similar to how Poisson's mean equals its variance.)

**Step 2 (Task 4):** took 1000 random samples of size 30 from this skewed
population, calculated the mean of each sample:
```python
sample_means = []
for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(sample.mean())
sample_means = np.array(sample_means)
# sample_means.mean() ≈ 4.98, sample_means.std() ≈ 0.885
```
The mean of 1000 sample means (4.98) landed very close to the true
population mean (5.01) — exactly as CLT predicts, even though the
original population (exponential) was heavily skewed, not Normal at all.

**Step 3 (Task 5):** verified the standard error formula against the
actual simulated spread:
```python
theoretical_se = population.std() / np.sqrt(30)   # ≈ 0.9129
# actual sample_means.std() ≈ 0.9193
```
Very close (difference of only ~0.006) — this confirms the `σ/√n`
formula accurately predicts the spread of sample means, regardless of
the original population's shape.

**Bug caught:** in Task 5, referenced `population.std()` without
recreating the `population` variable in that file — since each task file
runs independently (not sharing variables across separate files), the
population had to be regenerated at the top of Task 5's file too.

### Why CLT matters for the next 6 days (Days 15-20)

- **A/B testing** (comparing model versions, comparing designs) relies on
  CLT to make claims like "Model A is statistically significantly better
  than Model B"
- **Confidence intervals** ("model accuracy is 87% ± 2%") — that ± range
  comes directly from CLT/standard error math
- **Hypothesis testing** (Day 15 onward) is built entirely on this
  foundation — sample means behaving predictably (Normal-ish) is what
  makes p-values and significance testing valid at all

---

## Mistakes I Made & Fixed Today

- In Task 5, used `population.std()` without regenerating the
  `population` variable in that specific file — caused a `NameError`
  since variables don't carry over between separate task files. Fixed by
  adding the population generation line at the top of Task 5.
- In a couple of "compare" tasks (4c), explained the CLT concept
  correctly in words but didn't explicitly state the actual numbers being
  compared (4.98 vs 5.01) — same style issue flagged on Day 13's Task 3.
  Working on making numeric comparisons explicit rather than only
  conceptual.

---

## Resources Used

- "Log normal distribution | Math, Statistics for data science, machine
  learning" — https://www.youtube.com/watch?v=xtTX69JZ92w
- "Log Normal Distribution in Statistics" —
  https://www.youtube.com/watch?v=sPzPEeJ4OQ4
- "Central Limit Theorem - Dice Example" —
  https://www.youtube.com/watch?v=aUyk5V0dh3Y
- "Rolling 2 Dice: An Intuitive Explanation of The Central Limit Theorem"
  — https://www.youtube.com/watch?v=VZl7gkMbipk
- Interactive CLT dice simulator —
  https://math.bu.edu/people/rmagner/CLTdemo.html