import unittest
import pytest
import sys

sys.path.insert(0,'/home/justin/ff_tiers/src/')

import ff_dl

class TestClass(unittest.TestCase):
    def test_get_player_data_correct_length(self):
        file = '/home/justin/ff_tiers/data/rankings.html'
        self.assertEqual(496, len(ff_dl.get_player_data(file)))

    def test_player_data_column_headings(self):
        column_headings = ['consensus_ranking', 'player_name', 'team_name_abbrev', 'position', 'bye_week', 'best_ranking', 'worst_ranking', 'average_ranking', 'ranking_std', 'ADP', 'vs ADP'] 
        file = '/home/justin/ff_tiers/data/rankings.html'
        self.assertEqual(column_headings, ff_dl.get_player_data(file)[0]) 

if __name__ == "__main__":
        unittest.main()
