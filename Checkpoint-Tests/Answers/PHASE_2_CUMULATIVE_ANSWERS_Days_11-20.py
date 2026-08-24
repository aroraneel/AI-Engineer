"""
PHASE 2 CUMULATIVE TEST — Days 11-20 — ANSWER SHEET
Covers: Probability Fundamentals & Bernoulli, Binomial & Poisson, Normal/
        Z-score/Uniform, Skewed Distributions & CLT, Estimation & p-values,
        Z-test/t-test, Type I-II Errors/Bayes/CI, Chi-square, ANOVA, and
        the full hypothesis-testing workflow
"""

import numpy as np
import math
from scipy import stats


# =============================================================
# PART A — CONCEPTUAL ANSWERS
# =============================================================

# A1. Bernoulli -> one single trial, two outcomes.
#     Binomial -> Bernoulli repeated a FIXED number of times, counting
#     successes (adds the idea of "n trials").
#     Poisson -> like Binomial's counting idea, but no fixed n --
#     instead counts events over a continuous interval given a rate.
#     Normal -> the first CONTINUOUS distribution (not counting discrete
#     events anymore) -- models measurements clustering around a mean.
#     Uniform -> also continuous, but unlike Normal, every value in a
#     range is EQUALLY likely (no clustering around a center at all).

# A2. Example: take random samples of 30 customers from a population
#     with wildly skewed purchase amounts (a few huge spenders, mostly
#     small purchases). Calculate the mean spend of each sample,
#     repeated many times. Even though INDIVIDUAL purchases are skewed,
#     the distribution of SAMPLE MEANS will still form a Normal bell
#     curve. This is foundational for Days 15-20 because Z-tests,
#     t-tests, confidence intervals, and ANOVA all rely on sample means
#     behaving predictably (Normal-ish) -- without CLT, none of these
#     tools would be mathematically justified to use on real data,
#     which is rarely perfectly Normal to begin with.

# A3. A p-value of 0.001 tells you: IF the null hypothesis were true,
#     there would only be a 0.1% chance of observing data this extreme
#     (or more extreme) purely by random chance. It does NOT tell you
#     the probability that H0 is true or false, and it does NOT tell
#     you the size/importance of the effect -- only how surprising the
#     data would be under the assumption that H0 holds.

# A4. Small sample (n=12) and unknown population std -> use a
#     ONE-SAMPLE T-TEST (if comparing against a claimed value) or
#     TWO-SAMPLE T-TEST (if comparing two independent groups). Since
#     population std is unknown, it must be ESTIMATED from the sample,
#     which introduces extra uncertainty -- this is why the
#     STUDENT'S T-DISTRIBUTION is used instead of Normal: it has fatter
#     tails to account for that uncertainty, especially pronounced with
#     small n. As n grows, the t-distribution converges toward Normal.

# A5. Example: disease affects 2% of a population, test is 90% accurate
#     for sick people, 5% false positive rate for healthy people.
#     Split 100,000 people: 2,000 sick, 98,000 healthy.
#     Of the 2,000 sick: 90% test positive = 1,800 true positives.
#     Of the 98,000 healthy: 5% test positive = 4,900 false positives.
#     Total positives = 1,800 + 4,900 = 6,700.
#     P(Disease|Positive) = 1,800/6,700 ~= 27%, NOT 90%.
#     Even a highly accurate test produces mostly false positives when
#     applied to a rare condition, because the healthy population is so
#     much larger that even a small false-positive rate on it generates
#     more false alarms than the small sick population generates true
#     detections.

# A6. A confidence interval gives a RANGE likely to contain the true
#     population parameter, at a stated confidence level. A hypothesis
#     test gives a binary decision (reject/fail to reject H0) about
#     whether a specific claimed value is plausible. They're two views
#     of the same underlying math: if a 95% CI does NOT contain the
#     value claimed by H0, that's mathematically equivalent to
#     rejecting H0 at alpha=0.05 -- both are asking "is this claimed
#     value consistent with what the data shows," just presented
#     differently (a range vs a yes/no decision).

# A7. Courtroom analogy: H0 = "innocent" (the default assumption).
#     Type I error = convicting an innocent person (false alarm --
#     rejecting a TRUE H0). Type II error = letting a guilty person go
#     free (missed detection -- failing to reject a FALSE H0).
#     Lowering alpha (e.g. 0.05 -> 0.01) reduces Type I error risk (you
#     become more conservative about rejecting H0, so fewer innocent
#     people get wrongly convicted). The tradeoff: this INCREASES Type
#     II error risk -- you become more likely to miss real, guilty
#     effects, since you're demanding stronger evidence before acting.

# A8. Chi-square goodness-of-fit tests whether ONE CATEGORICAL
#     variable's observed distribution matches an EXPECTED distribution
#     -- it works with counts/frequencies in categories, not numeric
#     measurements. One-way ANOVA tests whether the MEANS of 3+
#     independent groups (based on NUMERIC/continuous data) are equal.
#     The key distinction: chi-square is about category COUNTS fitting
#     an expected pattern; ANOVA is about comparing numeric AVERAGES
#     across groups.

# A9. Each t-test carries its own Type I error risk (e.g. 5% at
#     alpha=0.05). Running 5 separate pairwise t-tests means that 5%
#     risk compounds/stacks across all 5 tests -- the TRUE overall
#     chance of at least one false positive somewhere climbs well above
#     5% (with 5 tests, ballpark ~23%). ANOVA solves this by testing all
#     groups together in ONE single test, keeping the true error rate
#     at the intended alpha level, rather than inflating it through
#     repeated testing.

# A10. Step-by-step decision framework:
#      1. Identify the DATA TYPE (numeric/continuous, or categorical/counts)
#      2. If categorical -> chi-square (goodness-of-fit for one variable,
#         independence test for two variables)
#      3. If numeric -> count how many GROUPS are being compared:
#         - 1 group vs a known/claimed value -> Z-test (if population std
#           known) or one-sample t-test (if unknown)
#         - 2 independent groups -> two-sample t-test
#         - 2 measurements on the SAME subjects -> paired t-test
#         - 3+ groups -> one-way ANOVA
#      4. State H0/H1 clearly in plain English BEFORE writing code
#      5. Check relevant assumptions (normality, independence, equal
#         variance) where applicable
#      6. Run the test, get the test statistic and p-value
#      7. Apply the decision rule (p <= alpha -> reject H0)
#      8. Translate the statistical result into a plain-English,
#         actionable conclusion, noting any caveats


# =============================================================
# PART B — MINI PROJECT ANSWERS
# =============================================================

# --- TASK B1 — Z-test ---
# Data type: numeric. Comparing 1 sample vs a known claimed value.
# Population std KNOWN (1.1 min) -> Z-test.
# H0: true average wait time = 4 minutes (matches the claim)
# H1: true average wait time != 4 minutes

sample_mean_b1 = 4.35
pop_mean_b1 = 4
pop_std_b1 = 1.1
n_b1 = 60
alpha = 0.05

z_b1 = (sample_mean_b1 - pop_mean_b1) / (pop_std_b1 / np.sqrt(n_b1))
p_value_b1 = 2 * (1 - stats.norm.cdf(abs(z_b1)))

print("=" * 60)
print("TASK B1: Wait time Z-test")
print("=" * 60)
print("z-statistic:", round(z_b1, 4))
print("p-value:", round(p_value_b1, 4))
if p_value_b1 <= alpha:
    print("Result: reject H0")
else:
    print("Result: fail to reject H0")
# Finding: z ~= 2.464, p ~= 0.0137 -> reject H0. There is statistically
# significant evidence that average wait time has increased from the
# claimed 4 minutes, consistent with this week's 4.35 minute average.


# --- TASK B2 — Two-sample (independent) t-test ---
# Data type: numeric. Two INDEPENDENT groups, population std unknown.
# H0: no difference in true average monthly spend between Program A and B
# H1: there IS a difference in true average monthly spend

program_a = np.array([45, 52, 38, 60, 48, 55, 42, 50, 47, 53])
program_b = np.array([62, 58, 65, 70, 60, 68, 64, 59, 66, 63])

t_stat_b2, p_value_b2 = stats.ttest_ind(program_a, program_b)

print("\n" + "=" * 60)
print("TASK B2: Loyalty program two-sample t-test")
print("=" * 60)
print("t-statistic:", round(t_stat_b2, 4))
print("p-value:", round(p_value_b2, 4))
if p_value_b2 <= alpha:
    print("Result: reject H0")
else:
    print("Result: fail to reject H0")
# Finding: strong evidence of a real difference (very small p-value).
# Program B leads to consistently higher average monthly spend than
# Program A -- BrewHouse should consider adopting Program B.


# --- TASK B3 — Chi-square goodness-of-fit ---
# Data type: categorical (flavor counts). Checking ONE variable's
# distribution against an expected even split.
# H0: syrup flavor orders ARE evenly split across the 4 flavors
# H1: syrup flavor orders are NOT evenly split

observed_flavors = np.array([100, 70, 60, 90])
n_total_b3 = 320
n_categories_b3 = 4
expected_flavors = np.array([n_total_b3 / n_categories_b3] * n_categories_b3)

chi2_b3, p_value_b3 = stats.chisquare(f_obs=observed_flavors, f_exp=expected_flavors)

print("\n" + "=" * 60)
print("TASK B3: Syrup flavor chi-square goodness-of-fit")
print("=" * 60)
print("chi2-statistic:", round(chi2_b3, 4))
print("p-value:", round(p_value_b3, 4))
if p_value_b3 <= alpha:
    print("Result: reject H0")
else:
    print("Result: fail to reject H0")
# Finding: significant evidence flavors are NOT evenly split. Vanilla
# (100) and Mocha (90) are ordered notably more than Hazelnut (60) --
# BrewHouse should consider adjusting syrup inventory allocation.


# --- TASK B4 — One-way ANOVA ---
# Data type: numeric. Comparing 3+ independent groups (3 store locations).
# H0: true average revenue is EQUAL across all 3 stores
# H1: at least ONE store's true average revenue differs from the others

store_downtown = np.array([1450, 1520, 1380, 1490, 1510, 1460])
store_mall = np.array([1200, 1250, 1180, 1220, 1240, 1210])
store_airport = np.array([1800, 1850, 1780, 1820, 1790, 1830])

f_stat_b4, p_value_b4 = stats.f_oneway(store_downtown, store_mall, store_airport)

print("\n" + "=" * 60)
print("TASK B4: Store revenue ANOVA")
print("=" * 60)
print("F-statistic:", round(f_stat_b4, 4))
print("p-value:", round(p_value_b4, 4))
if p_value_b4 <= alpha:
    print("Result: reject H0")
else:
    print("Result: fail to reject H0")
# Finding: extremely strong evidence of a real difference (huge F,
# tiny p). Airport location has clearly the highest average revenue,
# Mall the lowest -- worth investigating what's driving the gap
# (foot traffic, pricing, location type).


# --- TASK B5 — Paired t-test ---
# Data type: numeric. SAME store, measured twice (before/after) --
# NOT independent groups, so this needs a PAIRED t-test, not
# ttest_ind(). This is the key "trick" of this task.
# H0: no difference in true average sales before vs after installing
#     the new machine
# H1: there IS a difference (sales changed after installation)

before_machine = np.array([1200, 1250, 1180, 1300, 1220, 1260, 1190, 1240])
after_machine = np.array([1280, 1310, 1250, 1360, 1290, 1320, 1260, 1300])

t_stat_b5, p_value_b5 = stats.ttest_rel(before_machine, after_machine)

print("\n" + "=" * 60)
print("TASK B5: New espresso machine PAIRED t-test")
print("=" * 60)
print("t-statistic:", round(t_stat_b5, 4))
print("p-value:", round(p_value_b5, 4))
if p_value_b5 <= alpha:
    print("Result: reject H0")
else:
    print("Result: fail to reject H0")
# Finding: strong evidence of a real increase in sales after installing
# the new machine (small p-value, consistent increase across all 8
# days). BrewHouse should consider rolling out the new machine more
# broadly.
# NOTE: using ttest_ind() here instead of ttest_rel() would be the
# WRONG test, since it ignores that these are the same store measured
# twice (correlated data), not two independent groups.


# --- TASK B6 — Confidence Interval ---
sample_mean_b6 = 4.35
pop_std_b6 = 1.1
n_b6 = 60
standard_error_b6 = pop_std_b6 / np.sqrt(n_b6)

CI_95_b6 = stats.norm.interval(confidence=0.95, loc=sample_mean_b6, scale=standard_error_b6)

print("\n" + "=" * 60)
print("TASK B6: Wait time 95% Confidence Interval")
print("=" * 60)
print("95% CI:", CI_95_b6)
# Finding: we are 95% confident the true average wait time falls
# between approximately 4.07 and 4.63 minutes -- notably, this range
# does NOT include the originally claimed 4 minutes, consistent with
# B1's rejection of H0.


# --- TASK B7 — Summary Report ---
print("""
============================================================
TASK B7: Summary Report for BrewHouse Leadership
============================================================

1. Customer Wait Time
   Question: Has average wait time changed from the claimed 4 minutes?
   Test: Z-test (population std known)
   Result: z=2.464, p=0.0137 -> reject H0
   Finding: Wait time has significantly increased to ~4.35 minutes
   (95% CI: 4.07-4.63 min), consistent with a real, not random, shift.

2. Loyalty Program Comparison
   Question: Does Program A or B lead to higher average monthly spend?
   Test: Two-sample (independent) t-test
   Result: strong evidence of a difference -> reject H0
   Finding: Program B members spend significantly more on average.

3. Syrup Flavor Distribution
   Question: Does this month's flavor mix match the historical even split?
   Test: Chi-square goodness-of-fit
   Result: significant evidence of a mismatch -> reject H0
   Finding: Vanilla and Mocha are ordered more than expected, Hazelnut
   less -- inventory allocation may need adjusting.

4. Store Location Revenue
   Question: Do the 3 store locations have different average revenue?
   Test: One-way ANOVA
   Result: very strong evidence of a difference -> reject H0
   Finding: Airport location significantly outperforms Downtown and
   Mall -- worth investigating what's driving the gap.

5. New Espresso Machine Pilot
   Question: Did the new machine change daily sales at the pilot store?
   Test: Paired t-test (same store, before/after)
   Result: strong evidence of an increase -> reject H0
   Finding: Sales increased consistently across all 8 measured days
   after installation.

Overall Recommendation:
The new espresso machine pilot (finding 5) and the loyalty program
comparison (finding 2) represent the clearest, most actionable
opportunities -- both show strong, consistent evidence and a
straightforward next step (roll out the machine more broadly; promote
Program B). The store revenue gap (finding 4) deserves a deeper
investigation before any pricing or staffing changes, since the cause
isn't yet known. The wait time increase (finding 1) is worth monitoring
operationally, and the flavor mix shift (finding 3) is a lower-urgency
inventory adjustment.
""")
