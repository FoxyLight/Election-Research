# Hypothesis register

**Date:** 2026-10-31. **All items below are proposals, not findings.** Status `NOT TESTED` means no new analysis has been conducted in this project.

| ID | Hypothesis/question | Evidence needed | Testability assessment | Status |
| --- | --- | --- | --- | --- |
| H1 | State polling-margin errors have an election-wide shared component. | Comparable state signed errors for several cycles; field dates and provider coverage. | **Promising** with hierarchical or variance-components modeling, but election count is small. | NOT TESTED |
| H2 | Certain states repeatedly exhibit similar directional or unusually large residual errors across elections. | Multi-cycle state errors, source comparability, missing-state map. | **Exploratory** due to seven presidential cycles and national-shift confounding. | NOT TESTED |
| H3 | After removing election-wide shifts, geographically adjacent or regionally grouped states still show error clustering. | State errors, explicit spatial or regional mapping, repeated cycles. | **Conditional**; do not equate geographic autocorrelation with a mechanism. | NOT TESTED |
| H4 | Survey methods are associated with different error distributions after accounting for timing, sample and election. | Poll-level mode, sample population, weighting, pollster, field end, duplicate controls. | **Uncertain / observational**; missing disclosures and selection bias can prevent identification. | NOT TESTED |
| H5 | Individual polls and published polling averages have different error distributions under common windows. | Poll-level entries and actual archived average values/cutoffs. | **Conditional**; averages share constituent polls, requiring paired or dependency-aware analysis. | NOT TESTED |
| H6 | Polling error patterns vary across presidential cycles beyond measurement noise. | Standardized errors for 2000–2024 with coverage diagnostics. | **Exploratory**; variation is measurable but formal inference constrained by few cycles. | NOT TESTED |

## Clarifications

- **H1** should not be called a standard state-to-state correlation from one observation per state in one year. A common election shift may be described or estimated using repeated state/poll observations over time; dependence must be modeled.
- **Directional error** sign convention (proposed): polled Democratic-minus-Republican margin minus observed Democratic-minus-Republican margin. Positive = polls overstated D margin.
- A consistent sign over a few cycles does not prove lasting systematic behavior or intent.
- The task is descriptive and retrospective, **not** a prediction of future election outcomes.
- Each hypothesis needs predefined inputs, exclusions, test method, uncertainty treatment and sensitivity checks before testing.

## Decision gate before formal testing

Require: (1) file-level source audit, (2) fixed unit of analysis, (3) source/field-date/denominator definitions, (4) independence structure, and (5) a written rule for missing states and pollster duplicates.
