import numpy as np
import pandas as pd

scores = np.array([62, 68, 70, 71, 73, 75, 69, 66, 74, 72,
                    77, 65, 70, 68, 71, 73, 69, 76, 67, 70])
 
# 1a. Calculate and print the mean and standard deviation of scores
print(np.mean(scores))
print(np.std(scores))

# 1b. Calculate and print the range that should contain ~68% of scores
#     (mean - 1*std to mean + 1*std)
mean = np.mean(scores)
std = np.std(scores)

lower_68 = mean - 1*std
upper_68 = mean + 1*std

print(lower_68)
print(upper_68)

# 1c. Calculate and print the range that should contain ~95% of scores
#     (mean - 2*std to mean + 2*std)
mean = np.mean(scores)
std = np.std(scores)

lower_95 = mean - 2*std
upper_95 = mean + 2*std

print(lower_95)
print(upper_95)

# 1d. Count how many actual scores fall within the 68% range using
#     boolean indexing, and print that count out of 20 total
in_range = scores[(scores>= lower_68) & (scores <= upper_68)]
print(f"{len(in_range)} out 0f 20")