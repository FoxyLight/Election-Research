# Pilot 03 — final-window polling sources and conservative question selection

**Research date:** 2026-10-31  
**Status:** **PARTIAL PASS.** Secondary-archive final-14-day candidate shares acquired for 2016 and 2024; a deterministic, non-outcome-guided 2020 survey-question triage is implemented. **NOT YET a consistent full-universe three-cycle polling analysis.**

## Objective

Acquire 2016/2024 final-two-week candidate percentage measurements for the three pilot states (GA, PA, WI) to complement [2020 paired-question data](../data/processed/pilot_2020_final14_paired_questions.csv), check selected records against original pollster publications, and investigate duplicate question/survey handling without choosing records based on which estimate better matched the election outcome.

## 1. Acquired records

| Election | Source | GA | PA | WI | Total | Granularity |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 2016 | [RCP 2016 final battleground tables](https://www.realclearpolitics.com/epolls/2016/president/2016StateFinalResults.html) | 5 | 6 | 4 | **15** | One **published archive table row** per candidate-share matchup; includes dates, listed population and sample size, **but no unique poll/question identifiers** |
| 2020 | [538 original poll answers via Simon Willison 2020 mirror](https://github.com/simonw/fivethirtyeight-polls/blob/main/president_polls.csv), exact blob `cbe565b7647059de8b58414e420d2b8587250cc6` | 46 | 76 | 53 | **175** | Question-level matched Biden/Trump rows; **121 distinct poll IDs**. Original sample and question IDs available |
| 2024 | [Electoral-Vote.com 2024 state polling archive](https://www.electoral-vote.com/evp2024/Pres/pres_polls.html) | 9 | 18 | 12 | **39** | One published curated table entry per visible poll; dates and Harris/Trump shares, **but no poll ID, sample population, sample size, question wording, or method** |

The 2016 and 2024 records are in [the common archive extract](../data/processed/pilot_03_2016_2024_final14_archive_polls.csv), **54 rows**. Individual rows have stable project-only record IDs, source URLs, source-specific selection notes, original fieldwork start and end, candidate shares, missing sample values retained as blank, and check notes.

**Window:** poll fieldwork must end **1–14 whole calendar days before Election Day**, inclusive (2016-11-08 and 2024-11-05). Polls fielded on Election Day, post-election, and later-appearing "Election 2024" results rows were **not** included. Surveys that **began before** the fourteen-day window but **ended within it** remain included and are flagged for later sensitivity analysis; e.g., extended YouGov fieldwork. This is an end-date rule, not a claim that every respondent answered during those 14 days.

**2016 source limit:** The displayed RCP table is a selection of final battleground polls, not all statewide polls conducted. It can be used to test matching and validation, not full pollster-level coverage. The separately recovered [2016 FiveThirtyEight CSV preserved in an October 28 snapshot](https://github.com/ellisp/ellisp.github.io/blob/master/data/polls.csv), original Git blob `b8a5d58dae681a1710d164cee1e71430d9e75225`, contains model-duplicated poll rows and **does not include surveys released after October 28**. Another [2016 snapshot](https://github.com/cmerenstein/2016_house_elections/blob/master/president_general_polls_2016.csv) is earlier still. Neither snapshot was used to claim complete final-14-day coverage. A later final-cycle [2016 FTE dataset](https://projects.fivethirtyeight.com/general-model/president_general_polls_2016.csv) is documented in contemporaneous research, but its full Nov 8 vintage was not acquired here.

**2024 source limit:** Electoral-Vote.com explicitly selects its own nonpartisan survey universe. It is **not** identical to FiveThirtyEight's or RCP's inclusion, coverage, or candidate-question policy. Its labels and percentages should not be interpreted as identical questionnaires across providers. Its 2024 page can include pre-nomination Harris hypothetical pairings, but none of the chosen final-window rows are pre-nomination. AAPOR's [2024 task-force Appendix A](https://aapor.org/wp-content/uploads/2025/10/AAPOR-Task-Force-on-2024-Pre-Election-Polling_Report.pdf) documents a broader professionally collected poll archive; its complete question-level source has **not** been extracted in this research session.

## 2. Original reporting checks

| Year/state and source record | Archived shares | Original reporting | Finding |
| --- | --- | --- | --- |
| 2016 WI — Marquette, Oct. 26–31, LV | Clinton **46**, Trump **40** | [Marquette Law School original Nov. 2 release](https://law.marquette.edu/poll/2016/11/02/mlsp41release/) and [LV toplines](https://law.marquette.edu/poll/wp-content/uploads/2016/11/MLSP41ToplinesLV.pdf) | **Candidate values and dates match.** **Important unresolved sample-count discrepancy:** RCP reports **1,225 LV**, primary report says **1,255 unweighted LV** and **1,190 weighted LV**. No correction was silently applied |
| 2020 WI — Marquette Oct. 21–25, LV and RV, same poll ID 72151 | Biden/Trump **48/43 LV** and **47/43 RV** | [Original LV](https://law.marquette.edu/poll/wp-content/uploads/2020/10/MLSP65ToplinesLV.html) and [original RV](https://law.marquette.edu/poll/wp-content/uploads/2020/10/MLSP65ToplinesRV.html) questionnaire tables | **Both pairs and respective sample figures matched** in Pilot 02. They are **not independent** despite two question IDs |
| 2024 GA — East Carolina U., Oct. 28–31 | Harris **49**, Trump **50** | [East Carolina University Center for Survey Research original release](https://surveyresearch-ecu.reportablenews.com/pr/georgia-remains-a-tossup-as-election-day-nears) | **Shares and field dates match**; original reports likely/early voters and ±3% margin |
| 2024 PA — Marist, Oct. 27–30 | Harris **50**, Trump **48** | [Marist Pennsylvania original release](https://maristpoll.marist.edu/polls/marist-pennsylvania-poll-u-s-presidential-contest-in-pennsylvania-november-2024/) | **Shares and dates match**; 1,400 likely voters (archive extract sample left blank because secondary table does not provide it) |
| 2024 WI — Marist, Oct. 27–30 | Harris **50**, Trump **48** | [Marist Wisconsin original release](https://maristpoll.marist.edu/polls/marist-wisconsin-poll-u-s-presidential-contest-in-wisconsin-november-2024/) | **Shares and dates match**; 1,330 likely voters (archive extract sample left blank; preserve original archived missingness) |

These checks are **selected spot checks**, not validation of every row. Do not infer that all 54 secondary-source archive rows are correct or source-identical.

## 3. Conflicting descriptions requiring question-level investigation

- **2016 WI Marquette sample sizes:** RCP's displayed **1,225 LV** differs from primary Marquette's **1,255 unweighted likely-voter respondents** and **1,190 weighted likely-voter sample**. The primary numbers describe different sample definitions. The precise source of RCP's 1,225 remains unresolved. Keep raw source-specific values separate and do not silently overwrite either.
- **2024 WI Emerson (Oct. 30–Nov. 2):** Electoral-Vote.com gives **Harris 50 / Trump 50**, RCP's final table gives **49 / 49**, while The Hill's archive lists a ballot-test result near **49.4 / 49.4** among **800 likely voters**, as well as a related question with slightly different numbers. These may refer to different rounding, weighting, or question variants; **no cause verified**. Both secondary-source representations are preserved in research notes. This poll is **not** suitable for primary-source-verified cross-archive matching until the original questionnaire and precise question variant are identified.
- **2024 GA Siena:** A two-candidate question and a multiple-candidate question can report different Harris/Trump shares; [RCP's multilateral table](https://www.realclearpolling.com/polls/president/general/2024/georgia/trump-vs-harris-vs-kennedy-vs-west-vs-stein) differs from its two-way table. Do not treat this as a contradiction without matching actual questions.

These issues illustrate measurement-definition ambiguity, **not** evidence of wrongdoing, interference or intentional manipulation.

## 4. 2020 poll-question duplicates

The 175 matched questions represent **121 different state-specific poll IDs**. Applying only the following *outcome-blind* tier ranking of respondent population: **likely voters (LV) → registered voters (RV) → adults (A) → unknown/other**:

- **115 poll groups** have precisely one eligible top-tier question: [provisional single-question-per-poll file](../data/processed/pilot_03_2020_unique_poll_provisional.csv).
- **6 groups** have two or more questions *at the same highest available population priority*, sometimes reporting different candidate margins. These are explicitly recorded in [unresolved 2020 same-sample questions](../data/processed/pilot_03_2020_ambiguous_polls.csv), and **excluded** from the provisional single-question file.
- Those 6 unresolved groups are **GA poll 72146**, **PA polls 72599, 72507, 71976**, and **WI polls 72505, 71975**. In the full dataset they remain accessible, not discarded.
- Even the 115 selected questions are **not independent by default**: tracker waves, cross-state batches, overlapping fieldwork, syndicated releases, and post-hoc publication edits may duplicate respondents across poll IDs.

The tier ranking does **not** solve multi-candidate versus head-to-head ballot wording. We cannot impose that policy retrospectively without original question text, so the 115-row output is **provisional for data-structure testing**, not approved for pooled error inference. A missing source poll ID cannot be reconstructed merely from similar pollster names and dates.

## 5. Operational research decisions

**Working definitions, not a final authorization to model:**

1. Keep the original all-candidate denominator and published vote shares. Poll margin is simply original D minus original R, with no normalization, and actual margin uses the official outcome denominator selected in Pilots 01–02.
2. Use original **fieldwork end date**, not publication date or survey midpoint, wherever recorded. Flag surveys with early starts, tracking sequences and election-day overlap.
3. Count **poll IDs** separately from question IDs and raw candidate-answer rows. Maintain a separate list of unresolved duplicate groups.
4. **Never select an alternative questionnaire based on which candidate margin is closer to the final result.** This would contaminate any future historical analysis.
5. Do not pool the 15 RCP, 175 mirrored FTE questions, and 39 Electoral-Vote observations in a single statistical trend as if they were drawn from the same population. Differences in archive coverage, self-selection, pollster selection, sample reporting and candidate wording remain confounders.
6. Preserve alternative source figures, unknown sample variables and original primary-report discrepancies. Do not label secondary archive numbers **primary-source verified** until checked.

## 6. Reproducibility and execution

- [54-row 2016/2024 manually transcribed candidate-share extract](../data/processed/pilot_03_2016_2024_final14_archive_polls.csv), with source/date information and original limitations.
- [2020 175 paired questions](../data/processed/pilot_2020_final14_paired_questions.csv) remains unchanged.
- [115 provisional one-per-poll selection](../data/processed/pilot_03_2020_unique_poll_provisional.csv) and [six ambiguity records](../data/processed/pilot_03_2020_ambiguous_polls.csv), calculated by deterministic population ranking, with no outcome used in the ranking.
- [Offline validation script](../analysis/pilot_03_validate.py) checks date windows, candidate arithmetic, counts, identity and tier selection. The data were independently sanity-checked while producing these GitHub artifacts; **the Python file was not executed locally against a complete repository checkout in this session**.
- Published archival webpages are referenced, not copied wholesale. A fully automated source crawler with HTML snapshot hashes **does not exist yet**. Manual transcription makes additional audit sampling important.
- The 2016 October-28 partial 538 source's original Git blob is documented above, but this non-final copy was **not** merged into the final-week table.

## 7. Pilot 03 status and next research step

**Completed:** 2016/2024 candidate-share acquisition for a *bounded convenience selection*, initial primary-source spot checks across three years, 2020 ambiguous-survey triage, source discrepancy logging and documented provisional rules.

**Not completed:** complete 2016/2024 same-provider poll universe, question IDs and population/method fields for all cycles; resolving 2016 Marquette sample count and 2024 Emerson questionnaire; full stratified original-report check; local execution of the Pilot 03 Python audit.

**Recommend Pilot 04:** (a) independently execute validation scripts and check a stratified original-report sample, (b) obtain **same-source three-cycle question-level data** or independently construct a transparent all-source sampling frame with documented omissions, and (c) explicitly distinguish tracking waves / repeated voter samples. **Only after this** freeze the observation selection rules and begin inferential tests of geographic or recurring errors. AAPOR's public 2024/historical replication materials should be a priority for finding a comparable cross-cycle data frame.
