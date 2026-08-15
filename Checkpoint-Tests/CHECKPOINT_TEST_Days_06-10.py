"""
CHECKPOINT TEST — Days 6-10
Covers: Intro Statistics (6), Descriptive Stats (7), Std Dev & Random
        Variables (8), Percentiles & IQR (9), Correlation & Covariance (10)

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


# =============================================================
# PART A — CONCEPTUAL (answer in comments, no code needed)
# =============================================================

# A1. What's the difference between mean, median, and mode? In what
#     situation does the median give a more honest picture than the mean?
# -> 


# A2. What's the difference between population variance and sample
#     variance? Why do we divide by (n-1) instead of n for the sample?
# -> 


# A3. What does standard deviation actually measure, in plain English?
# -> 


# A4. What is the Coefficient of Variation, and why is it useful when
#     comparing the "spread" of two datasets with very different units
#     or scales?
# -> 


# A5. What is a percentile? What does "the 90th percentile" mean in
#     plain English?
# -> 


# A6. What is the IQR (Interquartile Range), and how is it used to
#     detect outliers?
# -> 


# A7. What's the difference between covariance and correlation? Why is
#     correlation generally more useful for comparing relationships?
# -> 


# A8. True or False, and explain why: "A strong correlation between two
#     variables proves one causes the other."
# -> 


# A9. If a dataset has a mean much higher than its median, what does
#     that suggest about the shape of the distribution?
# -> 


# A10. What's the difference between a discrete random variable and a
#      continuous random variable? Give one example of each.
# -> 


# =============================================================
# PART B — CODE (write and run the code)
# =============================================================

# A dataset of 15 employee salaries (in thousands) is given below.
salaries = np.array([42, 48, 51, 39, 62, 45, 58, 71, 44, 49, 53, 200, 47, 55, 60])

# B1. Calculate the mean and median of this dataset. Are they close to
#     each other, or far apart? What does that suggest about the data?

# --- your code here ---




# B2. Calculate the population variance and standard deviation, then
#     the sample variance and standard deviation. Print all four values.

# --- your code here ---




# B3. Calculate the 25th, 50th, and 75th percentiles (Q1, Q2, Q3) of
#     this dataset. Then calculate the IQR.

# --- your code here ---




# B4. Using the IQR rule (values outside Q1 - 1.5*IQR or Q3 + 1.5*IQR
#     are outliers), identify any outliers in this dataset.

# --- your code here ---




# B5. Create a second array representing years of experience for the
#     same 15 employees (make up reasonable values), then calculate the
#     correlation (Pearson r) between salary and years of experience.
# --- your code here ---
