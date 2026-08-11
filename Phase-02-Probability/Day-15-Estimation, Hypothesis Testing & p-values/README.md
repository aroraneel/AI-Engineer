# Day 15 — Estimation Theory; Hypothesis Testing Fundamentals; p-values

**Topics:** point vs interval estimates; null/alternative hypothesis (H0/H1); p-value decision rule; simulating a p-value; standard error from real sample data

## What I Learned

- **Estimation theory** — using sample data to estimate unknown population parameters, since measuring an entire population is rarely possible.
- **Point estimate** — a single number guess (e.g. sample mean). **Interval estimate** — a range that accounts for uncertainty (foundation for confidence intervals, coming Day 17).
- **Hypothesis testing logic** — assume H0 (null hypothesis, "no effect") is true, then ask: how likely would this data be if H0 really were true? If very unlikely, reject H0 in favor of H1 (alternative hypothesis, "there IS an effect").
- **p-value** — the probability of observing data this extreme (or more extreme) assuming H0 is true. Small p-value = strong evidence against H0.
- **Decision rule** — `p-value ≤ α → reject H0`; `p-value > α → fail to reject H0`. The boundary case (p = α exactly) counts as reject, since the rule uses `≤` not `<`.
- **Important misconception avoided:** failing to reject H0 does NOT prove H0 is true — it only means there wasn't enough evidence to reject it with the current data.
- **Simulating a p-value directly** (rather than using a formula) — generated 10,000 simulated fair-coin experiments and measured what fraction produced a result as extreme as what was actually observed. This built real intuition for what a p-value represents, rather than just plugging into a formula.
- **Standard error from real data** — `sample_std / √n`, using `ddof=1` for sample standard deviation (n-1, consistent with Day 7). Connects directly to Day 14's CLT lesson — this is literally how much a sample mean is expected to wobble from the true population mean.

## Diagram

A bell curve diagram was used to visualize the p-value concept: the curve represents the distribution of outcomes if H0 were true, centered on "no effect." The observed value is marked to the right of center, and the shaded area beyond it represents the p-value — the smaller and further right the shaded region, the smaller the p-value, and the stronger the evidence against H0.

## Resources Used

- "Tutorial 14 - What Is Hypothesis Testing Explained In Hindi | Krish Naik" — https://www.youtube.com/watch?v=pZ1d32ar_iY
- "Hypothesis Testing Explained with Solved Numerical in Hindi | Machine Learning Course" — https://www.youtube.com/watch?v=tyoTXLdTpC4

## Mistakes I Made & Fixed

- Used `if (p_value <= alpha) is True:` instead of the simpler, more direct `if p_value <= alpha:` — the comparison already returns True/False, so the extra `is True` check was redundant.
- In the coin-flip simulation task, wrote a contradictory comment ("fail to reject H0") that didn't match the actual printed output ("reject H0") — caught by cross-checking the written conclusion against the real printed result before finalizing.
- Initially left the plain-English interpretation blank in the simulation task's conclusion — the code correctly decided "reject H0," but didn't explain what that meant about the coin itself (likely biased, since 62+ heads out of 100 fair flips only happens ~1% of the time by chance).
- Used `sqrt()` directly instead of `np.sqrt()` when calculating standard error — caused a `NameError` since `sqrt` isn't a built-in Python function without an import; fixed by using the NumPy version already imported.
- Calculated the point estimate (mean) but forgot to print it in the final output — only printed standard error initially, missing half of what the task asked for.

## Exercises Completed

- [x] Task 1 — Point estimate vs interval estimate identification
- [x] Task 2 — Writing H0 and H1 for a drug-trial scenario
- [x] Task 3 — p-value decision rule practice, including the boundary case
- [x] Task 4 — Simulating a p-value with a coin flip test
- [x] Task 5 — Point estimate and standard error from real sample data

## Next Up

Day 16 — Z-test; Student's t-distribution and t-test; Z-test vs t-test

**📌 Checkpoint reminder:** Day 15 completes Days 11-15 — a review test covering this block is due now, before starting Day 16.