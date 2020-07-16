import requests

from bs4 import BeautifulSoup

def get_player_data(file_name):
    players = []
    column_headings = [
            'consensus_ranking', 'player_name', 'team_name_abbrev', 'position', 
            'bye_week', 'best_ranking', 'worst_ranking', 'average_ranking', 
            'ranking_std', 'ADP', 'vs_ADP'
    ]

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
    resp = requests.get(url,
                        auth=(user_info['username'], user_info['password'])) 
    output = open(file_name, 'w+b')
    output.write(resp.content)
    output.close()
