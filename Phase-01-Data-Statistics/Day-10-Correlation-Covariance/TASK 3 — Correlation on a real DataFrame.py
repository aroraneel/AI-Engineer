import numpy as np
import pandas as pd

df  = pd.DataFrame({
    "TV_Hours": [1, 2, 3, 4, 5, 2, 1, 6, 3, 4],
    "Exam_Score": [88, 80, 75, 65, 55, 78, 90, 50, 72, 68],
    "Sleep_Hours": [8, 7, 7, 6, 5, 7, 8, 5, 6, 6]
})
 
# 3a. Print the full correlation matrix using df.corr()
corr_matrix = df.corr()
print(corr_matrix)

# 3b. Print just the correlation between TV_Hours and Exam_Score
#     (hint: df.corr().loc["TV_Hours", "Exam_Score"])
correlation = df.corr().loc["TV_Hours", "Exam_Score"]
print(correlation)

# 3c. In a comment: is the relationship between TV hours and exam score
#     positive or negative? Does that match your intuition?
# -> The relationship between TV hours and exam scores is negative
#    (r ≈ -0.99), meaning more TV time is strongly associated with lower
#    exam scores. This matches intuition — more time watching TV likely
#    means less time studying.