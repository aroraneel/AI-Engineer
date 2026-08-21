# Day 20 — Capstone: Full Hypothesis-Testing Workflow — Notes

Topics covered: test-selection decision framework; end-to-end application
across 4 real-world business scenarios; written reporting

---

## 1. The Decision Framework

Built a decision tree covering every test learned across Days 16-19:

```
What data type?
├── Categorical → Chi-square goodness-of-fit / independence
└── Numeric → How many groups?
    ├── 1 group vs known value
    │   ├── Population σ known → Z-test
    │   └── Population σ unknown → One-sample t-test
    ├── 2 independent groups → Two-sample t-test
    └── 3+ groups → ANOVA (one-way)
```

Always confirm assumptions (normality, independence, equal variance)
before trusting results — same principle across every test type.

---

## 2. The Full Workflow Applied

1. Look at the data — data type, number of groups
2. State H0 and H1 in plain English before writing any code
3. Check assumptions where relevant
4. Choose the test using the decision tree
5. Run the test, get test statistic + p-value
6. Apply the decision rule (p ≤ α → reject H0)
7. Report findings in plain English, with caveats

---

## 3. Task 1 — Website Load Time (Z-test)

**Scenario:** claimed average load time = 2.0s, population σ known =
0.5s, sample of 45 loads averaged 2.15s.

```
H0: true average load time = 2.0 seconds
H1: true average load time ≠ 2.0 seconds
```

```python
z = (sample_mean - pop_mean) / (pop_std / np.sqrt(n))
p_value = 2 * (1 - stats.norm.cdf(abs(z)))
# z ≈ 2.0125, p ≈ 0.0442 → reject H0
```

**Note:** this was a borderline result (0.0442 vs 0.05 threshold) —
worth flagging as less conclusive than the other 3 tasks when reporting.

**Mistake caught:** initially framed H0/H1 around whether the sample's
specific result (2.15) was "true or false," rather than the population's
true value relative to the claimed 2.0 seconds. H0/H1 must always be
about the population parameter being tested, not the sample's outcome.

---

## 4. Task 2 — Two Email Subject Lines (Two-sample t-test)

**Scenario:** comparing minutes-to-first-purchase between two
independent groups (subject line A vs B), population σ unknown.

```
H0: no difference in true average minutes-to-first-purchase between A and B
H1: there IS a difference between A and B
```

```python
t_statistic, p_value = stats.ttest_ind(subject_a, subject_b)
# t ≈ 3.2577, p ≈ 0.0044 → reject H0
```

**Finding:** Subject Line B leads to consistently faster purchases —
clear, actionable result (low p-value, not borderline).

---

## 5. Task 3 — Support Ticket Distribution (Chi-square goodness-of-fit)

**Scenario:** checking if 200 support tickets split evenly across 4
categories (Shipping, Billing, Product, Account), historically assumed
even.

```
H0: tickets ARE evenly split across the 4 categories
H1: tickets are NOT evenly split
```

```python
expected = np.array([n_total_tickets / n_categories] * n_categories)
test_stat, p_value = stats.chisquare(f_obs=observed_tickets, f_exp=expected)
# chi2 = 15.0, p ≈ 0.0018 → reject H0
```

**Finding:** Shipping tickets (70) are notably higher than the expected
even split (50 each) — worth investigating.

**Mistakes caught:**
- Initially passed a single number to `f_exp` instead of an array
  matching each category — `stats.chisquare()` needs one expected value
  per category, same shape as `f_obs`.
- Notebook variable-collision bug: reused the name `p_value`, which
  briefly carried over a STALE value from Task 1's earlier cell instead
  of the freshly calculated chi-square p-value. Caught by noticing the
  printed number matched Task 1's exact result rather than a plausible
  new calculation. Fixed by ensuring the variable was consistently
  renamed and recalculated within the same cell before printing.

---

## 6. Task 4 — Shipping Times Across 4 Regions (One-way ANOVA)

**Scenario:** comparing average shipping time (days) across North,
South, East, West warehouse regions.

```
H0: true average shipping times are EQUAL across all 4 regions
H1: at least ONE region's true average shipping time differs
```

```python
f_statistic, p_value = stats.f_oneway(region_north, region_south, region_east, region_west)
# F ≈ 42.95, p ≈ 0.0 → reject H0
```

**Finding:** South region has noticeably longer shipping times
(3.9-4.5 days) compared to the other 3 regions (roughly 2.8-3.4 days).

---

## 7. Task 5 — Written Summary Report

Synthesized all 4 findings into a manager-ready report with sections:
Question, Test, Result, Finding — per task, plus an Overall
Recommendations section.

**Key synthesis insight:** Task 3 (Shipping ticket spike) and Task 4
(South region shipping delays) likely describe the **same underlying
operational problem** — slower shipping in the South region may be
directly driving the increase in shipping-related complaints. This
illustrates how findings across different statistical tests can combine
into a single, more valuable business insight.

**Prioritization logic used:** ranked recommendations by combining
statistical strength (p-value size) with practical business impact —
not just going by which p-value was smallest. Task 1's technically
significant but borderline result (p=0.0442) was correctly downgraded in
urgency compared to Tasks 2-4's much stronger, more actionable results
(all p<0.01).

---

## Mistakes I Made & Fixed Today

- Repeatedly misclassified numeric/continuous data (load times,
  minutes-to-purchase) as "categorical" across multiple tasks — a
  pattern worth deliberately checking going forward: is the value a
  measured NUMBER, or a discrete CATEGORY/LABEL?
- Framed H0/H1 around whether a specific sample result was "true or
  false" instead of correctly framing them around the population
  parameter being tested relative to a claimed or compared value.
- Passed a single number instead of a properly-shaped array to
  `f_exp` in the chi-square test.
- Encountered and fixed a notebook variable-collision bug: reusing
  `p_value` as a variable name allowed a stale value from an earlier
  cell (Task 1) to silently persist and print instead of the newly
  calculated result — a good practical lesson about Jupyter's
  cell-execution-order pitfalls, distinct from `.py` script execution
  where this wouldn't happen the same way.
- Left "Finding" and "Overall Recommendations" sections of the final
  report as placeholders initially, before synthesizing the individual
  conclusions already written earlier into a cohesive summary.

---

## Resources Used

- Decision-tree diagram synthesizing test-selection logic from Days
  16-19 (Z-test, t-test, ANOVA, chi-square criteria)