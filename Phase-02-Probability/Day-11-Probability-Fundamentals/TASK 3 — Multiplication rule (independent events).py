import numpy as np

# 3a. Calculate the probability of flipping a coin 3 times and getting
#     heads all 3 times
P_heads_on_1_flip = 0.5
P_heads_and_heads_and_heads = 0.5*0.5*0.5

# 3b. Calculate the probability of rolling a die twice and getting a 6
#     both times
P_six_on_1_roll = 1/6
P_six_and_six = (1/6)*(1/6)

# 3c. Print both results
print(round(P_heads_and_heads_and_heads, 4))
print(round(P_six_and_six, 4))