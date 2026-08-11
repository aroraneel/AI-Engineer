import numpy as np
from scipy import stats

# For each scenario, use the rule (p <= alpha -> reject H0, else fail to
# reject) to decide the outcome, then print it. alpha = 0.05 for all.
alpha = 0.05

# 3a. p-value = 0.001 -- print whether to reject or fail to reject H0
p_value_3a = 0.001

if p_value_3a <= alpha:
    print("p-value = 0.001 reject H0")
else:
    print("p-value = 0.001 fail to reject H0")

# 3b. p-value = 0.20  -- print whether to reject or fail to reject H0
p_value_3b = 0.20

if p_value_3b <= alpha:
    print("p-value = 0.20 reject H0")
else:
    print("p-value = 0.20 fail to reject H0")

# 3c. p-value = 0.05  -- print whether to reject or fail to reject H0
p_value_3c = 0.05

if p_value_3c <= alpha:
    print("p-value = 0.05 reject H0")
else:
    print("p-value = 0.05 fail to reject H0")