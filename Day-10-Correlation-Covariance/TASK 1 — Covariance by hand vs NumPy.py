import numpy as np
import pandas as pd

study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
exam_scores = np.array([50, 55, 58, 65, 70, 75, 82, 90])
 
# 1a. Calculate the covariance between study_hours and exam_scores using
#     np.cov(study_hours, exam_scores)
cov_matrix = np.cov(study_hours, exam_scores)

# 1b. Print just that value
covariance = cov_matrix[0, 1]
print(covariance)

# 1c. In a comment: is the covariance positive or negative? Does that match
#     what you'd expect from the data?
# -> The covariance is positive (33.64), which matches expectations:
#    as study_hours increases, exam_scores also increases, so both
#    variables move in the same direction.