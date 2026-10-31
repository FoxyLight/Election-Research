# Pilot 02 addendum: 2020 final-fourteen-day polling questions

**Date:** 2026-10-31  
**Status:** **Acquired and paired**, preliminary source spot-check **PASS** (2 original Marquette poll questions); full comprehensive integrity audit and inclusion-policy freeze **pending**. This was discovered *after* the earlier Pilot 02 report and supersedes its statement that no end-of-campaign candidate-share file had been acquired.

## Provenance

- **Original data publisher:** FiveThirtyEight.
- **Preserved 2020 historical mirror:** [Simon Willison's fivethirtyeight-polls repository](https://github.com/simonw/fivethirtyeight-polls), file [president_polls.csv](https://github.com/simonw/fivethirtyeight-polls/blob/main/president_polls.csv). Repository identifies the FiveThirtyEight `polls/` archive as its source and states **Creative Commons Attribution 4.0** licensing. Attribute FiveThirtyEight as original data publisher and Simon Willison as archive maintainer. The mirror's latest file is a historical **2020-cycle snapshot**, not a 2024 polling release.
- **Exact source Git blob SHA:** `cbe565b7647059de8b58414e420d2b8587250cc6`; retrieved in full using GitHub's blob API after the standard large-file text reader returned empty results.
- **Original source bytes:** 5,545,063, **16,438 candidate-answer rows** in the full mirror CSV. This complete 5.5 MB source was **not recommitted** to the research repository. The [filtered extract](../data/processed/pilot_2020_final14_paired_questions.csv) contains 175 candidate-paired questions, the upstream SHA, individual poll source links, and acquisition date.
- **Recreation recipe:** [analysis/extract_2020_final14_pairs.py](../analysis/extract_2020_final14_pairs.py) checks the exact Git blob and produces a stable question-level CSV from a locally downloaded copy. It has **not yet been executed against the full 5.5 MB source file in the local Python environment**. The 175-row extraction was performed and independently audited from the full blob through the available data-processing tool, and output was read back from GitHub byte-identical.

## Reproducible filtering and pairing

On the original FiveThirtyEight long-form candidate-answer rows:

1. `cycle == "2020"`, `stage == "general"`, `office_type == "U.S. President"`.
2. `state` exactly `Pennsylvania`, `Wisconsin`, or `Georgia`.
3. Use the original **survey field-end date**, with `1 <= (2020-11-03 - end_date in days) <= 14`; Election Day and post-election field ends excluded.
4. Group by `question_id`; require **exactly one** Democratic and **exactly one** Republican candidate response. Verify metadata consistency within each pair. All retained pairs were Biden versus Trump.
5. Retain `question_id` and `poll_id` separately, the original respondent population, sample size, method, pollster, poll source link, start/end dates, and the original party shares. **Do not** treat multiple questions or different LV/RV subsets in the same poll as independent polls.
6. The published two-candidate *margin* column is `dem_pct - rep_pct` without rescaling to a two-party voter-share denominator. These are polling question percentages, not election results.

## Observed coverage

| State | Paired questions | Distinct poll IDs | Missing methodology | Likely-voter questions | Registered-voter questions |
| --- | ---: | ---: | ---: | ---: | ---: |
| Pennsylvania | 76 | 55 | 6 | 54 | 19 |
| Wisconsin | 53 | 34 | 2 | 36 | 17 |
| Georgia | 46 | 32 | 6 | 32 | 13 |
| **Total** | **175** | **121** (state-specific counts) | **14** | **122** | **49** |

Remaining four questions have another or unclassified population code (do not silently label LV/RV). Individual `question_id` values are unique across these selected records; no ambiguous Democratic/Republican pairings were observed. The full mirror includes **408 answer rows** for these filtered questions, including answers for third parties/others, so each raw answer row is not an independent poll.

**These are archive coverage counts, not a randomly sampled estimate of all final-two-week polling conducted in those states.** A historical archive is subject to its own acquisition, reporting and source selection. Completion relative to all public contemporaneous polls is **not established**.

## Original-source validation: Marquette Wisconsin

Original dated Oct. 21–25, 2020 questionnaires were directly inspected:

| Historical mirror question ID | Poll ID | Population | Mirror Biden | Mirror Trump | Original source |
| --- | --- | --- | ---: | ---: | --- |
| 135295 | 72151 | 749 likely voters | 48% | 43% | [Marquette Q23 including leaners, LV](https://law.marquette.edu/poll/wp-content/uploads/2020/10/MLSP65ToplinesLV.html#q23:_(combined):_biden_vs_trump_vs_jorgensen,_including_leaners) |
| 135296 | 72151 | 806 registered voters | 47% | 43% | [Marquette Q23 including leaners, RV](https://law.marquette.edu/poll/wp-content/uploads/2020/10/MLSP65ToplinesRV.html#q23:_biden_vs_trump_vs_jorgensen) |

Both vote-share pairs and sample sizes match the primary published tables. **They are from the same original survey**, which produces two subgroup observations and shows why de-duplication rules require explicit population preference. The original tables also offer *other* Q23 treatments (unleaned votes or allocated nonresponse) with different shares. Do not combine them without checking the underlying question variant.

These **two** validated questions demonstrate that source matching is possible. They do **not** guarantee the remaining 173 questions match their respective original poll reports; those require a stratified further spot-check.

## Remaining work and conclusion

1. Run the committed Python extractor on the exact large source file, compare its generated CSV to the committed extracted file, and preserve the result in the research log.
2. Validate additional original polls across **all three** states, multiple pollsters, sample modes and dates. Decide how to handle missing methods, minor candidates, multiple questions per poll, LV vs RV and tracking polls; document coverage/selection.
3. Pursue equivalent final-14-day **2016 and 2024** vote-share sources. The archived 538 `state-of-the-polls-2024` files remain metadata for polls 15–180 days before Election Day and cannot be substituted.
4. Maintain the nine RCP *published averages* as a distinct source product; they must not be represented as means of these 175 polls.

**Research gate:** this is a **successful 2020 final-window acquisition pilot**, but not a completed three-cycle comparative source or a full statistical study. No inference about geographically correlated or persistent polling error is justified from extraction coverage alone.
