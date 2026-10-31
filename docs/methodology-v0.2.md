# Polling comparison methodology v0.2 — provisional, non-inferential

**Effective date:** 2026-10-31. **Replaces only the acquisition/deduplication details** of [v0.1](methodology-v0.1.md); retain earlier outcome-vote and margin definitions. This is a *working protocol*, **not a frozen design for a definitive historical comparison**.

## Source tiers

**Tier A:** original pollster report, explicit question wording and sample definition, field dates, response shares, ideally survey ID.  
**Tier B:** complete original aggregator row with poll ID + question ID, original candidate shares, dates, sample/method fields, source URL.  
**Tier C:** curated secondary polling table with pollster, dates and major-party shares but no source question ID (2016 RCP and 2024 Electoral-Vote pilot).  

Use Tier C only for provisional data feasibility and documented spot checks; do not calculate a provider-neutral cross-cycle error distribution from different Tier C selection rules.

## Inclusion proposed for individual surveys

- Election general, state GA/PA/WI for pilot only, matching the *actual general-election major-party nominees* (2016 Clinton/Trump; 2020 Biden/Trump; 2024 Harris/Trump).
- One primary window: field-end date **1–14 days** before Election Day (inclusive). Do not use midpoint or publication dates as substitutions. Include but tag fieldwork **started >14 days** beforehand, with a predefined sensitivity exclusion.
- Keep the original percentages on the source's original ballot-question denominator, not a two-party reallocation. Preserve minor-party/undecided labels and distinct hypothetical/head-to-head matchups when available.
- Avoid including survey releases after the election where election-day information could contaminate the response; this needs published-date validation in a complete poll-level archive.
- Do not infer population/sample size or question wording from an unrelated aggregator's similar poll without separately documenting the crosswalk.

## Deduplication, preliminary mechanical rule

1. Treat raw candidate-answer rows within the **same question ID** as a single ballot question with several candidate responses.
2. Pair exactly one DEM and one REP share for that question. Preserve all other candidate choices and residual share when possible.
3. Group questions by `(election_year, state, source_poll_id)` when a **real** poll ID exists. If no poll ID exists, mark unique survey identity *unknown*, not the archive-row number.
4. Prefer **LV over RV over adults**, then an unknown category, only as a provisional *population priority*. If exactly one question is in the highest available tier, select it; if two or more questions are tied, **hold the entire poll out pending primary-source question-wording review**.
5. Do not break remaining ties using observed candidate margin, closeness to the election result, arbitrary question_id ordering, or post-election interpretation.
6. Treat tracking poll waves, overlapping fieldwork, multi-state pooled samples and syndicated releases as potentially dependent even when identifiers differ. Track repeated field dates and provider releases. No automatic claim of survey independence.
7. For the *formal* analysis, a future prespecified questionnaire priority (e.g. actual multi-candidate ballot over a hypothetical two-candidate question) must be justified from a **verified question wording**, never assumed from sample type or candidate total alone.

## Audit gates

- Every source URL, original file version/hash, field-date convention, population code, poll/question ID, update vintage, and licensing/redistribution constraint documented.
- Re-run validation scripts locally on exact GitHub repository files; verify derived CSVs and original-source spot checks.
- Audit missingness, selection bias, pollster and survey coverage by year, plus the 6 ambiguous 2020 poll IDs.
- Resolve or exclude the documented 2016 WI Marquette sample-count disagreement and 2024 WI Emerson 49/49 versus 50/50 archive discrepancy.
- Do not attribute residual geographic correlations to systematic bias or model trend significance with only three convenience-selected states and seven independent presidential election cycles.

## Current deliverables and status

[2016 and 2024 pilot table](../data/processed/pilot_03_2016_2024_final14_archive_polls.csv) **54 rows** (15 RCP 2016; 39 Electoral-Vote 2024), [2020 matched questions](../data/processed/pilot_2020_final14_paired_questions.csv) **175 questions**, [provisional unique 2020 polls](../data/processed/pilot_03_2020_unique_poll_provisional.csv) **115**, and [2020 ambiguous poll IDs](../data/processed/pilot_03_2020_ambiguous_polls.csv) **6**. See [Pilot 03 research report](pilot-03.md).

**Verdict for research process:** **PARTIAL PASS for acquisition and mechanical dedup triage, HOLD for three-election inferential comparison** until the above gates are satisfied.
