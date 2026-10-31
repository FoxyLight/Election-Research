# Preliminary comparison methodology v0.1

**Status (2026-10-31):** Partial decision freeze after Pilot 02. These are operational definitions for data integrity, **not authorization for full statistical analysis**.

## Decisions that can now be used

1. **Unit:** one state × one presidential general election year for the published-average pilot. Individual poll questions are separate observations and are **not independent** merely because they are separate rows.
2. **Outcome:** full published **presidential-elector votes** (not all ballots cast). Divide the difference in Democratic and Republican presidential votes by all presidential votes included in the designated published outcome total, including separately recognized third-party and write-in votes.
3. **Preferred outcome sources:** state-certified comprehensive canvass or official federal compilation showing the numerator and total. For Georgia and Pennsylvania 2016, use the House Clerk's [2016 Statistics, state recapitulation tables](https://clerk.house.gov/member_info/electionInfo/2016/statistics2016.pdf). Record an explicit source URL and count vintage for every state-year.
4. **Signed margin:** `D_poll - R_poll` compared with `100*(D_votes-R_votes)/presidential_votes_total`; signed error is `polled margin - actual margin`. Positive indicates the polling estimate overstated the **Democratic margin**; negative indicates it overstated the **Republican margin**. Report percentage points.
5. **Poll share handling:** preserve the pollster's original candidate shares, including undecided/third-party responses and their original denominator. A poll margin is the direct difference of published D and R percentages; it need not be on the same vote-share denominator as eventual election results. Do **not** renormalize without a separately labeled sensitivity test.
6. **Missing values:** do not replace missing official denominators with unmarked poll-archive election percentages or imply that a source link proves a downloaded dataset.
7. **Archived averages:** keep published RCP averages separate from individual polls. They have different field windows and unknown/variable weighting. Do not call an average a "last-fourteen-day poll" unless its underlying sampling window is verified.

## Pending decisions requiring a genuine final-week poll-level dataset

- **Primary proposed final-week window:** surveys with field-end date **1–14 days before Election Day** (inclusive). Polls ending on Election Day are excluded from the initial primary protocol. Separately test 1–7 and 1–30 day alternatives. This is *proposed*, not yet frozen.
- **Question IDs and matching:** prefer source poll ID + question ID + candidate lineup + state + fieldwork end; avoid double-counting multiple questions, revised releases and syndicated polls. Define a deterministic priority for duplicate versions.
- **Survey populations:** keep LV, RV and adults distinct, and retain question mode, sample size and weighting metadata only if actually sourced. Do not impute sample sizes for an analysis of method effects.
- **Average vs poll-level errors:** compare within matched states, elections and time windows, with awareness averages reuse constituent polls.
- **2024 candidate replacements:** distinguish Biden/Trump from Harris/Trump questions; do not combine different candidate matchups into an undifferentiated 2024 presidential estimate.
- **Small independent cycle count:** seven elections in 2000–2024. Correlated state or poll observations do not provide seven times fifty independent presidential cycles.
- **Inference:** no geographic, persistent-bias, or methodology-causation claims until source coverage, selection bias, correlation structure and validation design are documented.

## Data validation gate to Phase 3

Require a substantial, machine-readable **final-window candidate-share** poll extract covering at least selected states in each 2016/2020/2024 cycle. Audit field dates, IDs, voting-population labels, candidate mapping, missingness, duplicate rates, source license, and sample provenance. Demonstrate a reproducible parser/transform and compare at least several rows to original poll reporting. Once satisfied, freeze inclusion and de-duplication rules **before** full data collection and model testing.

## What has been tested

- The original `analysis/pilot_accuracy.py` was reproduced in a local working directory, with Git blob hashes matching the committed script and its three data inputs. Running `--write` regenerated an output Git blob identical to the committed calculated CSV.
- Six local regression tests passed (including invalid dates, duplicate state-year selected poll keys, and incomplete vote totals); tests committed to `analysis/test_pilot_accuracy.py`.
- Three FiveThirtyEight 2016/2020/2024 **metadata-only** CSV archives copied to `data/raw/`; their upstream and destination Git blob hashes match. The 15–180-day scope excludes the proposed primary final-fourteen-day window.
- No broad statistical hypothesis test has been conducted.

## 2026-10-31 Pilot 02 end-of-window acquisition update

A [2020 paired-question extract](../data/processed/pilot_2020_final14_paired_questions.csv) from the historical [FiveThirtyEight mirror](https://github.com/simonw/fivethirtyeight-polls) contains **175** unique matched Democratic and Republican question IDs in Pennsylvania, Wisconsin and Georgia, whose survey **end date** was 1–14 days before 2020 election day (inclusive). It is not a source for 2016 or 2024 end-of-campaign surveys. Source and poll identifiers, candidate names, LV/RV populations, dates, pollster, sample size and original survey URLs are preserved. Fourteen question pairs have missing method classification; do not guess.

The 2020 pilot includes **multiple questions/populations per poll** (175 question IDs from 121 state-specific poll IDs), notably verified Marquette LV and RV figures. Until a nonarbitrary predeclared **one observation per poll** selection rule and tracking-poll handling are established, this file must **not** be used to claim an independent-poll error distribution. A source-specific field-end 1–14-day criterion worked in this pilot, but applying an identical window across all 2000–2024 sources remains proposed rather than frozen. Additional primary-source spot checks and 2016/2024 file-level acquisition are still required.

Full [acquisition and original poll spot-check documentation](pilot-02-poll-data-addendum.md). No inferential statistical hypotheses have been tested.
