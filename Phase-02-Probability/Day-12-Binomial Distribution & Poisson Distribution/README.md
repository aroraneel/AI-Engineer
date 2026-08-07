# Day 12 — Binomial Distribution & Poisson Distribution

**Topics:** Binomial distribution (formula, mean/variance, scipy); P(at least k) via CDF complement rule; Poisson distribution (formula, mean/variance, scipy); identifying Binomial vs Poisson scenarios

## What I Learned

- **Binomial distribution** — models a fixed number of independent trials (`n`), each with the same probability of success (`p`), counting how many succeed. Formula: `P(X=k) = C(n,k) × p^k × (1-p)^(n-k)`.
- **`math.comb(n, k)`** gives the number of ways to arrange k successes among n trials ("n choose k") — verified by manual calculation matching `scipy.stats.binom(n, p).pmf(k)` exactly.
- **Binomial mean/variance shortcuts:** `mean = n×p`, `variance = n×p×(1-p)` — confirmed against `.mean()` / `.var()`.
- **Complement rule for "at least" probabilities:** `P(X ≥ k) = 1 - P(X ≤ k-1) = 1 - CDF(k-1)`. Instead of adding up every probability from k to n individually, calculate everything below the threshold and subtract from 1 — fewer calculations and less error-prone.
- **Poisson distribution** — models the count of events over a fixed interval (time or space) given an average rate `λ`, with **no fixed number of trials**. Formula: `P(X=k) = (λ^k × e^(-λ)) / k!`.
- **Poisson mean/variance:** both equal `λ` exactly — a distinctive property that doesn't hold for Binomial.
- **Binomial vs Poisson — the real distinguishing question:** it's not just "are events independent" (both require that). It's whether there's a **fixed number of trials** (Binomial) or you're **counting occurrences over a continuous interval based on a rate** (Poisson).

## Resources Used

- Taught interactively (Binomial + Poisson theory, formula breakdowns, factorial/exponent basics) before moving to a self-guided, questions-only practice file

## Mistakes I Made & Fixed

- In the scenario-identification task (6b — customers arriving per hour), initially justified it as Poisson because "events happen independently" — but independence alone doesn't distinguish Poisson from Binomial (both require it). The actual distinguishing factor is the absence of a fixed `n` and counting occurrences over a fixed interval based on a rate. Corrected the reasoning to reflect that.
- Needed a refresher on factorial (`!`) and exponent (`^` in math notation, `**` in Python) notation before the Binomial formula made sense — walked through both with small worked examples until confident.

## Exercises Completed

- [x] Task 1 — Binomial distribution by manual formula
- [x] Task 2 — Binomial distribution with scipy (verified against Task 1, checked mean/variance)
- [x] Task 3 — Binomial P(at least k) using the CDF complement rule
- [x] Task 4 — Poisson distribution by manual formula
- [x] Task 5 — Poisson distribution with scipy (verified against Task 4, checked mean/variance)
- [x] Task 6 — Identifying Binomial vs Poisson scenarios with reasoning

## Next Up

Day 13 — Normal (Gaussian) distribution