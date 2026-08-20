# Day 18 — Chi-square Test & Chi-square Goodness-of-Fit Test

**Topics:** chi-square formula (manual); degrees of freedom and p-value; goodness-of-fit with scipy (equal and unequal expected frequencies); interpreting chi-square results

## What I Learned

- **Chi-square test** works with **categorical data** (counts/frequencies), unlike Z-test/t-test which work with numeric/continuous data.
- **Goodness-of-fit test** — compares ONE categorical variable's observed distribution against an expected distribution.
- **Formula:** `χ² = Σ [(Observed - Expected)² / Expected]` — squared gaps (to punish larger mismatches harder and stay positive) scaled relative to what was expected, summed across all categories.
- **Degrees of freedom** — `df = number of categories - 1`, same "n-1" pattern seen in Day 7 (sample variance) and Day 16 (t-distribution).
- **p-value from chi-square:** `stats.chi2.sf(chi2_statistic, df)` — same "survival function" concept from Day 15's simulation exercise (probability of a result this extreme or more).
- **scipy shortcut:** `stats.chisquare(f_obs=observed)` runs the full test in one line, defaulting to equal expected frequencies; pass `f_exp=expected_counts` for custom/unequal expected distributions.
- **Key intuition:** small χ² → observed close to expected → fits the pattern (large p-value, fail to reject H0). Large χ² → observed far from expected → doesn't fit (small p-value, reject H0).
- **Converting proportions to expected counts** — chi-square needs actual counts, not percentages; multiply each expected proportion by the total sample size to get expected counts.
- **ML relevance** — used in feature selection for categorical features (testing significance against the target variable) and in A/B testing when comparing categorical outcomes across groups.

## Resources Used

- "Tutorial 21- Chi Square test simply Explained In Stats- Krish Naik Hindi" — https://www.youtube.com/watch?v=O47boiErNwI
- "Tutorial 33- Chi Square Test Implementation with Python- Hypothesis Testing- Part 2" — https://www.youtube.com/watch?v=w5iKu1IrTJQ

## Mistakes I Made & Fixed

- In the scipy goodness-of-fit task, stored the two return values (chi2 statistic and p-value) from `stats.chisquare()` into a single variable instead of unpacking them separately — same unpacking pattern needed as Day 16's `ttest_1samp`/`ttest_ind`.
- Attempted to pass a text label directly as an argument INTO `round()` (e.g. `round("chi2: ", chi2, 4)`) — `round()` only accepts numbers; the label needs to stay in `print()`, separate from the rounding call.
- In a couple of interpretation comments, stated only "chi2 is small/big" as the reasoning without connecting it to the actual p-value and what that means for the reject/fail-to-reject decision — worked on tying both pieces of evidence (chi2 magnitude AND p-value vs alpha) together in the written conclusion.

## Exercises Completed

- [x] Task 1 — Chi-square statistic by manual formula
- [x] Task 2 — Degrees of freedom and p-value calculation
- [x] Task 3 — Goodness-of-fit test with scipy (verified against manual calculation)
- [x] Task 4 — Goodness-of-fit with custom/unequal expected frequencies
- [x] Task 5 — Interpreting chi-square results across two scenarios

## Next Up

Day 19 — ANOVA: types, assumptions, variance partitioning