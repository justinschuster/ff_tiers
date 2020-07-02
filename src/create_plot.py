import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

from sklearn.preprocessing import OrdinalEncoder
from sklearn.cluster import KMeans
from matplotlib.colors import rgb2hex
from matplotlib import style 

def select_position(data, pos):
    try:
        return data.loc[data['position'] == pos].reset_index(drop=True)
    except KeyError:
        print('Could not find: ' + pos)
        sys.exit()

def plot_cluster(data, labels):
    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(15,25))
    plt.ylabel('Consensus Rank')
    plt.xlabel('Average Rank')
    plt.title('Pre-Draft - Overall Tiers')
    plt.gca().invert_yaxis()

    colors = cm.rainbow(np.linspace(0,1, len(labels)))
    for cluster_num in range(len(labels)):
        c = colors[cluster_num][:-1]
        curr_cluster = data.loc[data['cluster'] == labels[cluster_num]]
        plt.errorbar(curr_cluster['average_ranking'], curr_cluster.index.values, xerr=curr_cluster['ranking_std'], zorder=2,linestyle='None', ecolor=rgb2hex(c))
        plt.scatter(curr_cluster['average_ranking'], curr_cluster.index.values, color='black', zorder=2)
    
    for i, txt in enumerate(data['player_name']):
        ax.annotate(txt, xy=(data['average_ranking'][i], data.index.values[i]), xytext=(4,6), textcoords="offset points")

    ax.grid(b=True, which='major', color='white', linestyle='-')
    plt.show()  

def clustering(data, k):
    categories = ['best_ranking', 'worst_ranking', 'average_ranking', 'consensus_ranking']
    data = data[categories]
    kmeans = KMeans(n_clusters=k)
    y_pred = kmeans.fit_predict(data)
    return y_pred

def handle_missing_values(data):
    data['bye_week'].fillna(method='ffill')
    data['vs ADP'].fillna(method='ffill')
    data['ADP'].fillna(method='ffill', inplace=True)
    return data

def handle_categorical_features(data):
    position_cat = data[['position']]
    ordinal_encoder = OrdinalEncoder()
    position_encode = ordinal_encoder.fit_transform(position_cat)
    data['position'] = position_encode
    return data

def get_data():
    df = pd.read_csv('../data/rankings.csv')
    return df

if __name__ == '__main__':
    data = get_data()
    data = select_position(data, 'WR') 
    data = data[:30]
    data = handle_categorical_features(data)
    data = handle_missing_values(data)
    data['cluster'] = clustering(data, 5)
    labels = data['cluster'].unique()
    plot_cluster(data, labels)
