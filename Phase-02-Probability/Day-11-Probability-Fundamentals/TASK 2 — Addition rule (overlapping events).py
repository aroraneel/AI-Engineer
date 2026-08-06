import numpy as np

# A standard 52-card deck.
p_queen = 4/52
p_spade = 13/52
p_queen_and_spade = 1/52

# 2a. Calculate P(drawing a Queen OR a Spade)
#     P(Queen) = 4/52, P(Spade) = 13/52, P(Queen AND Spade) = 1/52
#     (the Queen of Spades is counted in both groups)
p_queen_or_spade = p_queen + p_spade - p_queen_and_spade

# 2b. Print the result
print(round(p_queen_or_spade, 4))