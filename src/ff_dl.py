import sys
import argparse
import requests
import csv

from bs4 import BeautifulSoup

def create_csv_file(scoring_system, player_info):
    with open('/home/schuj/ff_tiers/data/{}-rankings.csv'.format(scoring_system), 'w+', newline='') as csv_file:
        wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for player in player_info:
            wr.writerow(player)

def get_player_data(file_name):
    players = []
    column_headings = ['consensus_ranking', 'player_name', 'team_name_abbrev', 'position', 'bye_week', 'best_ranking', 'worst_ranking',
            
                        'average_ranking', 'ranking_std', 'ADP', 'vs ADP']
    players.append(column_headings)

    with open(file_name) as fp:
        soup = BeautifulSoup(fp, "lxml")
    for player in soup.find_all("tr", class_="player-row"):
        player_data = []
        player_td_elements = player.find_all("td")
        player_data.append(player_td_elements[0].contents[0]) # append index
        info = player_td_elements[1].find("input", class_="wsis").attrs
        player_data.append(info['data-name']) # append player name
        player_data.append(info['data-team']) # append abbreviated team name  
        player_data.append(info['data-position']) # append player position

        for i in range(4, 11):
            try:
                player_data.append(player_td_elements[i].contents[0])
            except:
                player_data.append('')

        players.append(player_data)
    return players
    
def download_rankings(url, file_name, user_info):
    print(file_name)
    resp = requests.get(url, auth=(user_info['username'], user_info['password'])) 
    output = open(file_name, 'w+b')
    output.write(resp.content)
    output.close()

def get_url():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", dest="url", help="FantasyPros url", required=True)
    parser.add_argument("-f", dest="file_name", help="Name of rankings file", required=True)
    args = parser.parse_args()
    url = args.url
    file_name = args.file_name
    return url, file_name
