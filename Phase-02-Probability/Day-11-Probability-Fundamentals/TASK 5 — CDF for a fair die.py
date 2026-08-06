import numpy as np

# 5a. Using the simulated rolls from Task 4, calculate the OBSERVED CDF
#     at X=3 (the proportion of rolls that were 3 or less)
rolls = np.random.randint(1, 7, size=100000)
observed = np.sum(rolls <= 3) / 100000

# 5b. Compare it to the theoretical CDF(3) = 3/6 = 0.5
theoretical = 3/6

# 5c. Print both values
print("observed: ", np.round(observed, 4))
print("theoretical: ", np.round(theoretical, 4))