"""
PHASE 1 CUMULATIVE TEST — Days 1-10 (Data & Statistics Foundations)
Covers: NumPy, Pandas, Reading Data, Matplotlib, Seaborn/EDA, Intro Stats,
        Descriptive Stats, Std Dev & Random Variables, Percentiles & IQR,
        Correlation & Covariance

RULES:
- This is a BIGGER test than the 5-day checkpoints -- it covers the entire
  phase and mixes topics together, the way a real interview or project would.
- Attempt Part A completely from memory first.
- Part B is a mini end-to-end project -- treat it like a real task.
- This is a checkpoint, not a graded exam -- the point is to reveal what
  needs review before starting Phase 2 topics from scratch, or moving into
  Phase 3.

SETUP:
- pip install numpy pandas matplotlib seaborn scipy (if not already installed)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =============================================================
# PART A — CONCEPTUAL REVIEW (mixed, from memory)
# =============================================================

# A1. Explain broadcasting in NumPy AND vectorization -- how are they
#     related, and why do both make NumPy faster than plain Python loops?
# -> 


# A2. Walk through, step by step, how you would explore a brand new
#     CSV file for the first time using Pandas -- what functions would
#     you call, in what order, and why?
# -> 


# A3. You're given a dataset where the mean is much higher than the
#     median. Without plotting anything, what does that tell you about
#     the data's shape, and which measure (mean or median) would you
#     trust more to describe a "typical" value?
# -> 


# A4. Explain the relationship between standard deviation, the empirical
#     rule (68-95-99.7), and outlier detection using Z-scores.
# -> 


# A5. What's the difference between using the IQR method vs the Z-score
#     method for detecting outliers? When might you prefer one over the
#     other?
# -> 


# A6. A scatter plot shows a strong positive correlation between ice
#     cream sales and shark attacks. Explain why this does NOT mean ice
#     cream causes shark attacks, using the concept of a confounding
#     variable.
# -> 


# A7. If you wanted to visually check BOTH the distribution shape of a
#     single column AND compare that column across categories, which
#     two specific plots would you use, and why not just one?
# -> 


# =============================================================
# PART B — MINI PROJECT (end-to-end, mixing everything)
# =============================================================

# You are given sales data for a small business across 20 days.
days = np.arange(1, 21)
daily_sales = np.array([1200, 1350, 1100, 1450, 1600, 1300, 1250, 1700,
                          1800, 1150, 1400, 1500, 1650, 1900, 12000,
                          1350, 1420, 1380, 1550, 1600])
daily_customers = np.array([45, 52, 40, 55, 60, 48, 46, 63, 68, 42,
                              53, 57, 61, 70, 90, 50, 54, 51, 58, 60])

# B1. Combine the above into a Pandas DataFrame with columns "Day",
#     "Sales", and "Customers". Print the first 5 rows and the shape.

# --- your code here ---




# B2. Print the full descriptive statistics summary (.describe()) for
#     Sales and Customers. Based on the mean vs median, does Sales look
#     skewed?

# --- your code here ---




# B3. Calculate the mean, median, standard deviation (sample), and IQR
#     for the Sales column. Using the IQR rule, identify any outlier day(s).

# --- your code here ---




# B4. Create a LINE plot of Sales over the 20 days, with proper title
#     and axis labels. Does the outlier day stand out visually?

# --- your code here ---




# B5. Create a SCATTER plot of Sales vs Customers. Calculate the Pearson
#     correlation coefficient between them. Does the outlier day distort
#     this relationship? (Hint: try calculating correlation WITH and
#     WITHOUT the outlier day, and compare.)

# --- your code here ---




# B6. Create a BOX plot of the Sales column alone to visually confirm
#     the outlier you found in B3.

# --- your code here ---




# B7. In a comment: write a 3-4 sentence summary as if reporting to a
#     manager -- what does this data show, what's unusual about it, and
#     would you recommend investigating the outlier day before drawing
#     conclusions about the sales-customers relationship?
# -> 