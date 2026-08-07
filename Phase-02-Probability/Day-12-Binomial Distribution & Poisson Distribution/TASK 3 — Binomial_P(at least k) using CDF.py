import numpy as np
import math
from scipy import stats

# Same distribution: n=8, p=0.6
n = 8
p = 0.6

# 3a. Calculate P(at least 6 heads) -- i.e. P(X >= 6)
binomial = stats.binom(n, p)
p_at_least_6 = 1 - binomial.cdf(5)

# 3b. Print the result
print(round(p_at_least_6, 4))