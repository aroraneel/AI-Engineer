import numpy as np
from scipy import stats

# Same heights distribution: mean=170, std=7
mean = 170
std = 7

# 2a. Calculate and print the range that covers 68% of heights (mean +/- 1*std)
lower_68 = mean - 1 * std
upper_68 = mean + 1 * std
print(f"Range covering 68% of heights: {lower_68} to {upper_68}")

# 2b. Calculate and print the range that covers 95% of heights (mean +/- 2*std)
lower_95 = mean - 2 * std
upper_95 = mean + 2 * std
print(f"Range covering 95% of heights: {lower_95} to {upper_95}")

# 2c. Calculate and print the range that covers 99.7% of heights (mean +/- 3*std)
lower_997 = mean - 3 * std
upper_997 = mean + 3 * std
print(f"Range covering 99.7% of heights: {lower_997} to {upper_997}")