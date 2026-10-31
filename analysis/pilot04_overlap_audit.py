#!/usr/bin/env python3
"""Pilot 04 dependency audit. No third-party Python packages required.

Run from repository root:
    python analysis/pilot04_overlap_audit.py --check
    python analysis/pilot04_overlap_audit.py --write

This tests whether poll field intervals overlap within the same state+pollster.
Overlapping dates are a *possible dependence warning*, not proof of shared
respondents. The 2020 mirror's tracking field is either TRUE or BLANK; blank
does NOT mean false.

Source: 2020 FiveThirtyEight polling CSV via the exact Simon Willison mirror
Git blob cbe565b7647059de8b58414e420d2b8587250cc6.
"""
import argparse
import csv
from collections import Counter
from datetime import date
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/processed'
SOURCE = DATA / 'pilot_03_2020_unique_poll_provisional.csv'
FLAGS = DATA / 'pilot04_2020_poll_dependency_audit.csv'
PAIRS = DATA / 'pilot04_2020_overlap_pairs.csv'
ELECTION = date(2020, 11, 3)

FLAGS_FIELDS = [
    'state', 'poll_id', 'question_id', 'pollster', 'field_start',
    'field_end', 'field_span_days', 'field_start_outside_primary_14_days',
    'source_mirror_tracking_flag', 'overlap_pair_count_same_pollster_state',
    'overlap_unique_distinct_poll_ids'
]
PAIRS_FIELDS = [
    'state', 'pollster', 'poll_id_a', 'poll_id_b',
    'question_id_a', 'question_id_b',
    'field_start_a', 'field_end_a', 'field_start_b', 'field_end_b'
]


def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def calculate(polls, tracking_values):
    pair_rows, by_poll = [], {}
    if len({(x['state'], x['poll_id']) for x in polls}) != len(polls):
        raise ValueError('Duplicate state/poll ID in selected rows')

    for a, b in combinations(polls, 2):
        if (a['state'] != b['state'] or a['pollster'] != b['pollster']
                or a['poll_id'] == b['poll_id']):
            continue
        if (a['field_start'] <= b['field_end'] and
                b['field_start'] <= a['field_end']):
            pair_rows.append({
                'state': a['state'], 'pollster': a['pollster'],
                'poll_id_a': a['poll_id'], 'poll_id_b': b['poll_id'],
                'question_id_a': a['question_id'], 'question_id_b': b['question_id'],
                'field_start_a': a['field_start'], 'field_end_a': a['field_end'],
                'field_start_b': b['field_start'], 'field_end_b': b['field_end'],
            })
            for x, y in ((a, b), (b, a)):
                by_poll.setdefault((x['state'], x['poll_id']), []).append(y['poll_id'])

    flags_rows = []
    for x in polls:
        start, end = date.fromisoformat(x['field_start']), date.fromisoformat(x['field_end'])
        if not (start <= end < ELECTION and 1 <= (ELECTION-end).days <= 14):
            raise ValueError('Invalid date window in selected polling record')
        key = (x['state'], x['poll_id'])
        if key not in tracking_values:
            raise ValueError(f'Missing independently extracted tracking metadata for {key}')
        overlap = by_poll.get(key, [])
        flags_rows.append({
            'state': x['state'], 'poll_id': x['poll_id'],
            'question_id': x['question_id'], 'pollster': x['pollster'],
            'field_start': x['field_start'], 'field_end': x['field_end'],
            'field_span_days': str((end-start).days+1),
            'field_start_outside_primary_14_days':
                'TRUE' if (ELECTION-start).days > 14 else 'FALSE',
            'source_mirror_tracking_flag': tracking_values[key],
            'overlap_pair_count_same_pollster_state': str(len(overlap)),
            'overlap_unique_distinct_poll_ids': str(len(set(overlap))),
        })
    return flags_rows, pair_rows


def save(path, records, fields):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        w.writerows(records)


def run(write=False):
    source, old_flags, old_pairs = read(SOURCE), read(FLAGS), read(PAIRS)
    tracking_values = {
        (x['state'], x['poll_id']): x['source_mirror_tracking_flag']
        for x in old_flags
    }
    if any(v not in ('TRUE', '') for v in tracking_values.values()):
        raise ValueError('Unexpected tracking flag; blank != FALSE')
    flag_rows, pair_rows = calculate(source, tracking_values)
    counts = Counter(x['pollster'] for x in pair_rows)
    assert len(source) == 115
    assert len(flag_rows) == 115
    assert len(pair_rows) == 200
    assert sum(x['field_start_outside_primary_14_days'] == 'TRUE' for x in flag_rows) == 52
    assert sum(int(x['overlap_pair_count_same_pollster_state']) > 0 for x in flag_rows) == 40
    assert sum(x['source_mirror_tracking_flag'] == 'TRUE' for x in flag_rows) == 42
    assert counts == Counter({'SurveyMonkey': 198, 'YouGov': 2})
    if write:
        save(FLAGS, flag_rows, FLAGS_FIELDS)
        save(PAIRS, pair_rows, PAIRS_FIELDS)
    else:
        if flag_rows != old_flags or pair_rows != old_pairs:
            raise ValueError('GitHub output differs from deterministic recomputation')
    print('PASS: 115 poll IDs, 52 early starts, 40 at-risk poll IDs, 200 date-overlap pairs')
    print('Source tracking TRUE: 42; missing tracking flag: 73 (not FALSE)')
    print('Overlapping same-pollster/state pairs: SurveyMonkey 198; YouGov 2')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    x = p.add_mutually_exclusive_group(required=True)
    x.add_argument('--check', action='store_true')
    x.add_argument('--write', action='store_true')
    args = p.parse_args()
    run(write=args.write)
