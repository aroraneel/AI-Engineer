import numpy as np
from scipy import stats

# A factory claims its light bulbs last on average 1200 hours, with a
# KNOWN population standard deviation of 80 hours. A sample of 40 bulbs
# has a sample mean of 1180 hours.
# H0: the true mean is 1200 hours (no difference from the claim)
sample_mean = 1180
pop_mean = 1200
pop_std = 80
n = 40

# 1a. Calculate the z-statistic using: z = (sample_mean - pop_mean) / (pop_std / sqrt(n))
z = (sample_mean - pop_mean) / (pop_std / np.sqrt(n))

# 1b. Print the z-statistic (rounded to 4 decimal places)
print(round(z,4))