import numpy as np
from scipy import stats

# Three groups representing test scores from 3 different classrooms,
# all taught using the same method (should NOT show a real difference):
class_1 = np.array([78, 82, 75, 80, 79, 81])
class_2 = np.array([77, 80, 83, 79, 78, 82])
class_3 = np.array([80, 78, 81, 77, 82, 79])
 
# 3a. Run a one-way ANOVA on these 3 groups using stats.f_oneway()
f_statistic, p_value = stats.f_oneway(class_1, class_2, class_3)

# 3b. Print the F-statistic and p-value
print("F-statistic:", round(f_statistic, 4))
print("p-value:", round(p_value, 4))

# 3c. In a comment: using alpha=0.05, do you reject or fail to reject
#     H0? Does this match the expectation that these classrooms perform
#     similarly?
alpha = 0.05
if p_value <= alpha:
    print("reject H0")
else:
    print("fail to reject H0")

# -> Since p-value (0.8765) > alpha (0.05), fail to reject H0. This
#    matches the expectation -- since all 3 classrooms were taught with
#    the same method, there's no significant evidence their average
#    test scores actually differ; the small variations seen are
#    consistent with random chance.