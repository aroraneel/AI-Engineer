import numpy as np
import pandas as pd

scores = np.array([55, 60, 65, 70, 75, 80, 85])
 
# 4a. Print the POPULATION variance using np.var(scores)
print(np.var(scores)) # (NumPy's default divides by N)

# 4b. Print the SAMPLE variance using np.var(scores, ddof=1)
print(np.var(scores, ddof=1)) # (ddof=1 tells NumPy to divide by N-1 instead of N)

# 4c. Compare — which one is bigger? Does that match today's lesson?
# -> Sample variance (116.67) is bigger than population variance (100.0),
#    which matches the lesson: dividing by n-1 instead of n makes the
#    result slightly bigger, correcting for the fact that using the
#    sample's own mean makes the calculated variance underestimate the
#    true spread.