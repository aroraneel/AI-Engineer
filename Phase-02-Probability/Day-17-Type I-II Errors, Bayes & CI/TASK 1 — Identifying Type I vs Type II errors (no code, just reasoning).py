# For each scenario below, write a comment saying whether it describes
# a TYPE I or TYPE II error, and briefly why.

# 1a. A spam filter marks a legitimate, important email as spam.
# -> TYPE I error.
# -> Reject H0 (H0 = "this email is not spam") when H0 was actually true
#    -- a false alarm, since a legitimate email got wrongly flagged.

# 1b. A spam filter lets an actual spam email through to the inbox.
# -> TYPE II error.
# -> Fail to reject H0 (H0 = "this email is not spam") when H0 was
#    actually false -- a missed detection, since real spam went unflagged.

# 1c. A court finds an innocent person guilty.
# -> TYPE I error.
# -> Reject H0 (H0 = "the person is innocent") when H0 was actually true
#    -- a false alarm, since an innocent person was wrongly convicted.