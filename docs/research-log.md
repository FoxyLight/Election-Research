# Research log

## 2026-10-31 — Phase 1 initial source assessment

**Request:** Start source investigation and establish the authoritative research record in `FoxyLight/Election-Research`; investigate presidential general-election polls 2000–2024, with recurring/geographic error as a major priority. Do not begin full analysis.

**Checked:** GitHub repository was empty at the start. Reviewed FEC federal-election-result index; MIT Election Lab portal and external Dataverse catalogue; FiveThirtyEight `polls/`, `pollster-ratings/`, and `state-of-the-polls-2024/` READMEs; RealClearPolling historical archive; Roper Center iPoll access description; AAPOR polling accuracy pages and 2024 code repository.

**Findings:** Official results are readily indexed for all seven presidential cycles. Public polling archive indexes exist, but true poll-level coverage (especially 2000–2008), uniform final-window availability, exact current download access and methodological metadata remain unverified. Roper full-study access can be restricted. FiveThirtyEight's 2024 comparative archive explicitly excludes the last 14 days (uses 15–180 days before Election Day), so it is not a complete final-poll source.

**Limitations:** No historical comparison file was downloaded, parsed, cleaned or statistically analyzed. The Harvard Dataverse site and certain CSV URLs could not be retrieved through the research web interface. AAPOR's public 2024 GitHub code was located, but full promised replication CSVs were not confirmed.

**Documentation created:** README and Phase 1 source inventory, assessment and hypotheses register.

**Next activity:** Execute a small file-level acquisition/schema pilot for 2016, 2020, 2024 and matching official returns; document duplicates, field-date cutoffs and candidate/denominator mapping before finalizing methods.

## 2026-10-31 — Pilot 01, narrow source-level acquisition and comparison

**Scope:** Georgia, Pennsylvania, Wisconsin for presidential elections 2016, 2020, 2024. Nine published RCP average rows plus nine illustrative individual-poll rows transcribed from directly viewed source tables. URLs and retrieval dates are stored with each observation.

**Verified official vote counts:** 2024 all three states from visually reviewed FEC tables, 2020 Pennsylvania from its Department of State, **2016 Wisconsin and 2020 Wisconsin from visually reviewed National Archives certification**, and **2020 Georgia from the amended December 7 certification** in the National Archives. **Not yet independently verified:** full 2016 Georgia and Pennsylvania presidential vote totals/denominators. These **two** rows retain RCP's rounded final-results benchmark and are explicitly marked provisional.

**Calculation check:** all 9 state-year keys joined with a selected archived poll, selected polls' field end dates precede Election Day, and signed Democratic-minus-Republican margin errors were independently recomputed from the extracted values. The Python script was committed to allow another researcher to regenerate the derived CSV; the Python script itself has not been executed here.

**Data quality issue:** RCP's 2024 Pennsylvania reported winner and runner-up result percentages differ from percentages derived from the FEC's full statewide presidential vote denominator. Preserve the raw percentages and source-specific denominator, and do not assert a cause without supporting evidence.

**Deliverables:** `docs/pilot-01.md`, two source-data pilot CSVs, computed-errors CSV, `analysis/pilot_accuracy.py`. **Research gate:** official-count backfill, complete individual-poll data acquisition, reproducible script execution and inclusion criteria before full statistical analysis.

## 2026-10-31 — Pilot 01 source-validation addendum

Reviewed Wisconsin's 2016 and 2020 presidential certificates and Georgia's amended December 7, 2020 certificate (including the superseded Georgia certificate in the same PDF). Backfilled three official result rows (2016 WI, 2020 WI, 2020 GA) and recomputed the affected margin errors. **Now 7/9 pilot results use official-count denominators; 2016 GA/PA remain provisional.** Source URLs and changed data live in the pilot average and derived-error CSVs. The repo contains a recalculation Python script, but it has not yet been executed through a local checkout. See [Pilot 01](pilot-01.md).

## 2026-10-31 — Pilot 01 source discrepancy identified

A Georgia SOS 2016 official statewide summary prints 4,092,373 votes across three named presidential candidates, while historical compilations show other totals when including different write-in or other candidate categories (4,146,825 in the election atlas; 4,114,732 in Ballotpedia). The 2016 Georgia National Archives Certificate of Ascertainment certifies the three named candidate counts but not all write-ins. **No denominator chosen yet; 2016 GA and PA remain provisional.** This is a data-definition issue, not an inference of irregularity. Full provenance and source links in [Pilot 01](pilot-01.md).

## 2026-10-31 — Pilot 02: official denominator resolution and file-level acquisition

**Official outcomes:** U.S. House Clerk original PDF recapitulation pages inspected for Georgia and Pennsylvania 2016. GA: D 1,877,963, R 2,089,104, other 147,665, total **4,114,732** including **22,359 write-ins**. PA: D 2,926,441, R 2,970,733, other 218,228, total **6,115,402**. All **9/9** pilot state-years now have independently referenced official published totals. The historical 4,146,825 GA alternative is not used because it follows a different compilation convention; no inference about election irregularity.

**Reproducibility:** Exact GitHub Python script and pilot CSV input blob hashes verified in a local directory; `python analysis/pilot_accuracy.py --write` generated the **same Git blob SHA** as committed derived comparison CSV. Six standard-library regression tests executed, **6/6 pass**. Tests committed to `analysis/test_pilot_accuracy.py`.

**Poll-file acquisition:** Retrieved complete 2016, 2020, 2024 FiveThirtyEight `state-of-the-polls-2024` **metadata-only** CSV files, and committed unchanged under `data/raw/fivethirtyeight/` with source hashes, size and CC BY 4.0 attribution. Per-state metadata records and tracking counts computed, saved to `data/processed/pilot_538_metadata_coverage.csv`. They end **15–180 days** before Election Day and lack candidate shares. Companion audit Python script source was compiled locally; full-file Python execution remains to be independently run in a checkout.

**Blocked source:** original final-week vote-share poll CSVs are not yet extracted across all three cycles. Big 538 pollster-rating raw files exceed the file-content tool's read limit; old hosted CSV URLs failed this session.

**Decision:** Freeze only signed error and outcome denominator/candidate-share preservation conventions; keep final-14-day field-end cutoff, poll-question matching and de-duplication rules **provisional** until we can inspect a real final-window poll dataset. See [Pilot 02](pilot-02.md) and [Methodology v0.1](methodology-v0.1.md). No H1–H6 test.

## 2026-10-31 — Late Pilot 02: full 2020 presidential poll mirror and final14 questions

The GitHub blob endpoint successfully returned the exact 5,545,063-byte historical [2020 FiveThirtyEight data mirror](https://github.com/simonw/fivethirtyeight-polls/blob/main/president_polls.csv) (blob `cbe565b7647059de8b58414e420d2b8587250cc6`), where ordinary file content retrieval was empty. Parsing 16,438 answer rows produced 175 Biden/Trump question pairs satisfying state GA/PA/WI, presidential general, field end 1–14 days before 2020-11-03. Distinct poll IDs by state: Pennsylvania 55, Wisconsin 34, Georgia 32. Fourteen paired questions have blank methodology.

Original Marquette Law School 2020 Wisconsin October 21–25 LV and RV toplines were verified: question IDs 135295 and 135296, poll ID 72151; respectively Biden/Trump 48/43 with 749 LV and 47/43 with 806 RV. These are distinct subsets of **the same poll**, not independent samples.

Committed [175 paired questions](../data/processed/pilot_2020_final14_paired_questions.csv), [blob-verified extraction recipe](../analysis/extract_2020_final14_pairs.py), and [provenance/limits addendum](pilot-02-poll-data-addendum.md). Question-level extraction performed against full blob through data-processing tools; **the Python extraction recipe has not been executed on the 5.5MB source in a local checkout**. A 2024 final-week source and a comparable 2016 field-end-date source remain outstanding. Previous 2020 access-block note was a snapshot from before using blob retrieval. No H1–H6 tests conducted.
