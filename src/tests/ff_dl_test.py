# Got this from stackoverflow so I could import ff_dl 
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import unittest
import pytest
import ff_dl 

class TestClass(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def capfd(self, capfd):
        self.capfd = capfd
    """   
    def test_url_arg(self):
        os.system("python3 ~/ff_tiers/src/ff_dl.py -u www.test.com -f ~/ff_tiers/data/rankings.xls")
        captured = self.capfd.readouterr()
        self.assertEqual('www.test.com\n~/ff_tiers/data/rankings.xls\n', captured.out)
    """

    def test_get_player_data(self):
        file = '/home/justin/ff_tiers/data/consensus-cheatsheet.html'
        self.assertEqual(478, len(ff_dl.get_player_data(file)))

if __name__ == "__main__":
        unittest.main()