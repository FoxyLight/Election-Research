# American Election Polling Research

An evidence-based, politically neutral investigation of how U.S. election polls compare with actual election returns, emphasizing historical error, geographic patterns, and recurrence across election cycles.

**Authoritative research record:** this repository. **Initial scope:** U.S. presidential general elections, 2000–2024. **As of:** 2026-10-31. **Current stage:** Pilot 04 partial pass (2026-10-31). Original-report checks and 2020 tracking-wave overlap audits are documented; a validated common-source poll universe for 2016/2020/2024 is **still missing**. Official results verified for 9/9 pilot state-years. No cross-cycle statistical inference or H1–H6 tests have begun.

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

**Pilot 05: locate versioned, final-window question-level data consistently covering 2016, 2020, 2024**, ideally the original 538 historical files or downloadable AAPOR cleaned data; validate candidate/question/field-date identifiers across cycles, and define tracking-family and source-completeness rules before modeling errors.


This project is exploratory: hypotheses may be revised or rejected as evidence develops.
## Pilot 02: official returns complete, reproducibility validated (2026-10-31)

- [Pilot 02 report](docs/pilot-02.md) and [preliminary methodology v0.1](docs/methodology-v0.1.md).
- Official published presidential-vote denominators independently checked for **9/9** pilot state-years, including 2016 Georgia and Pennsylvania via the [U.S. House Clerk's election statistics](https://clerk.house.gov/member_info/electionInfo/2016/statistics2016.pdf).
- [Pilot comparisons](data/processed/pilot_margin_errors.csv) regenerated **exactly** by [the local Python script](analysis/pilot_accuracy.py). [Six regression checks](analysis/test_pilot_accuracy.py) passed.
- Original FiveThirtyEight [2016, 2020 and 2024 15–180-day polling metadata files](data/raw/fivethirtyeight/state-of-the-polls-2024/README.md) copied unchanged with Git blob hashes matched to upstream; they contain **no candidate vote shares and no final 14-day surveys**.
- [Metadata availability audit](data/processed/pilot_538_metadata_coverage.csv) and [reproducibility script](analysis/audit_538_metadata.py) (latter source-compiled, not run locally against full archived raw inputs in this session).
- **Additional acquisition:** [2020 final-fourteen-day paired question dataset](data/processed/pilot_2020_final14_paired_questions.csv) contains **175 Biden/Trump question pairs** across Georgia, Pennsylvania and Wisconsin, representing **121 state-specific distinct poll IDs**, with population and field dates. [Source and original-poll audit](docs/pilot-02-poll-data-addendum.md), [reproduction recipe](analysis/extract_2020_final14_pairs.py). This is a 2020-only sample of an archive, not 175 independent surveys; full integrity checking remains open.
- **Research gate:** do not infer polling accuracy trends or test persistent geographic bias from these illustrative nine cases or the unweighted question-level 2020 extract. Historical poll-level 2016 and 2024 data remain missing.

## Pilot 01 historical record

[Pilot 01](docs/pilot-01.md) documented the initial nine-state-year source comparison and found official-outcome gaps. The Pilot 02 report supersedes its provisional figures; old status notes remain in the dated research log for audit history.

## Pilot 03: final-window pilot, source checks and duplicate triage (2026-10-31)

- [Pilot 03 report](docs/pilot-03.md), [provisional methodology v0.2](docs/methodology-v0.2.md), and [offline validation script](analysis/pilot_03_validate.py).
- [2016/2024 archive extract](data/processed/pilot_03_2016_2024_final14_archive_polls.csv): **54 records** (15 in 2016, 39 in 2024) across GA, PA, WI.
- [2020 question-level extract](data/processed/pilot_2020_final14_paired_questions.csv): **175 paired questions** from 121 state-specific poll IDs. **115** unique top-tier [provisional survey records](data/processed/pilot_03_2020_unique_poll_provisional.csv); **6** [ambiguous poll groups](data/processed/pilot_03_2020_ambiguous_polls.csv) excluded, not arbitrarily resolved.
- Original source checks for 2016 WI Marquette, 2020 WI Marquette, and 2024 GA ECU, PA Marist, WI Marist. Unresolved 2016 Marquette sample-count and 2024 Emerson poll-share discrepancies are documented, not silently reconciled.
- **Caution:** Archive coverage, polling-question variants, tracking overlap and independence are not established across cycles. These extracts do **not** support cross-cycle significance or persistent geographic-bias claims. A deterministic independent consistency check of the GitHub CSVs passed; the committed Python Pilot 03 validator still needs a local checkout execution.

## Pilot 04: independence warnings and audit gate (2026-10-31)

- [Full Pilot 04 report](docs/pilot-04.md); [data-integrity methodology v0.3](docs/methodology-v0.3.md). **Status: PARTIAL PASS / inferential HOLD**.
- [115-record 2020 dependency audit](data/processed/pilot04_2020_poll_dependency_audit.csv) and [200 overlapping-fieldwork pairs](data/processed/pilot04_2020_overlap_pairs.csv), with a [Python verification script](analysis/pilot04_overlap_audit.py). **52** selected polling records begin >14 days before election; **40** distinct survey IDs participate in at least one same-pollster/state overlap; **42** are source-flagged tracking, **73** have a missing tracking flag.
- [13 primary-source crosschecks](data/processed/pilot04_primary_source_check_register.csv): confirms different likely-voter turnout models in two 2020 Monmouth polls, and documents 2016 Marquette sample count and 2024 Wisconsin Emerson percentages without inventing a reconciliation.
- [GitHub Actions validation workflow](.github/workflows/validate-research.yml) committed to run Python checks on code/data pushes; **the workflow's hosted run status was not accessible here**. Source-level overlap and consistency calculations were executed independently through the connected data-processing tools.
- **No validated uniform three-cycle question-level polling source yet**. The AAPOR research repository contains helpful scripts but the needed complete cleaned survey file was not found there; the fiveThirtyEight original post-election historical archive remains a research target.
