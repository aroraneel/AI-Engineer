# Day 11 — Probability Fundamentals; PMF/PDF/CDF; Bernoulli Distribution — Notes

Topics covered: addition rule; multiplication rule; PMF (simulated vs theoretical);
CDF (simulated vs theoretical); Bernoulli distribution

---

## 1. Addition Rule — P(A or B)

### Mutually Exclusive Events (cannot both happen at once)

```
P(A or B) = P(A) + P(B)
```

**Example:** rolling a fair die, P(1 or 6):
```
P(1) = 1/6
P(6) = 1/6
P(1 or 6) = 1/6 + 1/6 = 2/6 = 1/3 ≈ 0.3333
```

### Overlapping Events (can both happen at once)

```
P(A or B) = P(A) + P(B) - P(A and B)
```

We subtract the overlap because otherwise it gets counted twice.

**Example:** drawing a card that is a Queen OR a Spade:
```
P(Queen) = 4/52
P(Spade) = 13/52
P(Queen and Spade) = 1/52   (the Queen of Spades)
P(Queen or Spade) = 4/52 + 13/52 - 1/52 = 16/52 ≈ 0.3077
```

> Addition rule: mutually exclusive events → just add. Overlapping events →
> add then subtract the intersection to avoid double-counting.

---

## 2. Multiplication Rule — P(A and B)

For **independent events** (one doesn't affect the other):

```
P(A and B) = P(A) × P(B)
```

Extends to more than 2 events by chaining the multiplication:

**Example — coin flipped 3 times, all heads:**
```
P(heads) = 0.5
P(heads and heads and heads) = 0.5 × 0.5 × 0.5 = 0.125
```

Same idea using exponents when the probability repeats: `p ** n`

**Example — die rolled twice, both times a 6:**
```
P(6) = 1/6
P(6 and 6) = 1/6 × 1/6 = 1/36 ≈ 0.0278
```

> Multiplication rule: for independent events, multiply the individual
> probabilities together. Repeating the same probability n times = `p ** n`.

---

## 3. PMF — Simulated vs Theoretical

The PMF gives the exact probability of each value for a **discrete**
random variable. Rather than just trusting the formula, this was verified
by simulation:

```python
rolls = np.random.randint(1, 7, size=100000)   # 100,000 simulated die rolls
observed = np.bincount(rolls)[1:] / 100000     # observed probability per value
theoretical = np.array([1/6] * 6)              # true probability per value
```

**Key gotcha:** `np.random.randint(low, high)` treats `high` as
**exclusive** — so `randint(1, 7)` correctly generates values 1 through 6
(not 1 through 7).

**Key gotcha:** `np.bincount(rolls)` counts starting from index 0. Since
die values start at 1, this produces a 7-element array where index 0 is
always 0 (nothing rolled a "0"). Slicing with `[1:]` removes that useless
leading zero and aligns the array with values 1-6.

**Result observed (one run):**
```
observed:    [0.1676 0.167  0.1668 0.1673 0.1648 0.1666]
theoretical: [0.1667 0.1667 0.1667 0.1667 0.1667 0.1667]
```

Every observed value is close to but not exactly 0.1667 — this is the
**Law of Large Numbers**: the more times a random experiment repeats, the
closer the observed results converge to the true theoretical probability.

> PMF = for discrete variables, exact probability per value. Simulating
> confirms theory: `randint(low, high)` is high-exclusive, and
> `bincount()` needs slicing `[1:]` when values start at 1, not 0.

---

## 4. CDF — Simulated vs Theoretical

The CDF answers: what is P(X ≤ x)? Works for discrete and continuous
variables. Verified the same simulation-first way:

```python
rolls = np.random.randint(1, 7, size=100000)      # full die, 1-6
observed_cdf_3 = np.sum(rolls <= 3) / 100000       # proportion <= 3
theoretical_cdf_3 = 3/6                            # = 0.5
```

**Key idea:** `rolls <= 3` creates a boolean array (`True`/`False` per
roll). `np.sum()` on a boolean array works because Python treats `True`
as 1 and `False` as 0 — so summing counts how many rolls satisfied the
condition.

**Mistake caught during this task:** the die was originally simulated
with `np.random.randint(1, 4, size=100000)` — which only generates values
1, 2, 3. Every single roll would then automatically satisfy "≤ 3,"
making the result trivially 100% instead of measuring anything real.
Fixed by simulating the **full die range** `(1, 7)` first, then filtering
for `<= 3` afterward.

**Result observed (one run):**
```
observed:     0.4981
theoretical:  0.5
```

> CDF(x) = P(X ≤ x). To simulate: generate the FULL range of outcomes
> first, then use a boolean mask + `np.sum()` to count how many satisfy
> the condition. Don't restrict the simulation range itself — that
> answers a different question.

---

## 5. Bernoulli Distribution

Models a single trial with exactly two outcomes: success (1) or
failure (0).

```python
from scipy import stats

bernoulli_dist = stats.bernoulli(0.7)   # P(success) = 0.7

bernoulli_dist.pmf(1)   # 0.7   -> P(success)
bernoulli_dist.pmf(0)   # 0.3   -> P(failure)

draws = bernoulli_dist.rvs(size=10000)  # simulate 10,000 draws
success_fraction = np.mean(draws)       # fraction that were 1
```

**Why `.mean()` works to get the success fraction:** since draws are
only ever 0 or 1, averaging them = (number of 1s) / (total draws), which
is exactly the observed proportion of successes. No manual counting
needed.

**Result observed (one run):**
```
P(success) = 0.7
P(failure) = 0.30000000000000004   (floating point representation, not an error)
Simulated success fraction = 0.7015
```

**Why this matters for ML:** Bernoulli isn't just a concept that helps
explain binary classification — it IS what the model is estimating.
When a classifier outputs "80% chance of spam," it is literally
estimating the parameter `p` of a Bernoulli distribution for that one
input. Every single prediction is its own Bernoulli random variable with
its own `p`. This is the direct mathematical foundation of logistic
regression, covered formally in Phase 4.

> Bernoulli = single trial, two outcomes. `p` = P(success), `1-p` =
> P(failure). `.mean()` of many draws converges to `p` (Law of Large
> Numbers again). Classifiers don't just relate to Bernoulli — they
> estimate its parameter directly.

---

## Mistakes I Made & Fixed Today

- `import scipy as stats` instead of `from scipy import stats` — imports
  the wrong thing entirely; only didn't error because no `stats.`
  function was called in that particular task, but would break
  immediately once one was.
- `np.bincount(rolls)` indexing — forgot it starts counting from 0, so a
  1-6 value array produces a misleading 7-element result with an
  always-empty leading zero. Needed `[1:]` to align it correctly.
- Restricted the die roll range for the CDF task
  (`np.random.randint(1, 4, ...)`) instead of simulating the full die and
  then filtering — this silently guaranteed a meaningless 100% result
  instead of actually testing anything.
- Copied over the wrong shape of `theoretical` variable from the PMF task
  (an array of 6 values) into the CDF task, where a single number
  (0.5) was needed instead.
- Defined variables for individual-event probabilities but didn't reuse
  them in the multiplication rule task — fixed by using `** n` on the
  base variable instead of hardcoding repeated multiplication.

---

## Resources Used

- Practice file built around addition rule, multiplication rule, PMF/CDF
  simulation vs theory, and Bernoulli distribution (self-guided,
  questions-only format, checked task-by-task)
