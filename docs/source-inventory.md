# Historical polling and election-result source inventory

**Review date:** 2026-10-31. **Status labels:** **Documented** = primary provider page/README examined; **Partially verified** = index/metadata exists but exact file and contents not directly inspected; **Access limited** = requires credentials, payment, or endpoint inaccessible in this review. A link being present is *not* proof that a downloadable data file has been acquired or parsed. No local datasets have been collected yet.

| ID | Source and access link | Confirmed scope and usefulness | Access / limitation | Status |
| --- | --- | --- | --- | --- |
| R01 | [Federal Election Commission, election results](https://www.fec.gov/introduction-campaign-finance/election-results-and-voting-information/) | Federal Elections compilations include certified returns for presidential cycles 2000, 2004, 2008, 2012, 2016, 2020; a separate 2024 presidential results PDF/Excel is linked. State officials certify originals. | Detailed harmonization, vote denominator, write-ins and version checking still needed. | **Documented** |
| R02 | [MIT Election Data and Science Lab data portal](https://electionlab.mit.edu/data) and [presidential Dataverse DOI](https://doi.org/10.7910/DVN/42MVDX) | MIT portal lists presidential state returns 1976–2020 and county returns 2000–2024. Third-party catalogue lists a newer *U.S. President 1976–2024* entry under the DOI. | Live Harvard Dataverse page challenged automated access; verify current official release, schema, 2024 inclusion, and checksum before using. | **Partially verified** |
| P01 | [FiveThirtyEight historical presidential polling README](https://github.com/fivethirtyeight/data/blob/master/polls/README.md) | Official archive indexes presidential general-election individual-poll CSVs and separate historical files, plus 2020 polling averages. | Date coverage, file row count, field dates and download success not yet checked; direct CSV could not be loaded through this browsing interface. | **Documented index, file unverified** |
| P02 | [FiveThirtyEight pollster-ratings README](https://github.com/fivethirtyeight/data/blob/master/pollster-ratings/README.md) | Explains poll-level raw-polls.csv, election cycle, contest and location; potential cross-cycle individual poll observations. | Dataset optimized for pollster ratings, not necessarily comprehensive election-census coverage; candidate normalization, inclusion rules and methodology changes require audit. | **Documented index, extract pending** |
| P03 | [FiveThirtyEight State of the Polls 2024](https://github.com/fivethirtyeight/data/tree/master/state-of-the-polls-2024) | Documents 2012, 2016, 2020, 2024 individual poll files with common metadata. | Critically: documentation selects polls whose end dates fall **15–180 days before Election Day**; not a suitable final-14-day series without additional data. 2024 file also had publication cutoff Oct. 28. | **Documented** |
| P04 | [RealClearPolling historical archive](https://www.realclearpolling.com/historical-polling-archive) | Public index includes final averages/results for 2004, 2008, 2012 and newer elections, plus historical state/battleground polling links. | Not yet shown to provide a uniform downloadable poll-level dataset, reproducible average weights, or complete 2000 coverage; manually archived values are not interchangeable with raw polls. | **Documented index; extraction pending** |
| P05 | [Roper Center iPoll](https://ropercenter.cornell.edu/learnteach/what-roper-ipoll) | Long-running archive with survey questions, toplines, field dates, methods and some full datasets; possible early-cycle gap filler. | Full records and advanced analysis may require institutional membership; not assumed freely reusable. | **Access limited** |
| M01 | [AAPOR polling accuracy summaries](https://aapor.org/polling-accuracy/) and [reports](https://aapor.org/publications-resources/reports/) | Retrospective assessment of 2016, 2020 and 2024 accuracy and methodology. Useful for comparison/validation, not to replace independent reconstruction. | Task-force inclusion rules and metrics must be checked before comparing numerical findings. | **Documented** |
| M02 | [AAPOR 2024 task-force announcement](https://aapor.org/announcements/2024-pre-election-polling-report/) and [task-force code repository](https://github.com/umisrcps/aapor_preelection_2024) | Task-force report and public R scripts are available. Its report describes a final-two-week analysis and a replication archive. | Code repository has R scripts but the promised cleaned poll-level CSV/replication files have **not been located/verified** in this review; do not mark complete data as downloadable. Some contributed respondent-level microdata remain restricted. | **Partially verified** |

## Source priority and limitations

1. **Outcome ground truth:** official state-certified results, using FEC compilation for common format; MIT/MEDSL as independently cross-checkable standardized returns.
2. **Individual polls:** original polls, archived FiveThirtyEight rows and their source links; use available Roper records to fill *specific* gaps, not assumed full coverage.
3. **Historical averages:** archive the actual published final average and its cutoff if available; do not describe a newly calculated mean as an original archived polling average.
4. **Methods/context:** AAPOR reviews and original pollster methodology disclosures, with clear provenance.
5. **Licensing:** record publisher and license for *each file* before mirroring or committing; an openly browsable source is not necessarily public-domain or redistributable.

## Not yet verified

- Which election years and geographic units have comparable final-14-day individual polling records (particularly 2000–2008).
- Whether pollster names, sample types, weighting attributes and field dates survive historical exports.
- Direct download/readability of the latest FiveThirtyEight historical CSV, AAPOR replication materials and current Harvard Dataverse presidential file.
- Availability of complete historical *state* averages, original cutoffs and archived methodologies.
- Whether third-party archives' licensing and historical revisions permit repository storage.

## Audit procedure for each candidate file

Record URL, publisher, download timestamp (UTC), file version/hash, data license, election years, contests, geographic identifiers, field-date definition, candidate mapping, sample population, denominator definition, missingness, duplicate rules, number of rows before/after filters and any known revisions. Do not label a dataset usable until its content has been opened and inspected.

## 2026-10-31 Pilot 01 follow-up: archives actually inspected

- **RCP 2016**: [2016 presidential battleground final tables](https://www.realclearpolitics.com/epolls/2016/president/2016StateFinalResults.html) expose 2016 GA/PA/WI candidate percentages, final averages, field-date windows and selected poll entries. **Verified HTML-level records; dataset-level CSV download not established.**
- **RCP 2020**: [PA](https://www.realclearpolitics.com/epolls/2020/president/Pennsylvania.html), [WI](https://www.realclearpolitics.com/epolls/2020/president/Wisconsin.html) and [GA](https://www.realclearpolitics.com/epolls/2020/president/Georgia.html) provide analogous summary rows and some sampled poll field dates/populations. **Verified HTML-level records.**
- **RCP 2024**: [2024 battleground final table](https://www.realclearpolling.com/polls/battlegrounds/2024) provides final averages and poll entries in all three pilot states. The combined table does **not** expose sample size/population for selected polls. **Verified HTML-level records.**
- **FEC 2024**: [2024 presidential certified counts PDF](https://www.fec.gov/documents/5644/2024presgeresults.pdf) pp. 3, 5, 6, visually examined for candidate counts and full-state presidential vote totals for GA, PA and WI. **Verified numerical observations for all three pilot states.**
- **Pennsylvania 2020 official record**: [Department of State fact-check page](https://www.pa.gov/agencies/vote/elections/fact-checking-pa-related-election-claims) explicitly gives certified candidate totals and 6,915,283 total presidential votes. **Verified numerical observations.**

See [Pilot 01](pilot-01.md) for provenance and gaps. RCP's retrospective `Final Results` row is *not* an acceptable permanent substitute for official counts; check denominator differences before producing aggregate historical statistics.
