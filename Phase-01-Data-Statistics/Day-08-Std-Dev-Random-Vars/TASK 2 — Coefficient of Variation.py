import numpy as np
import pandas as pd

class_a = np.array([45, 50, 48, 52, 55, 47, 53, 49, 51, 50])
class_b = np.array([85, 90, 88, 92, 95, 87, 93, 89, 91, 90])
 
# 2a. Calculate mean and std dev for both class_a and class_b
mean_class_a = np.mean(class_a)
std_class_a = np.std(class_a)

mean_class_b = np.mean(class_b)
std_class_b = np.std(class_b)

# 2b. Calculate CV for both: (std / mean) * 100
class_a_cv = (std_class_a / mean_class_a) * 100
class_b_cv = (std_class_b / mean_class_b) * 100

# 2c. Print both CVs 
print(class_a_cv)
print(class_b_cv)

# state which class has more RELATIVE variability
# -> class_a has more RELATIVE variability