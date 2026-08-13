import numpy as np
from scipy import stats

# A nutritionist claims the average calorie count of a snack bar is 250
# calories. A sample of 10 bars was tested (population std is UNKNOWN,
# so a t-test is appropriate, not a z-test):
sample_bars = np.array([245, 260, 255, 238, 250, 262, 248, 253, 241, 258])
 
# 3a. Use stats.ttest_1samp(sample_bars, popmean=250) to run a one-sample
#     t-test. This returns both a t-statistic and a p-value.
t_statistic, p_value = stats.ttest_1samp(sample_bars, popmean=250)

# 3b. Print both the t-statistic and the p-value
print("t-statistic: ",t_statistic)
print("p-value: ", p_value)

# 3c. In a comment: using alpha=0.05, do you reject or fail to reject H0
#     (that the true mean calorie count is 250)?
alpha = 0.05

if p_value <= alpha:
    print("reject H0")
else:
    print("fail to reject H0")

# -> Since the p-value (0.7042) is greater than alpha (0.05), we fail to
#    reject H0. There is no evidece of proving that cnack ber 250 is wrong.