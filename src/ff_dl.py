import sys
import argparse
import requests
import csv

from bs4 import BeautifulSoup

def create_csv_file(player_info):
    with open('/home/justin/ff_tiers/data/rankings.csv', 'w', newline='') as csv_file:
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

        try: # append bye week
            player_data.append(player_td_elements[4].contents[0])
        except:
            player_data.append('')

        player_data.append(player_td_elements[5].contents[0]) # append best rank
        player_data.append(player_td_elements[6].contents[0]) # append worst rank
        player_data.append(player_td_elements[7].contents[0]) # append avg rank
        player_data.append(player_td_elements[8].contents[0]) # append std of ranks 

        try: # append ADP
            player_data.append(player_td_elements[9].contents[0])
        except:
            player_data.append('')

        try: # append .vs ADP 
            player_data.append(player_td_elements[10].contents[0])
        except:
            player_data.append('')

        players.append(player_data)
    return players
    
def download_rankings(url, file_name, user_info):
    resp = requests.get(url, auth=(user_info['username'], user_info['password']))
    output = open(file_name, 'wb')
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

def main():
    ffp_url, file_name = get_url()
    #ffp_url = 'https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php?export=xls'
    #file_name = '~/ff_tiers/data/rankings.html'
    user_info = {'username':'schujustin', 'password':'justin1', 'token':'1'}
    download_rankings(ffp_url, file_name, user_info)
    player_info = get_player_data(file_name)
    create_csv_file(player_info)

if __name__ == "__main__":
    main()