import numpy as np
from scipy import stats

# A company tests 3 different ad designs and measures click-through
# rates (as percentages) across independent groups of users:
design_a = np.array([2.1, 2.4, 1.9, 2.3, 2.0, 2.2])
design_b = np.array([3.5, 3.2, 3.8, 3.6, 3.4, 3.7])
design_c = np.array([2.2, 2.0, 2.5, 2.1, 2.3, 1.9])
 
# 1a. Use stats.f_oneway(design_a, design_b, design_c) to run a one-way
#     ANOVA test. This returns an F-statistic and a p-value.
f_statistic, p_value = stats.f_oneway(design_a, design_b, design_c)

# 1b. Print both values
print("F-statistic: ", round(f_statistic, 4))
print("p-value: ", round(p_value, 4))

# 1c. In a comment: using alpha=0.05, do you reject or fail to reject
#     H0? What does that suggest about the 3 ad designs?
alpha = 0.05

if p_value <= alpha:
    print("reject H0")
else:
    print("fail to reject H0")

# -> Since p-value (~0.0) is far less than alpha (0.05), we reject H0.
#    There is strong evidence that at least one of the 3 ad designs has
#    a significantly different average click-through rate from the
#    others -- looking at the raw data, Design B's rates (3.2-3.8%) are
#    clearly higher than Design A and C (both roughly 1.9-2.5%).