"""
CHECKPOINT TEST — Days 11-15 — ANSWER SHEET
Covers: Probability fundamentals & Bernoulli (11), Binomial & Poisson (12),
        Normal/Z-score/Uniform (13), Skewed distributions & CLT (14),
        Estimation/Hypothesis testing/p-values (15)
"""

import numpy as np
import math
from scipy import stats


# =============================================================
# PART A — CONCEPTUAL ANSWERS
# =============================================================

# A1. Addition rule: P(A or B) -- used when you want the probability
#     that AT LEAST ONE of two events happens. Add probabilities
#     directly if mutually exclusive; subtract the overlap
#     (P(A)+P(B)-P(A and B)) if they can both happen.
#     Multiplication rule: P(A and B) -- used when you want the
#     probability that BOTH events happen. Multiply directly if
#     independent; use P(A)*P(B|A) if dependent.

# A2. Binomial: a FIXED number of independent trials (n), counting
#     successes, with the same probability of success (p) each trial.
#     Example: number of heads in 10 coin flips.
#     Poisson: counts events over a fixed interval (time/space), given
#     an average rate (lambda), with NO fixed number of trials.
#     Example: number of customers arriving at a store per hour.

# A3. Sigma (standard deviation) controls the WIDTH of the bell curve.
#     Small sigma -> narrow, tall curve (data tightly clustered).
#     Large sigma -> wide, flat curve (data spread out).

# A4. A Z-score tells you how many standard deviations a value is from
#     the mean. Formula: z = (x - mean) / std

# A5. CLT: if you take many random samples from ANY population (any
#     shape, even skewed), and calculate the MEAN of each sample, those
#     sample means will form a Normal (bell-shaped) distribution --
#     regardless of the original population's shape, as long as sample
#     size is reasonably large (n>=30 rule of thumb). This matters
#     because it lets us use Normal-distribution-based tools (z-scores,
#     confidence intervals, hypothesis tests) on sample means even when
#     the underlying raw data isn't Normal at all.

# A6. Null hypothesis (H0): the default "no effect / no difference"
#     assumption. Alternative hypothesis (H1): the claim that there IS
#     a real effect or difference.
#     Example: testing a new drug's effect on blood pressure.
#     H0 = the drug has no effect on blood pressure.
#     H1 = the drug DOES lower blood pressure.

# A7. A p-value measures the probability of observing data this extreme
#     (or more extreme), ASSUMING the null hypothesis is true. It does
#     NOT directly measure whether H0 is true or false -- only how
#     surprising the observed data would be if H0 were true.

# A8. False. A p-value greater than 0.05 only means there isn't enough
#     evidence to REJECT H0 based on the current data -- it does NOT
#     prove H0 is true. "Fail to reject" is not the same as "proven true."

# A9. Point estimate: a single number guess (e.g. sample mean).
#     Interval estimate: a range of values, which honestly reflects
#     the uncertainty in the estimate (e.g. a confidence interval).

# A10. More likely Log-normal/Power law/Pareto (a skewed distribution),
#      not Normal -- a huge spike near zero with a long thin tail is
#      the signature shape of these skewed distributions, not a
#      symmetric bell curve. It matters because for skewed data, the
#      "average" (mean) gets badly distorted by a few extreme values,
#      making it a misleading summary of what's "typical" -- the median
#      is usually a more honest measure for this kind of data.


# =============================================================
# PART B — CALCULATION ANSWERS
# =============================================================

# B1
p_2_b1 = 1/6
p_5_b1 = 1/6
p_2_or_5_b1 = p_2_b1 + p_5_b1   # mutually exclusive, so just add
print("B1 P(2 or 5):", round(p_2_or_5_b1, 4))
print("B1: mutually exclusive (can't roll a 2 AND a 5 at once)")

# B2
n_b2, k_b2, p_b2 = 6, 4, 0.65
combination_b2 = math.comb(n_b2, k_b2)
p_success_b2 = p_b2 ** k_b2
p_failure_b2 = (1 - p_b2) ** (n_b2 - k_b2)
binomial_b2 = combination_b2 * p_success_b2 * p_failure_b2
print("\nB2 P(exactly 4 heads):", round(binomial_b2, 4))

# B3
lam_b3, k_b3 = 5, 3
lambda_power_b3 = lam_b3 ** k_b3
e_term_b3 = math.exp(-lam_b3)
k_factorial_b3 = math.factorial(k_b3)
poisson_b3 = (lambda_power_b3 * e_term_b3) / k_factorial_b3
print("\nB3 P(exactly 3 tickets):", round(poisson_b3, 4))

# B4
mean_b4, std_b4 = 100, 15
lower_b4 = mean_b4 - 2 * std_b4
upper_b4 = mean_b4 + 2 * std_b4
print(f"\nB4 95% range: ({lower_b4}, {upper_b4})")

# B5
x_b5 = 118
z_b5 = (x_b5 - mean_b4) / std_b4
print("\nB5 z-score:", round(z_b5, 4))

# B6
std_b6, n_b6 = 40, 64
se_b6 = std_b6 / np.sqrt(n_b6)
print("\nB6 standard error:", round(se_b6, 4))

# B7
p_value_b7, alpha_b7 = 0.03, 0.05
if p_value_b7 <= alpha_b7:
    print("\nB7: reject H0")
else:
    print("\nB7: fail to reject H0")
