#!/usr/bin/env python3
"""Audit 538's 15–180-day metadata archive, NOT final-week polling shares.

From the repository root, run:
    python analysis/audit_538_metadata.py
    python analysis/audit_538_metadata.py --write

Only records with has_prez? == TRUE are counted. Some tracking-poll records
are overlapping repeated measures, not independent poll samples.
"""
import argparse
import csv
import hashlib
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_DIR = ROOT / 'data/raw/fivethirtyeight/state-of-the-polls-2024'
RESULTS = ROOT / 'data/processed/pilot_538_metadata_coverage.csv'
EXPECTED = {
    2016: 'aab9ab74e9e29b086a7700499a5284a259a3c4f9',
    2020: '43e8b5beb864359fd6f3e4bd1561f015bd7074e3',
    2024: '1d9f5565079c93217ff92f897da2da051ba15499',
}
STATES = ('GA', 'PA', 'WI')
FIELDS = (
    'year', 'state', 'presidential_question_poll_records',
    'tracking_records', 'earliest_field_end', 'latest_field_end',
    'provider_window_days_before_election', 'upstream_git_blob_sha',
    'upstream_file_url',
)


def blob_hash(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def audit_year(year):
    path = UPSTREAM_DIR / f'{year}_polls.csv'
    data = path.read_bytes()
    actual_sha = blob_hash(data)
    if actual_sha != EXPECTED[year]:
        raise ValueError(f'Source file changed for {year}: {actual_sha}')
    with path.open(encoding='utf-8-sig', newline='') as f:
        raw = list(csv.DictReader(f))
    required = {'state', 'has_prez?', 'tracking', 'end_date'}
    if not raw or not required.issubset(raw[0]):
        raise ValueError(f'Incomplete 538 metadata schema in {year}')
    result = []
    for state in STATES:
        selected = [p for p in raw if p['state'] == state and p['has_prez?'] == 'TRUE']
        endings = sorted(datetime.strptime(p['end_date'], '%m/%d/%y').date().isoformat()
                         for p in selected)
        if not endings:
            raise ValueError(f'No presidential-question poll metadata: {year} {state}')
        result.append(dict(zip(FIELDS, (
            str(year), state, str(len(selected)),
            str(sum(p['tracking'] == 'TRUE' for p in selected)),
            endings[0], endings[-1], '15-180', EXPECTED[year],
            f'https://github.com/fivethirtyeight/data/blob/master/'
            f'state-of-the-polls-2024/{year}_polls.csv',
        ))))
    return result


def run():
    return [item for year in sorted(EXPECTED) for item in audit_year(year)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    rows = run()
    if args.write:
        with RESULTS.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
            w.writeheader()
            w.writerows(rows)
        print(f'Wrote {RESULTS.relative_to(ROOT)}')
    else:
        with RESULTS.open(newline='', encoding='utf-8') as f:
            existing = list(csv.DictReader(f))
        if rows != existing:
            raise SystemExit('FAIL: committed audit summary differs from raw source files')
        print('PASS: 538 metadata summaries equal the committed CSV (9 state-years)')


if __name__ == '__main__':
    main()
