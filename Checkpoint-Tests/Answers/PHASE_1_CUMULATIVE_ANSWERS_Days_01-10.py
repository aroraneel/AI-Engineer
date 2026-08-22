"""
PHASE 1 CUMULATIVE TEST — Days 1-10 — ANSWER SHEET
Covers: NumPy, Pandas, Reading Data, Matplotlib, Seaborn/EDA, Intro Stats,
        Descriptive Stats, Std Dev & Random Variables, Percentiles & IQR,
        Correlation & Covariance
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =============================================================
# PART A — CONCEPTUAL ANSWERS
# =============================================================

# A1. Broadcasting lets NumPy operate on arrays of different shapes by
#     automatically stretching the smaller one without copying data.
#     Vectorization means applying an operation to an entire array at
#     once (in fast, compiled C code under the hood) instead of looping
#     element-by-element in Python. They're related because broadcasting
#     is what MAKES vectorized operations possible between
#     differently-shaped arrays. Both are faster than plain Python loops
#     because the looping happens in optimized, compiled C code rather
#     than slow, interpreted Python bytecode.

# A2. Step-by-step exploration of a new CSV:
#     1. df = pd.read_csv() -- load the data
#     2. df.head() -- first look at a few rows
#     3. df.shape -- how many rows/columns
#     4. df.info() -- data types, non-null counts per column
#     5. df.isnull().sum() -- check for missing values
#     6. df.describe() -- summary statistics for numeric columns
#     7. Visualize key columns (histograms, boxplots) to check
#        distributions and spot outliers before doing anything else.

# A3. A mean much higher than the median suggests the data is
#     RIGHT-SKEWED -- a few unusually large values are pulling the mean
#     up while the median stays close to where most data actually sits.
#     The MEDIAN would be trusted more to describe a "typical" value,
#     since it's resistant to being distorted by extreme outliers.

# A4. Standard deviation measures typical spread from the mean. The
#     empirical rule (68-95-99.7) uses std to estimate what fraction of
#     Normally-distributed data falls within 1, 2, or 3 std devs of the
#     mean. Z-scores (z = (x-mean)/std) convert this into "how many std
#     devs away is this specific point" -- commonly, points with |z| > 3
#     are flagged as outliers, since the empirical rule says only ~0.3%
#     of data should fall that far from the mean if it's Normal.

# A5. The IQR method flags outliers based on the middle 50% of the data
#     (Q1/Q3), making it robust to extreme values and not requiring a
#     Normal distribution assumption -- good for skewed data. The
#     Z-score method assumes roughly Normal data and can be less
#     reliable on skewed distributions (since extreme values themselves
#     inflate the mean/std used to calculate z). Prefer IQR for skewed
#     or unknown-shape data; Z-score is fine for data that's roughly
#     Normal already.

# A6. This does NOT mean ice cream causes shark attacks -- both are
#     actually driven by a CONFOUNDING VARIABLE: warmer weather/summer
#     season. Hot weather causes both more ice cream sales AND more
#     people swimming in the ocean (leading to more shark encounters).
#     The two variables move together because they share a common
#     underlying cause, not because one causes the other directly.

# A7. Use a HISTOGRAM to check the distribution shape of a single
#     numeric column (skew, bimodal patterns, etc), and a BOX PLOT to
#     compare that column's spread/outliers ACROSS categories. A
#     histogram alone can't easily compare multiple categories side by
#     side; a box plot alone hides the true shape (two very different
#     distributions can produce identical-looking box plots) -- using
#     both together covers what neither can show alone.


# =============================================================
# PART B — MINI PROJECT ANSWERS
# =============================================================

days = np.arange(1, 21)
daily_sales = np.array([1200, 1350, 1100, 1450, 1600, 1300, 1250, 1700,
                          1800, 1150, 1400, 1500, 1650, 1900, 12000,
                          1350, 1420, 1380, 1550, 1600])
daily_customers = np.array([45, 52, 40, 55, 60, 48, 46, 63, 68, 42,
                              53, 57, 61, 70, 90, 50, 54, 51, 58, 60])

# B1
df_b1 = pd.DataFrame({"Day": days, "Sales": daily_sales, "Customers": daily_customers})
print("B1 head:")
print(df_b1.head())
print("B1 shape:", df_b1.shape)

# B2
print("\nB2 describe():")
print(df_b1[["Sales", "Customers"]].describe())
print("B2: Sales mean is much higher than its median -- suggests Sales")
print("    is right-skewed (likely due to the day-15 outlier of 12000).")

# B3
mean_b3 = df_b1["Sales"].mean()
median_b3 = df_b1["Sales"].median()
std_b3 = df_b1["Sales"].std(ddof=1)
q1_b3 = df_b1["Sales"].quantile(0.25)
q3_b3 = df_b1["Sales"].quantile(0.75)
iqr_b3 = q3_b3 - q1_b3
lower_b3 = q1_b3 - 1.5 * iqr_b3
upper_b3 = q3_b3 + 1.5 * iqr_b3
outliers_b3 = df_b1[(df_b1["Sales"] < lower_b3) | (df_b1["Sales"] > upper_b3)]
print("\nB3 mean:", round(mean_b3, 2), " median:", median_b3, " std:", round(std_b3, 2))
print("B3 IQR:", iqr_b3)
print("B3 outlier day(s):")
print(outliers_b3)

# B4
plt.figure(figsize=(8, 4))
plt.plot(df_b1["Day"], df_b1["Sales"], marker='o')
plt.title("Daily Sales Over 20 Days")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("b4_sales_line.png")
print("\nB4: line plot saved -- day 15's spike to 12000 stands out sharply.")

# B5
correlation_with_outlier_b5 = df_b1["Sales"].corr(df_b1["Customers"])
df_no_outlier_b5 = df_b1[df_b1["Day"] != 15]
correlation_without_outlier_b5 = df_no_outlier_b5["Sales"].corr(df_no_outlier_b5["Customers"])

plt.figure(figsize=(6, 4))
plt.scatter(df_b1["Sales"], df_b1["Customers"])
plt.title("Sales vs Customers")
plt.xlabel("Sales")
plt.ylabel("Customers")
plt.tight_layout()
plt.savefig("b5_scatter.png")

print("\nB5 correlation WITH outlier:", round(correlation_with_outlier_b5, 4))
print("B5 correlation WITHOUT outlier:", round(correlation_without_outlier_b5, 4))
print("B5: the outlier day actually REDUCES the measured correlation --")
print("    without it, sales and customers are almost perfectly correlated")
print("    (0.9955), since day 15's disproportionately huge sales relative")
print("    to its customer count throws off the otherwise strong pattern.")

# B6
plt.figure(figsize=(4, 5))
sns.boxplot(y=df_b1["Sales"])
plt.title("Sales Distribution (Box Plot)")
plt.tight_layout()
plt.savefig("b6_boxplot.png")
print("\nB6: box plot saved -- confirms day 15 (12000) as a clear outlier point.")

# B7
print("""
B7 Summary for manager:
Daily sales over the 20-day period average around 1,983, but this is
skewed upward by a single outlier -- the median (1,435) better reflects
a typical day. Day 15 is a significant outlier at 12,000 -- roughly 8x a
typical day's sales -- and should be investigated before drawing further
conclusions, as it may reflect a data entry error, a one-off bulk order,
or a special promotion. Interestingly, this outlier actually WEAKENS the
measured sales-customers correlation (0.76 with it vs 0.996 without it),
so any relationship analysis should be re-run excluding day 15 to see
the true, much stronger underlying pattern between sales and customers.
""")
