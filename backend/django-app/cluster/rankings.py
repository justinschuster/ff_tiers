""" Contains all data extraction and manipution. """

import requests
import pandas as pd
from django.conf import settings
from .models import Player

class RankingsData():
    """ For retrieving and saving player ranking data. """

    @staticmethod
    def update_player_data():
        """ Updates database with new player data. """
        for position in settings.PLAYER_POSITIONS:
            data = RankingsData.player_data_from_csv(position)
            if data is None:
                continue
            for ind in data.index:
                RankingsData.save_player(data.iloc[ind], position)

    @staticmethod
    def player_data_from_csv(pos):
        """ Loads data from csv's to Player model """
        file_path = f'{settings.RANKINGS_DIR}FantasyPros_2021_Draft_{pos}_Rankings.csv'
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
           return None

    @staticmethod
    def save_player(player_data, pos):
        """ Saves player information to database.
        TODO: Multiple scoring formats 
        """
        player = RankingsData.safe_get(player_data['PLAYER NAME'])
        if player is None:
            player = Player(
                scoring = 'STD',
                consensus_ranking = player_data['RK'],
                player_name = player_data['PLAYER NAME'],
                team_name_abbrev = player_data['TEAM'],
                position = pos,
                best_ranking = player_data['BEST'],
                worst_ranking = player_data['WORST'],
                average_ranking = player_data['AVG.'],
                ranking_std = player_data['STD.DEV']
            )
        else:
            player.best_ranking = player_data['BEST']
            player.worst_ranking = player_data['WORST']
            player.average_ranking = player_data['AVG.']
            player.ranking_std = player_data['STD.DEV']
        player.save()

    @staticmethod
    def safe_get(name):
        """
        Wrapper for Django Model.objects.get()
        Handles DoesNotExist exception
        """
        try:
            player = Player.objects.get(player_name=name)
        except Player.DoesNotExist:
            player = None
        return player
