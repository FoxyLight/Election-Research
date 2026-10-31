# FiveThirtyEight original metadata archive: 2016, 2020, 2024

**Archived here:** 2026-10-31, using the authenticated GitHub read connector to retrieve upstream text files. Each destination Git blob SHA was compared with its original upstream Git blob SHA and matched **byte for byte**.

**Source:** [FiveThirtyEight/data, state-of-the-polls-2024](https://github.com/fivethirtyeight/data/tree/master/state-of-the-polls-2024).

**Data author/publisher:** FiveThirtyEight (ABC News).

**License:** Unless otherwise noted, [FiveThirtyEight's dataset repository](https://github.com/fivethirtyeight/data/blob/master/README.md) distributes its **datasets under Creative Commons Attribution 4.0 International (CC BY 4.0)**. These files are original upstream data, copied unchanged and credited to FiveThirtyEight. The research project's calculations and commentary are separate work. Retain attribution on any further redistribution.

| File | Bytes | Upstream Git blob SHA |
| --- | ---: | --- |
| `2016_polls.csv` | 288,013 | `aab9ab74e9e29b086a7700499a5284a259a3c4f9` |
| `2020_polls.csv` | 283,767 | `43e8b5beb864359fd6f3e4bd1561f015bd7074e3` |
| `2024_polls.csv` | 185,239 | `1d9f5565079c93217ff92f897da2da051ba15499` |

**Critical limitations:**

- These files include polls ending **15–180 days before Election Day**, per the [original codebook](https://github.com/fivethirtyeight/data/blob/master/state-of-the-polls-2024/README.md), and cannot support the project's final-fourteen-day accuracy comparison.
- They hold pollster, state, fieldwork timing, tracking, and classification **metadata** but **no candidate polling vote-share estimates**.
- The `has_prez?` column is a flag meaning a survey contained *at least one presidential voting-preference question*, not the number of presidential questions or a unique survey ID.
- Some tracking polls overlap or repeat; counts of rows are **not** counts of independent samples.
- The 2024 archive has an October 28, 2024 publication cutoff.
- Do not merge these files into the RCP published final-average pilot as if they were candidate-preference measurements.

Reproduce the metadata counts in [the processed audit](../../../processed/pilot_538_metadata_coverage.csv) using `python analysis/audit_538_metadata.py` from the project root. The script checks the source blobs before summarizing.
