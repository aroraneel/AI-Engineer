import numpy as np
import math
from scipy import stats

# A website receives on average lambda=3 errors per day.
lam = 3
k = 5

# 4a. Calculate P(exactly 5 errors in a day) using the Poisson formula:
lambda_power = lam ** k
e_term = math.exp(-lam)
k_factorial = math.factorial(k)

# 4b. Print the result (rounded to 4 decimal places)
print(round((lambda_power * e_term) / k_factorial, 4))