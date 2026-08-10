# Day 14 — Log-normal, Power law, Pareto Distributions; Central Limit Theorem

**Topics:** recognizing skewed distributions (Log-normal, Power law, Pareto); standard error; simulating the Central Limit Theorem from a non-normal population

## What I Learned

- **Log-normal distribution** — if the log of a dataset looks Normal, the original data is log-normal. Happens when a variable is the *product* of many independent factors (not a sum, which leads to Normal via CLT). Real examples: income, file sizes, stock prices. Sharp peak near low values, long right tail, never negative.
- **Power law distribution** — `y = x^(-a)`, where frequency is inversely proportional to magnitude. A tiny number of items dominate the total. Real examples: word frequency, city sizes, website traffic. Shows up as a straight line on a log-log plot.
- **Pareto distribution** — a specific, well-known power law: the "80/20 rule" — 80% of effects come from 20% of causes. Real examples: 80% of revenue from 20% of customers, 20% of code causing 80% of bugs.
- **Practical takeaway for all three:** don't blindly apply mean/std to this kind of data — a huge spike near zero with a long thin tail signals log-normal/power law/Pareto, not Normal, and the "average" becomes a misleading summary when a few extreme values dominate.
- **Central Limit Theorem (CLT):** the distribution of *sample means* approaches Normal, regardless of the original population's shape, as sample size grows (n≥30 rule of thumb). Demonstrated this directly in code — built a skewed exponential population, took 1000 sample means, and confirmed the result was approximately Normal and centered on the true population mean.
- **Standard error** — `σ/√n`, the standard deviation of sample means. Shrinks as sample size `n` grows, which is why larger samples give more reliable estimates. Verified the formula's prediction (0.9129) closely matched the actual simulated standard deviation of sample means (0.9193), even though the original population was heavily skewed, not Normal.
- **Why CLT matters going forward:** it's the foundation for A/B testing, confidence intervals, and hypothesis testing (Days 15-17) — those tools work specifically because sample means behave predictably (Normal-ish) regardless of the underlying population.

## Resources Used

- "Log normal distribution | Math, Statistics for data science, machine learning" — https://www.youtube.com/watch?v=xtTX69JZ92w
- "Log Normal Distribution in Statistics" — https://www.youtube.com/watch?v=sPzPEeJ4OQ4
- "Central Limit Theorem - Dice Example" — https://www.youtube.com/watch?v=aUyk5V0dh3Y
- "Rolling 2 Dice: An Intuitive Explanation of The Central Limit Theorem" — https://www.youtube.com/watch?v=VZl7gkMbipk
- Interactive CLT dice simulator — https://math.bu.edu/people/rmagner/CLTdemo.html

## Mistakes I Made & Fixed

- In Task 5, referenced `population.std()` without recreating the `population` variable in that file — each task file runs independently, so a variable from Task 3's file doesn't carry over. Fixed by regenerating the population with `np.random.exponential(scale=5, size=100000)` at the top of the Task 5 file.
- In a couple of "compare" tasks (4c), explained the general CLT concept correctly but didn't explicitly cite the actual computed numbers being compared (e.g., 4.98 vs 5.01) — same pattern as a mistake from Day 13. Working on making comparisons numerically explicit, not just conceptually correct.

## Exercises Completed

- [x] Task 1 — Identifying Normal vs skewed (Log-normal/Power law/Pareto) scenarios
- [x] Task 2 — Standard error calculation for two sample sizes
- [x] Task 3 — Building a skewed population (exponential distribution)
- [x] Task 4 — Taking 1000 sample means from the skewed population (CLT demonstration)
- [x] Task 5 — Verifying the standard error formula against the simulation

## Next Up

Day 15 — Estimation theory; hypothesis testing fundamentals; p-values

**📌 Checkpoint reminder:** Day 15 completes the first 5-day block (Days 11-15) — a review test covering this block is due after Day 15.