# American Election Polling Research

An evidence-based, politically neutral investigation of how U.S. election polls compare with actual election returns, emphasizing historical error, geographic patterns, and recurrence across election cycles.

**Authoritative research record:** this repository. **Initial scope:** U.S. presidential general elections, 2000–2024. **As of:** 2026-10-31. **Current stage:** Phase 1, source investigation and feasibility assessment. No historical polling-error calculations have been performed here yet.

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

Test acquisition of a small **2016, 2020, 2024 state-level** sample from FiveThirtyEight and independent official/FEC returns; record schema, licenses, coverage, date fields, missingness and extraction provenance. Freeze metric definitions before any full analysis. Earlier cycles remain in scope but need separate source-quality checks.

This project is exploratory: hypotheses may be revised or rejected as evidence develops.
## Pilot 01: archived state polling versus election returns (2026-10-31)

- [Nine state-year pilot report](docs/pilot-01.md), including sources, comparisons and unresolved official-return coverage.
- [Nine RCP final-average observations](data/processed/pilot_rcp_state_averages.csv) and [nine illustrative individual poll entries](data/processed/pilot_selected_polls.csv).
- [Derived comparison CSV](data/processed/pilot_margin_errors.csv) and [recalculation script](analysis/pilot_accuracy.py).
- **Status:** PARTIAL PASS for archive extraction, joins and initial margin calculations. Exact certified vote totals independently checked for 2020 Pennsylvania and all three 2024 pilot states; five state-years still use rounded archive-reported outcome percentages as provisional comparison values.
- **Important:** these nine state-years and nine hand-selected polls are *not* representative observations. Do not infer nationwide accuracy or election-to-election persistence from them. The complete original poll CSV acquisition has not been verified.
