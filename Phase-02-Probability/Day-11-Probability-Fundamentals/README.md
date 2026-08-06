# Day 11 — Probability Fundamentals; PMF/PDF/CDF; Bernoulli Distribution

**Topics:** addition rule (mutually exclusive & overlapping events); multiplication rule (independent events); PMF (simulated vs theoretical); CDF (simulated vs theoretical); Bernoulli distribution

## What I Learned

- **Addition rule** — for P(A OR B): if events are mutually exclusive, just add `P(A) + P(B)`. If they can overlap, subtract the overlap: `P(A) + P(B) - P(A and B)`, otherwise the overlap gets double-counted.
- **Multiplication rule** — for independent events, P(A AND B) = `P(A) × P(B)`. Extends to more than two events by multiplying all of them together (e.g. 3 coin flips = `p ** 3`).
- **PMF (Probability Mass Function)** — the exact probability of each value for a discrete variable. Verified by simulating 100,000 die rolls with `np.random.randint(1, 7, size=100000)` and comparing the observed frequency of each value to the theoretical 1/6.
- **CDF (Cumulative Distribution Function)** — P(X ≤ x). Verified the same way: simulated rolls, then used a boolean mask (`rolls <= 3`) with `np.sum()` to get the observed proportion, and compared it to the theoretical CDF(3) = 0.5.
- **Law of Large Numbers** — the more times a random experiment is repeated, the closer the observed probability gets to the true theoretical probability. Saw this directly in both the PMF and CDF simulations (observed values landed close to but not exactly at the theoretical ones).
- **Bernoulli distribution** — models a single trial with two outcomes (1 = success, 0 = failure), using `scipy.stats.bernoulli(p)`. Confirmed `.pmf(1)` and `.pmf(0)` match `p` and `1-p`, and that simulating 10,000 draws with `.rvs()` and taking the mean converges to `p`.
- **Connection to ML** — Bernoulli isn't just a helper concept for understanding binary classification, it IS what the model estimates. A classifier predicting "80% chance of spam" is estimating the parameter `p` of a Bernoulli distribution for that specific input. This is the direct mathematical foundation of logistic regression (Phase 4).

## Resources Used

- Practice file built around addition rule, multiplication rule, PMF/CDF simulation, and Bernoulli distribution (self-guided, questions-only format)

## Mistakes I Made & Fixed

- Used `import scipy as stats` instead of `from scipy import stats` — this imports the wrong thing and would silently fail the moment a `stats.` function is actually called.
- In `np.bincount(rolls)`, forgot that it counts starting from index 0, so a die roll array (values 1-6) produces 7 elements with a useless leading 0 at index 0 — needed to slice with `[1:]`.
- In the CDF task, generated rolls with `np.random.randint(1, 4, size=100000)` instead of the full die range `(1, 7)` — this restricted every roll to 1-3, making the "P(X≤3)" answer trivially 100% instead of measuring anything real.
- Also reused the wrong `theoretical` variable shape for the CDF task (copied the PMF's array of 6 values instead of a single number for CDF(3) = 0.5).
- Left variables defined but unused in the multiplication rule task (e.g. `P_heads_on_1_flip` defined but not reused in the actual calculation) — fixed by using `** 3` / `** 2` on the base variable instead of hardcoding the multiplication.

## Exercises Completed

- [x] Task 1 — Addition rule (mutually exclusive events)
- [x] Task 2 — Addition rule (overlapping events)
- [x] Task 3 — Multiplication rule (independent events)
- [x] Task 4 — PMF for a fair die (simulated vs theoretical)
- [x] Task 5 — CDF for a fair die (simulated vs theoretical)
- [x] Task 6 — Bernoulli distribution (scipy.stats)

## Next Up

Day 12 — Probability distributions: Binomial, Normal (Gaussian), and the Central Limit Theorem
