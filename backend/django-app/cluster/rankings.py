import requests 
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from django.conf import settings

class GetRankings():
    def download():
        for url in settings.RANKINGS_URLS:
            resp = requests.get(url, auth=(settings.FP_USER, settings.FP_PWD))
            file_name = url.split('/')[5].split('-')[0]
            with open(f'{settings.RANKINGS_DIR}{file_name}.html', 'wb') as curr_file:
                curr_file.write(resp.content)

    def get_player_data():
        pass
