# Day 19 — ANOVA: Types, Assumptions, Variance Partitioning — Notes

Topics covered: one-way ANOVA; variance partitioning; assumptions; F-statistic;
ANOVA vs multiple t-tests

---

## 1. Why ANOVA? The Problem It Solves

Day 16's t-test compares means of **2 groups**. ANOVA compares the means
of **3 or more groups simultaneously**.

**Why not just run multiple t-tests for pairwise comparisons?** Running
many separate t-tests increases the risk of Type I errors (Day 17) —
each test carries its own 5% false-positive risk, and these risks
compound across multiple tests. ANOVA tests all groups at once in a
single test, properly controlling this risk.

---

## 2. Variance Partitioning — What ANOVA Actually Does

ANOVA splits total variability in a dataset into two components:

- **Between-group variance** — variation attributable to the differences
  among group means
- **Within-group variance** — variation due to individual differences
  inside each group (also called residual or error variance)

If between-group variance is substantially larger than within-group
variance, ANOVA concludes the group means are unlikely to all be equal.

**Despite the name "Analysis of Variance," ANOVA analyzes variances in
order to draw conclusions about MEANS.**

### The core intuition

Imagine comparing average test scores across 3 teaching methods:
- **If all 3 methods truly work the same:** individual scores scatter
  from normal randomness, but group averages land close together —
  within-group variance dominates.
- **If one method genuinely works better:** group averages spread apart
  MORE than random noise alone would explain — between-group variance
  becomes large relative to within-group variance.

ANOVA measures this ratio and decides if it's large enough to be
meaningful, not just random luck.

---

## 3. Hypotheses

```
H0: all group means are equal (μ1 = μ2 = μ3 = ...)
H1: at least ONE group mean is different from the others
```

Note: H1 does NOT claim all means differ — just that at least one does.

---

## 4. Types of ANOVA

- **One-Way ANOVA** — one independent variable (factor) with 2+ levels.
  Example: comparing plant growth across 3 fertilizer types.
- **Two-Way ANOVA** — two independent variables, each with multiple
  levels; tests main effects of each factor AND possible interaction
  effects between them. Example: soda brand AND calorie level together.
- **Repeated Measures ANOVA** — same participants measured multiple
  times under different conditions, accounting for correlation between
  repeated measurements.

*(One-way ANOVA is the foundational type worked through today.)*

---

## 5. Assumptions

1. **Independence** — observations independent of each other within
   each group
2. **Normality** — each population/group must be normally distributed
3. **Homogeneity of variance (homoscedasticity)** — all populations must
   have the same variance
4. **Random sampling** — sample selected randomly from the population

Same "check your assumptions before trusting the test" principle as
Z-test/t-test from Day 16.

---

## 6. The F-statistic

```
F = between-group variance / within-group variance
```

- **F close to 1** → between and within variance similar → group means
  probably ARE equal → fail to reject H0
- **F much greater than 1** → between-group variance dominates → group
  means probably differ → reject H0

**Decision rule (same pattern as always):**
```
if p-value <= alpha:  reject H0 (at least one group mean differs)
if p-value > alpha:   fail to reject H0 (no evidence of a difference)
```

---

## 7. Worked Example — One-way ANOVA with scipy (Task 1)

Three ad designs, click-through rates measured across independent groups:

```python
design_a = np.array([2.1, 2.4, 1.9, 2.3, 2.0, 2.2])
design_b = np.array([3.5, 3.2, 3.8, 3.6, 3.4, 3.7])
design_c = np.array([2.2, 2.0, 2.5, 2.1, 2.3, 1.9])

f_statistic, p_value = stats.f_oneway(design_a, design_b, design_c)
# f_statistic ≈ 88.40, p_value ≈ 0.0 (extremely small)
```

Since p-value is far below 0.05 → reject H0. Strong evidence at least
one design has a significantly different average click-through rate.

### Building intuition with group means (Task 2)

```python
mean_a = design_a.mean()   # 2.15
mean_b = design_b.mean()   # 3.5333
mean_c = design_c.mean()   # 2.1667

all_values = np.concatenate((design_a, design_b, design_c))
overall_mean = all_values.mean()   # 2.6167
```

**Distance from overall mean:**
```
|Mean A - Overall| ≈ 0.4667
|Mean B - Overall| ≈ 0.9166   <- furthest
|Mean C - Overall| ≈ 0.45
```

Mean B is furthest from the overall mean, by a wide margin — this
directly explains WHY ANOVA rejected H0: Design B is the standout group
driving the large between-group variance, consistent with its clearly
higher raw click-through rates.

---

## 8. A Case Where ANOVA Should NOT Find a Difference (Task 3)

Three classrooms, all taught with the same method (expect similar means):

```python
class_1 = np.array([78, 82, 75, 80, 79, 81])
class_2 = np.array([77, 80, 83, 79, 78, 82])
class_3 = np.array([80, 78, 81, 77, 82, 79])

f_statistic, p_value = stats.f_oneway(class_1, class_2, class_3)
# f_statistic ≈ 0.133, p_value ≈ 0.8765
```

F-statistic close to 1 (well below the large F seen in Task 1), p-value
far above 0.05 → fail to reject H0. Matches expectation: since all 3
classrooms were taught identically, there's no significant evidence
their average scores actually differ — small variations are consistent
with random chance.

---

## 9. Checking the Homogeneity of Variance Assumption (Task 4)

Before trusting an ANOVA result, check that groups have roughly equal
variance.

```python
var_a = np.var(design_a, ddof=1)   # 0.0350
var_b = np.var(design_b, ddof=1)   # 0.0467
var_c = np.var(design_c, ddof=1)   # 0.0467
```

All three variances are similar in magnitude — no group is a wild
outlier — supporting the assumption is reasonably satisfied here, which
lends more confidence to trusting Task 1's ANOVA result.

*(Note: `stats.levene()` provides a formal statistical test for this
assumption; eyeballing was sufficient for today's task.)*

---

## 10. ANOVA vs Multiple T-tests (Task 5)

**Scenario:** comparing average delivery times across 4 companies. Doing
this pairwise would require 6 separate t-tests (every possible pair).

**Is this appropriate?** No. Each t-test carries its own 5% (α=0.05)
Type I error (false alarm) risk. Running 6 separate tests stacks that
risk up — the overall chance of AT LEAST ONE false alarm across all 6
tests climbs to roughly **26%**, far higher than the intended 5%.

**ANOVA's fix:** tests all groups together in ONE single test, so the 5%
risk is only taken once, not 6 times.

**The specific problem that increases:** Type I error (false alarm) —
wrongly concluding a real difference exists between some pair of groups,
purely from accumulated random chance across multiple tests.

---

## 11. Connection to ML

- Feature selection: testing if a categorical feature with 3+ categories
  has a statistically significant relationship with a continuous target
- A/B/C testing: comparing 3+ product/webpage variants at once, instead
  of running many separate pairwise t-tests

---

## Mistakes I Made & Fixed Today

- In the group-means task, initially tried to re-run `stats.f_oneway()`
  on a combined array instead of simply calculating `.mean()` per group
  and overall — misunderstood the task as another hypothesis test rather
  than basic descriptive statistics to build intuition.
- Used `np.concatenate(design_a, design_b, design_c)` with separate
  arguments instead of the required single tuple:
  `np.concatenate((design_a, design_b, design_c))` — missing the extra
  parentheses that wrap the arrays into one tuple argument.
- In the "similar classrooms" ANOVA task, accidentally passed `class_3`
  twice into `stats.f_oneway()`, omitting `class_2` entirely. The final
  conclusion happened to still be correct by coincidence (since all 3
  classrooms were genuinely similar), but the calculation itself ran on
  incorrect input data.
- Interpretation comments initially stated conclusions without
  supporting reasoning (e.g. "ANOVA do all in one" instead of explaining
  the compounding Type I error risk) — worked on connecting conclusions
  back to the specific underlying statistical mechanism.

---

## Resources Used

- "Tutorial 22-Analysis Of Variance(ANOVA) and its types Part 1- Krish
  Naik Hindi" — https://www.youtube.com/watch?v=BtTvYflNMjk