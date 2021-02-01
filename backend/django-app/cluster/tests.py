""" For testing the Ranking class. """

import os
from django.test import TestCase
from django.conf import settings
from .rankings import Rankings

class RankingsTestCase(TestCase):
    """ Holds test cases for the rankings class. """

    def test_player_data_from_missing_csv(self):
        """ Make sure that handles not found csv properly. """
        position = 'K'
        self.assertEqual(None, Rankings.player_data_from_csv(position))

    def test_update_player_data(self):
        """ tests Rankings.update_player_data. """
        Rankings.update_player_data()
