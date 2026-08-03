# Day 6 — What is Statistics, Types of Statistics, Population vs Sample — Notes

Topics covered: what is statistics; types of statistics; population vs sample

---

## 1. What is Statistics?

Statistics is the science of **collecting, analyzing, interpreting, and
presenting data** to make sense of the world and make informed decisions,
especially under uncertainty.

In AI/ML: statistics is what lets you go from "here's a pile of numbers" to
"here's what those numbers actually mean, and how confident I should be about
conclusions drawn from them." Every ML model is, underneath, doing statistics
at scale.

> Statistics = collecting, analyzing, interpreting data to draw conclusions
> and make decisions under uncertainty.

---

## 2. Two Types of Statistics

**Descriptive statistics** — summarizing and describing the data you actually
have in front of you. No guessing beyond the data, just organizing and
summarizing it.
- Examples: mean, median, mode, standard deviation, charts (everything from
  Days 1-5).

**Inferential statistics** — using a smaller sample of data to make
**generalizations or predictions** about a larger group you didn't fully
measure.
- Examples: hypothesis testing, confidence intervals, predicting an election
  outcome from a poll of 1,000 people instead of asking everyone.

> Descriptive = summarizes data you have. Inferential = uses a sample to make
> conclusions about a larger group you don't have full data on.

---

## 3. Population vs Sample

The single most foundational concept in statistics — comes up constantly in
ML.

**Population** = the *entire* group you're interested in studying. Every
single member.

**Sample** = a smaller, manageable subset of the population, actually
collected/measured.

**Concrete example:** wanting the average height of all adults in India (the
population — 900M+ people). Measuring everyone is impossible, so 5,000
randomly selected adults are measured (the sample) to *estimate* the
population's average height.

**Why this matters for ML specifically:** training data is almost always a
**sample**, not the full population of "all possible data that could ever
exist" for a problem. A big part of ML is ensuring that sample is
*representative* enough that conclusions/models built on it generalize well
to new, unseen data (the rest of the "population").

> Population = entire group. Sample = subset actually measured. ML training
> data is a sample; models must generalize to the broader population of
> unseen data.

**Worked example:** A hospital wants the average recovery time for a new
treatment. They can't track every patient who will ever receive it, so they
study 200 patients who took it last year.
- **Population** = all patients who will ever receive this treatment (past,
  present, future).
- **Sample** = the 200 patients actually studied.
- The hospital uses the sample's results to make a claim about the entire
  population — the core move inferential statistics allows, with proper
  uncertainty accounted for.

---

## Quick Reference Cheat Sheet

```
Statistics
|-- Descriptive  -> summarize data you HAVE (mean, median, std dev, charts)
`-- Inferential  -> use a SAMPLE to generalize about a POPULATION
                    (hypothesis testing, confidence intervals)

Population = entire group of interest
Sample     = subset actually measured/collected
```

---

## Session Notes

- Concept-only day — no coding practical, consistent with the roadmap
  structure (hands-on statistics work with formulas begins Day 7 onward).
- Correction made during this session: initially over-extended "Day 6" to
  include content that actually belongs to Day 7 and Day 8 (central
  tendency, dispersion, standard deviation, n-1). Caught and corrected before
  covering that material out of sequence — worth double-checking day
  boundaries against the source roadmap rather than relying on memory.