# Day 12 — Binomial Distribution & Poisson Distribution — Notes

Topics covered: Binomial distribution (formula, mean/variance, scipy); P(at least k)
via CDF complement rule; Poisson distribution (formula, mean/variance, scipy);
identifying Binomial vs Poisson scenarios

---

## 1. The Binomial Distribution — "repeated Bernoulli trials"

Bernoulli (Day 11) = one trial, two outcomes. **Binomial = a fixed number of
independent Bernoulli trials, counting how many were successes.**

**Requirements (all 4 must hold):**
1. A fixed number of trials, `n`
2. Each trial is independent
3. Each trial has only two outcomes (success/failure)
4. Same probability of success `p`, every trial

**Formula:**

```
P(X = k) = C(n, k) × p^k × (1-p)^(n-k)
```

- `n` = total trials
- `k` = number of successes asked about
- `p` = probability of success on one trial
- `C(n, k)` = "n choose k" = number of arrangements = `n! / (k! × (n-k)!)`

### Breaking the formula into 3 pieces

**Piece 1 — `C(n,k)`: how many arrangements give this count?**

Example: `C(4,2)` — out of 4 coin flips, how many arrangements have exactly
2 heads? Listed by hand:
```
HHTT, HTHT, HTTH, THHT, THTH, TTHH   -> 6 arrangements
```
Formula check: `4! / (2! × 2!) = 24 / 4 = 6` — matches.

**Piece 2 — `p^k`: probability of getting the successes wanted**
```
p^k = 0.5^2 = 0.25
```

**Piece 3 — `(1-p)^(n-k)`: probability of getting the failures wanted**
```
(1-p)^(n-k) = 0.5^2 = 0.25
```

**Multiply all 3 together:**
```
P(X=2) = 6 × 0.25 × 0.25 = 0.375
```

### Factorial (`!`) and exponent (`^` / `**`) refresher

`n!` = multiply n by every whole number below it down to 1:
```
4! = 4 × 3 × 2 × 1 = 24
3! = 3 × 2 × 1 = 6
```

`a^b` = multiply a by itself, b times (in Python: `a ** b`):
```
0.5^2 = 0.5 × 0.5 = 0.25
0.5^3 = 0.5 × 0.5 × 0.5 = 0.125
```

### Worked example — Task 1/2

Biased coin, P(heads)=0.6, flipped 8 times. P(exactly 5 heads)?

```python
n, k, p = 8, 5, 0.6
combination = math.comb(n, k)        # 56
p_success = p ** k                   # 0.6^5 = 0.07776
p_failure = (1 - p) ** (n - k)       # 0.4^3 = 0.064

P(X=5) = 56 × 0.07776 × 0.064 ≈ 0.2787
```

Verified with `scipy.stats.binom(8, 0.6).pmf(5)` → matches exactly, 0.2787.

### Mean and Variance shortcuts

```
Mean = n × p
Variance = n × p × (1-p)
```

For n=8, p=0.6: mean = 4.8, variance = 1.92 — both confirmed against
`.mean()` and `.var()`.

> Binomial = n independent Bernoulli trials, count of successes.
> P(X=k) = C(n,k) × p^k × (1-p)^(n-k). Mean = n×p, Variance = n×p×(1-p).

---

## 2. P(at least k) — the Complement Rule

Calculating P(X ≥ k) directly means adding P(k) + P(k+1) + ... + P(n) —
multiple separate calculations. There's a shortcut.

**The logic:** all possible outcomes sum to 1:
```
P(X=0) + P(X=1) + ... + P(X=n) = 1
```

Split into two groups — everything below k, and everything k and above:
```
[P(X=0) + ... + P(X=k-1)]  +  [P(X=k) + ... + P(X=n)]  =  1
        (this is CDF(k-1))          (this is what we want)
```

So:
```
P(X >= k) = 1 - P(X <= k-1) = 1 - CDF(k-1)
```

### Worked example — Task 3

n=8, p=0.6. P(at least 6 heads)?

```python
n, p = 8, 0.6
k = 6
binomial = stats.binom(n, p)
p_at_least_6 = 1 - binomial.cdf(k - 1)   # 1 - CDF(5)
# result ≈ 0.3154
```

**Design choice worth noting:** using `k - 1` instead of hardcoding the
number `5` directly is better practice — it's self-documenting (shows the
relationship between k and the CDF cutoff) and stays correct automatically
if k changes later. Hardcoding `5` would silently break if k were changed
without also updating the hardcoded number — a classic "magic number" bug.

> Complement rule: P(X >= k) = 1 - CDF(k-1). Fewer calculations than
> summing every individual probability from k to n. Prefer `k-1` over a
> hardcoded number for flexibility and clarity.

---

## 3. The Poisson Distribution — "counting rare events over a fixed interval"

Poisson answers a different question than Binomial: not "out of n fixed
trials, how many succeed," but **"how many times does an event happen in
a fixed window of time or space, given events happen randomly at a known
average rate?"**

**Requirements:**
1. Events happen independently of each other
2. Events happen at a known average rate, `λ` (lambda), over an interval
3. No fixed "number of trials" — counting occurrences over continuous
   time/space instead
4. Two events essentially can't happen at the exact same instant

**Real examples:** customers arriving per hour, emails received per day,
typos per page, server crashes per month.

**Formula:**

```
P(X = k) = (λ^k × e^(-λ)) / k!
```

- `λ` = average/expected number of events in the interval
- `k` = exact number of events asked about
- `e` ≈ 2.71828 (Euler's number, a fixed constant)
- `k!` = factorial of k

### Worked example — Task 4/5

Website receives on average λ=3 errors/day. P(exactly 5 errors in a day)?

```python
lam, k = 3, 5
lambda_power = lam ** k          # 3^5 = 243
e_term = math.exp(-lam)          # e^(-3) ≈ 0.0498
k_factorial = math.factorial(k)  # 5! = 120

P(X=5) = (243 × 0.0498) / 120 ≈ 0.1008
```

Verified with `scipy.stats.poisson(3).pmf(5)` → matches exactly, 0.1008.

### Mean and Variance

```
Mean = λ
Variance = λ
```

Both equal λ exactly — confirmed: mean=3.0, variance=3.0. This is a
distinctive property of Poisson (unlike Binomial, where mean and variance
are different formulas).

> Poisson = counts of rare/random events over a fixed interval, given an
> average rate λ. P(X=k) = (λ^k × e^(-λ)) / k!. Mean = Variance = λ.
> No fixed "n trials" like Binomial has.

---

## 4. Binomial vs Poisson — How to Tell Them Apart

| | Binomial | Poisson |
|---|---|---|
| Use when | Fixed number of trials (n) | No fixed n, just a rate (λ) over time/space |
| Example | Flip a coin 10 times | Count calls received per hour |
| Parameters | n and p | just λ |
| Mean | n×p | λ |
| Variance | n×p×(1-p) | λ |

**Important distinction that's easy to get wrong:** independence alone
does NOT separate the two — both distributions require independent
events. The real question is whether there's a **fixed number of trials**
you're counting successes out of (Binomial), or you're **counting
occurrences over a continuous interval based on a rate** with no fixed n
(Poisson).

**Scenarios worked through (Task 6):**
- Flipping a coin 20 times, counting heads → **Binomial** (fixed n=20,
  independent, same p each time)
- Customers walking into a store in an hour → **Poisson** (no fixed n,
  counting occurrences over a fixed time interval based on a rate)
- Defective items in a batch of 50 parts, same probability each →
  **Binomial** (fixed n=50, independent, same p each time)

---

## Mistakes I Made & Fixed Today

- Justified the "customers per hour" scenario as Poisson using
  "independence" as the reasoning — but independence is required by BOTH
  distributions, so it doesn't actually distinguish them. Corrected the
  reasoning to focus on the real distinguishing factor: no fixed number
  of trials, counting occurrences over a continuous interval instead.
- Needed to slow down and rebuild factorial (`!`) and exponent (`^`/`**`)
  intuition from scratch with small worked examples before the Binomial
  formula made sense — both are core to the formula and worth being
  completely comfortable with going forward.

---

## Resources Used

- Taught interactively: Binomial distribution (formula breakdown,
  factorial/exponent refresher, mean/variance shortcuts), the complement
  rule for "at least" probabilities, Poisson distribution (formula
  breakdown, mean/variance), and Binomial vs Poisson scenario reasoning —
  followed by a self-guided, questions-only practice file, checked
  task-by-task