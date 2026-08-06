import numpy as np

# You roll a fair 6-sided die once.
p_one = 1/6
p_six = 1/6

# 1a. Calculate P(rolling a 1 or a 6) using the addition rule
p_one_or_six = p_one + p_six

# 1b. Print the result as a fraction-style decimal (e.g. round to 4 places)
print(round(p_one_or_six, 4))