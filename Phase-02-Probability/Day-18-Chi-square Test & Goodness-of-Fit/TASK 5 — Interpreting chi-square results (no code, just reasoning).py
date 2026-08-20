# For each scenario, state whether the chi-square value described
# suggests the data FITS or DOES NOT FIT the expected pattern, and why.

# 5a. A goodness-of-fit test produces chi2 = 0.85, p-value = 0.93
# -> FITS the expected pattern.
# -> chi2 (0.85) is small, meaning observed counts are close to
#    expected. p-value (0.93) is far above 0.05, so fail to reject H0
#    -- strong evidence the data matches the expected distribution.

# 5b. A goodness-of-fit test produces chi2 = 24.6, p-value = 0.0001
# -> DOES NOT FIT the expected pattern.
# -> chi2 (24.6) is large, meaning observed counts are far from
#    expected. p-value (0.0001) is far below 0.05, so reject H0 --
#    strong evidence the data does NOT match the expected distribution.