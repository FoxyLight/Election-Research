# American Election Polling Research

An evidence-based, politically neutral investigation of how U.S. election polls compare with actual election returns, emphasizing historical error, geographic patterns, and recurrence across election cycles.

**Authoritative research record:** this repository. **Initial scope:** U.S. presidential general elections, 2000–2024. **As of:** 2026-10-31. **Current stage:** Pilot 02 outcome reconciliation and a limited poll-metadata archive audit. All nine official outcome references validated; comprehensive final-week candidate-level polling acquisition remains open. No historical polling-error calculations have been performed here yet.

## Questions

- How accurately did final polls measure candidate vote shares and two-candidate margins?
- Did polling errors vary systematically by state, region, election, or method?
- Were recurring patterns persistent or limited to particular election years?
- Which hypotheses are actually testable with publicly accessible data?

## Research documents

- [Source inventory](docs/source-inventory.md): verified source listings and access limitations.
- [Phase 1 assessment](docs/phase-1-assessment.md): data coverage, preliminary methods, evidence gaps and next activity.
- [Hypothesis register](docs/hypotheses.md): testability decisions and methodological cautions.
- [Research log](docs/research-log.md): dated progress and change history.

## Research standards

Distinguish poll measurements from polling averages and probabilistic election forecasts. Compare like with like, preserve raw data and provenance, specify each error metric's denominator and sign, and account for correlated polls, overlapping samples, and few independent election cycles. Document missing data rather than reconstructing it from assumptions. Research conclusions should be based on reproducible calculations and source documentation, not political preference or post-hoc storytelling.

## Current next step

Acquire and validate **machine-readable, final-two-week individual poll vote-share data** for 2016/2020/2024. The three archival FiveThirtyEight metadata CSVs from 15–180 days before Election Day cannot substitute for the needed candidate-preference estimates.


This project is exploratory: hypotheses may be revised or rejected as evidence develops.
## Pilot 02: official returns complete, reproducibility validated (2026-10-31)

- [Pilot 02 report](docs/pilot-02.md) and [preliminary methodology v0.1](docs/methodology-v0.1.md).
- Official published presidential-vote denominators independently checked for **9/9** pilot state-years, including 2016 Georgia and Pennsylvania via the [U.S. House Clerk's election statistics](https://clerk.house.gov/member_info/electionInfo/2016/statistics2016.pdf).
- [Pilot comparisons](data/processed/pilot_margin_errors.csv) regenerated **exactly** by [the local Python script](analysis/pilot_accuracy.py). [Six regression checks](analysis/test_pilot_accuracy.py) passed.
- Original FiveThirtyEight [2016, 2020 and 2024 15–180-day polling metadata files](data/raw/fivethirtyeight/state-of-the-polls-2024/README.md) copied unchanged with Git blob hashes matched to upstream; they contain **no candidate vote shares and no final 14-day surveys**.
- [Metadata availability audit](data/processed/pilot_538_metadata_coverage.csv) and [reproducibility script](analysis/audit_538_metadata.py) (latter source-compiled, not run locally against full archived raw inputs in this session).
- **Research gate:** do not infer polling accuracy trends or test persistent geographic bias from these illustrative nine cases; acquire candidate-level end-of-campaign polls first.

## Pilot 01 historical record

[Pilot 01](docs/pilot-01.md) documented the initial nine-state-year source comparison and found official-outcome gaps. The Pilot 02 report supersedes its provisional figures; old status notes remain in the dated research log for audit history.
