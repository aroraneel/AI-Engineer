# Day 13 — Normal/Gaussian Distribution; Standard Normal & Z-score; Uniform Distribution

**Topics:** Normal (Gaussian) distribution — shape, formula intuition, scipy; empirical rule (68-95-99.7); Z-scores; Uniform distribution — formula, scipy, mean

## What I Learned

- **Normal distribution** — a continuous, symmetric, bell-shaped distribution fully defined by two parameters: `μ` (mean, location/center) and `σ` (standard deviation, scale/width). Mean = median = mode, all at the center.
- **Formula intuition** — `f(x) = (1/(σ√2π)) × e^(-(x-μ)²/2σ²)`. The `(x-μ)²` term measures squared distance from center (always positive, punishes large distances faster than small ones). The `e^(-...)` term creates the decay — 1 at the mean, shrinking toward 0 further away. The `1/(σ√2π)` term is purely a normalizing constant so total area under the curve equals exactly 1 (the PDF rule from Day 11).
- **σ controls width, not just spread** — larger σ → wider, flatter bell; smaller σ → narrower, taller bell. Verified this both visually (diagram) and mathematically (dividing by 2σ² inside the exponent).
- **Empirical Rule (68-95-99.7)** — for any Normal distribution: ~68% of data within μ±1σ, ~95% within μ±2σ, ~99.7% within μ±3σ. Verified the 68% approximation is precisely 68.27% using `norm_dist.cdf()`.
- **Z-scores** — `z = (x-μ)/σ` tells you how many standard deviations a value is from the mean. Positive = above average, negative = below average. Comparing **distance from average** means comparing `|z|` (absolute value), not the raw z-score, since sign only indicates direction.
- **Uniform distribution** — every value in a range `[a,b]` is equally likely (flat, not bell-shaped). Formula: `f(x) = 1/(b-a)`. Mean = midpoint `(a+b)/2`. Used for scenarios like "any minute in a fixed window" or "any face of a fair die" — no clustering around a center.
- **Normal vs Uniform — the real distinguishing question:** does the data cluster around a typical/average value (Normal), or is every outcome equally likely with no "typical" value standing out (Uniform)?

## Resources Used

- "Normal Distribution Explained in Hindi | Statistics Series" — https://www.youtube.com/watch?v=2CGvLkj-V4Q (covered shape, symmetry, mean=median=mode, location vs scale parameter terminology for μ/σ)
- "Normalization Constant for the Normal/Gaussian | Full Derivation with visualizations" — https://www.youtube.com/watch?v=u2q7YmwfcyU (optional, formal calculus derivation of the `1/(σ√2π)` normalizing constant — not required for the applied depth used day-to-day, kept as an advanced reference)

## Mistakes I Made & Fixed

- Initially calculated the 95% empirical rule range using ±1σ instead of ±2σ (gave 60-80 instead of the correct 50-90) — mixed up the 68% range with the 95% range. Corrected by explicitly re-deriving each range (1σ→68%, 2σ→95%, 3σ→99.7%) with the actual numbers.
- In the CDF verification task, printed the exact probability but didn't explicitly state the comparison to the 68% approximation the task asked for — technically correct math, but incomplete answer to what was asked. Learned to make comparisons explicit in output (side-by-side print, difference, or a comment), not just leave the raw number for the reader to compare mentally.
- In the z-score comparison task, wrote the wrong z-score value in the explanation comment (1.0 instead of the correctly computed 2.0) — a copy-paste slip since the printed output was correct. Also initially answered the "who is further from average" question by describing each person separately instead of directly comparing them via `|z|` (absolute value) — fixed by adding an explicit concluding comparison line.
- Named a density variable generically as `x` in the Uniform task instead of something descriptive like `density` — not a bug, but reduces readability since `x` usually refers to the input value, not the output density.
- Left the reasoning blank for why adult heights are Normal (not Uniform) in the scenario-identification task — filled it in by contrasting with the Uniform examples: heights cluster around a typical average (bell-shaped), while Uniform scenarios have no typical value at all (every outcome equally likely).

## Exercises Completed

- [x] Task 1 — Normal distribution with scipy (density at mean vs far from mean)
- [x] Task 2 — Empirical Rule ranges (68/95/99.7%)
- [x] Task 3 — Verifying the empirical rule using CDF
- [x] Task 4 — Z-scores and comparing distance from average
- [x] Task 5 — Uniform distribution (manual formula, scipy, mean)
- [x] Task 6 — Identifying Normal vs Uniform scenarios with reasoning

## Next Up

Day 14 — Log-normal, Power law, Pareto distributions; Central Limit Theorem