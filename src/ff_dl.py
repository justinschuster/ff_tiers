"""Contains methods that scrape the FantasyPros.com rankings.

Downloads the FantasyPros.com consensus rankings html files then scrapes
the data using BeautifulSoup4.
"""

import requests

from bs4 import BeautifulSoup

def get_player_data(file_name):
    """Scrapes player data from downloaded FP.com ranking html file. """

    players = []
    column_headings = [
        'consensus_ranking', 'player_name', 'team_name_abbrev', 'position',
        'bye_week', 'best_ranking', 'worst_ranking', 'average_ranking',
        'ranking_std', 'ADP', 'vs_ADP'
    ]

    players.append(column_headings)
    with open(file_name) as rankings_file:
        soup = BeautifulSoup(rankings_file, "lxml")
    for player in soup.find_all("tr", class_="player-row"):
        player_data = []
        player_td_elements = player.find_all("td")
        player_data.append(player_td_elements[0].contents[0])
        info = player_td_elements[1].find("input", class_="wsis").attrs
        player_data.append(info['data-name'])
        player_data.append(info['data-team'])
        player_data.append(info['data-position'])

        for i in range(4, 11):
            try:
                player_data.append(player_td_elements[i].contents[0])
            except IndexError:
                player_data.append('')

        players.append(player_data)
    return players

def download_rankings(url, file_name, user_info):
    """Downloads and saves html file."""

    resp = requests.get(url,
                        auth=(user_info['username'], user_info['password']))
    output = open(file_name, 'w+b')
    output.write(resp.content)
    output.close()
