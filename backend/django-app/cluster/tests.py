import os
from .rankings import GetRankings 
from django.test import TestCase
from django.conf import settings

class RankingsTestCase(TestCase):
    def test_rankings_file_save(self):
        file_names = [
            'consensus.html',
            'ppr.html',
            'half.html',
        ]

        GetRankings.download()
        for name in file_names:
            self.assertIn(name, os.listdir(settings.RANKINGS_DIR))
