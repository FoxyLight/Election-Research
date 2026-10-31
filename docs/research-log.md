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

**Verified official vote counts:** 2024 all three states from the FEC's visually reviewed presidential table (official candidate counts and total votes) and 2020 Pennsylvania from its Department of State's official certification discussion. **Not yet independently verified:** 2016 GA/PA/WI and 2020 GA/WI complete official vote denominator/major-candidate counts. These five rows retain RCP's one-decimal final-results benchmark and are explicitly marked provisional.

**Calculation check:** all 9 state-year keys joined with a selected archived poll, selected polls' field end dates precede Election Day, and signed Democratic-minus-Republican margin errors were independently recomputed from the extracted values. The Python script was committed to allow another researcher to regenerate the derived CSV; the Python script itself has not been executed here.

**Data quality issue:** RCP's 2024 Pennsylvania reported winner and runner-up result percentages differ from percentages derived from the FEC's full statewide presidential vote denominator. Preserve the raw percentages and source-specific denominator, and do not assert a cause without supporting evidence.

**Deliverables:** `docs/pilot-01.md`, two source-data pilot CSVs, computed-errors CSV, `analysis/pilot_accuracy.py`. **Research gate:** official-count backfill, complete individual-poll data acquisition, reproducible script execution and inclusion criteria before full statistical analysis.
