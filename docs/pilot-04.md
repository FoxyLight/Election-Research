# Pilot 04 — independent survey units, source reconciliation and comparability gate

**Date:** 2026-10-31  
**Result:** **PARTIAL PASS / ANALYTIC HOLD.** Tracking/dependence risk quantified, selected original reports checked and a repeatable CI validation workflow installed. A consistent *three-cycle* individual-poll sampling universe and defensible treatment of overlapping tracking waves are **not** established. No H1–H6 hypothesis was tested.

## Scope and evidence

The authoritative starting files remain [Pilot 03](pilot-03.md), [provisional methodology v0.2](methodology-v0.2.md), and the original 2020 FiveThirtyEight data snapshot hosted in [Simon Willison's archive](https://github.com/simonw/fivethirtyeight-polls/blob/main/president_polls.csv), source blob SHA `cbe565b7647059de8b58414e420d2b8587250cc6`. The 115 provisional question-per-poll records are in [pilot_03_2020_unique_poll_provisional.csv](../data/processed/pilot_03_2020_unique_poll_provisional.csv). This snapshot is **not** a complete three-cycle archive.

### Reproduction artifacts

- [Per-poll dependency audit](../data/processed/pilot04_2020_poll_dependency_audit.csv): 115 selected 2020 records with field-date span, early-start flag, original archive tracking flag and overlap counts.
- [All overlapping record pairs](../data/processed/pilot04_2020_overlap_pairs.csv): 200 pairs with state, pollster, source poll/question IDs and dates.
- [Offline Python audit](../analysis/pilot04_overlap_audit.py): recomputes overlap flags and pairs from the committed selected file, checks expected totals and compares exact output rows.
- [Primary-source checks](../data/processed/pilot04_primary_source_check_register.csv): 13 concrete question-level or archive-level comparisons to original published pollster sources, including unresolved mismatches.
- [GitHub Actions workflow](../.github/workflows/validate-research.yml): on matching pushes or manual dispatch, intends to run original Pilot 01–03 checks, source-metadata audit and Pilot 04 dependency audit with Python 3.12. The workflow **was committed**, but its hosted job conclusion **could not be read back** with the available GitHub connection; do **not** say the Actions run passed.

The independent source-file **consistency calculations were executed against files retrieved directly from GitHub using the connected data-processing environment**. The committed Python Pilot 04 script has *not* independently been executed in a locally checked-out repository in this session. Thus the source-level audit result is independently reproduced in code, while CI/Python runner success is **unverified**.

## 1. Survey independence: quantified warnings

The selected 2020 dataset has **115** state/poll ID records (GA 31, PA 52, WI 32) after excluding 6 same-tier ambiguous poll groups. These 115 records should **not** be described as 115 statistically independent surveys.

| Warning or observed property | Count | Interpretation |
| --- | ---: | --- |
| Selected 2020 poll IDs | 115 | One chosen question per poll ID, not necessarily independent samples |
| Fieldwork *started* more than 14 days before Election Day | **52** | Final-14-day **end-date** window does not imply all interviews took place in that window |
| Distinct selected poll IDs participating in a same-pollster, same-state date overlap | **40** | Potential dependence; not proof of duplicated respondents |
| Overlapping poll-ID **pairs** | **200** | Count of overlapping unordered pairs, not number of polls |
| SurveyMonkey pairs | **198** | Most overlap pairs reflect repeated SurveyMonkey periods |
| YouGov pairs | **2** | Additional source of overlapping same-state entries |
| Original mirror rows with `tracking == TRUE` | **42** | 36 SurveyMonkey, 6 Morning Consult; 14 explicitly flagged in each pilot state |
| Original mirror rows with `tracking` **blank** | **73** | Missing source flag, **not** evidence that these polls are nontracking |

A date-overlap pair is detected only when two **different** poll IDs in the **same state**, with the **exact same archived pollster label**, have intersecting inclusive fieldwork intervals. This narrow rule may **miss** dependence across different pollsters, sponsors, variants or states (shared sampling systems). Conversely, simultaneous independent surveys could trigger it. Report the pairs as **possible dependence warnings**, not duplicate surveys.

The original source's `tracking` field is explicitly TRUE or **blank**, not a reliable binary TRUE/FALSE value. Treat blank as unknown. The underlying number of distinct respondents and fractional sample overlap are unavailable. Do **not** derive effective sample size from pairs or simple wave counts.

**Decision:** A prospective error-analysis dataset needs a **wave/sample-family grouping rule** supported by pollster reports or instrument metadata, plus clustered dependence-aware uncertainty estimation. Alternatively one may predefine a single non-overlapping final wave per tracking family as a sensitivity analysis, not select the best-performing wave retrospectively.

## 2. Questionnaire variants validated at original sources

The [13-row source check register](../data/processed/pilot04_primary_source_check_register.csv) includes:
- **2020 Monmouth Georgia, poll 72146:** [original Monmouth report](https://www.monmouth.edu/polling-institute/reports/monmouthpoll_ga_102820/) confirms 50/45 Biden/Trump **RV**, 50/46 **high-turnout LV**, and 50/48 **low-turnout LV**. The original publication clearly distinguishes models of the **same data collection**, not independent survey samples. Source questions 135280, 135281 and 135282 match the historical mirror.
- **2020 Monmouth Pennsylvania, poll 72599:** [original Monmouth report](https://www.monmouth.edu/polling-institute/reports/monmouthpoll_pa_110220/) confirms 50/45 **RV**, 51/44 **high-turnout LV**, and 50/45 **low-turnout LV**. Mirror questions 136264, 136265 and 136266 match; the report's likely-voter figures are alternative weighting/model scenarios, **not separate polls**.
- **2016 Monmouth Pennsylvania:** [original Monmouth report](https://www.monmouth.edu/polling-institute/reports/monmouthpoll_pa_110216/) confirms Clinton 48 / Trump 44 (Oct 29–Nov 1; 403 LV), matching RCP's 2016 PA archive entry.
- **2016 Marquette Wisconsin:** [original Marquette release](https://law.marquette.edu/poll/2016/11/02/mlsp41release/) confirms Clinton 46 / Trump 40 and 1,255 **unweighted LV**, with 1,190 **weighted LV**. [RCP's 2016 table](https://www.realclearpolitics.com/epolls/2016/president/2016StateFinalResults.html) shows **1,225 LV**. RCP sample figure is unverified relative to the primary survey report; preserve the discrepancy. This is **not** evidence of electoral irregularity.
- **2020 Emerson Georgia:** [original pollster news release](https://emersonpolling.reportablenews.com/pr/super-poll-sunday-democrats-within-striking-distance-in-key-southern-states) reports rounded Biden 48 / Trump 49; the historical candidate-answer mirror shows Biden **48.8** / Trump **49.4** for question 136083, n=749 LV. Rounding does **not** fully explain Biden's 48 versus 48.8 (which rounds to 49). Original precise ballot question and source version need checking. Treat this as an unresolved precision/variant discrepancy rather than a matched pair.
- **2024 Emerson Wisconsin (Oct 30–Nov 2):** [original Emerson release](https://emersoncollegepolling.com/november-2024-final-swing-state-polls-too-close-to-call-election-for-president/) says Harris **49 / Trump 49** among **800 LV**; [270toWin's archived record](https://www.270towin.com/2024-presidential-election-polls/wisconsin) likewise reports **49/49**, and [The Hill's detailed tracker](https://elections2024.thehill.com/wisconsin/) reports **49.4/49.4** on one ballot test. [Electoral-Vote.com's 2024 table](https://www.electoral-vote.com/evp2024/Pres/pres_polls.html) lists **50/50**. The original report establishes 49/49 as a defensible **primary-source figure** for that reported result; why the secondary site reports 50/50 has **not** been established (normalization, question variant or transcription are possibilities, not findings). Retain both; do not silently overwrite the prior archive.
- Previously audited 2024 [East Carolina Georgia](https://surveyresearch-ecu.reportablenews.com/pr/georgia-remains-a-tossup-as-election-day-nears), [Marist Pennsylvania](https://maristpoll.marist.edu/polls/marist-pennsylvania-poll-u-s-presidential-contest-in-pennsylvania-november-2024/) and [Marist Wisconsin](https://maristpoll.marist.edu/polls/marist-wisconsin-poll-u-s-presidential-contest-in-wisconsin-november-2024/) shares remain consistent in their respective selected archived records.

The two Monmouth cases demonstrate a **real** question-identity problem, not just bad labels. Six ambiguous 2020 poll groups remain excluded; two are now **explained** by verified competing turnout models, **but no preferred model is selected**. That choice belongs in a prospective protocol that does not depend on election outcomes.

## 3. Three-cycle common-source search

**Candidate A: FiveThirtyEight presidential-question archive.** The [original polls index](https://github.com/fivethirtyeight/data/blob/master/polls/README.md) names both current and historical `president_polls*.csv` resources and includes source poll/question IDs, field dates and samples. The archival 2020 mirror has been retrieved; an **October 28, 2016 snapshot** is incomplete for the final days, while the 2024 modern dataset has not yet been acquired at a known after-election vintage. A FiveThirtyEight 2024 metadata collection that only includes polls ending **15–180 days before Election Day** is **not** interchangeable with final-14-day candidate-share data.

**Candidate B: AAPOR 2024 Task Force reconstruction.** The [official AAPOR report](https://aapor.org/announcements/2024-pre-election-polling-report/) describes a task-force effort to collect the 2016, 2020 and 2024 general-election poll data with comparable cleaning rules. Its [public GitHub code](https://github.com/umisrcps/aapor_preelection_2024) includes a [FiveThirtyEight polling-data download script](https://github.com/umisrcps/aapor_preelection_2024/blob/main/script_01_01_download538files.r), an RCP JSON fetcher and cleaning logic. **The complete cleaned historical poll-level data and all required intermediary files were not located within the examined public repository.** Some code references local analysis files absent from that repository. A reproducible independent replication cannot be claimed from scripts alone.

**Important nonidentical time windows:** AAPOR's described 2024 final two weeks covers polls **ending Oct 23 through Nov 5, 2024**, including Election Day; this project's prospective rule covers **Oct 22 through Nov 4**, excluding Election Day. AAPOR also distinguishes individual surveys from contest-specific matchups, which this project should mirror. Their published 403 survey / 611 matchup figures are across multiple offices, not a count of state presidential polls in our three states.

**Candidate C: RealClearPolitics historical source.** It publishes source-specific final tables in 2016 and 2020 (and newer tables for 2024). A single publisher's archive is **not automatically a uniform selection frame**, because poll lists, aggregation, sample definitions and qualifying pollsters may vary. Each year would require audited completeness and candidate-question crosswalks before being merged.

**Conclusion:** No acquired, fully inspectable **uniform final-14-day question-level dataset across all three presidential cycles** has passed coverage and question-matching validation. This is a source-access and design limitation, not evidence that historical polling research is impossible.

*Access caveat:* An attempted screenshot of the long AAPOR report PDF failed because of the service's document-size limit. The report's indexed text was accessible and its R-code repository was inspected; the report's appendix page images were **not** visually verified during this phase.

## 4. Which methodology rules can be fixed now?

**Accept as integrity requirements:** preserve original percent denominator and candidate names; official outcome counts per state-year; end dates and start dates; source/time/version identifiers; distinguish raw responses, questions, survey IDs, published averages and tracking waves; do not impute missing sample-size/mode or turn blank tracking into FALSE; exclude unresolved equal-tier questions from a definitive single-question sample; no ex-post margin-based tie breaking.

**Do not freeze as inference-ready:** the LV>RV priority for every race, a fixed fallback across head-to-head vs all-candidate questions, one record per tracker, the collection universe, weighting of individual polls, and geographic error models. These require original questionnaire definitions and a uniform historical sample frame. See [Methodology v0.3](methodology-v0.3.md).

## 5. Pilot 04 conclusion and gate to Pilot 05

**Evidence passed:** reproducible **source-level overlap calculation** against exact selected 2020 records, 115-row metadata and 200-pair files committed; original 2020 Monmouth competing models confirmed; original 2024 Emerson figure established; same-source historical paths evaluated; Python CI workflow committed.

**Unverified:** GitHub Actions run conclusion and exact Python job output; 2016 and 2024 comprehensive poll-question dataset; 2020 sample-overlap fractions; why 2016 Marquette RCP sample count differs; why secondary 2024 Emerson values were transformed; four other ambiguous 2020 poll IDs; fully reproducible AAPOR task-force cleaned data.

**Recommended Pilot 05:** prioritize acquiring versioned 2016/2020/2024 original FiveThirtyEight historical files (or an AAPOR task-force cleaned poll archive, if genuinely downloadable), run an audited question-schema crosswalk with at least 10 deliberately stratified source checks per cycle, classify tracking families and sensitivity rules **before** historical error modeling. If access cannot be obtained, define a deliberately smaller *single-publisher descriptive exercise* with clear limits rather than pretending source comparability.

**Decision:** **HOLD on cross-cycle statistical inference** and on substantive H1–H6 hypothesis testing; keep this as a research pipeline readiness and primary-source audit.
