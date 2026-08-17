import numpy as np
from scipy import stats

# A sample of 60 packages has an average weight of 2.5 kg, with a KNOWN
# population standard deviation of 0.4 kg.
n = 60
std = 0.4
sample_mean = 2.5
z = 1.96  

# 3a. Calculate the standard error (std / sqrt(n))
standard_error = (std / np.sqrt(n))

# 3b. Calculate the margin of error for a 95% confidence interval
#     (use z* = 1.96)

margin_of_error = z * standard_error

# 3c. Calculate and print the lower and upper bounds of the confidence
#     interval
upper_bound = sample_mean + margin_of_error
lower_bound = sample_mean - margin_of_error

print("lower bound: ", lower_bound)
print("upper bound: ", upper_bound)

# 3d. In a comment: state what this confidence interval means in plain
#     English
# -> We are 95% confident that the TRUE AVERAGE weight of all packages
#    (the whole population, not just this sample) falls between
#    [lower_bound] kg and [upper_bound] kg.