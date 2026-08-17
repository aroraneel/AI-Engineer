import numpy as np
from scipy import stats

# A rare disease affects 2% of a population (P(Disease) = 0.02).
# A test for the disease is 90% accurate for people who HAVE the disease
# (P(Positive | Disease) = 0.90), and has a 5% false positive rate for
# people who DON'T have the disease (P(Positive | No Disease) = 0.05).
P_Disease = 0.02 
P_Positive_Disease = 0.90
P_Positive_No_Disease = 0.05
p_no_disease = 1 - P_Disease

# 2a. Calculate P(Positive) -- the overall probability of testing positive.
#     Hint: P(Positive) = P(Positive|Disease)*P(Disease) +
#                          P(Positive|No Disease)*P(No Disease)
P_Positive = (P_Positive_Disease* P_Disease) + (P_Positive_No_Disease * p_no_disease)

# 2b. Calculate P(Disease | Positive) using Bayes' theorem:
#     P(Disease|Positive) = [P(Positive|Disease) * P(Disease)] / P(Positive)
P_Disease_Positive = (P_Positive_Disease * P_Disease) / P_Positive

# 2c. Print the result (rounded to 4 decimal places)
print(round(P_Disease_Positive,4))

# 2d. In a comment: is this number surprising given the test is "90%
#     accurate"? Why does the disease's rarity matter so much here?
# -> Yes, this is surprising: even with 90% test accuracy, only
#    ~27% of positive results are truly sick. This is because the
#    disease is so rare (2%) that the healthy population (98%) is
#    huge -- even a small 5% false positive rate on that large
#    group produces MORE false positives than true positives from
#    the small sick group.