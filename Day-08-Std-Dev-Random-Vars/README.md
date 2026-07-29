# Day 8 — Standard Deviation Deep Dive; Variables & Random Variables

**Topics:** interpreting standard deviation (empirical rule), coefficient of variation, variable types, random variables

## What I Learned

- **The Empirical Rule (68-95-99.7 rule):** for roughly bell-shaped data, ~68% of values fall within 1 standard deviation of the mean, ~95% within 2, ~99.7% within 3. Lets you judge how "unusual" a value is just from mean and std dev, without inspecting every data point.
- **Coefficient of Variation (CV)** = `(std dev / mean) × 100%`. Expresses spread as a percentage of the mean, making variability comparable across datasets with very different scales (e.g. comparing "spread in cm" to "spread in dollars" directly wouldn't be meaningful, but CV is).
- **Variable types:**
  - Quantitative (numeric): **discrete** (countable whole numbers — e.g. number of emails) vs **continuous** (any value in a range, incl. decimals — e.g. exact temperature)
  - Qualitative (categorical): **nominal** (no natural order — e.g. movie genre) vs **ordinal** (has a natural order — e.g. education level)
  - First question to ask: is it a number I can do math with, or a label/category? Then subdivide from there.
- **Random variable** = the numerical outcome of a random process, with specific possible values and probabilities attached (not just "a thing that varies" — specifically maps randomness to numbers).
- **Discrete random variable** = countable, specific values only (e.g. number on a die roll: 1-6, nothing in between). **Continuous random variable** = any value within a range, infinitely divisible (e.g. exact load time).
- Simulated 10,000 fair die rolls — the observed mean (3.5048) landed extremely close to the theoretical mean (3.5), a hands-on preview of the Law of Large Numbers (formally covered later in the probability unit).

## Resources Used

- General statistics fundamentals (empirical rule, coefficient of variation, variable classification, random variables)

## Mistakes I Made & Fixed

- Wrote `np.mean(scores, ddof=0)` when computing a value range — `ddof` only applies to `.std()`/`.var()`, not `.mean()`, since mean has no sample/population division distinction.
- Copy-paste bug: wrote `np.mean(class_b)` instead of `np.std(class_b)` when computing class_b's standard deviation, producing a meaningless CV of exactly 100.0 (mean divided by itself). Caught by noticing the result didn't make sense, then fixed and re-verified the conclusion still held after correcting the number.
- In variable classification, initially forgot "discrete" and "continuous" were valid options at all, mislabeling several numeric (count-based) variables as ordinal/nominal. Fixed by applying a first-question filter: "is this a number, or a category?" before choosing the specific subtype.

## Exercises Completed

- [x] Task 1 — Empirical rule verified on real test-score data (13/20 scores fell within the 68% range)
- [x] Task 2 — Coefficient of Variation compared across two classes with different scales
- [x] Task 3 — Variable classification (discrete/continuous/nominal/ordinal)
- [x] Task 4 — Simulated 10,000 dice rolls; confirmed discrete random variable behavior

## Next Up

Day 9 — Histograms; percentiles & quartiles; the 5-number summary