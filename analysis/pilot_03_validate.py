#!/usr/bin/env python3
"""Offline Pilot 03 acquisition and deduplication audit (Python stdlib only).

Run from repository root:
    python analysis/pilot_03_validate.py

This checks source-extract arithmetic and selection logic, NOT the accuracy
or completeness of the source archives themselves.
"""
import csv
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/processed"
ARCHIVE = DATA / "pilot_03_2016_2024_final14_archive_polls.csv"
QUESTIONS = DATA / "pilot_2020_final14_paired_questions.csv"
SELECTED = DATA / "pilot_03_2020_unique_poll_provisional.csv"
AMBIGUOUS = DATA / "pilot_03_2020_ambiguous_polls.csv"

ELECTION = {2016: date(2016, 11, 8), 2020: date(2020, 11, 3),
            2024: date(2024, 11, 5)}
POP_RANK = {"lv": 0, "rv": 1, "a": 2}
EXPECTED_ARCHIVES = {
    (2016, "GA"): 5, (2016, "PA"): 6, (2016, "WI"): 4,
    (2024, "GA"): 9, (2024, "PA"): 18, (2024, "WI"): 12,
}


def read(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_window(year, start, end):
    a, b = date.fromisoformat(start), date.fromisoformat(end)
    assert a <= b, (year, start, end)
    offset = (ELECTION[year] - b).days
    assert 1 <= offset <= 14, (year, start, end)
    return (ELECTION[year] - a).days > 14


def check_archive():
    rows = read(ARCHIVE)
    assert len(rows) == 54, len(rows)
    counts = Counter()
    ids = set()
    extended = 0
    for r in rows:
        year, state = int(r["year"]), r["state"]
        counts[year, state] += 1
        assert r["record_id"] not in ids
        ids.add(r["record_id"])
        extended += check_window(year, r["field_start"], r["field_end"])
        d, p = float(r["candidate_dem_pct"]), float(r["candidate_rep_pct"])
        assert 0 <= d <= 100 and 0 <= p <= 100
        assert abs((d - p) - float(r["dem_minus_rep_pp"])) < 0.00001
        assert r["source_url"]
        if year == 2024:
            assert r["reported_sample_size"] == ""
            assert r["reported_population"] == ""
    assert dict(counts) == EXPECTED_ARCHIVES, counts
    marquette = next(r for r in rows if r["record_id"] == "2016-WI-003")
    assert (marquette["candidate_dem_pct"], marquette["candidate_rep_pct"]) == ("46", "40")
    assert "1225" in marquette["data_quality_notes"]
    marist_wi = next(r for r in rows if r["record_id"] == "2024-WI-005")
    assert (marist_wi["candidate_dem_pct"], marist_wi["candidate_rep_pct"]) == ("50", "48")
    marist_pa = next(r for r in rows if r["record_id"] == "2024-PA-008")
    assert (marist_pa["candidate_dem_pct"], marist_pa["candidate_rep_pct"]) == ("50", "48")
    return len(rows), extended


def check_question_selection():
    rows = read(QUESTIONS)
    assert len(rows) == 175
    groups = defaultdict(list)
    question_ids = set()
    for r in rows:
        check_window(2020, r["field_start"], r["field_end"])
        assert r["question_id"] not in question_ids
        question_ids.add(r["question_id"])
        assert r["dem_candidate"] == "Joseph R. Biden Jr."
        assert r["rep_candidate"] == "Donald Trump"
        assert abs(float(r["dem_pct"]) - float(r["rep_pct"])
                   - float(r["published_two_candidate_margin_pp"])) < 1e-6
        groups[r["state"], r["poll_id"]].append(r)
    assert len(groups) == 121
    chosen = {}
    ties = {}
    for key, group in groups.items():
        preferred = min(POP_RANK.get(r["population"], 3) for r in group)
        top = [r for r in group if POP_RANK.get(r["population"], 3) == preferred]
        if len(top) == 1:
            chosen[key] = top[0]["question_id"]
        else:
            ties[key] = {r["question_id"] for r in top}
    assert len(chosen) == 115 and len(ties) == 6
    s = read(SELECTED)
    a = read(AMBIGUOUS)
    assert len(s) == 115 and len(a) == 6
    assert len({(r["state"], r["poll_id"]) for r in s}) == 115
    assert {(r["state"], r["poll_id"]): r["question_id"] for r in s} == chosen
    assert {(r["state"], r["poll_id"]): set(r["candidate_question_ids"].split("|"))
            for r in a} == ties
    return len(rows), len(groups), len(chosen), len(ties)


if __name__ == "__main__":
    archive_count, long_windows = check_archive()
    questions, polls, selected, ambiguous = check_question_selection()
    print("PASS: 2016/2024 archive records:", archive_count)
    print("PASS: source polls with field starts >14 days before election:", long_windows)
    print("PASS: 2020 paired questions / distinct poll IDs:", questions, polls)
    print("PASS: selected unique poll IDs / ambiguous groups:", selected, ambiguous)
    print("PASS: all 3 source extracts preserve candidates and field-end window")
