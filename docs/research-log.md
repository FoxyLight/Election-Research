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

## 2026-10-31 — Pilot 03, 2016/2024 final-window source acquisition and de-duplication triage

**Question:** Are final 1–14 day candidate-preference measurements accessible for 2016 and 2024 in PA, WI, GA, and how can 2020 multiple-question polls be triaged without looking at election results?

**Acquisition:** From [RCP's 2016 final battleground polling table](https://www.realclearpolitics.com/epolls/2016/president/2016StateFinalResults.html), manually transcribed **5 GA / 6 PA / 4 WI** entries, including sample population and sizes when the table provided them. From [Electoral-Vote.com's 2024 state polling archive](https://www.electoral-vote.com/evp2024/Pres/pres_polls.html), manually transcribed **9 GA / 18 PA / 12 WI** entries; the latter source curates pollsters and supplies **no poll-question IDs, sample population or size**. Stored 54 dated candidate-share rows in `data/processed/pilot_03_2016_2024_final14_archive_polls.csv`. Both archives are bounded subsets, **not a verified comprehensive poll universe**. The available Oct. 28, 2016 FiveThirtyEight snapshot is too early to cover the last 14 days and was **not** substituted for complete final-week 2016 data.

**Original-source checks:** Marquette Wisconsin 2016 46/40 Clinton/Trump, but its published LV sample counts conflict with RCP (1,255 unweighted / 1,190 weighted versus 1,225 on RCP); East Carolina Georgia 2024 49/50 Harris/Trump; Marist Pennsylvania and Wisconsin 2024 both 50/48. Earlier 2020 Marquette LV/RV source checks retained. The 2024 Wisconsin Emerson value 50/50 in Electoral-Vote.com differs from RCP 49/49; a Hill poll tracker shows roughly 49.4/49.4 in a comparable question, but the exact question normalization is **unverified**.

**2020 poll-level selection:** 175 Biden/Trump questions correspond to 121 state+poll IDs. A pre-outcome, mechanically applied population ranking LV > RV > adults > other yields **115 unambiguous one-question groups** and **6 ambiguous same-tier groups** held out and logged. No cherry-picking by closeness to actual returns; tracking-wave and questionnaire-dependence risks remain untested.

**Validation:** Source-extract 2016/2024 counts, date windows, candidate subtraction, absent fields and 2020 deterministic selection were independently checked by re-reading all committed CSVs via the GitHub connector. This check **passed**. A companion Python audit script was committed, but **not executed in a local checkout**. Detailed report [Pilot 03](pilot-03.md) and working protocol [Methodology v0.2](methodology-v0.2.md).

**Decision:** **PARTIAL PASS** for bounded acquisition and method triage; **HOLD** for cross-cycle inferential analysis and H1–H6 tests. Pilot 04 should prioritize consistent source/question frames, verification of multiple question versions and non-independent poll waves, and a real local script execution.

## 2026-10-31 — Pilot 04: tracking overlap, original-report audits, and inference gate

**Independent audit of repo data:** The 115 selected 2020 poll IDs were re-read directly from GitHub and compared pairwise for identical state/pollster and intersecting fieldwork dates. Result: **200** overlapping **pairs**, involving **40** distinct poll IDs; 198 pairs SurveyMonkey, 2 pairs YouGov. **52** records started more than 14 days before election despite fieldwork ending inside the final-14-day window. Source 2020 FiveThirtyEight mirror tracking flag TRUE for **42**, blank for **73** (blank is unknown, NOT FALSE). Per-ID audit and pairs written to `data/processed/pilot04_2020_poll_dependency_audit.csv` and `data/processed/pilot04_2020_overlap_pairs.csv`. The matching `analysis/pilot04_overlap_audit.py` is in repo; the separate Python runner's conclusion is not established in this session.

**Original question and primary release checks:** [2020 Georgia Monmouth](https://www.monmouth.edu/polling-institute/reports/monmouthpoll_ga_102820/) 50/45 RV, 50/46 high LV, 50/48 low LV, all **same poll ID 72146**; [2020 Pennsylvania Monmouth](https://www.monmouth.edu/polling-institute/reports/monmouthpoll_pa_110220/) 50/45 RV, 51/44 high LV, 50/45 low LV, **same ID 72599**. These model differences are substantively real, so no unprincipled choice was made. [2016 Monmouth PA](https://www.monmouth.edu/polling-institute/reports/monmouthpoll_pa_110216/) 48/44 confirmed. [2016 Marquette WI](https://law.marquette.edu/poll/2016/11/02/mlsp41release/) primary 1,255 LV unweighted/1,190 weighted, RCP 1,225 still differs. [2024 WI Emerson primary](https://emersoncollegepolling.com/november-2024-final-swing-state-polls-too-close-to-call-election-for-president/) 49/49, secondary Electoral-Vote 50/50; alternative normalization or question not verified. [2020 GA Emerson](https://emersonpolling.reportablenews.com/pr/super-poll-sunday-democrats-within-striking-distance-in-key-southern-states) 48/49 rounded vs mirror 48.8/49.4, precise question unresolved. All 13 documented rows at `data/processed/pilot04_primary_source_check_register.csv`.

**Uniform source assessment:** AAPOR's 2024 report and [public task-force repository](https://github.com/umisrcps/aapor_preelection_2024) show a viable historical data assembly workflow but **do not contain the complete cleaned downloadable poll-level historical file** in the examined repository. Key `president_polls_historical.csv` original endpoints are archived as links and current direct access is uncertain; the separate 2016 snapshot ends Oct 28. Note AAPOR's final window includes Election Day, unlike our provisional rule. Full source-by-source data coverage cannot yet be equated.

**CI:** Committed `.github/workflows/validate-research.yml` to run existing Python data checks and new overlap audit on code/data pushes or manual dispatch. **Hosted GitHub Actions run conclusion not retrieved/verified**, therefore no assertion of completed CI pass.

**Pilot disposition:** PARTIAL PASS for source-integrity and overlap diagnostics. **HOLD** on claims of independent poll counts, cross-cycle polling trends, geographically persistent errors, causal polling method effects or H1–H6 test results. Next: [Pilot 05](pilot-04.md#5-pilot-04-conclusion-and-gate-to-pilot-05) historical question-level archive reconstruction.
