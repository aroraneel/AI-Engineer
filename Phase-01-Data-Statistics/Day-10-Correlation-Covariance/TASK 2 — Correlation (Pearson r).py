import numpy as np
import pandas as pd

# Using the same study_hours and exam_scores:
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
exam_scores = np.array([50, 55, 58, 65, 70, 75, 82, 90])

# 2a. Calculate the correlation using np.corrcoef(study_hours, exam_scores)
#     — again a 2x2 matrix, the value you want is at position [0, 1]
corrcoef_matrix = np.corrcoef(study_hours, exam_scores)

# 2b. Print just that value
correlation = corrcoef_matrix[1, 0]
print(correlation)

# 2c. In a comment: classify the strength (weak/moderate/strong) and
#     direction (positive/negative) of this relationship
# -> The strength is strong and the direction is positive relationship