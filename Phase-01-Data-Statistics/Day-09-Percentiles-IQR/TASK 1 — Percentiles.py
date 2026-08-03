import numpy as np
import pandas as pd

scores = np.array([45, 52, 58, 61, 65, 68, 70, 72, 75, 78,
                    80, 82, 85, 88, 90, 92, 95, 97, 99, 100])
 
# 1a. Find the value at the 25th percentile using np.percentile(scores, 25)
print(np.percentile(scores , 25))

# 1b. Find the value at the 50th percentile (should match the median)
print(np.percentile(scores, 50))

# 1c. Find the value at the 90th percentile
print(np.percentile(scores, 90))

# 1d. In a comment: if a student's score is at the 90th percentile, what
#     does that mean in plain English?
# -> Being at the 90th percentile means 90% of other students scored
#    lower than this student, and only 10% scored higher — placing them
#    in roughly the top 10% of the class.