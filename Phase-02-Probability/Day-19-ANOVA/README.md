# Day 19 — ANOVA: Types, Assumptions, Variance Partitioning

**Topics:** one-way ANOVA with scipy; group means and variance partitioning intuition; checking the homogeneity of variance assumption; ANOVA vs multiple t-tests

## What I Learned

- **ANOVA** compares the means of 3+ groups simultaneously, using a single test — unlike a t-test, which only compares 2 groups at a time.
- **Variance partitioning** — ANOVA splits total variability into **between-group variance** (differences among group means) and **within-group variance** (individual differences inside each group, aka residual/error variance).
- **The core intuition** — if between-group variance is much larger than within-group variance, the group means are unlikely to all be equal (reject H0). If they're similar, differences are likely just random noise (fail to reject H0).
- **Hypotheses:** H0 = all group means are equal. H1 = at least ONE group mean differs (not necessarily all of them).
- **Types of ANOVA:** One-way (one factor, 2+ groups), Two-way (two factors, tests main effects + interaction), Repeated Measures (same participants measured multiple times).
- **Assumptions:** independence of observations, normality within each group, homogeneity of variance (equal variance across groups), random sampling.
- **F-statistic** — the ratio of between-group variance to within-group variance. F close to 1 → groups probably similar. F much greater than 1 → groups probably differ.
- **scipy shortcut:** `stats.f_oneway(group1, group2, group3, ...)` returns both the F-statistic and p-value directly.
- **Why ANOVA instead of many t-tests** — running multiple separate pairwise t-tests stacks up Type I error risk (Day 17). With 6 separate tests at α=0.05 each, the overall chance of at least one false alarm climbs to roughly 26%, far above the intended 5%. ANOVA tests all groups together in one test, keeping the true error rate at the intended level.

## Resources Used

- "Tutorial 22-Analysis Of Variance(ANOVA) and its types Part 1- Krish Naik Hindi" — https://www.youtube.com/watch?v=BtTvYflNMjk

## Mistakes I Made & Fixed

- In the group-means task, initially tried to re-run `stats.f_oneway()` on a single combined array instead of simply calculating `.mean()` on each group and the overall combined data — misunderstood what the task was actually asking for (basic descriptive statistics to build intuition, not another hypothesis test).
- Used `np.concatenate(design_a, design_b, design_c)` with separate arguments instead of the required single tuple: `np.concatenate((design_a, design_b, design_c))` — missing the extra parentheses.
- In the "similar classrooms" ANOVA task, accidentally passed `class_3` twice into `stats.f_oneway()` instead of `class_1, class_2, class_3` — omitted `class_2` entirely. The final conclusion happened to still be correct by coincidence (since all 3 classrooms were genuinely similar), but the underlying calculation was run on the wrong data.
- Interpretation comments initially stated conclusions without the supporting "why" (e.g. "ANOVA do all in one" instead of explaining the compounding Type I error risk from multiple t-tests) — worked on connecting conclusions back to the specific underlying statistical reasoning.

## Exercises Completed

- [x] Task 1 — One-way ANOVA with scipy (comparing 3 ad designs)
- [x] Task 2 — Manual group means, building variance-partitioning intuition
- [x] Task 3 — ANOVA on genuinely similar groups (expected non-significant result)
- [x] Task 4 — Checking the homogeneity of variance assumption
- [x] Task 5 — ANOVA vs multiple t-tests reasoning (Type I error accumulation)

## Next Up

Day 20 — Capstone: full hypothesis-testing workflow on a real dataset (choosing the right test, interpreting results, reporting findings)

**📌 This is the final day of Phase 2 (Probability & Inference). A Phase 2 cumulative test should be taken after completing Day 20.**