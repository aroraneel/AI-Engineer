# Statistical Tests — Cheat Sheet

A quick reference covering the core hypothesis tests used in statistics and
machine learning, when to use each, and how to run them with scipy.

---

## Decision Tree — Which Test Do I Use?

```
What data type?
├── Categorical → Chi-square
│   ├── One variable vs an expected distribution → Goodness-of-fit
│   └── Two variables, checking if related → Test of independence
└── Numeric → How many groups?
    ├── 1 group vs a known/claimed value
    │   ├── Population std known → Z-test
    │   └── Population std unknown → One-sample t-test
    ├── 2 groups
    │   ├── Independent groups → Two-sample (independent) t-test
    │   └── Same subjects, measured twice (before/after) → Paired t-test
    └── 3+ groups
        ├── One factor → One-way ANOVA
        └── Two factors → Two-way ANOVA
```

---

## 1. Z-test

**Use when:** comparing one sample mean to a known/claimed value, **population standard deviation is known**.

**Formula:** `z = (x̄ - μ) / (σ/√n)`

```python
z = (sample_mean - pop_mean) / (pop_std / np.sqrt(n))
p_value = 2 * (1 - stats.norm.cdf(abs(z)))
```

**Real example:** factory claims light bulbs last 1200 hours (σ known from years of data); does a new sample match?

---

## 2. One-Sample t-test

**Use when:** comparing one sample mean to a known/claimed value, **population standard deviation is UNKNOWN** (the common real-world case).

```python
t_statistic, p_value = stats.ttest_1samp(sample, popmean=claimed_value)
```

**Real example:** nutritionist claims a snack bar has 250 calories; does a sample of 10 bars support that?

---

## 3. Two-Sample (Independent) t-test

**Use when:** comparing the means of **two independent groups** (different subjects in each group).

```python
t_statistic, p_value = stats.ttest_ind(group_a, group_b)
```

**Real example:** comparing average time-on-page between Website Design A and Website Design B (different visitors in each group).

---

## 4. Paired t-test

**Use when:** comparing **two measurements on the SAME subjects** (before/after, or matched pairs) — not independent groups.

```python
t_statistic, p_value = stats.ttest_rel(before, after)
```

**Real example:** measuring the same 20 patients' blood pressure before and after taking a drug — same people, two time points.

**Key difference from the independent t-test:** paired data is correlated (same subject twice), so this test accounts for that — using the independent version here would be the wrong test.

---

## 5. Chi-square Goodness-of-Fit Test

**Use when:** checking if **ONE categorical variable's** observed distribution matches an expected distribution.

**Formula:** `χ² = Σ [(Observed - Expected)² / Expected]`

```python
chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
# f_exp defaults to equal frequencies if omitted
```

**Real example:** does the distribution of support tickets across 4 categories match the historically expected even split?

---

## 6. Chi-square Test of Independence

**Use when:** checking if **TWO categorical variables** are related/dependent on each other (not just one variable's fit to an expectation).

```python
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
```

`contingency_table` is a 2D array/table of counts (e.g., rows = gender, columns = product preference).

**Real example:** is there a relationship between customer gender and which product category they buy?

---

## 7. One-Way ANOVA

**Use when:** comparing the means of **3 or more groups**, split by **ONE factor**.

**Formula (conceptual):** `F = between-group variance / within-group variance`

```python
f_statistic, p_value = stats.f_oneway(group1, group2, group3, ...)
```

**Real example:** comparing average shipping times across 4 warehouse regions.

---

## 8. Two-Way ANOVA

**Use when:** comparing group means across **TWO factors simultaneously**, testing both factors' individual effects AND whether they interact.

```python
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('outcome ~ C(factor1) + C(factor2) + C(factor1):C(factor2)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
```

**Real example:** testing whether both soda brand AND calorie level (diet vs regular) affect taste ratings, and whether the two factors interact.

**Note:** requires `statsmodels`, not just `scipy` — a different library than the other tests here.

---

## Bayes' Theorem (not a hypothesis test, but related)

**Use when:** updating a probability based on new evidence — commonly for interpreting test results (e.g., medical test accuracy given disease prevalence).

**Formula:** `P(A|B) = [P(B|A) × P(A)] / P(B)`

```python
p_a_given_b = (p_b_given_a * p_a) / p_b
```

---

## Quick Comparison Table

| Test | Data Type | Groups | Population σ | scipy Function |
|---|---|---|---|---|
| Z-test | Numeric | 1 vs known value | Known | `stats.norm.cdf()` (manual) |
| One-sample t-test | Numeric | 1 vs known value | Unknown | `stats.ttest_1samp()` |
| Two-sample t-test | Numeric | 2 independent | Unknown | `stats.ttest_ind()` |
| Paired t-test | Numeric | 2 (same subjects) | Unknown | `stats.ttest_rel()` |
| Chi-square goodness-of-fit | Categorical | 1 variable | N/A | `stats.chisquare()` |
| Chi-square independence | Categorical | 2 variables | N/A | `stats.chi2_contingency()` |
| One-way ANOVA | Numeric | 3+, one factor | Unknown | `stats.f_oneway()` |
| Two-way ANOVA | Numeric | 3+, two factors | Unknown | `statsmodels` (ols + anova_lm) |

---

## The Universal Decision Rule (applies to every test above)

```
if p_value <= alpha:   reject H0 (statistically significant result)
if p_value > alpha:    fail to reject H0 (not enough evidence)
```

Common alpha: 0.05. A result never *proves* H0 true — failing to reject
just means insufficient evidence against it.

---

## Confidence Intervals (related, not a test itself)

**Known population σ:**
```python
stats.norm.interval(confidence=0.95, loc=sample_mean, scale=standard_error)
```

**Unknown population σ (small sample):**
```python
stats.t.interval(confidence=0.95, df=n-1, loc=sample_mean, scale=standard_error)
```

---

## Assumptions to Check Before Trusting Any Test

- **Independence** — observations shouldn't influence each other (except paired tests, which specifically handle dependence)
- **Normality** — data (or residuals) should be roughly normally distributed, especially important for small samples
- **Homogeneity of variance** — for t-tests/ANOVA comparing groups, groups should have similar spread
- **Random sampling** — sample should represent the population without systematic bias
