# Phase 1 — Formulas by Day

A day-by-day list of every formula covered in Phase 1 (Data & Statistics
Foundations), with what each symbol stands for and a short explanation.

---

## Day 7 — Descriptive Statistics

### Mean
```
mean = (sum of all values) / (number of values)
```
**What it measures:** the average value — adds everything up and divides
by how many values there are.

---

### Median
```
median = the middle value when data is sorted
```
**What it measures:** the value exactly in the middle of the sorted
data — resistant to outliers.

---

### Mode
```
mode = the most frequently occurring value
```
**What it measures:** whichever value shows up most often in the dataset.

---

### Population Variance
```
σ² = Σ(x - μ)² / N
```
| Symbol | Stands for |
|---|---|
| σ² | population variance |
| Σ | "sum of" — add up everything that follows |
| x | each individual value in the dataset |
| μ | the population mean |
| N | total number of values in the population |

**What it measures:** the average of the squared distances from the
mean, using the FULL population (divide by N).

---

### Sample Variance
```
s² = Σ(x - x̄)² / (n - 1)
```
| Symbol | Stands for |
|---|---|
| s² | sample variance |
| Σ | "sum of" |
| x | each individual value in the sample |
| x̄ | the sample mean |
| n | number of values in the sample |

**What it measures:** same idea as population variance, but divides by
(n-1) instead of n — corrects for the bias of estimating spread from a
sample instead of the full population.

---

### Standard Deviation
```
σ = √(variance)
```
| Symbol | Stands for |
|---|---|
| σ | population standard deviation (or `s` for sample) |
| √ | square root |

**What it measures:** the square root of variance — brings the spread
measure back into the original units (since variance is in squared units).

---

## Day 8 — Standard Deviation Deep Dive & Random Variables

### Coefficient of Variation (CV)
```
CV = std / mean
```
| Symbol | Stands for |
|---|---|
| CV | coefficient of variation |
| std | standard deviation |
| mean | the average value |

**What it measures:** standard deviation expressed relative to the
mean — lets you compare "spread" fairly between two datasets with
different units or vastly different scales.

---

### Empirical Rule (68-95-99.7)
```
68% of data within mean ± 1 std
95% of data within mean ± 2 std
99.7% of data within mean ± 3 std
```
| Symbol | Stands for |
|---|---|
| mean | the average value |
| std | standard deviation |
| ± | "plus or minus" — extends this far above AND below the mean |

**What it measures:** a quick way to estimate how much data falls
within a certain range, for roughly Normal-shaped data.

---

## Day 9 — Percentiles, Quartiles & IQR

### Percentile
```
The value below which a given percentage of the data falls
```
**Example:** the 90th percentile is the value where 90% of the data is
below it.

---

### Interquartile Range (IQR)
```
IQR = Q3 - Q1
```
| Symbol | Stands for |
|---|---|
| IQR | interquartile range |
| Q3 | the 75th percentile (third quartile) |
| Q1 | the 25th percentile (first quartile) |

**What it measures:** the range covering the middle 50% of the data —
a spread measure that ignores extreme outliers.

---

### Outlier Detection Rule (IQR method)
```
Outlier if value < Q1 - 1.5×IQR  OR  value > Q3 + 1.5×IQR
```
| Symbol | Stands for |
|---|---|
| Q1 | 25th percentile |
| Q3 | 75th percentile |
| IQR | interquartile range (Q3-Q1) |
| 1.5 | a fixed multiplier used by convention to set the outlier boundary |

**What it measures:** flags any value that falls unusually far below
Q1 or above Q3 as a likely outlier.

---

## Day 10 — Correlation & Covariance

### Covariance
```
cov(X,Y) = Σ[(x - x̄)(y - ȳ)] / (n - 1)
```
| Symbol | Stands for |
|---|---|
| cov(X,Y) | covariance between variable X and variable Y |
| Σ | "sum of" |
| x | each individual value of variable X |
| x̄ | the mean of variable X |
| y | each individual value of variable Y |
| ȳ | the mean of variable Y |
| n | number of paired data points |

**What it measures:** the DIRECTION two variables move together
(positive or negative) — but its size is affected by the variables'
units, making it hard to compare across different datasets.

---

### Correlation (Pearson r)
```
r = cov(X,Y) / (std(X) × std(Y))
```
| Symbol | Stands for |
|---|---|
| r | the correlation coefficient (always between -1 and 1) |
| cov(X,Y) | covariance between X and Y |
| std(X) | standard deviation of X |
| std(Y) | standard deviation of Y |

**What it measures:** covariance, normalized to always fall between -1
and 1 — makes the strength/direction of a relationship comparable
across any two variables, regardless of their original units.

---

## Quick Reference — All Phase 1 Formulas

| Day | Formula | What it measures |
|---|---|---|
| 7 | Mean = sum/count | Average value |
| 7 | Median = middle sorted value | Typical value, outlier-resistant |
| 7 | σ² = Σ(x-μ)²/N | Population variance |
| 7 | s² = Σ(x-x̄)²/(n-1) | Sample variance |
| 7 | σ = √variance | Standard deviation |
| 8 | CV = std/mean | Relative spread (unit-independent) |
| 8 | 68-95-99.7 rule | % of data within 1/2/3 std devs |
| 9 | IQR = Q3-Q1 | Middle-50% spread |
| 9 | Outlier: <Q1-1.5×IQR or >Q3+1.5×IQR | Outlier detection |
| 10 | cov(X,Y) | Direction of relationship |
| 10 | r = cov(X,Y)/(std(X)×std(Y)) | Normalized strength of relationship |
