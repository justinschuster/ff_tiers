import pandas as pd 
import numpy as np

import ff_dl
import create_plot

if __name__ == '__main__':
    urls = ["consensus", "ppr", "half-point-ppr"]
    user_info = {'username':'schujustin', 'password':'justin1', 'token':'1'}
    file_names = ["standard", "ppr", "half-ppr"]
    positions = ['QB', 'RB', 'WR', 'TE', 'K']

    for i in range(0, 3):
        url = "https://www.fantasypros.com/nfl/rankings/{}-cheatsheets.php?export=xls".format(urls[i])
        file_name = "/home/schuj/ff_tiers/data/{}-rankings.html".format(file_names[i])
        ff_dl.download_rankings(url, file_name, user_info)
        player_info = ff_dl.get_player_data(file_name)
        player_df = pd.DataFrame(np.array(player_info[1:]), columns=player_info[0])        
        
        data = create_plot.handle_wrong_dtypes(player_df)
        for pos in positions:
            position_data = create_plot.get_position_data(data, pos)
            position_data = position_data[:50]
            position_data = create_plot.handle_categorical_features(position_data)
            position_data = create_plot.handle_missing_values(position_data)
            position_data['cluster'] = create_plot.clustering(position_data, 7)
            labels = position_data['cluster'].unique()
            create_plot.plot_cluster(position_data, labels, pos, file_names[i])
