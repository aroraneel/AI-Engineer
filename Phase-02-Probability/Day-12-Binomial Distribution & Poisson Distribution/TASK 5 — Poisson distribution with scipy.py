import numpy as np
import math
from scipy import stats

# Same setup as Task 4: lambda=3
lam = 3
k = 5

# 5a. Use stats.poisson(lam) to create a Poisson distribution
poisson = stats.poisson(lam)

# 5b. Print the probability of exactly 5 errors using .pmf(5)
#     -- it should match your manual answer from Task 4
print(round(poisson.pmf(k), 4))

# 5c. Print the mean and variance using .mean() and .var()
#     -- for Poisson, both should equal lambda
print("Mean: ", poisson.mean())
print("Variance: ", poisson.var())