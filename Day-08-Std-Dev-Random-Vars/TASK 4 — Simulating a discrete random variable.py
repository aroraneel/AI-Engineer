import numpy as np
import pandas as pd

# 4a. Use np.random.randint(1, 7, size=10000) to simulate 10,000 rolls
#     of a fair six-sided die. Store in a variable called rolls.
rolls = np.random.randint(1, 7, size=10000)

# 4b. Print the mean of rolls
print(np.mean(rolls))

# 4c. Print how many times each value (1-6) appeared, using
#     pd.Series(rolls).value_counts() (import pandas first)
print(pd.Series(rolls).value_counts())

# 4d. In a comment: is `rolls` representing a discrete or continuous
#     random variable? Why?
# -> Discrete, because it takes on a countable set of specific values