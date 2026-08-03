import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Age": [25, 30, 28, 45, 33, 29, 31, 27, 60, 26]
})
 
# 5a. Print the mean, median, and standard deviation of the "Age" column
print(df["Age"].mean())
print(df["Age"].median())
print(df["Age"].std())

# 5b. NOTE: Pandas' .std() and .var() default to SAMPLE statistics
#     (divides by n-1) automatically — confirm this by also computing
#     df["Age"].std(ddof=0) (population version) and comparing the two
print(df["Age"].var(ddof=0))
print(df["Age"].std(ddof=0))

# which is bigger, the mean or median here? What does
# that suggest about a possible outlier in the Age column?
# -> Mean (33.4) is bigger than median (29.5). This gap suggests there's
#    at least one high outlier pulling the mean upward — looking at the
#    data, the value 60 stands out as noticeably higher than the rest
#    of the ages (which mostly cluster between 25-33), so it's likely
#    the outlier responsible for the difference.