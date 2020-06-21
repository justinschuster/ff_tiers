"""
Written by Justin Schuster
This file tests the functions found in
ff_dl.py.
"""
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
        
    def test_url_arg(self):
        os.system("python3 ~/ff_tiers/src/ff_dl.py -u www.test.com")
        captured = self.capfd.readouterr()
        #self.assertEqual('www.test.com\n', captured.out)
        assert captured.out == "www.test.com\n"
        

if __name__ == "__main__":
        unittest.main()