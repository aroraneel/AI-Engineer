# Day 20 — Capstone: Full Hypothesis-Testing Workflow on a Real Dataset

**Topics:** choosing the right statistical test; applying Z-test, two-sample t-test, chi-square goodness-of-fit, and ANOVA across 4 real business scenarios; reporting findings

**Format note:** unlike Days 11-19, this capstone was built in a `.ipynb` (Jupyter Notebook) rather than a `.py` file, since it better suits mixing code, output, and written reporting for a project-style deliverable. Days 21+ return to `.py`.

## What I Learned

- **The decision framework for choosing a test:**
  - Categorical data (checking distribution fit) → Chi-square goodness-of-fit
  - One numeric group vs a known value, σ known → Z-test
  - One numeric group vs a known value, σ unknown → One-sample t-test
  - Two independent numeric groups → Two-sample t-test
  - Three or more numeric groups → ANOVA
- **The full workflow, practiced end-to-end 4 times:** identify data type → state H0/H1 → choose the test → run it → apply the decision rule → translate the result into a plain-English, manager-ready conclusion.
- **H0/H1 must always be about the population parameter being tested** (a claimed value, or whether group means are equal) — NOT about whether a specific sample result is "true or false." This was the most common correction needed across all 4 tasks.
- **A borderline p-value still counts as "reject H0"** technically (Task 1: p=0.0442), but is worth flagging as less conclusive than a very small p-value (Tasks 2-4, all p<0.01) when reporting to a non-technical audience — statistical significance and practical/business urgency aren't automatically the same thing.
- **Findings can connect across tests** — the ANOVA result (South region shipping delays, Task 4) and the chi-square result (spike in Shipping support tickets, Task 3) likely describe the same underlying operational problem, illustrating how multiple statistical findings can combine into a single actionable business insight.
- **Notebook variable persistence is a real bug risk** — reused variable names across cells (e.g. `p_value` vs `p_val`) can silently carry over stale values from a previous cell's calculation if not renamed/recalculated carefully, producing a result that looks plausible but isn't actually from the current test.

## Resources Used

- Decision-tree diagram built from the accumulated logic of Days 16-19 (Z-test vs t-test vs ANOVA vs chi-square selection criteria)

## Mistakes I Made & Fixed

- Repeatedly misclassified data type as "categorical" for numeric/continuous measurements (load times, minutes-to-purchase) across multiple tasks — a recurring confusion worth deliberately double-checking on future real-world data: is it a measured NUMBER, or a discrete CATEGORY/LABEL?
- Wrote H0/H1 in terms of whether the specific sample result was "true or false" (e.g. "H0 = 2.15 seconds is true") instead of correctly framing them around the population parameter and the claimed/compared value.
- In Task 3's chi-square test, passed a single number instead of an array to `f_exp`, and separately triggered a notebook variable-collision bug — reused `p_value` name matched a stale value left over from Task 1's cell before recalculating and renaming variables consistently within the same cell.
- Initially left the "Finding" and "Overall Recommendations" sections of the final report as placeholders instead of synthesizing the individual task conclusions already written earlier in the notebook.

## Exercises Completed

- [x] Task 1 — Website load time claim (Z-test)
- [x] Task 2 — Two marketing email subject lines (two-sample t-test)
- [x] Task 3 — Customer support ticket category distribution (chi-square goodness-of-fit)
- [x] Task 4 — Shipping times across 4 warehouse regions (one-way ANOVA)
- [x] Task 5 — Full written summary report synthesizing all 4 findings

## Next Up

**Phase 2 (Probability & Inference) is now complete (Days 11-20).**

**📌 Checkpoint reminder:** a Phase 2 cumulative test covering Days 11-20 is due now, before moving into Phase 3.

Phase 3 begins next — SQL & Data Engineering.