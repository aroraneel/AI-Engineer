import numpy as np
from scipy import stats

# A sample of 8 reaction times (in seconds) was collected. Population
# std is UNKNOWN, so this requires the t-distribution, not Z.
reaction_times = np.array([0.42, 0.39, 0.45, 0.41, 0.38, 0.44, 0.40, 0.43])
n = 8
 
# 5a. Calculate the sample mean and sample standard deviation (ddof=1)
sample_mean = np.mean(reaction_times)
sample_standars_deviation = np.std(reaction_times, ddof = 1)

# 5b. Calculate the standard error
standard_error = (sample_standars_deviation / np.sqrt(n))

# 5c. Use stats.t.interval(confidence=0.95, df=n-1, loc=sample_mean,
#     scale=standard_error) to calculate the 95% confidence interval
CI_95 = stats.t.interval(confidence = 0.95, df = n-1, loc = sample_mean, scale = standard_error)

# 5d. Print the result
print("CI 95%: ", CI_95)

# 5e. In a comment: why must this task use the t-distribution instead
#     of the Z-distribution?
# -> The population variance is unknown and the sample size is not large(n<30).