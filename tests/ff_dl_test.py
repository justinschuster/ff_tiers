import unittest
import pytest
import sys

sys.path.insert(0,'/home/justin/ff_tiers/src/')

import ff_dl

class TestClass(unittest.TestCase):
    def test_get_player_data(self):
        file = '/home/justin/ff_tiers/data/rankings.html'
        self.assertEqual(495, len(ff_dl.get_player_data(file)))

if __name__ == "__main__":
        unittest.main()
