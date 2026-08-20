# Day 18 — Chi-square Test & Chi-square Goodness-of-Fit Test — Notes

Topics covered: chi-square formula; degrees of freedom; goodness-of-fit test
(equal and unequal expected frequencies); interpreting results

---

## 1. What Problem Does Chi-Square Solve?

Previous tests (Z-test, t-test) worked with **numeric/continuous data**
(heights, weights, scores). Chi-square works with **categorical data** —
counts/frequencies in categories (colors, yes/no, product types).

Answers: "does my observed count data match what I'd expect?"

### Two types of chi-square tests

1. **Goodness-of-fit test** — compares ONE categorical variable's observed
   distribution against an expected distribution.
2. **Chi-square test of independence** — compares TWO categorical
   variables to see if they're related (not covered today, but a natural
   extension).

---

## 2. The Formula

```
χ² = Σ [(Observed - Expected)² / Expected]
```

- `Observed (O)` = actual count measured in each category
- `Expected (E)` = count expected if H0 were true
- `Σ` = sum across every category

### Piece by piece

- `(Observed - Expected)` → how far off actual data is from expectation
- **squared** → always positive, punishes bigger gaps harder (same logic
  as variance/std, Day 7)
- **divide by Expected** → scales the gap relative to the expected size
  (a gap of 10 matters more if expected was 20 than if expected was 2000)
- **sum across categories** → combines every mismatch into one overall
  test statistic

---

## 3. Worked Example — Manual Calculation (Task 1 & 2)

**Scenario:** bag of candy claims equal mix of 5 colors, 100 candies
counted.

```python
observed = np.array([25, 15, 22, 18, 20])
n_total, n_categories = 100, 5

expected = n_total / n_categories   # = 20 per category
chi2 = np.sum((observed - expected)**2 / expected)
# = 1.25 + 1.25 + 0.2 + 0.2 + 0.0 = 2.9
```

**Degrees of freedom:**
```python
df = n_categories - 1   # = 4
```
Same "n-1" pattern as Day 7's sample variance and Day 16's t-distribution.

**Converting chi2 to a p-value:**
```python
p_value = stats.chi2.sf(chi2, df)   # ≈ 0.5747
```
(`sf` = "survival function" — probability of a value at least this
extreme, same p-value concept from Day 15's simulation exercise.)

**Decision:** 0.5747 > 0.05 → fail to reject H0. Candy colors appear
evenly distributed; observed differences are consistent with random
chance.

---

## 4. Goodness-of-Fit with scipy (Task 3)

```python
chi2_scipy, p_value_scipy = stats.chisquare(f_obs=observed)
# chi2_scipy = 2.9, p_value_scipy = 0.5747 -- matches manual exactly
```

`stats.chisquare()` assumes **equal expected frequencies by default** —
confirmed it performs the identical calculation done manually in Tasks 1-2.

---

## 5. Goodness-of-Fit with UNEQUAL Expected Frequencies (Task 4)

When categories aren't expected to be equal, provide `f_exp` explicitly.

**Scenario:** website expects browser traffic: Chrome=50%, Safari=25%,
Firefox=15%, Edge=10%. Actual counts out of 400 visitors:
```python
observed_browsers = np.array([185, 110, 65, 40])
expected_proportions = np.array([0.50, 0.25, 0.15, 0.10])
```

**Key step — convert proportions to counts** (chi-square needs actual
counts, not percentages):
```python
expected_counts = expected_proportions * total_visitors
# = [200, 100, 60, 40]
```

**Run the test with custom expected values:**
```python
chi2_stat, p_val = stats.chisquare(f_obs=observed_browsers, f_exp=expected_counts)
# chi2_stat ≈ 2.5417, p_val ≈ 0.4678
```

**Decision:** 0.4678 > 0.05 → fail to reject H0. No significant evidence
the browser distribution has shifted from the historical 50/25/15/10
pattern — observed counts are close enough to expected that the
difference could be random variation.

---

## 6. Interpreting Chi-Square Results (Task 5)

**Key intuition:**
```
Small χ²  -> observed close to expected -> fits the pattern
Large χ²  -> observed far from expected -> does NOT fit the pattern
```

**Worked scenarios:**
- χ²=0.85, p=0.93 → **FITS**. Small χ² means observed counts are close
  to expected; large p-value (far above 0.05) means fail to reject H0 —
  strong evidence the data matches the expected distribution.
- χ²=24.6, p=0.0001 → **DOES NOT FIT**. Large χ² means observed counts
  are far from expected; tiny p-value (far below 0.05) means reject H0
  — strong evidence the data does NOT match the expected distribution.

**Important:** both chi2 magnitude AND the p-value tell the same story
together — citing only one without the other is an incomplete
interpretation.

---

## 7. Connection to ML

- **Feature selection** — testing if a categorical feature has a
  statistically significant relationship with the target variable
- **A/B testing** — comparing categorical outcomes (e.g. click vs
  no-click) across groups

---

## Mistakes I Made & Fixed Today

- Stored `stats.chisquare()`'s two return values (chi2 statistic and
  p-value) into a single variable instead of unpacking them separately —
  same unpacking pattern required as Day 16's `ttest_1samp`/`ttest_ind`.
- Attempted to pass a text label directly as an argument INTO `round()`
  (e.g. `round("chi2: ", chi2, 4)`) — `round()` only accepts numbers; the
  label needs to stay in a separate `print()` argument.
- In interpretation comments, initially stated only "chi2 is small/big"
  as the full reasoning, without connecting it to the actual p-value and
  what that means for the decision — worked on tying both pieces of
  evidence (chi2 magnitude AND p-value vs alpha) together explicitly.

---

## Resources Used

- "Tutorial 21- Chi Square test simply Explained In Stats- Krish Naik
  Hindi" — https://www.youtube.com/watch?v=O47boiErNwI
- "Tutorial 33- Chi Square Test Implementation with Python- Hypothesis
  Testing- Part 2" — https://www.youtube.com/watch?v=w5iKu1IrTJQ