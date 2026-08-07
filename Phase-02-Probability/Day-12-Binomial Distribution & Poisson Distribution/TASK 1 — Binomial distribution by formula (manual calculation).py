import numpy as np
import math

# A biased coin has P(heads) = 0.6. It is flipped 8 times.
n = 8
k = 5
p = 0.6

# 1a. Calculate P(exactly 5 heads) using the binomial formula:
combination = math.comb(n, k)
p_success = p ** k
p_failure = (1 - p) ** (n - k)

# 1b. Print the result (rounded to 4 decimal places)
print(round(combination * p_success * p_failure, 4))