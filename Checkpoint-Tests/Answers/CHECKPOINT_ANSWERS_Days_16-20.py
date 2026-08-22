"""
CHECKPOINT TEST — Days 16-20 — ANSWER SHEET
Covers: Z-test & t-test (16), Type I/II Errors, Bayes' Theorem & Confidence
        Intervals (17), Chi-square Test (18), ANOVA (19), Capstone workflow (20)

This is the corrected, complete answer key for CHECKPOINT_TEST_Days_16-20.py
"""

import numpy as np
from scipy import stats


# =============================================================
# PART A — CONCEPTUAL ANSWERS
# =============================================================

# A1. Z-test requires the population standard deviation to be KNOWN.
#     t-test is used when population std is UNKNOWN and must be
#     estimated from the sample instead. As sample size grows, the
#     t-distribution's tails SHRINK and it converges toward looking
#     like the Normal distribution -- a larger sample gives a more
#     reliable estimate of the population's spread, needing less
#     "extra caution" in the tails.

# A2. Type I error = a false positive: rejecting H0 when it is
#     actually TRUE. Type II error = a false negative: failing to
#     reject H0 when it is actually FALSE.
#     Example (Type I): a spam filter marks a legitimate email as spam
#     (H0 = "not spam" was true, wrongly rejected).
#     Example (Type II): a spam filter lets real spam through to the
#     inbox (H0 = "not spam" was false, failed to reject it).

# A3. P(A) = prior (belief before any evidence).
#     P(B|A) = likelihood (how likely the evidence is, given the
#     scenario is true).
#     P(A|B) = posterior (updated belief, after seeing the evidence).
#     Formula: P(A|B) = [P(B|A) * P(A)] / P(B)

# A4. Split 100,000 people using the population's disease rate (e.g.
#     2%): 2,000 have the disease, 98,000 don't.
#     Of the 2,000 sick: 90% test positive = 1,800 true positives.
#     Of the 98,000 healthy: 5% test positive = 4,900 false positives.
#     Total positives = 1,800 + 4,900 = 6,700.
#     P(Disease|Positive) = 1,800/6,700 ~= 0.2687 (27%), NOT 90%.
#     The disease's rarity matters because even a small false-positive
#     rate applied to a huge healthy population produces more false
#     alarms than true detections from the small sick population.

# A5. "95% confident" means: if you repeated the sampling process many
#     times, building a new confidence interval each time, 95% of
#     those intervals would contain the true population value.
#     Common misconception: thinking it means "there's a 95% chance
#     the true value is in THIS ONE specific interval" -- but the true
#     value is a fixed number, already either in or out once the
#     interval is calculated. It's a statement about the reliability
#     of the METHOD across repeated sampling, not a probability about
#     any single interval.

# A6. Increasing confidence level (95% -> 99%) makes the interval
#     WIDER -- more room needed to be more certain of capturing the
#     true value. Increasing sample size makes the interval NARROWER
#     -- more data shrinks the standard error (sigma/sqrt(n)), giving
#     a more precise estimate that needs less room.

# A7. Chi-square works with CATEGORICAL data (counts/frequencies in
#     categories). The formula chi^2 = sum[(Observed-Expected)^2 /
#     Expected] measures how far observed counts are from expected
#     counts, scaled relative to the expected size, summed across all
#     categories.

# A8. Goodness-of-fit test compares ONE categorical variable's
#     observed distribution against an EXPECTED distribution.
#     Test of independence compares TWO categorical variables to see
#     if they are related/dependent on each other.

# A9. ANOVA tests whether the means of 3+ groups are all equal, using
#     ONE single test. It's preferred over running many separate
#     t-tests because each t-test carries its own Type I error risk
#     (e.g. 5%), and running many of them stacks that risk up --
#     6 separate tests can push the TRUE overall error rate to ~26%,
#     far above the intended 5%. ANOVA keeps the true error rate at
#     the intended level by testing everything in one single test.

# A10. A large F-statistic means between-group variance is much bigger
#      than within-group variance -- group averages are spread apart
#      MORE than ordinary random scatter would explain. This suggests
#      the group means are likely DIFFERENT from each other, leading
#      to a small p-value and rejecting H0.

# A11. 1. Independence  2. Normality  3. Homogeneity of variance
#      (equal variance across groups)  4. Random sampling

# A12. First figure out the DATA TYPE (numeric or categorical) and
#      the NUMBER OF GROUPS being compared -- this determines which
#      test applies (per the Day 20 decision tree). Only after that
#      should H0/H1 be written, based on the chosen test's structure.


# =============================================================
# PART B — CALCULATION ANSWERS
# =============================================================

# B1. Z-test
sample_mean_B1 = 5.4
pop_mean_B1 = 5
pop_std_B1 = 1.2
n_B1 = 50
alpha_b1 = 0.05

z_statistic_B1 = (sample_mean_B1 - pop_mean_B1) / (pop_std_B1 / np.sqrt(n_B1))
p_value_B1 = 2 * (1 - stats.norm.cdf(abs(z_statistic_B1)))

print("B1 z-statistic:", round(z_statistic_B1, 4))
print("B1 p-value:", round(p_value_B1, 4))

if p_value_B1 <= alpha_b1:
    print("B1: reject H0")
else:
    print("B1: fail to reject H0")
# Expected: z ~= 2.357, p ~= 0.0184 -> reject H0. Strong evidence the
# true average weight loss differs from the claimed 5kg.


# B2. Bayes' Theorem
p_disease_b2 = 0.01
p_positive_disease_b2 = 0.85
p_positive_no_disease_b2 = 0.04
p_no_disease_b2 = 1 - p_disease_b2

p_positive_b2 = (p_positive_disease_b2 * p_disease_b2) + \
                (p_positive_no_disease_b2 * p_no_disease_b2)

p_disease_positive_b2 = (p_positive_disease_b2 * p_disease_b2) / p_positive_b2

print("B2 P(Condition|Positive):", round(p_disease_positive_b2, 4))
# Result: ~= 0.1767 (about 17.7%) -- again, far below the test's
# "85% accurate" framing, due to the condition's rarity (1%).


# B3. Confidence Interval (t-distribution, since population std unknown)
n_b3 = 30
sample_std_b3 = 8
sample_mean_b3 = 45

standard_error_b3 = sample_std_b3 / np.sqrt(n_b3)

CI_95_b3 = stats.t.interval(confidence=0.95, df=n_b3 - 1,
                             loc=sample_mean_b3, scale=standard_error_b3)
print("B3 95% CI (t-distribution):", CI_95_b3)
# Expected: approximately (41.99, 48.01)
# Uses stats.t.interval(), NOT stats.norm.interval(), because
# population std is unknown -- matches the Z-test vs t-test rule.


# B4. Chi-square goodness-of-fit
observed_b4 = np.array([60, 45, 55, 40, 50])
n_total_b4 = 250
n_categories_b4 = 5
alpha_b4 = 0.05

expected_b4 = np.array([n_total_b4 / n_categories_b4] * n_categories_b4)

chi2_scipy_b4, p_value_scipy_b4 = stats.chisquare(f_obs=observed_b4, f_exp=expected_b4)

print("B4 chi2:", round(chi2_scipy_b4, 4))
print("B4 p-value:", round(p_value_scipy_b4, 4))

if p_value_scipy_b4 <= alpha_b4:
    print("B4: reject H0")
else:
    print("B4: fail to reject H0")
# Result: chi2 = 5.0, p ~= 0.2873 -> fail to reject H0. No significant
# evidence the sales distribution differs from an even split.


# B5. One-way ANOVA
campaign_a = np.array([2.1, 2.4, 1.9, 2.3, 2.0])
campaign_b = np.array([3.0, 2.8, 3.2, 2.9, 3.1])
campaign_c = np.array([2.2, 2.0, 2.5, 2.1, 2.3])
alpha_b5 = 0.05

f_statistic_b5, p_value_b5 = stats.f_oneway(campaign_a, campaign_b, campaign_c)

print("B5 F-statistic:", round(f_statistic_b5, 4))
print("B5 p-value:", round(p_value_b5, 4))

if p_value_b5 <= alpha_b5:
    print("B5: reject H0")
else:
    print("B5: fail to reject H0")
# Expected: large F, very small p -> reject H0. Campaign B clearly
# stands out with higher conversion rates than A and C.


# B6. Confidence interval width comparison
sample_mean_b6 = 100
standard_error_b6 = 2.5

CI_90_b6 = stats.norm.interval(confidence=0.90, loc=sample_mean_b6, scale=standard_error_b6)
CI_99_b6 = stats.norm.interval(confidence=0.99, loc=sample_mean_b6, scale=standard_error_b6)

print("B6 CI-90%:", CI_90_b6)
print("B6 CI-99%:", CI_99_b6)
# The 99% CI is wider than the 90% CI -- higher confidence requires a
# wider interval to be more certain of capturing the true value.


# =============================================================
# PART C — SCENARIO-BASED TEST SELECTION ANSWERS
# =============================================================

# C1. One-way ANOVA -- comparing means across 5 independent groups
#     (store locations), numeric data (satisfaction scores).

# C2. Chi-square goodness-of-fit -- categorical/count data (heads vs
#     tails), checking observed counts against an expected even split.

# C3. One-sample t-test -- one numeric sample compared against a
#     claimed value, population std unknown.

# C4. Two-sample (independent) t-test -- comparing exactly 2
#     independent groups. NOT ANOVA, since ANOVA is specifically for
#     3+ groups; with only 2 groups, a two-sample t-test is the
#     correct and more standard choice.
