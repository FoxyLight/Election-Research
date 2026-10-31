#!/usr/bin/env python3
"""Standard-library regression checks for the nine-row polling pilot.

Run from repository root: python -m unittest discover -s analysis -p 'test_*.py' -v
"""
import csv
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path
from unittest.mock import patch

import pilot_accuracy as pilot


class PilotAccuracyTests(unittest.TestCase):
    def test_nine_records_and_official_comparators(self):
        rows = pilot.run()
        self.assertEqual(len(rows), 9)
        self.assertEqual(len({(r['year'], r['state']) for r in rows}), 9)
        self.assertTrue(all(r['reference_basis'] == 'official_count' for r in rows))

    def test_2016_margins_using_house_clerk_vote_totals(self):
        rows = {(r['year'], r['state']): r for r in pilot.run()}
        ga = rows[('2016', 'Georgia')]
        pa = rows[('2016', 'Pennsylvania')]
        self.assertEqual(ga['official_margin_d_minus_r_pp'], '-5.131')
        self.assertEqual(ga['avg_margin_error_pp'], '0.331')
        self.assertEqual(pa['official_margin_d_minus_r_pp'], '-0.724')
        self.assertEqual(pa['avg_margin_error_pp'], '2.624')

    def test_committed_calculated_csv_matches_recalculation(self):
        rows = pilot.run()
        with pilot.OUTPUT.open(newline='', encoding='utf-8') as f:
            saved = list(csv.DictReader(f))
        self.assertEqual(rows, saved)

    def test_invalid_poll_field_dates_rejected(self):
        with self.assertRaises(ValueError):
            pilot.validate_dates(2024, '2024-11-04', '2024-11-05')
        with self.assertRaises(ValueError):
            pilot.validate_dates(2016, '2016-11-05', '2016-11-03')

    def test_incomplete_official_vote_counts_rejected(self):
        source = pilot.AVERAGES.read_text(encoding='utf-8').splitlines()
        fields = source[0].split(',')
        idx = fields.index('certified_total_pres_votes')
        original = source[1].split(',')
        original[idx] = ''
        source[1] = ','.join(original)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'bad_counts.csv'
            path.write_text('\n'.join(source) + '\n', encoding='utf-8')
            with patch.object(pilot, 'AVERAGES', path):
                with self.assertRaisesRegex(ValueError, 'Incomplete official vote totals'):
                    pilot.run()

    def test_duplicate_selected_poll_key_rejected(self):
        source = pilot.POLLS.read_text(encoding='utf-8').splitlines()
        row = source[1].split(',')
        row[0] = '2016'
        row[1] = 'Wisconsin'
        source[1] = ','.join(row)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'dup.csv'
            path.write_text('\n'.join(source) + '\n', encoding='utf-8')
            with patch.object(pilot, 'POLLS', path):
                with self.assertRaisesRegex(ValueError, 'Repeated selected poll'):
                    pilot.run()


if __name__ == '__main__':
    unittest.main()
