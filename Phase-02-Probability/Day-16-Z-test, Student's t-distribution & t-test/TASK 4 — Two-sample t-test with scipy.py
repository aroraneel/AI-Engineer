import numpy as np
from scipy import stats

# A company wants to know if Website Design A gets a different average
# time-on-page than Website Design B. Two independent samples (in
# seconds) were collected:
design_a = np.array([45, 52, 48, 41, 50, 46, 44, 49, 47, 51])
design_b = np.array([55, 60, 58, 62, 57, 59, 61, 56, 63, 58])
 
# 4a. Use stats.ttest_ind(design_a, design_b) to run an independent
#     two-sample t-test. This returns a t-statistic and a p-value.
t_statistics, p_value = stats.ttest_ind(design_a, design_b)

# 4b. Print both values
print("t-statistics: ", t_statistics)
print("p-value", p_value)

# 4c. In a comment: using alpha=0.05, is there a statistically
#     significant difference in time-on-page between the two designs?
alpha = 0.05

if p_value <= alpha:
    print("reject H0")
else:
    print("fail to reject H0")

# -> Since the p-value (0.0000000912, extremely close to 0) is far less
#    than alpha (0.05), we reject H0. There is strong evidence that
#    Website Design A has a different average time-on-page than
#    Website Design B.