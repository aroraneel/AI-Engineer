import numpy as np 
import time

grid = np.array([[1,2,3],
                                      [4,5,6],
                                      [7,8,9]])

# 3a. Print the element at row 2, column 0
print(grid[2,0])

# 3b. Print the entire column at index 2
print(grid[:,2])

# 3c. Print the entire row at index 1
print(grid[1])

# 3d. Print the top-left 2x2 block of grid
print(grid[:2,:2])