import numpy as np
from scipy import stats

# Same data as Task 3: sample mean=2.5, population std=0.4, n=60
n = 60
std = 0.4
sample_mean = 2.5
z = 1.96  
standard_error = (std / np.sqrt(n))

# 4a. Use stats.norm.interval(confidence=0.95, loc=sample_mean,
#     scale=standard_error) to calculate the 95% CI directly
CI_95 = stats.norm.interval(confidence=0.95, loc=sample_mean, scale=standard_error)

# 4b. Print the result and compare it to your manual calculation from
#     Task 3 -- do they match?
print("CI 95%: ", CI_95)

# 4c. Now calculate a 99% CI using the same function (just change
#     confidence=0.99). Print it. Is it wider or narrower than the 95% CI?
CI_99 = stats.norm.interval(confidence=0.99, loc=sample_mean, scale=standard_error)
print("CI 99%: ", CI_99)