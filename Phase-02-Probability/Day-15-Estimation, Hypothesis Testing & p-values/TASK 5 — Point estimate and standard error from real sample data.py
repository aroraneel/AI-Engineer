import numpy as np
from scipy import stats

# A sample of 40 customer satisfaction scores (out of 10) is given below.
scores = np.array([7,8,6,9,7,8,5,7,9,8,6,7,8,9,7,6,8,7,9,8,
                    7,6,8,9,7,8,6,7,9,8,7,6,8,7,9,8,7,6,8,9])
 
# 5a. Calculate the point estimate (sample mean) for the true average
#     satisfaction score
sample_size = 40
mean = scores.mean()

# 5b. Calculate the standard error of this estimate
sample_std = scores.std(ddof=1)
standard_error = sample_std / np.sqrt(sample_size)

# 5c. Print both values
print("mean:", mean)
print("standard error:",standard_error)