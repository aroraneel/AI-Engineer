import numpy as np
from scipy import stats

# Same heights distribution: mean=170, std=7
mean = 170
std = 7

# 4a. Calculate the z-score for a person who is 184cm tall
#     z = (x - mean) / std
x_184 = 184
z_score_184 = (x_184 - mean) / std

# 4b. Calculate the z-score for a person who is 159cm tall
x_159 = 159
z_scores_159 = (x_159 - mean) / std

# 4c. Print both z-scores
print(f"Z-score for 184cm tall person: {z_score_184}")
print(f"Z-score for 159cm tall person: {z_scores_159}")

# 4d. In a comment: which person is further from average, and how do you
#     know just from looking at the z-scores?
# -> The person who is 184cm tall has a positive z-score (2.0), indicating they are above the average.
# -> The person who is 159cm tall has a negative z-score (-1.57), indicating they are below the average.