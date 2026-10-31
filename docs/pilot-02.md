> **Late discovery update, 2026-10-31:** This report was written before successful retrieval of the 2020 historical FiveThirtyEight mirror. Section 6's earlier access-block statements are historical. **175 final-fourteen-day Biden/Trump question pairs have now been extracted for Georgia, Pennsylvania and Wisconsin.** See the [Pilot 02 polling-data addendum](pilot-02-poll-data-addendum.md) and [2020 dataset](../data/processed/pilot_2020_final14_paired_questions.csv). The 2016 and 2024 equivalent data remain unacquired. No broad polling-error trend analysis has been conducted.

# Pilot 02 — official-result completion, poll-file acquisition, reproducibility

**Review date:** 2026-10-31  
**Status:** **PASS** on nine official-result records, calculation reproduction, and the 2020 three-state final-window question-data acquisition; **PARTIAL** on original-poll validation and cross-cycle 2016/2024 acquisition. No inferential statistical analysis or H1–H6 hypothesis tests conducted.

## 1. Official 2016 source reconciliation

Verified the **Office of the Clerk of the U.S. House of Representatives**' [Statistics of the Presidential and Congressional Election of November 8, 2016](https://clerk.house.gov/member_info/electionInfo/2016/statistics2016.pdf) by inspecting original PDF tables, not relying on search snippets:

| State | PDF printed page (PDF zero-based screenshot) | Clinton (D) | Trump (R) | Additional votes in official publication | Total presidential votes |
| --- | --- | ---: | ---: | --- | ---: |
| Georgia | 16 (17) | 1,877,963 | 2,089,104 | Libertarian 125,306; write-in 22,359 | **4,114,732** |
| Pennsylvania | 64 (65) | 2,926,441 | 2,970,733 | Constitution 21,572; Green 49,941; Libertarian 146,715 | **6,115,402** |

These totals use the House Clerk's published statewide recapitulation, a federal official compilation. The original Georgia state election web summary printed **4,092,373**, summing only three named candidates; the House Clerk total adds **22,359 write-ins**. **4,165,405** is ballots cast, not presidential votes. Dave Leip's Atlas shows **4,146,825** based on a more expansive compilation, including additional county write-in counts; this is **not interchangeable** with the House Clerk total. It remains an alternate-source question rather than an allegation of irregularity. See [Georgia official PDF](https://sos.ga.gov/sites/default/files/2022-01/november_2016_generalelection_totals.pdf), [House Clerk](https://clerk.house.gov/member_info/electionInfo/2016/statistics2016.pdf), and [Atlas notes](https://uselectionatlas.org/RESULTS/state.php?fips=13&off=0&year=2016).

With these updates, the **nine** Pilot 01 state-year records now all have an independently checked official published presidential vote total. The 2016 Georgia denominator is **the House Clerk published total**, not a claim to have independently counted all possible county write-ins.

## 2. Corrected nine-row archived-average comparisons

| Year | State | RCP final average D−R (pp) | Official D−R (pp) | Signed error (pp) |
| ---: | --- | ---: | ---: | ---: |
| 2016 | PA | +1.900 | −0.724 | +2.624 |
| 2016 | WI | +6.500 | −0.764 | +7.264 |
| 2016 | GA | −4.800 | −5.131 | +0.331 |
| 2020 | PA | +1.200 | +1.165 | +0.035 |
| 2020 | WI | +6.700 | +0.627 | +6.073 |
| 2020 | GA | −1.000 | +0.236 | −1.236 |
| 2024 | PA | −0.400 | −1.704 | +1.304 |
| 2024 | WI | +0.400 | −0.859 | +1.259 |
| 2024 | GA | −1.300 | −2.192 | +0.892 |

All figures are percentage points. **Positive = archive polling margin overstated Democratic D−R margin**, negative = overstated Republican D−R margin. This is only a nine-state-year, three-state convenience pilot, **not** an estimate of national/state historical error trends or a test of recurring patterns. Original archive poll averages have **varying polling windows** (including field dates older than 14 days); these figures must not be relabeled as final-two-week individual polling estimates.

Updated files: [input state outcomes](../data/processed/pilot_rcp_state_averages.csv), [derived margins](../data/processed/pilot_margin_errors.csv), and [calculation script](../analysis/pilot_accuracy.py). The full pilot remains source-preserving rather than converting RCP's final result percentage to an official one without keeping both.

## 3. Calculation script executed and verified

Created a local working directory containing the exact GitHub script and input CSV contents. The Git blob SHA of each mirrored file **matched** the authoritative GitHub blob:

| File | Git blob SHA |
| --- | --- |
| `analysis/pilot_accuracy.py` | `34339024e984217e2a13a79856f35a101de13248` |
| `data/processed/pilot_rcp_state_averages.csv` | `11eac10e49b40f97747084a87b7b389c03a2035e` |
| `data/processed/pilot_selected_polls.csv` | `96e14332887d5db3c0e623a1f84726014fbfa934` |
| Generated `data/processed/pilot_margin_errors.csv` | `3bfc36b0fcdeb0b89156a60b0b05582d88e82c23` |

Executed `python analysis/pilot_accuracy.py --write`. **The generated output Git blob exactly matches the GitHub committed derived CSV**. Executed `python -m unittest discover -s analysis -p 'test_*.py' -v`; **6/6 tests passed**, including the two corrected 2016 values and malformed-input checks. Test source was committed and its Git blob SHA verified.

## 4. Machine-readable FiveThirtyEight archives actually acquired

Directly retrieved these **complete original CSV files** through the connected GitHub source and copied them unchanged into [data/raw/fivethirtyeight/state-of-the-polls-2024](../data/raw/fivethirtyeight/state-of-the-polls-2024/README.md):

- `2016_polls.csv` — 2,677 records
- `2020_polls.csv` — 2,663 records
- `2024_polls.csv` — 1,700 records

Upstream and destination Git blob hashes are identical (see raw-data README). FiveThirtyEight's upstream repository says datasets are CC BY 4.0 unless otherwise noted; provenance and attribution are retained.

**These files do NOT provide final-window candidate polling results.** They contain polling metadata only and surveys whose fieldwork ended **15–180 days** before Election Day, as explained in the [original source README](https://github.com/fivethirtyeight/data/blob/master/state-of-the-polls-2024/README.md). No candidate preference percentages, question-level matchups, or final 14-day records are present. Do not insert them into the RCP polling-vs-results comparisons.

## 5. Metadata coverage audit, pilot states only

Filtered original files for `state` in `GA`, `PA`, `WI` and `has_prez? = TRUE`. The number of archive records with a presidential question is **not** the number of unique samples, independent polls, final-week polls or polling candidates.

| Cycle | GA | PA | WI |
| ---: | ---: | ---: | ---: |
| 2016 | 48 | 68 | 46 |
| 2020 | 59 | 99 | 216 |
| 2024 | 84 | 124 | 96 |

The 2020 Wisconsin subset contains **141 tracking records out of 216**, showing why raw row counts must not be treated as independent poll observations. These figures describe the exact archived metadata snapshot, not changes in total polling conducted across election cycles.

Source hashes, dates, tracking counts and all nine state-year results are preserved in [metadata coverage audit](../data/processed/pilot_538_metadata_coverage.csv). The [audit script](../analysis/audit_538_metadata.py) validates the source Git blobs and is provided for reproduction; it was **syntax-compiled locally but not run against the complete raw CSVs in the local working directory** (those source files were acquired via the GitHub connector).

## 6. Poll-level vote-share acquisition status

Attempted: FiveThirtyEight hosted `president_polls.csv` and `president_polls_historical.csv`, its archived `pres_pollaverages_1968-2016.csv`, historical 2020 forecast sources, and GitHub pollster-rating `raw_polls.csv` plus 2016/2020 previous versions.

- Several host URLs could not be retrieved in this session. The historical 1968–2016 average CSV exceeds browser response-size limits; some 538 raw-poll files exceed the GitHub connector's file-content limit and return no text.
- The current upstream [FiveThirtyEight pollster-ratings codebook](https://github.com/fivethirtyeight/data/blob/master/pollster-ratings/README.md) identifies **poll ID, question ID, state, methodology, survey median field date, candidate vote-share columns** in a pollster-rating study dataset. This is a **promising candidate**, but not a verified complete final-two-week polling universe. Some sample sizes are imputed, and publication/field end date handling is different.
- A third-party archive/mirror, [simonw/fivethirtyeight-polls](https://github.com/simonw/fivethirtyeight-polls), exists but the full polling CSV could not be extracted into the local research dataset here. A mirrored dataset requires time-vintage, license and row-level integrity checking before use.
- The [2016 538 general-model dataset](https://projects.fivethirtyeight.com/general-model/president_general_polls_2016.csv) is identified by an [independent 2016 R documentation mirror](https://search.r-project.org/CRAN/refmans/dslabs/html/polls_us_election_2016.html), but its original download has not been independently retrieved or inspected in this pilot.

**Result:** Full source-file acquisition succeeded for **metadata only**; acquisition of a consistent, complete **final-window candidate-share poll dataset** remains **OPEN**.

## 7. Decisions and next step

The outcome vote denominator, major-party signed-margin definition, official source priority, raw-source preservation, and source-version/hash logging are documented in [preliminary methodology v0.1](methodology-v0.1.md). The *proposed* final 1–14-day field-end window and de-duplication policy remain provisional pending a poll-level file audit.

**Updated next activity: Pilot 03, complete cross-cycle and original-report validation.** The [2020 addendum](pilot-02-poll-data-addendum.md) now documents 175 selected final-14-day Biden/Trump question pairs with poll/question IDs and other key fields. First reproduce the extract in Python using the exact historical mirror; check more questions against original pollster reports and establish a consistent sample-selection policy. Then acquire equivalent final-window vote-share datasets for 2016 and 2024, preserving candidate matchups. Do not conduct broad statistical modeling until these steps pass.
