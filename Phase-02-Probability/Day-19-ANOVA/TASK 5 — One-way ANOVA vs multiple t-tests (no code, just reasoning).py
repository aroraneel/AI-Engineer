# You want to compare average delivery times across 4 different
# delivery companies.

# 5a. Would it be statistically appropriate to just run 6 separate
#     t-tests (comparing every possible pair among the 4 companies)
#     instead of one ANOVA? Why or why not?
# -> No, running 6 separate t-tests is NOT appropriate. Each t-test
#    carries its own 5% false-alarm risk, and running 6 of them stacks
#    that risk up to roughly 26% overall -- much higher than intended.
#    ANOVA tests all 4 groups together in ONE test, keeping the true
#    error rate at the intended 5%.

# 5b. What specific problem from Day 17 does running many separate
#     t-tests risk increasing?
# -> Running many separate t-tests increases the risk of a Type I
#    error (false alarm) -- wrongly concluding a real difference
#    exists between some pair of companies, just from accumulated
#    random chance across multiple tests.