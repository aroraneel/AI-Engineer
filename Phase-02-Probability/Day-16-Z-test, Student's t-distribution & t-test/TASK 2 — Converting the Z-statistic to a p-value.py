import numpy as np
from scipy import stats

# 2a. Using the z-statistic from Task 1, calculate the two-tailed p-value:
sample_mean = 1180
pop_mean = 1200
pop_std = 80
n = 40

z = (sample_mean - pop_mean) / (pop_std / np.sqrt(n))

p_value = 2 * (1 - stats.norm.cdf(abs(z)))

# 2b. Print the p-value
print("p-value: ",p_value)

# 2c. In a comment: using alpha=0.05, do you reject or fail to reject H0?
#     What does that suggest about the factory's claim?
alpha = 0.05

if p_value <= alpha:
    print("reject H0")
else:
    print("fail to reject H0")

# -> Since the p-value (0.11384) is greater than alpha (0.05), we fail to
#    reject H0. This suggests there is NOT enough evidence to conclude
#    the factory's claim of 1200 hours is wrong -- the observed sample
#    mean of 1180 hours could plausibly happen just by random sampling
#    variation, even if the true average really is 1200 hours.