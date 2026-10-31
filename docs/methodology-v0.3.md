# Research methodology v0.3 — data-integrity rules versus unapproved inference rules

**Date:** 2026-10-31. **Status:** integrity requirements accepted; statistical comparison protocol **NOT frozen**.

## Fixed integrity rules

- **Signed margin error:** (published poll D minus R share) minus (official D minus R vote margin), percentage points. Preserve all original published candidate percentages and denominator definitions. Do not normalize to D+R=100 without explicitly labeling a sensitivity test.
- **Outcomes:** official published presidential-vote totals with the exact source and vintage for each state; never substitute total ballots cast for presidential candidate votes.
- **Date window for acquisition pilot:** source fieldwork end 1–14 calendar days before the election; retain field start and tag a survey if **any fieldwork starts before that window**. Date window is provisional for inferential work.
- **Multiple data layers:** candidate-answer row != ballot question != survey/poll ID != survey wave != distinct respondents != publisher's polling average. Report each count with its unit.
- **Candidate/question crosswalk:** verify actual major-party matchup and response wording. A common poll ID with separate LV/RV estimates or high/low-turnout models is **one survey** containing multiple estimates, not multiple independent samples.
- **Missing flags:** the 2020 mirror's `tracking` value is TRUE or blank; blank is **UNKNOWN**, not FALSE. No imputed population, sample size, question type, or pollster method without independently sourced crosswalk.
- **No hindsight selection:** never select based on closeness to actual result, party-direction error or inferred intent. Hold equal-tier question ambiguity as unresolved and record the candidate alternatives.
- **Dependence:** same pollster/state overlapping field dates are a **warning flag**, not direct proof of reused respondents. Model source/repeated-wave structure rather than incorrectly claiming independence.
- **Archived results vs actual:** polling aggregator "Final Results" values remain distinct from certified vote-total calculations. Historical average aggregation is not independent of its constituent polls.

## Rules held for prospective design

- **Question selection:** LV>RV>adults priority in 2020 is mechanical *triage*, not general-purpose validation of survey comparability. Both Monmouth high/low LV turnout models are substantively real; selecting one without a predeclared justification is arbitrary.
- **Tracking wave policy:** field-start overlaps and source tracking TRUE suggest dependence. A single latest fully eligible wave per explicitly verified tracker family could be a candidate sensitivity analysis, but wave family needs verified source evidence.
- **Primary versus archival precision:** compare the same ballot question, population and candidate list; if original and secondary shares differ, retain both and assign `UNRESOLVED_VARIANT`, do not pick the figure that fits results.
- **Three-cycle comparability:** do not combine 2016 RCP, 2020 FTE and 2024 Electoral-Vote data as if they were a common sampling universe. Compare full-archive coverage, missingness, source license and revision vintage first.
- **Time window sensitivity:** AAPOR 2024 includes Election Day in final-two-week fieldwork end; this pilot excludes it. Never present AAPOR's reported errors as precisely reproducing the project's window.
- **Cross-cycle uncertainty:** with only seven presidential elections from 2000–2024 and geographically correlated state errors, neither row-level large n nor overlapping trackers imply a large number of independent election cycles.

## Current observed dependency warnings

[Audit of 115 2020 provisional survey records](../data/processed/pilot04_2020_poll_dependency_audit.csv):
52 start before 14-day window; 40 poll IDs involved in 200 pairwise same-state/same-pollster field-date overlaps; 198 of those pairs are SurveyMonkey and 2 are YouGov. The source declares TRUE tracking for 42 records and is blank for 73. These are **descriptive diagnostic counts**, not estimates of effective sample size or bias.

[Crosschecks and unresolved questions](../data/processed/pilot04_primary_source_check_register.csv): the 2020 Monmouth RV/high-LV/low-LV model variants are primary-source validated; Marquette 2016 sample-size discrepancy and 2024 WI Emerson source-value disagreement remain flagged.

## Gate to inferential statistics

Require all: a source-verified question-level dataset across target cycles or a deliberately smaller consistently sourced scope; stable IDs and field dates; independent original-source checks of candidate definition and category; explicit repeated tracking family definitions; prespecified question priority; source and state coverage diagnostics; realistic uncertainty model. If a gate fails, make only explicitly labeled *descriptive convenience-sample* comparisons.

See [Pilot 04](pilot-04.md), then the planned Pilot 05 archival reconstruction.
