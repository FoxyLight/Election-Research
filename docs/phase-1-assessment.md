# Phase 1: data and methodology assessment

**Date:** 2026-10-31
**Stage:** Initial source investigation and feasibility assessment; **no full statistical analysis or independent polling error estimates have been completed**.

## 1. Feasibility by research task

| Task | Provisional feasibility | Reason / gate |
| --- | --- | --- |
| Actual presidential state returns, 2000–2024 | **High** | FEC provides federal-results compilations, including 2024 presidential results. Confirm denomination and data version. |
| National and state final polling errors, 2016/2020/2024 | **Promising** | FiveThirtyEight archived poll-level resources, RCP averages, and AAPOR reviews exist. File-level coverage and comparable sample criteria remain to be checked. |
| Comparable state poll errors, 2000–2012 | **Uncertain** | RCP has old final averages; earlier individual state polls, field dates and consistent aggregation are less well established. Do not backfill gaps silently. |
| Geographic clustering within election | **Potentially feasible** | Need consistent state-level directional margin errors. Distinguish nationwide common shift from spatial residuals. |
| Error persistence across cycles | **Exploratory only at first** | 2000–2024 has **seven** presidential cycles; correlated state observations cannot substitute for more independent election cycles. |
| Methodology versus error | **Conditional** | Only possible where mode, weighting, sampling frame, sample population and timing metadata are sufficiently recorded; observational comparisons are not causal identification. |
| Individual polls versus published averages | **Conditional** | Require like-for-like windows and independent handling of overlapping constituents; archived and reconstructed averages must be marked differently. |

## 2. Preliminary measurement definitions (proposed, not frozen)

- A poll observation is a published estimate with pollster, geography, field start/end, target population, question/candidate structure, and version where available.
- Initial principal outcome: **two-candidate margin (Democratic candidate % minus Republican candidate %)**. Record whether original percentages use *all respondents*, *decided voters*, or a two-party-normalized denominator. Never combine denominators silently.
- Actual margin on an **all-valid-votes** basis: 100 × (D votes − R votes) / all valid presidential votes, including other candidates in the denominator. State candidate share uses the same denominator. Other definitions can be calculated as sensitivity checks.
- Signed error: **polled margin minus actual margin**, in percentage points; positive means overestimated the Democratic margin, negative the Republican margin. Absolute error is magnitude of signed error. Preserve candidate-specific share errors independently.
- Classify polls by **fieldwork end date** relative to Election Day. Predefine final 14 days as starting comparison (consistent with AAPOR task-force convention); evaluate 7/30-day windows separately with attention to Election Day fieldwork and poll timing.
- Treat poll averages as separate source products with explicit computation/cutoff; do not combine individual polls and averages as independent observations.
- Use same inclusion rules across elections wherever feasible; if impossible, analyze noncomparable periods separately.

## 3. Data design and safeguards

Maintain separate source tables: `election_results`, `individual_polls`, `published_averages`, `sources`. Link by election year, office, jurisdiction, candidate ID, and source version. Preserve raw candidate labels and normalize names in a transparent mapping. Include source ID/URL, source's field dates, extraction date, provider update information, and missing-value reasons. Exact schema will be finalized once actual files are opened.

Rules:
- Exclude primaries from the initial general-election dataset; check presidential matchups before candidate mapping.
- Avoid double-counting revised releases, multiple survey questions and syndicated poll entries; predeclare deduplication.
- Do not turn an unweighted average into a provider-reported aggregate.
- Track undecided/third-party treatments, registered/likely voter sampling, and sampling-mode differences.
- Do not calculate a single cross-cycle trend with inconsistent source definitions without sensitivity analyses.

## 4. Geographic and recurring-error design

Begin descriptively with jurisdiction-by-year signed and absolute errors, counts of contributing polls, and missingness. Then:
1. Compare election-wide mean signed error with each state's residual after removing that election-wide shift.
2. Inspect whether residual error magnitude/direction clusters by region and whether that pattern is robust to geographic grouping and poll sample quality.
3. Check state error persistence using sign and magnitude across election years; distinguish state effects from shared national shocks and repeated use of a polling house.
4. Before formal inference, design a method that respects dependence among pollster-state-election observations and the small independent cycle count.
5. Avoid claiming one state-to-state correlation within one cycle from a single margin-error observation per state. Additional repeated measures are needed for conventional correlation estimation; spatial diagnostics are a different concept.

## 5. Evidence gaps and operational risks

- **Earliest-cycle availability:** the 2000 and 2004 raw state-poll record is not verified; an early vs late trend may reflect archive selection.
- **Access:** Harvard Dataverse page requested browser verification during review; direct hosted FiveThirtyEight CSV endpoints were indexed but not retrievable through this research browser. Validate via permitted download environment before claiming acquisition.
- **AAPOR replication:** a public R-code repository exists, but a complete downloadable poll-level replication dataset was not verified during review.
- **Different denominators:** all-candidate vs two-party shares, undecideds, and likely-voter assumptions change apparent errors.
- **Selection and dependence:** final-poll coverage is nonrandom; state, pollster and election errors are correlated. Published averages reuse poll data.
- **Versioning and licensing:** preserve the precise file and methodology vintage and check redistribution permissions.

## 6. Next recommended activity: small, audited pilot

1. Acquire and inspect a manageable set of presidential *state* polls from 2016, 2020, 2024, recording which provider/year/fields are actually available.
2. Acquire presidential returns for matching states from FEC and verify against independent MIT/official sources; record version and denominator.
3. Propose a codebook and match rules using **one election and a handful of states**, with field end date and candidate checks; **do not run the full historical comparison**.
4. Audit gaps, duplicates, 2024 candidate replacement, 2020 polling methods, and late-fielded polls before freezing a consistent analysis protocol.
5. Return to Phase 2 methodology decision; only then approve broad acquisition and calculations.

## 7. Phase 1 conclusion

It is realistic to investigate **historical polling error**, and probably some **cross-state common-shift and geographic-residual patterns**, but the original 2000–2024 all-state/all-poll aspiration must remain conditional on data access and comparability. Repeated-error hypotheses may be descriptive rather than statistically decisive with only seven presidential cycles. Do not confuse the existence of a historical archive, a published review, or an R script with verified complete source data.
