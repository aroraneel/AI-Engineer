import numpy as np
from scipy import stats

# A dataset of adult heights has mean=170cm, std=7cm.
mean = 170
std = 7

# 1a. Use stats.norm(mean, std) to create a Normal distribution
normal_dist = stats.norm(mean, std)

# 1b. Print the probability DENSITY at x=170 using .pdf(170)
#     (this should be the peak/maximum density, since 170 is the mean)
print("Probability density at x=170:", normal_dist.pdf(170))

# 1c. Print the probability density at x=190 using .pdf(190)
#     (this should be much smaller, since 190 is far from the mean)
print("Probability density at x=190:", normal_dist.pdf(190))