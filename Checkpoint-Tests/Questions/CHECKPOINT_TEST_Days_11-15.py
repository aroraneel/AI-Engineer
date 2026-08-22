"""
CHECKPOINT TEST — Days 11-15
Covers: Probability fundamentals & Bernoulli (11), Binomial & Poisson (12),
        Normal/Z-score/Uniform (13), Skewed distributions & CLT (14),
        Estimation/Hypothesis testing/p-values (15)

RULES:
- No looking at your notes for Part A (conceptual questions) -- answer from memory.
- You MAY use your notes/previous task files for Part B (code) if truly stuck,
  but try from memory first.
- Write all answers directly in this file, in the spaces provided.
- This is a checkpoint, not a graded exam -- the point is to reveal what
  needs review before moving to Day 16.
"""

import numpy as np
from scipy import stats


# =============================================================
# PART A — CONCEPTUAL (answer in comments, no code needed)
# =============================================================

# A1. What is the difference between the addition rule and the
#     multiplication rule? When do you use each one?
# -> 


# A2. What's the difference between a Binomial distribution and a
#     Poisson distribution? Give one real-world example of each.
# -> 


# A3. In the Normal distribution formula, what does the standard
#     deviation (sigma) control? What happens to the curve's shape
#     when sigma is very small vs very large?
# -> 


# A4. What does a Z-score tell you? Write the formula from memory.
# -> 


# A5. What is the Central Limit Theorem, in your own words? Why does
#     it matter even when the original population isn't Normal?
# -> 


# A6. What is a null hypothesis (H0)? What is an alternative hypothesis
#     (H1)? Give an example of each for a scenario of your choosing.
# -> 


# A7. What does a p-value actually measure? (Be precise -- this is
#     commonly misunderstood.)
# -> 


# A8. True or False, and explain why: "A p-value greater than 0.05
#     proves the null hypothesis is true."
# -> 


# A9. What's the difference between a point estimate and an interval
#     estimate?
# -> 


# A10. A dataset shows a huge spike near zero and a long thin tail
#      stretching far right (like income or city populations). Is this
#      more likely Normal, or Log-normal/Power law/Pareto? Why does it
#      matter which one you assume when calculating "average"?
# -> 


# =============================================================
# PART B — CALCULATION (show your work in code)
# =============================================================

# B1. A fair 6-sided die is rolled once. Calculate P(rolling a 2 OR a 5).
#     State whether these events are mutually exclusive.

# --- your code here ---




# B2. A biased coin has P(heads) = 0.65. It's flipped 6 times.
#     Calculate P(exactly 4 heads) using the binomial formula
#     (you may use math.comb or scipy).

# --- your code here ---




# B3. A support center receives on average lambda=5 tickets per hour.
#     Calculate P(exactly 3 tickets in an hour) using the Poisson formula.

# --- your code here ---




# B4. A dataset has mean=100, std=15 (Normal distribution).
#     Calculate the range that covers 95% of the data using the
#     empirical rule.

# --- your code here ---




# B5. Using the same dataset (mean=100, std=15), calculate the z-score
#     for a value of x=118.

# --- your code here ---




# B6. A population has std=40. Calculate the standard error for a
#     sample size of n=64.

# --- your code here ---




# B7. A p-value of 0.03 is obtained, using alpha=0.05. Do you reject or
#     fail to reject H0? Print your answer.

# --- your code here ---