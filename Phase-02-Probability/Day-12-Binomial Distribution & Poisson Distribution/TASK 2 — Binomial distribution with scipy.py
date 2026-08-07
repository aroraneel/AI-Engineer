import numpy as np
import math
from scipy import stats

# Same setup as Task 1: n=8 trials, p=0.6
n = 8
k = 5
p = 0.6

# 2a. Use stats.binom(n, p) to create a binomial distribution
binomial = stats.binom(n, p)

# 2b. Print the probability of exactly 5 successes using .pmf(5)
#     -- it should match your manual answer from Task 1
print(round(binomial.pmf(k), 4))

# 2c. Print the mean and variance using .mean() and .var()
#     -- compare to the shortcut formulas: mean = n*p, variance = n*p*(1-p)
print("Mean: ", binomial.mean())
print("Variance: ", binomial.var())