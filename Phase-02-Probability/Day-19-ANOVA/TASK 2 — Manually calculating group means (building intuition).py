import numpy as np
from scipy import stats

# Using the same 3 groups from Task 1:
# 2a. Calculate and print the mean of each group (design_a, design_b,
#     design_c)
design_a = np.array([2.1, 2.4, 1.9, 2.3, 2.0, 2.2])
design_b = np.array([3.5, 3.2, 3.8, 3.6, 3.4, 3.7])
design_c = np.array([2.2, 2.0, 2.5, 2.1, 2.3, 1.9])

mean_a = design_a.mean()
mean_b = design_b.mean()
mean_c = design_c.mean()
print("Mean A:", round(mean_a, 4))
print("Mean B:", round(mean_b, 4))
print("Mean C:", round(mean_c, 4))

# 2b. Calculate and print the OVERALL mean (all 18 values combined --
#     hint: use np.concatenate() to combine all 3 arrays first)
all_values = np.concatenate((design_a, design_b, design_c))
overall_mean = all_values.mean()
print("Overall Mean:", round(overall_mean, 4))

# 2c. In a comment: which group's mean is furthest from the overall
#     mean? Does this match which group seemed different in Task 1's
#     result?
# -> Mean B (3.5333) is furthest from the overall mean (2.6167), with a
#    gap of about 0.92 -- much larger than A or C's gap (~0.45-0.47 each).
#    This matches Task 1's ANOVA result: Design B is the standout group
#    driving the significant difference, consistent with its clearly
#    higher click-through rates in the raw data.