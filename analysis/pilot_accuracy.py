#!/usr/bin/env python3
"""Recalculate Pilot 01 errors from archived-source transcriptions.

No network and no third-party packages are required.
Run from the repository root: python analysis/pilot_accuracy.py
To write the derived CSV: python analysis/pilot_accuracy.py --write

IMPORTANT: this is an acquisition/matching feasibility pilot, not an inferential
study. Individual polls are selected examples, not a representative sample.
"""
import argparse
import csv
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AVERAGES = ROOT / "data/processed/pilot_rcp_state_averages.csv"
POLLS = ROOT / "data/processed/pilot_selected_polls.csv"
OUTPUT = ROOT / "data/processed/pilot_margin_errors.csv"
ELECTION_DATES = {2016: date(2016, 11, 8), 2020: date(2020, 11, 3),
                  2024: date(2024, 11, 5)}

HEADERS = [
    "year", "state", "rcp_avg_margin_d_minus_r_pp",
    "rcp_reported_result_margin_d_minus_r_pp",
    "official_margin_d_minus_r_pp", "reference_basis",
    "avg_margin_error_pp", "selected_poll_margin_d_minus_r_pp",
    "selected_poll_error_pp"
]

def pct(s):
    n = Decimal(s)
    if not (0 <= n <= 100):
        raise ValueError("Vote percentage outside 0..100: " + s)
    return n

def f3(n):
    if n is None:
        return ""
    return str(n.quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))

def load(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def validate_dates(year, start, end):
    a, b = date.fromisoformat(start), date.fromisoformat(end)
    if not a <= b < ELECTION_DATES[year]:
        raise ValueError(f"Invalid field dates: {year} {start} {end}")

def run():
    averages = load(AVERAGES)
    polls = load(POLLS)
    if len(averages) != 9 or len(polls) != 9:
        raise ValueError("Expected exactly 9 state-year average and selected-poll rows")

    index = {}
    for p in polls:
        key = (int(p["year"]), p["state"])
        if key in index:
            raise ValueError(f"Repeated selected poll for {key}")
        validate_dates(key[0], p["field_start"], p["field_end"])
        pct(p["dem_pct"]); pct(p["rep_pct"])
        index[key] = p

    out = []
    for row in averages:
        key = (int(row["year"]), row["state"])
        validate_dates(key[0], row["avg_first_field_date"],
                       row["avg_last_field_date"])
        poll = index.pop(key)
        poll_margin = pct(poll["dem_pct"]) - pct(poll["rep_pct"])
        avg_margin = (pct(row["rcp_avg_dem_pct"]) -
                      pct(row["rcp_avg_rep_pct"]))
        rcp_result_margin = (pct(row["rcp_final_dem_pct"]) -
                             pct(row["rcp_final_rep_pct"]))

        vote_fields = ["certified_dem_votes", "certified_rep_votes",
                       "certified_total_pres_votes"]
        has_counts = [bool(row[x]) for x in vote_fields]
        if any(has_counts) and not all(has_counts):
            raise ValueError(f"Incomplete official vote totals for {key}")

        official_margin = None
        if all(has_counts):
            dem, rep, total = [int(row[x]) for x in vote_fields]
            if not (0 <= dem <= total and 0 <= rep <= total and
                    dem + rep <= total and total > 0):
                raise ValueError(f"Invalid certified vote totals for {key}")
            official_margin = (Decimal(dem - rep) * 100 / Decimal(total))
        reference = official_margin if official_margin is not None else rcp_result_margin
        basis = ("official_count" if official_margin is not None
                 else "rcp_rounded_reference")
        out.append(dict(zip(HEADERS, [
            row["year"], row["state"], f3(avg_margin), f3(rcp_result_margin),
            f3(official_margin), basis, f3(avg_margin - reference),
            f3(poll_margin), f3(poll_margin - reference)
        ])))

    if index:
        raise ValueError(f"Selected polls did not match average records: {list(index)}")
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true",
                        help="write derived comparison CSV in data/processed")
    args = parser.parse_args()
    result = run()
    if args.write:
        with OUTPUT.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=HEADERS, lineterminator="\n")
            w.writeheader()
            w.writerows(result)
        print("Wrote", OUTPUT.relative_to(ROOT))
    else:
        for r in result:
            print(f'{r["year"]} {r["state"]:<12} '
                  f'RCP avg D-R: {r["rcp_avg_margin_d_minus_r_pp"]:>7} pp; '
                  f'error: {r["avg_margin_error_pp"]:>7} pp '
                  f'({r["reference_basis"]})')
