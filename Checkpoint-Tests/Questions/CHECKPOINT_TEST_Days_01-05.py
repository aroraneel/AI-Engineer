"""
CHECKPOINT TEST — Days 1-5
Covers: NumPy Basics (1), Pandas Basics (2), Reading Data (3),
        Matplotlib Basics (4), Seaborn EDA (5)

RULES:
- No looking at your notes for Part A (conceptual questions) -- answer from memory.
- You MAY use your notes/previous task files for Part B (code) if truly stuck,
  but try from memory first.
- Write all answers directly in this file, in the spaces provided.
- This is a checkpoint, not a graded exam -- the point is to reveal what
  needs review before continuing.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =============================================================
# PART A — CONCEPTUAL (answer in comments, no code needed)
# =============================================================

# A1. What is the difference between a Python list and a NumPy array?
#     Why do we use NumPy arrays for numerical work?
# -> 


# A2. What is "broadcasting" in NumPy? Give a one-line example.
# -> 


# A3. What is the difference between a Pandas Series and a DataFrame?
# -> 


# A4. How do you select a single column vs multiple columns from a
#     DataFrame? Write both syntax patterns from memory.
# -> 


# A5. What's the difference between .loc[] and .iloc[]?
# -> 


# A6. Name three file formats you can read into Pandas, and the
#     function used for each.
# -> 


# A7. When would you use a line plot vs a bar plot vs a scatter plot?
#     One sentence each.
# -> 


# A8. What does sns.heatmap() combined with df.corr() show you, and
#     what do values close to 1, -1, and 0 mean?
# -> 


# A9. What's the difference between a histogram and a box plot? When
#     would each one mislead you if used alone?
# -> 


# A10. What is the purpose of plt.tight_layout() when using subplots?
# -> 


# =============================================================
# PART B — CODE (write and run the code)
# =============================================================

# B1. Create a NumPy array of the numbers 1 through 20. Reshape it into
#     a 4x5 2D array. Print its shape.

# --- your code here ---




# B2. From the array in B1, use boolean indexing to select only the
#     even numbers. Print the result.

# --- your code here ---




# B3. Create a Pandas DataFrame with 3 columns: "Name", "Age", "City"
#     and at least 4 rows of made-up data. Print the DataFrame.

# --- your code here ---




# B4. From the DataFrame in B3, filter to show only rows where Age > 25.

# --- your code here ---




# B5. Add a new column to the DataFrame from B3 called "Is_Adult" that
#     is True if Age >= 18, False otherwise.

# --- your code here ---




# B6. Using the DataFrame from B3, create a bar plot showing Age by Name
#     (using either matplotlib or seaborn). Add a title and axis labels.

# --- your code here ---