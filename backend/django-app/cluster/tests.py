import os
from .rankings import GetRankings 
from django.test import TestCase

class RankingsTestCase(TestCase):
    def test_rankings_file_save(self):
        test_dir = '/home/justin/ff_tiers/backend/django-app/cluster/download/'
        file_names = [
            'consensus.html',
            'ppr.html',
            'half.html',
        ]

        GetRankings.download()
        for name in file_names:
            self.assertIn(name, os.listdir(test_dir))
