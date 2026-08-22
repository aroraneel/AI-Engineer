"""
CHECKPOINT TEST — Days 6-10 — ANSWER SHEET
Covers: Intro Statistics (6), Descriptive Stats (7), Std Dev & Random
        Variables (8), Percentiles & IQR (9), Correlation & Covariance (10)
"""

import numpy as np
import pandas as pd


# =============================================================
# PART A — CONCEPTUAL ANSWERS
# =============================================================

# A1. Mean = average of all values. Median = the middle value when
#     sorted. Mode = the most frequent value. The median gives a more
#     honest picture when data is skewed or has outliers, since extreme
#     values pull the mean but barely affect the median.

# A2. Population variance divides by N (total population size). Sample
#     variance divides by (n-1) instead of n. We use (n-1) because a
#     sample tends to UNDERESTIMATE the true population variance (the
#     sample mean is calculated FROM the same data, slightly reducing
#     the spread around it) -- dividing by a smaller number (n-1)
#     corrects this bias, giving a more accurate estimate of the true
#     population variance.

# A3. Standard deviation measures, on average, how far data points
#     typically are from the mean -- a measure of spread/variability
#     in the same units as the original data.

# A4. Coefficient of Variation (CV) = std / mean, often expressed as a
#     percentage. It's useful for comparing spread between two datasets
#     with different units or vastly different scales, since raw std
#     alone can't be fairly compared across different units (e.g.
#     comparing variability in salary (in dollars) vs age (in years)) --
#     CV normalizes spread relative to the mean.

# A5. A percentile indicates the value below which a given percentage
#     of the data falls. "The 90th percentile" means 90% of the data
#     is below that value (and 10% is above it).

# A6. IQR = Q3 - Q1 (the range containing the middle 50% of the data).
#     Outlier detection rule: any value below Q1 - 1.5*IQR or above
#     Q3 + 1.5*IQR is flagged as an outlier.

# A7. Covariance measures the DIRECTION of a relationship between two
#     variables (positive/negative), but its magnitude is affected by
#     the variables' units/scale, making it hard to interpret directly.
#     Correlation is covariance NORMALIZED to a fixed range (-1 to 1),
#     making it comparable across any pair of variables regardless of
#     their units -- which is why correlation is generally more useful.

# A8. False. Correlation only shows that two variables move together
#     (a statistical relationship) -- it does NOT prove that one causes
#     the other. There could be a confounding variable, reverse
#     causation, or pure coincidence behind the correlation.

# A9. If the mean is much higher than the median, the data is likely
#     RIGHT-SKEWED (positively skewed) -- a few unusually large values
#     are pulling the mean upward, while the median stays closer to
#     where most of the data actually sits.

# A10. A discrete random variable can only take specific, countable
#      values (e.g. number of heads in 10 coin flips: 0,1,2...10). A
#      continuous random variable can take any value within a range,
#      including decimals (e.g. a person's exact height).


# =============================================================
# PART B — CODE ANSWERS
# =============================================================

salaries = np.array([42, 48, 51, 39, 62, 45, 58, 71, 44, 49, 53, 200, 47, 55, 60])

# B1
mean_b1 = salaries.mean()
median_b1 = np.median(salaries)
print("B1 mean:", round(mean_b1, 2))
print("B1 median:", median_b1)
# The mean (61.6) is noticeably higher than the median (51.0) -- this
# suggests the data is right-skewed, likely due to the 200 outlier
# pulling the mean upward while barely affecting the median.

# B2
pop_var_b2 = salaries.var(ddof=0)
pop_std_b2 = salaries.std(ddof=0)
sample_var_b2 = salaries.var(ddof=1)
sample_std_b2 = salaries.std(ddof=1)
print("\nB2 population variance:", round(pop_var_b2, 2))
print("B2 population std:", round(pop_std_b2, 2))
print("B2 sample variance:", round(sample_var_b2, 2))
print("B2 sample std:", round(sample_std_b2, 2))

# B3
q1_b3 = np.percentile(salaries, 25)
q2_b3 = np.percentile(salaries, 50)
q3_b3 = np.percentile(salaries, 75)
iqr_b3 = q3_b3 - q1_b3
print("\nB3 Q1:", q1_b3)
print("B3 Q2 (median):", q2_b3)
print("B3 Q3:", q3_b3)
print("B3 IQR:", iqr_b3)

# B4
lower_bound_b4 = q1_b3 - 1.5 * iqr_b3
upper_bound_b4 = q3_b3 + 1.5 * iqr_b3
outliers_b4 = salaries[(salaries < lower_bound_b4) | (salaries > upper_bound_b4)]
print("\nB4 lower bound:", lower_bound_b4)
print("B4 upper bound:", upper_bound_b4)
print("B4 outliers:", outliers_b4)
# The value 200 is correctly flagged as an outlier.

# B5
years_experience_b5 = np.array([3, 5, 6, 2, 10, 4, 8, 12, 3, 5, 7, 15, 4, 6, 9])
correlation_b5 = np.corrcoef(salaries, years_experience_b5)[0, 1]
print("\nB5 correlation (salary vs experience):", round(correlation_b5, 4))
