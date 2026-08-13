# Day 16 — Z-test; Student's t-distribution and t-test; Z-test vs t-test

**Topics:** Z-test (manual formula + p-value conversion); Student's t-distribution; one-sample and two-sample t-tests with scipy; Z-test vs t-test decision rule

## What I Learned

- **Z-test** — tests whether a sample mean differs significantly from a known population mean. Formula: `z = (x̄-μ)/(σ/√n)`. Requires the population standard deviation (σ) to be **known** — the key limiting requirement.
- **Converting a z-statistic to a p-value** — `p = 2 × (1 - norm.cdf(|z|))` for a two-tailed test, using scipy's Normal CDF.
- **Student's t-distribution** — similar to Normal, but with fatter tails, used when the population σ is unknown and must be estimated from the sample itself. The fatter tails build in extra caution for the added uncertainty of estimating spread from limited data.
- **Degrees of freedom (df = n-1)** — as sample size grows, the t-distribution's tails shrink and it converges toward Normal, which is why Z-test and t-test results become similar for large samples.
- **t-test formula** — `t = (x̄-μ)/(s/√n)`, identical structure to the Z-test formula, but uses sample standard deviation (`s`, estimated) instead of population σ (known).
- **scipy shortcuts:** `stats.ttest_1samp(sample, popmean)` for comparing one sample against a known/claimed mean; `stats.ttest_ind(sample1, sample2)` for comparing two independent samples against each other — both return `(t_statistic, p_value)` together.
- **Z-test vs t-test decision rule:** known population σ + large sample (n≥30) → Z-test. Unknown population σ and/or small sample → t-test. In practice, population σ is rarely known, making t-test the more commonly used real-world test.
- **Reading scientific notation in scipy output** (e.g. `9.116e-08`) — the `e-08` means "move the decimal 8 places left," producing an extremely small number, not a typo or a large value.

## Diagram

Compared Normal distribution vs Student's t-distribution: same symmetric bell shape and center, but the t-distribution has a slightly lower peak and visibly fatter tails — reflecting the extra uncertainty from estimating population spread using only a sample. As sample size (degrees of freedom) increases, the t-distribution's tails shrink and it converges toward the Normal shape.

## Resources Used

- "Student t Distribution in Hindi Part 1 | Properties of t Distribution | When to use t test and z test" — https://www.youtube.com/watch?v=TIc9Sj5Mx4c
- "Z-Statistics vs. T-Statistics EXPLAINED in 4 Minutes" — https://www.youtube.com/watch?v=DEkPZv5ppHI

## Mistakes I Made & Fixed

- In the Z-test manual calculation, set `n = 1200` (the population mean) instead of `n = 40` (the actual sample size) — a variable mix-up that would have completely broken the formula's denominator.
- In the decision-rule check for the t-test, compared `t_statistic <= p_value` instead of the correct rule `p_value <= alpha` — an entirely wrong comparison that happened to still be checkable against the real numbers to catch the error.
- Misread scipy's scientific notation output (`9.116e-08`) as literally "9.1160" in a written comment, when it actually represents an extremely small number (~0.0000000912) — learned to properly convert `e-XX` notation by moving the decimal point left by that many places.
- Used a hyphen in a variable name (`t-statistic`) which Python interprets as subtraction, not a valid identifier — needed an underscore (`t_statistic`) instead.
- In the Z-test vs t-test scenario task, initially reasoned using vague terms ("there is a std" / "no std") instead of the precise distinguishing factor — whether the *population* standard deviation specifically is known or unknown (a sample always has some calculable std, so that alone isn't the deciding factor).

## Exercises Completed

- [x] Task 1 — Z-test by manual formula
- [x] Task 2 — Converting Z-statistic to a p-value and interpreting the result
- [x] Task 3 — One-sample t-test with scipy (`ttest_1samp`)
- [x] Task 4 — Two-sample t-test with scipy (`ttest_ind`)
- [x] Task 5 — Identifying Z-test vs t-test scenarios with precise reasoning

## Next Up

Day 17 — Type I/II errors; Bayes' theorem; confidence intervals