#!/usr/bin/env python3
"""Recreate Pilot 02's 2020 final-14-day paired candidate-question extract.

Original archived source: https://github.com/simonw/fivethirtyeight-polls/blob/main/president_polls.csv
Git blob SHA1: cbe565b7647059de8b58414e420d2b8587250cc6

The 5.5 MB historical source is not committed to this project. Download the
specific source revision, then run from the repository root:

    python analysis/extract_2020_final14_pairs.py --input /path/to/president_polls.csv --check

To overwrite the derived CSV only after review, replace --check with --write.
Python standard library only. No averaging or statistical inference.
"""
import argparse
import csv
import hashlib
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'data/processed/pilot_2020_final14_paired_questions.csv'
SOURCE_BLOB = 'cbe565b7647059de8b58414e420d2b8587250cc6'
ELECTION_DAY = date(2020, 11, 3)
STATE_MAP = {'Pennsylvania': 'PA', 'Wisconsin': 'WI', 'Georgia': 'GA'}
FIELDS = [
    'year', 'state', 'question_id', 'poll_id', 'pollster', 'field_start',
    'field_end', 'sample_size', 'population', 'methodology',
    'dem_candidate', 'rep_candidate', 'dem_pct', 'rep_pct',
    'published_two_candidate_margin_pp', 'poll_source_url',
    'upstream_git_blob_sha', 'retrieved_utc_date',
]


def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def to_iso(s):
    return datetime.strptime(s, '%m/%d/%y').date().isoformat()


def extract(source):
    data = Path(source).read_bytes()
    if blob_sha(data) != SOURCE_BLOB:
        raise ValueError('Upstream mirror Git blob does not match audited vintage')
    with Path(source).open(newline='', encoding='utf-8') as f:
        raw = csv.DictReader(f)
        groups = {}
        for record in raw:
            if (record['cycle'] != '2020'
                    or record['stage'] != 'general'
                    or record['office_type'] != 'U.S. President'
                    or record['state'] not in STATE_MAP):
                continue
            field_end = datetime.strptime(record['end_date'], '%m/%d/%y').date()
            delta = (ELECTION_DAY - field_end).days
            if not (1 <= delta <= 14):
                continue
            groups.setdefault(record['question_id'], []).append(record)

    result = []
    for qid, items in groups.items():
        dem = [x for x in items if x['candidate_party'] == 'DEM']
        rep = [x for x in items if x['candidate_party'] == 'REP']
        if len(dem) != 1 or len(rep) != 1:
            raise ValueError('Ambiguous Democratic/Republican pairing: ' + qid)
        a, b = dem[0], rep[0]
        for key in ('poll_id', 'start_date', 'end_date', 'state', 'pollster'):
            if a[key] != b[key]:
                raise ValueError(f'Inconsistent {key} for question {qid}')
        if 'Biden' not in a['candidate_name'] or 'Trump' not in b['candidate_name']:
            raise ValueError('Unexpected presidential matchup: ' + qid)
        d, r = float(a['pct']), float(b['pct'])
        if not (0 <= d <= 100 and 0 <= r <= 100):
            raise ValueError('Candidate share out of bounds: ' + qid)
        result.append(dict(zip(FIELDS, [
            '2020', STATE_MAP[a['state']], qid, a['poll_id'], a['pollster'],
            to_iso(a['start_date']), to_iso(a['end_date']), a['sample_size'],
            a['population'], a['methodology'], a['candidate_name'],
            b['candidate_name'], a['pct'], b['pct'], f'{d-r:.2f}',
            a['url'], SOURCE_BLOB, '2026-10-31',
        ])))
    if len(result) != 175:
        raise ValueError('Expected 175 unique paired questions, found ' + str(len(result)))
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True, help='Exact original 2020 GitHub mirror CSV')
    actions = p.add_mutually_exclusive_group(required=True)
    actions.add_argument('--check', action='store_true')
    actions.add_argument('--write', action='store_true')
    args = p.parse_args()
    rows = extract(args.input)
    if args.write:
        with OUTPUT.open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
            w.writeheader()
            w.writerows(rows)
        print('Regenerated', OUTPUT)
    else:
        with OUTPUT.open(encoding='utf-8', newline='') as f:
            saved = list(csv.DictReader(f))
        if rows != saved:
            raise SystemExit('FAIL: extraction differs from repository 2020 paired data')
        print('PASS: reproduced 175 paired questions exactly')


if __name__ == '__main__':
    main()
