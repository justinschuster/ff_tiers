""" Contains testing methods for ff_dl.py.

Tests the functions and uses of ff_dl.py.
"""

import sys
import unittest

sys.path.insert(0, '/home/schuj/ff_tiers/src/')

import ff_dl

class TestClass(unittest.TestCase):
    """ Class for test functions for ff_dl.py """

    def test_get_player_data_correct_length(self):
        """ Checks to see if the player data is correct length. """

        file = '/home/schuj/ff_tiers/data/standard-rankings.html'
        self.assertEqual(496, len(ff_dl.get_player_data(file)))

    def test_player_data_column_headings(self):
        """ Checks for proper column headings. """

        column_headings = [
            'consensus_ranking', 'player_name', 'team_name_abbrev',
            'position', 'bye_week', 'best_ranking', 'worst_ranking',
            'average_ranking', 'ranking_std', 'ADP', 'vs_ADP'
        ]
        file = '/home/schuj/ff_tiers/data/standard-rankings.html'
        self.assertEqual(column_headings, ff_dl.get_player_data(file)[0])

if __name__ == "__main__":
    unittest.main()
