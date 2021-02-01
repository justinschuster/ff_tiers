""" For testing the Ranking class. """

import os
from django.test import TestCase
from django.conf import settings
from .rankings import Rankings

class RankingsTestCase(TestCase):
    """ Holds test cases for the rankings class. """
    """
    def test_rankings_file_save(self):
        file_names = [
            'consensus.html',
            'ppr.html',
            'half.html',
        ]

        Rankings.download()
        for name in file_names:
            self.assertIn(name, os.listdir(settings.RANKINGS_DIR))
    """
    
    def test_player_data_from_missing_csv(self):
        """ Make sure that handles not found csv properly. """
        position = 'K'
        self.assertEqual(0, Rankings.player_data_from_csv(position))
