# Day 24 — Advanced SQL: Query Optimization, Indexes, Reading EXPLAIN Plans

**Topics:** indexes (primary/secondary, composite), the read/write tradeoff, `EXPLAIN QUERY PLAN`, LIKE patterns and index usage, avoiding `SELECT *`

## What I Learned

- **Indexes** speed up reads by letting the database jump directly to matching rows instead of scanning every row — like a book's table of contents. Verified directly: before an index, `EXPLAIN QUERY PLAN` showed `SCAN customers` (full scan); after creating `idx_email`, the same query showed `SEARCH customers USING INDEX idx_email (email=?)`.
- **The read/write tradeoff** — indexes aren't free; they speed up SELECT queries but slow down INSERT/UPDATE/DELETE, since the index itself must be updated whenever the underlying data changes.
- **Composite indexes work left-to-right only** — verified directly on a `(city, name)` composite index: filtering by `city` alone used the index (`SEARCH ... USING INDEX`), but filtering by `name` alone fell back to a full scan, since `name` isn't the leftmost column.
- **`EXPLAIN QUERY PLAN`** (SQLite's human-readable execution plan) shows exactly what the database will do before running a query — `SCAN` means a full table scan (often a red flag), `SEARCH ... USING INDEX` confirms an index is being used effectively.
- **LIKE patterns and index usage — a genuinely non-obvious SQLite detail:** a trailing-`%` pattern (`'Customer5%'`) CAN use an index, but only if `PRAGMA case_sensitive_like = ON` is set first — without it, SQLite can't guarantee the case-insensitive LIKE matching lines up with the case-sensitive sort order of the index, so it defaults to a full scan even for a prefix-anchored search. A leading-`%` pattern (`'%50'`) can never use an index, since the database can't "jump to a starting point" in a sorted index without knowing what the string begins with.
- **`SELECT *` vs specific columns** — both return the same number of rows for an identical filter, but `SELECT *` retrieves every column's data for each row, while selecting only needed columns reduces the actual data transferred and processed. This gap grows significantly on tables with many more columns or many more rows.

## Resources Used

- "Mastering MySQL Query Performance: An In Depth Analysis and Index Tuning Guide" — https://www.youtube.com/watch?v=7ygH7DYO7yw
- "SQL indexing best practices | How to make your database FASTER!" — https://www.youtube.com/watch?v=BIlFTFrEFOI

## Mistakes I Made & Fixed

- In Task 1 (1b), executed `CREATE INDEX` but never re-ran the actual `EXPLAIN QUERY PLAN` query afterward — printed an empty result (`[]`) since `CREATE INDEX` returns no rows to fetch. Fixed by adding a separate `cursor.execute()` call re-running the same EXPLAIN query after the index existed, to properly compare before/after.
- Minor recurring typos in written explanations ("diffrence," "specifies" instead of "specified," "retrives") — didn't affect the correctness of the reasoning, just typing speed.
- Learned through direct testing (not just theory) that SQLite's LIKE-to-index optimization has a real prerequisite (`PRAGMA case_sensitive_like = ON`) that isn't obvious from the general "trailing % can use an index" rule most SQL tutorials state — this only became clear by actually running the query both with and without the pragma set.

## Exercises Completed

- [x] Task 1 — EXPLAIN QUERY PLAN before and after adding an index
- [x] Task 2 — Composite index left-to-right behavior
- [x] Task 3 — LIKE patterns and index usage (including the `case_sensitive_like` gotcha)
- [x] Task 4 — SELECT * vs specific columns
- [x] Task 5 — Reading EXPLAIN QUERY PLAN on a JOIN query

## Next Up

Days 21-24 (SQL fundamentals, joins, window functions, and optimization) are now complete — this closes out the first block of Phase 3.

**📌 Checkpoint reminder:** a review test covering Days 21-24 is due now, before continuing further into Phase 3.