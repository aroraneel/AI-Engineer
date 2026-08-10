import numpy as np
from scipy import stats

# A population has mean=50, std=30.
mean = 50
std = 30

# 2a. Calculate the standard error for a sample size of n=36
#     (standard error = std / sqrt(n))
se_36 = std / np.sqrt(36)

# 2b. Calculate the standard error for a sample size of n=100
se_100 = std / np.sqrt(100)

# 2c. Print both results
print("Standard error for n=36:", se_36)
print("Standard error for n=100:", se_100)


# 2d. In a comment: as n increased from 36 to 100, did the standard
#     error go up or down? Does that match what CLT predicts?
# -> The standard error went down as n increased from 36 to 100,
# -> which matches what the Central Limit Theorem predicts: as sample size increases,
# -> the standard error decreases, leading to a more precise estimate of the population mean.