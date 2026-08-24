"""
PHASE 2 CUMULATIVE TEST — Days 11-20 (Probability & Inference)
Covers: Probability Fundamentals & Bernoulli, Binomial & Poisson, Normal/
        Z-score/Uniform, Skewed Distributions & CLT, Estimation & p-values,
        Z-test/t-test, Type I-II Errors/Bayes/CI, Chi-square, ANOVA, and
        the full hypothesis-testing workflow

RULES:
- This is a BIGGER test than the 5-day checkpoints -- it covers the entire
  phase and mixes topics together, the way a real interview or project would.
- Attempt Part A completely from memory first.
- Part B is a mini end-to-end project -- treat it like a real task, choosing
  the right test yourself (nothing is labeled for you).
- This is a checkpoint, not a graded exam -- the point is to reveal what
  needs review before starting Phase 3.

SETUP:
- pip install numpy scipy (if not already installed)
"""

import numpy as np
import math
from scipy import stats


# =============================================================
# PART A — CONCEPTUAL REVIEW (mixed, from memory)
# =============================================================

# A1. Walk through the full chain of distributions in the order you
#     learned them: Bernoulli -> Binomial -> Poisson -> Normal ->
#     Uniform. For each, state in one sentence what makes it distinct
#     from the one before it.
# -> 


# A2. Explain the Central Limit Theorem using a concrete example (not
#     just the definition) -- and explain why it's the foundation for
#     nearly everything covered in Days 15-20.
# -> 


# A3. You calculate a p-value of 0.001. Explain, precisely, what this
#     number does and does NOT tell you about the null hypothesis.
# -> 


# A4. A dataset has a small sample size (n=12) and the population
#     standard deviation is unknown. Walk through, step by step, which
#     test you'd use and why -- referencing the underlying distribution.
# -> 


# A5. Explain, using the 100,000-person breakdown technique, why a
#     highly accurate medical test can still produce a low probability
#     of actually having a rare condition after a positive result.
# -> 


# A6. What is the difference between a confidence interval and a
#     hypothesis test? Explain how a 95% CI not containing a claimed
#     value connects to rejecting H0 at alpha=0.05.
# -> 


# A7. Explain the difference between a Type I and Type II error using
#     the courtroom analogy (innocent until proven guilty). Which type
#     does lowering alpha reduce, and what's the tradeoff?
# -> 


# A8. What's the difference between a chi-square goodness-of-fit test
#     and a one-way ANOVA? Both can involve multiple categories/groups
#     -- what's the key distinction in what kind of data and question
#     each one handles?
# -> 


# A9. Why does running 5 separate t-tests to compare 5 groups increase
#     your risk of a false positive, and how does ANOVA solve this?
# -> 


# A10. Walk through the FULL decision framework from Day 20: given any
#      real-world dataset and question, what's the step-by-step process
#      for choosing the right statistical test?
# -> 


# =============================================================
# PART B — MINI PROJECT (choose your own test, end-to-end)
# =============================================================

# You're analyzing data for "BrewHouse", a fictional coffee chain
# considering several operational changes. For EACH task below: state
# which test applies and why, write H0/H1, run the test, and interpret
# the result in plain English -- exactly like the Day 20 capstone.


# --- TASK B1 ---
# BrewHouse claims average customer wait time is 4 minutes, with a
# KNOWN population standard deviation of 1.1 minutes (from years of
# monitoring). A sample of 60 customers this week averaged 4.35 minutes.
# Has wait time actually changed?

# --- your code here ---




# --- TASK B2 ---
# BrewHouse tested two loyalty program designs and tracked monthly
# spend ($) for members who joined under each design (population std
# UNKNOWN):
program_a = np.array([45, 52, 38, 60, 48, 55, 42, 50, 47, 53])
program_b = np.array([62, 58, 65, 70, 60, 68, 64, 59, 66, 63])
# Does one program lead to higher average monthly spend?

# --- your code here ---




# --- TASK B3 ---
# BrewHouse's inventory team historically assumes syrup flavor orders
# split evenly across 4 flavors: Vanilla, Caramel, Hazelnut, Mocha.
# This month, out of 320 total syrup orders, the actual counts were:
observed_flavors = np.array([100, 70, 60, 90])
# Does this month's distribution match the historical assumption?

# --- your code here ---




# --- TASK B4 ---
# BrewHouse wants to know if average daily revenue ($) differs across
# 3 store locations:
store_downtown = np.array([1450, 1520, 1380, 1490, 1510, 1460])
store_mall = np.array([1200, 1250, 1180, 1220, 1240, 1210])
store_airport = np.array([1800, 1850, 1780, 1820, 1790, 1830])
# Do these 3 locations have significantly different average revenue?

# --- your code here ---




# --- TASK B5 ---
# BrewHouse ran a small pilot testing a new espresso machine on 8
# specific days, comparing the SAME store's daily sales BEFORE
# installing it vs AFTER installing it (same store, same days of week,
# matched pairs):
before_machine = np.array([1200, 1250, 1180, 1300, 1220, 1260, 1190, 1240])
after_machine = np.array([1280, 1310, 1250, 1360, 1290, 1320, 1260, 1300])
# Did installing the new machine significantly change daily sales?
# (Hint: this is a different structure than B2 -- same subjects,
# measured twice. Think about which t-test variant applies.)

# --- your code here ---




# --- TASK B6 ---
# Using a 95% confidence interval, estimate the true average customer
# wait time using this week's sample: mean=4.35 minutes, KNOWN
# population std=1.1 minutes, n=60 (same data as B1).

# --- your code here ---




# --- TASK B7 ---
# Write a short summary report (as comments) presenting all 5 findings
# (B1-B5) to BrewHouse's leadership team. For each, include: the
# business question, the test used, the result, and the plain-English
# conclusion. Close with 1-2 sentences on what BrewHouse should
# prioritize acting on first.

# --- your written report here ---
