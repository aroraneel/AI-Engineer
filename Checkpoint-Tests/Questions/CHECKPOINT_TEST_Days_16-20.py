"""
CHECKPOINT TEST — Days 16-20
Covers: Z-test & t-test (16), Type I/II Errors, Bayes' Theorem & Confidence
        Intervals (17), Chi-square Test (18), ANOVA (19), Capstone workflow (20)

RULES:
- No looking at your notes for Part A (conceptual questions) -- answer from memory.
- You MAY use your notes/previous task files for Part B (code) if truly stuck,
  but try from memory first.
- Write all answers directly in this file, in the spaces provided.
- This is a checkpoint, not a graded exam -- the point is to reveal what
  needs review before starting Phase 3.
"""

import numpy as np
from scipy import stats


# =============================================================
# PART A — CONCEPTUAL (answer in comments, no code needed)
# =============================================================

# A1. What's the key requirement that determines whether you use a
#     Z-test or a t-test? What happens to the t-distribution as sample
#     size grows?
# -> 


# A2. What is a Type I error? What is a Type II error? Give one
#     real-world example of each.
# -> 


# A3. In Bayes' theorem, what do the terms "prior," "likelihood," and
#     "posterior" mean? Write the formula from memory.
# -> 


# A4. Why can a "90% accurate" medical test still give a low probability
#     of actually having a disease after a positive result? What role
#     does the disease's rarity play?
# -> 


# A5. What does "95% confident" actually mean in a confidence interval?
#     What is the common misconception about this phrase?
# -> 


# A6. What happens to a confidence interval's width when you increase
#     the confidence level from 95% to 99%? What happens when you
#     increase the sample size?
# -> 


# A7. What type of data does a chi-square test work with? What does the
#     chi-square formula actually measure?
# -> 


# A8. What is the difference between a chi-square goodness-of-fit test
#     and a chi-square test of independence?
# -> 


# A9. What does ANOVA actually test for? Why is it preferred over
#     running many separate t-tests when comparing 3+ groups?
# -> 


# A10. What does a large F-statistic suggest about the relationship
#      between between-group variance and within-group variance?
# -> 


# A11. List the 4 assumptions that should hold for ANOVA to be valid.
# -> 


# A12. Given a real-world business question, what's the first thing you
#      should figure out before choosing a statistical test?
# -> 


# =============================================================
# PART B — CALCULATION (show your work in code)
# =============================================================

# B1. A gym claims its members lose an average of 5kg in 3 months, with
#     a KNOWN population std of 1.2kg. A sample of 50 members lost an
#     average of 5.4kg. Calculate the z-statistic and p-value. Using
#     alpha=0.05, reject or fail to reject H0?

# --- your code here ---




# B2. A rare genetic condition affects 1% of a population. A test is
#     85% accurate for people who HAVE the condition, with a 4% false
#     positive rate for people who DON'T. Calculate P(Condition |
#     Positive) using Bayes' theorem.

# --- your code here ---




# B3. A sample of 30 delivery times has a mean of 45 minutes and a
#     sample standard deviation of 8 minutes (population std unknown).
#     Calculate the 95% confidence interval using the t-distribution.

# --- your code here ---




# B4. A store expects daily sales to split evenly across 5 product
#     categories. Out of 250 total sales, the observed counts were:
#     [60, 45, 55, 40, 50]. Run a chi-square goodness-of-fit test.
#     Using alpha=0.05, reject or fail to reject H0?

# --- your code here ---




# B5. Three different marketing campaigns produced these conversion
#     rates (%) across independent customer groups:
campaign_a = np.array([2.1, 2.4, 1.9, 2.3, 2.0])
campaign_b = np.array([3.0, 2.8, 3.2, 2.9, 3.1])
campaign_c = np.array([2.2, 2.0, 2.5, 2.1, 2.3])
#     Run a one-way ANOVA. Using alpha=0.05, reject or fail to reject H0?

# --- your code here ---




# B6. Using stats.norm.interval(), calculate BOTH a 90% and a 99%
#     confidence interval for a sample with mean=100, standard
#     error=2.5. Print both. Which is wider?

# --- your code here ---




# =============================================================
# PART C — SCENARIO-BASED TEST SELECTION (no code, just reasoning)
# =============================================================

# For each scenario, state which test you would use and why.

# C1. Comparing average customer satisfaction scores across 5 different
#     store locations.
# -> 


# C2. Checking if a coin is fair after 200 flips resulted in 115 heads
#     (this is categorical/count data).
# -> 


# C3. A restaurant claims average wait time is 12 minutes. Population
#     std is unknown. A sample of 20 customers is measured.
# -> 


# C4. Comparing conversion rates between exactly 2 versions of a
#     checkout page, with independent visitor groups for each.
# -> 
