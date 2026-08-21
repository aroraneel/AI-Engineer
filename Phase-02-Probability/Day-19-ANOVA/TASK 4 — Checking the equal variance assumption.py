import numpy as np
from scipy import stats

# Before trusting an ANOVA result, one assumption is that all groups
# have roughly equal variance (homogeneity of variance).
design_a = np.array([2.1, 2.4, 1.9, 2.3, 2.0, 2.2])
design_b = np.array([3.5, 3.2, 3.8, 3.6, 3.4, 3.7])
design_c = np.array([2.2, 2.0, 2.5, 2.1, 2.3, 1.9])

# 4a. Using the 3 ad design groups from Task 1, calculate the variance
#     (use ddof=1 for sample variance) of each group
var_a = np.var(design_a, ddof = 1)
var_b = np.var(design_b, ddof = 1)
var_c = np.var(design_c, ddof = 1)

# 4b. Print all three variances
print("Variance of A:", round(var_a, 4))
print("Variance of B:", round(var_b, 4))
print("Variance of C:", round(var_c, 4))

# 4c. In a comment: do the variances look roughly similar, or is one
#     noticeably different from the others? (Note: scipy also has
#     stats.levene() to formally test this assumption, but for this
#     task just eyeball the numbers)
# -> Variance are similar to each other.