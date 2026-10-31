# Pilot 01 — nine state-year polling comparisons

**Date:** 2026-10-31  
**Status:** Data transcribed and joined; independent vote totals verified for four of nine state-years; a complete raw poll-level download remains blocked. **This is an acquisition/matching pilot, not a representative accuracy study.**

## Objective and bounded design

Test whether archival *published final polling averages* and *individual poll entries* can be matched to presidential returns using three states (Georgia, Pennsylvania, Wisconsin) and three past elections (2016, 2020, 2024). These are illustrative locations, **not** an unbiased sample of states or polls. Do not infer national, regional, or long-term polling accuracy from these nine rows.

Archival browser-visible RCP tables provide complete published final average values for all nine state-years and *one selected individual poll listing* per state-year. This is enough to test schema, date parsing, party-to-candidate mapping and error arithmetic. It does **not** prove that individual poll-level downloads are available in standardized machine-readable form. Poll entries are secondary archive transcriptions rather than original pollsters' questionnaires.

## Files

- [Published state averages and archive-reported outcomes](../data/processed/pilot_rcp_state_averages.csv): 9 source-specific rows, plus official counts when independently checked.
- [Selected archived individual poll entries](../data/processed/pilot_selected_polls.csv): 9 *illustrative* entries, including dates and source labels. These polls were **not randomly or systematically sampled** and are never used to infer pollster quality.
- [Calculated margins and errors](../data/processed/pilot_margin_errors.csv): derived values, not additional original evidence.
- [Recalculation script](../analysis/pilot_accuracy.py): standard-library code to validate joins, pre-election field dates, vote shares and official-count denominators, then regenerate the output.

The nine average and poll rows were manually transcribed from the linked source HTML pages, not obtained from the original publishers as downloadable CSV files. All data are a snapshot of pages accessed on 2026-10-31. Historical webpages may have been retrospectively edited. Their calculated final averages cannot be assumed identical to independent poll-level computations.

## Source provenance

- 2016 state averages, reported election percentages and listed polls: [RCP 2016 battleground results](https://www.realclearpolitics.com/epolls/2016/president/2016StateFinalResults.html). For the 2016 Wisconsin poll entry, the [Wisconsin race archive](https://www1.realclearpolitics.com/epolls/2016/president/wi/wisconsin_trump_vs_clinton_vs_johnson_vs_stein-5976.html) supplies the same poll fields.
- 2020 archives: [Georgia](https://www.realclearpolitics.com/epolls/2020/president/Georgia.html), [Pennsylvania](https://www.realclearpolitics.com/epolls/2020/president/Pennsylvania.html), [Wisconsin](https://www.realclearpolitics.com/epolls/2020/president/Wisconsin.html).
- 2024 averages, reported election percentages and selected polls: [RCP 2024 battleground tables](https://www.realclearpolling.com/polls/battlegrounds/2024).
- Official 2024 vote counts and statewide presidential vote denominators, all three states: [FEC compiled 2024 presidential returns, pp. 3, 5 and 6](https://www.fec.gov/documents/5644/2024presgeresults.pdf); these pages were inspected visually.
- Official 2020 Pennsylvania counts: [Pennsylvania Department of State, 2020 certified presidential total](https://www.pa.gov/agencies/vote/elections/fact-checking-pa-related-election-claims). It reports Biden 3,458,229; Trump 3,377,674; Jorgensen 79,380; **6,915,283 presidential votes**.
- Official 2024 Pennsylvania major-candidate totals are also independently stated in the [Pennsylvania certification notice](https://www.pa.gov/agencies/dos/newsroom/governor-shapiro-certifies-2024-presidential-election-results).

**Validation boundary:** Exact certified vote counts have been independently inspected for **2020 PA and 2024 GA, PA, WI only**. The remaining five state-years use RCP's own rounded "Final Results" percentage row as an **archive-reported provisional comparator**, not a verified full-denominator official return. Before a real longitudinal comparison, fill these rows from official canvasses and recalculate.

## Metrics

Let `D` and `R` represent the Democratic and Republican candidate's percentages on the published poll/average question:

- Published polling margin (percentage points): `D_poll - R_poll`
- Official all-valid-presidential-votes margin: `100 * (D_votes - R_votes) / total_presidential_votes`
- Signed margin error: `poll_margin - reference_margin`; **positive** means the poll overstated the Democratic margin, **negative** means it overstated the Republican margin
- Absolute margin error: `abs(signed_margin_error)`

The benchmark is exact official all-valid-vote margin **when independently acquired**; otherwise the available RCP one-decimal result margin is used *solely to test arithmetic*. Mixing these different reference types for a trend or average is inappropriate. RCP final average field dates describe its included polling window, not the date an average was calculated or a single poll's continuous fieldwork.

## Initial audited comparisons

Rounded to three decimal places. Differences in the lower rows may diverge slightly from simple subtraction of rounded RCP result percentages because the precise official vote counts were used.

| Year | State | RCP avg D−R | Reference D−R | Reference source | Signed error (pp) |
| ---: | --- | ---: | ---: | --- | ---: |
| 2016 | Pennsylvania | +1.900 | −0.700 | RCP rounded | +2.600 |
| 2016 | Wisconsin | +6.500 | −0.700 | RCP rounded | +7.200 |
| 2016 | Georgia | −4.800 | −5.100 | RCP rounded | +0.300 |
| 2020 | Pennsylvania | +1.200 | +1.165 | State-certified counts | +0.035 |
| 2020 | Wisconsin | +6.700 | +0.700 | RCP rounded | +6.000 |
| 2020 | Georgia | −1.000 | +0.300 | RCP rounded | −1.300 |
| 2024 | Pennsylvania | −0.400 | −1.704 | FEC-certified counts | +1.304 |
| 2024 | Wisconsin | +0.400 | −0.859 | FEC-certified counts | +1.259 |
| 2024 | Georgia | −1.300 | −2.192 | FEC-certified counts | +0.892 |

**Interpretation restricted to this pilot:** The rows demonstrate that archive values can be joined and their margin errors calculated. They are not evidence, by themselves, for persistent bias, geographically correlated errors, or any comparative pollster assessment. The deliberately selected individual polls are present to test record-level matching; they are not representative.

## Specific data-quality finding: 2024 Pennsylvania

RCP's archived final-result line lists Harris at **48.7%** and Trump at **50.4%**. Dividing the FEC's official Harris votes **3,423,042** and Trump votes **3,543,308** by its full presidential vote total **7,058,732** yields approximately **48.494%** and **50.198%**, respectively. Although both pairs produce almost the same *candidate margin*, they **do not use identical reported candidate shares**.

This discrepancy is **verified** from the two sources; its cause **has not been established**. Possible differences in vote denominator, reporting coverage or source vintage require investigation. The discrepancy is a reason to retain original percentages *and* verified vote counts with explicit denominators, not a license to silently rescale them.

## Individual-poll feasibility findings

RCP supplies candidate percentages and start/end dates for each selected poll. The six selected 2016/2020 entries also show an LV sample count. On the 2024 combined battleground summary page, poll-level sample population/count were not supplied for the three selected Hill/Emerson entries; leave these fields **blank** rather than infer them.

The pilot therefore demonstrates a limited feasible extraction path, but not a uniform *sample-size/methodology* dataset suitable for H4 method-effect testing.

A key source trap remains: FiveThirtyEight's "State of the Polls 2024" dataset is limited to surveys ending **15–180 days before Election Day**, so it cannot substitute for complete final-fourteen-day polling records ([README](https://github.com/fivethirtyeight/data/blob/master/state-of-the-polls-2024/README.md)).

## Calculation checks and caveats

- Nine unique year/state averages were matched to nine selected year/state poll entries; matching records use consistent year, state, general election and major-party labels.
- All selected poll fieldwork ends before Election Day.
- Initial margin calculations were independently recomputed from the saved transcriptions and compared with the published RCP direction/margins. The accompanying Python standard-library script supplies repeatable validation and CSV generation for a local checkout.
- The CSV used for this pilot was manually extracted because some source CSV/Excel download endpoints were inaccessible from the current execution environment. An archive page's existence is not evidence of a completed direct-file acquisition.
- Reproduction code has been committed, but it has **not been executed in a local checkout in this research session**; the nine-row calculations and join checks were run separately in the connected analysis environment.
- An RCP "average" is a published aggregation, not necessarily a mean of every poll available; do not synthesize one from the nine selected entries.
- No inferential statistics, cross-year significance tests or formal H1–H6 hypothesis tests were run.

## Exit criteria and next recommended work

**Pilot status: PARTIAL PASS (archive matching and arithmetic); open for official result coverage and original poll-file retrieval.**

1. Replace the five provisional RCP rounded result references with **independently sourced official certified candidate counts and all-presidential-vote totals** for 2016 GA/PA/WI and 2020 GA/WI; validate that the FEC and state results agree.
2. Attempt authenticated/licensed access or a permitted download tool for complete **2016, 2020 and 2024 individual-poll records** with poll/question IDs and documented candidate, date, sample and methodology fields.
3. Re-run `python analysis/pilot_accuracy.py --write` and confirm output matches the committed derived CSV after any changes.
4. Freeze candidate handling and the **final-14-day inclusion rule**, plus poll deduplication and tracking rules, before scaling.
5. Only then design representative sampling and data-quality sensitivity checks. Do **not** label the pilot's nine chosen records as estimates for all states.
