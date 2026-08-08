import numpy as np
from scipy import stats

# scipy's .cdf(x) gives P(X <= x). You can use it to find the actual
# probability of falling within a range, and compare it to the 68/95/99.7
# approximations from Task 2.
mean = 170
std = 7

lower_68 = mean - 1 * std
upper_68 = mean + 1 * std

# 3a. Calculate P(163 <= X <= 177) using:
#     norm_dist.cdf(177) - norm_dist.cdf(163)
#     (this is the range for +/- 1 std from Task 2a)
norm_dist = stats.norm(mean, std)
prob = norm_dist.cdf(upper_68) - norm_dist.cdf(lower_68)

# 3b. Print the result and compare it to 68% -- how close is it?
print(f"Probability of falling within 1 std: {prob}")
print(f"Empirical rule estimate: 0.68")