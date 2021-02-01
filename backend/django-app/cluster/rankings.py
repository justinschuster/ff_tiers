""" Contains all data extraction and manipution. """

import requests
import pandas as pd
from django.conf import settings
from .models import Player

class Rankings():
    """ For retrieving and saving player ranking data. """
    
    @staticmethod
    def update_player_data():
        """ Updates database with new player data. """
        for position in settings.PLAYER_POSITIONS:
            data = Rankings.player_data_from_csv(position)  
            if data is None:
                continue
            for ind in data.index:
                Rankings.save_player(data.iloc[ind], position)

    @staticmethod
    def player_data_from_csv(pos):
        """ Loads data from csv's to Player model """
        file_path = f'{settings.RANKINGS_DIR}FantasyPros_2021_Draft_{pos}_Rankings.csv' 
        try:
            data = pd.read_csv(file_path) 
            return data
        except FileNotFoundError:
            print(f'Unable to find file at {file_path}')
            print(f'Could not retrieve {pos} data from file.')
            return None

    @staticmethod
    def save_player(player_data, pos):
        """ Saves player information to database. 
        TODO: add check to see if the players is already in db
        """
        p = Player(
            scoring = 'STD',
            consensus_ranking = player_data['RK'],
            player_name = player_data['PLAYER NAME'],
            team_name_abbrev = player_data['TEAM'],
            best_ranking = player_data['BEST'],
            worst_ranking = player_data['WORST'],
            average_ranking = player_data['AVG.'],
            ranking_std = player_data['STD.DEV']
        )
        p.save()
