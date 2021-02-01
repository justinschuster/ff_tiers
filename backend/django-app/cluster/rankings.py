""" Contains all data extraction and manipution. """

import requests
import pandas as pd
from django.conf import settings
from .models import Player

class Rankings():
    """ For retrieving and saving player ranking data. """
    
    """
    @staticmethod
    def download():
        for url in settings.RANKINGS_URLS:
            resp = requests.get(url, auth=(settings.FP_USER, settings.FP_PWD))
            file_name = url.split('/')[5].split('-')[0]
            with open(f'{settings.RANKINGS_DIR}{file_name}.html', 'wb') as curr_file:
                curr_file.write(resp.content)
    """ 

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
            return 0


    def update_player_data():
        pass
