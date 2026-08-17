# Day 17 — Type I/II Errors; Bayes' Theorem; Confidence Intervals

**Topics:** identifying Type I vs Type II errors; Bayes' theorem calculation; confidence intervals (manual, scipy, and t-distribution for unknown population std)

## What I Learned

- **Type I error** — a false positive: rejecting H0 when it's actually true. **Type II error** — a false negative: failing to reject H0 when it's actually false. Applied this to spam filters and legal verdicts (courtroom "innocent until proven guilty" framing).
- **Bayes' theorem** — `P(A|B) = [P(B|A) × P(A)] / P(B)`. Updates a probability based on new evidence, combining a prior (`P(A)`) with a likelihood (`P(B|A)`) to get a posterior (`P(A|B)`).
- **The rare disease example** — a test with 90% accuracy still only gives ~27% actual probability of having a rare disease (2% prevalence) after a positive result. Worked through the "100,000 people" breakdown to see why: false positives from the huge healthy population (4,900) outnumber true positives from the small sick population (1,800). Test accuracy alone isn't enough — the base rate (prior) matters enormously.
- **Confidence intervals (CI)** — a range, calculated from sample data, likely to contain the true population parameter at a stated confidence level. `CI = x̄ ± (z* × SE)` for known population σ.
- **The correct interpretation of "95% confident"** — NOT "95% chance the true value is in this specific interval" (a common misconception). It means: if you repeated the sampling process many times, 95% of the resulting intervals would contain the true value. A statement about the reliability of the method, not a probability about one interval.
- **Confidence level vs interval width** — higher confidence (99% vs 95%) → wider interval (more room needed for more certainty). Verified directly: 95% CI width ≈ 0.202, 99% CI width ≈ 0.266.
- **scipy shortcuts** — `stats.norm.interval(confidence, loc, scale)` for known population σ; `stats.t.interval(confidence, df, loc, scale)` for unknown population σ (using `df=n-1`, connecting directly to Day 16's t-distribution).

## Diagram

Used a 2×2 grid to visualize Type I vs Type II errors: rows = decision (reject H0 / fail to reject H0), columns = reality (H0 true / H0 false). The two "correct decision" cells sit on the diagonal; Type I error (false positive) sits where you reject a true H0; Type II error (false negative) sits where you fail to reject a false H0.

## Resources Used

- "Tutorial 19 - Type 1 And Type 2 Error In Statistics - Krish Naik" — https://www.youtube.com/watch?v=8BxVMGn3c3o
- "Naive Bayes Classifier Algorithm Theorem Explained in Detail in Hindi" — https://www.youtube.com/watch?v=HUlOkr16ZCc
- "How To Perform Hypothesis Testing - Confidence Interval | Z-test..." — https://www.youtube.com/watch?v=Ib5UUBYzvPw

## Mistakes I Made & Fixed

- In the Bayes' theorem calculation, wrapped the result in square brackets (`[...]`), accidentally turning a single number into a one-item list — `round()` then failed since it expects a plain number, not a list.
- In the confidence interval manual calculation, used a completely wrong variable (`confidence_interval = 95`, meant to represent "95%") in place of the actual sample mean (2.5 kg) when calculating the bounds — a variable mix-up that produced nonsensical results (~95 instead of ~2.5). Also had the lower/upper bound formulas swapped (adding margin for lower, subtracting for upper, instead of the reverse).
- Used `z = 1.90` instead of the specified `z* = 1.96` for the 95% confidence level — a small but meaningful precision typo.
- Left written interpretation comments too brief in a few places (e.g. "range likely to contain true population" without stating the actual calculated numbers) — working on including the specific values when a task asks for a plain-English interpretation of a result.

## Exercises Completed

- [x] Task 1 — Identifying Type I vs Type II errors across 3 scenarios
- [x] Task 2 — Bayes' theorem manual calculation (rare disease example)
- [x] Task 3 — Confidence interval by manual formula
- [x] Task 4 — Confidence interval with scipy (95% vs 99% comparison)
- [x] Task 5 — Confidence interval from raw sample data using the t-distribution

## Next Up

Day 18 — Chi-square test and goodness-of-fit