import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sklearn.preprocessing import OrdinalEncoder
from sklearn.cluster import KMeans
from matplotlib.colors import rgb2hex

def plot_cluster(data, labels):
    fig, ax = plt.subplots(figsize=(15,15))
    plt.ylabel('Consensus Rank')
    plt.xlabel('Average Rank')

    colors = cm.rainbow(np.linspace(0,1, len(labels)))
    for cluster_num in range(len(labels)):
        c = colors[cluster_num][:-1]
        curr_cluster = data.loc[data['cluster'] == labels[cluster_num]]
        plt.scatter(curr_cluster['average_ranking'], curr_cluster['consensus_ranking'], color=rgb2hex(c))
        plt.errorbar(curr_cluster['average_ranking'], curr_cluster['consensus_ranking'], xerr=curr_cluster['ranking_std'], linestyle='None', ecolor=rgb2hex(c))

    for i, txt in enumerate(data['player_name']):
        ax.annotate(txt, xy=(data['average_ranking'][i], data['consensus_ranking'][i]), xytext=(4,6), textcoords="offset points")
        
    plt.grid()
    plt.show()

def clustering(data, k):
    categories = ['best_ranking', 'worst_ranking', 'average_ranking']
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
    data = data[:100]
    data = handle_categorical_features(data)
    data = handle_missing_values(data)
    data['cluster'] = clustering(data, 10)
    labels = data['cluster'].unique()
    plot_cluster(data, labels)