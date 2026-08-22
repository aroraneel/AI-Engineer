"""
CHECKPOINT TEST — Days 1-5 — ANSWER SHEET
Covers: NumPy Basics (1), Pandas Basics (2), Reading Data (3),
        Matplotlib Basics (4), Seaborn EDA (5)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =============================================================
# PART A — CONCEPTUAL ANSWERS
# =============================================================

# A1. A Python list can hold mixed data types and is slower for
#     numerical work because it stores references to objects scattered
#     in memory. A NumPy array holds a single data type in one
#     contiguous memory block, enabling fast, vectorized operations
#     (no Python-level loop needed) -- this makes NumPy arrays much
#     faster and more memory-efficient for numerical work.

# A2. Broadcasting lets NumPy perform operations between arrays of
#     different shapes by automatically "stretching" the smaller one,
#     without actually copying data.
#     Example: np.array([1, 2, 3]) + 5  ->  array([6, 7, 8])
#     (the scalar 5 is "broadcast" across every element)

# A3. A Series is a single labeled 1D column of data. A DataFrame is a
#     2D table made of multiple Series sharing the same index --
#     essentially a collection of columns (Series) with row labels.

# A4. Single column: df['col_name']  or  df.col_name
#     Multiple columns: df[['col1', 'col2']]  (note the double brackets
#     -- a list of column names inside the selection brackets)

# A5. .loc[] selects by LABEL (the actual index/column names).
#     .iloc[] selects by INTEGER POSITION (0-based, like list indexing),
#     regardless of what the actual labels are.

# A6. CSV -> pd.read_csv()
#     JSON -> pd.read_json()
#     SQL database -> pd.read_sql()
#     (Excel -> pd.read_excel() is another common one)

# A7. Line plot: for showing a trend over time/continuous sequence.
#     Bar plot: for comparing a numeric value across discrete categories.
#     Scatter plot: for showing the relationship between two numeric
#     variables.

# A8. df.corr() computes the pairwise correlation coefficient (-1 to 1)
#     between every numeric column. sns.heatmap() visualizes that
#     correlation matrix with color. Values close to 1 = strong positive
#     relationship, close to -1 = strong negative relationship, close
#     to 0 = little/no linear relationship.

# A9. A histogram shows the actual SHAPE/distribution of a single
#     numeric variable (skew, bimodal patterns, etc). A box plot only
#     shows 5 summary numbers (min, Q1, median, Q3, max) and can hide
#     the true shape -- two very differently-shaped distributions
#     (e.g. evenly spread vs bimodal) can produce an identical-looking
#     box plot. A box plot alone would mislead you about the actual
#     shape; a histogram alone doesn't easily let you compare spread
#     across multiple categories side by side.

# A10. plt.tight_layout() automatically adjusts spacing between
#      subplots so titles, axis labels, and plots don't overlap or get
#      cut off -- especially important with plt.subplots() grids.


# =============================================================
# PART B — CODE ANSWERS
# =============================================================

# B1
arr_b1 = np.arange(1, 21).reshape(4, 5)
print("B1 shape:", arr_b1.shape)
print(arr_b1)

# B2
even_numbers_b2 = arr_b1[arr_b1 % 2 == 0]
print("\nB2 even numbers:", even_numbers_b2)

# B3
df_b3 = pd.DataFrame({
    "Name": ["Riya", "Aman", "Sara", "Vikram"],
    "Age": [22, 28, 19, 35],
    "City": ["Mumbai", "Delhi", "Bangalore", "Chennai"]
})
print("\nB3 DataFrame:")
print(df_b3)

# B4
adults_over_25_b4 = df_b3[df_b3["Age"] > 25]
print("\nB4 Age > 25:")
print(adults_over_25_b4)

# B5
df_b3["Is_Adult"] = df_b3["Age"] >= 18
print("\nB5 with Is_Adult column:")
print(df_b3)

# B6
plt.figure(figsize=(6, 4))
sns.barplot(data=df_b3, x="Name", y="Age")
plt.title("Age by Name")
plt.xlabel("Name")
plt.ylabel("Age")
plt.tight_layout()
plt.savefig("b6_age_by_name.png")
print("\nB6: bar plot saved as b6_age_by_name.png")
