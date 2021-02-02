""" For testing the Ranking class. """

import os
from django.test import TestCase
from django.conf import settings
from .rankings import RankingsData
from .models import Player

class RankingsTestCase(TestCase):
    """ Holds test cases for the rankings class. """

    def setUp(self):
        test_player = Player(
            scoring = 'STD',
            consensus_ranking = 1,
            player_name = 'test name',
            team_name_abbrev = 'OAK',
            position = 'QB',
            best_ranking = 1,
            worst_ranking = 3,
            average_ranking = 1,
            ranking_std = 1
        )
        test_player.save()

    def test_player_data_from_missing_csv(self):
        """ Make sure that handles not found csv properly. """
        position = 'K'
        self.assertEqual(None, RankingsData.player_data_from_csv(position))

    def test_update_player_data(self):
        """ tests Rankings.update_player_data. """
        RankingsData.update_player_data()

    def test_safe_get_doesnt_exist(self):
        """ RankingsData.safe_get should return None if name not found. """
        self.assertEqual(None, RankingsData.safe_get('does not exist'))

    def test_safe_get_does_exist(self):
        """ RankingsData.safe_get should return Player object if player exists """
        self.assertIsInstance(RankingsData.safe_get('test name'), Player)
