import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm

from sklearn.preprocessing import OrdinalEncoder
from sklearn.cluster import KMeans

def plot_cluster(data, colors, labels):
    fig, ax = plt.subplots(figsize=(15,15))
    plt.ylabel('Consensus Rank')
    plt.xlabel('Average Rank')

    for cluster_num in range(0, len(labels)):
        curr_cluster = data.loc[data['cluster'] == labels[cluster_num]]
        plt.scatter(curr_cluster['average_ranking'], curr_cluster['consensus_ranking'], c=colors[cluster_num])
        plt.errorbar(curr_cluster['average_ranking'], curr_cluster['consensus_ranking'], xerr=curr_cluster['ranking_std'], linestyle='None', ecolor=colors[cluster_num])

    for i, txt in enumerate(data['player_name']):
        ax.annotate(txt, xy=(data['average_ranking'][i], data['consensus_ranking'][i]), xytext=(4,6), textcoords="offset points")
        
    plt.grid()
    plt.show()

def get_colors(data):
    colors = []
    color_iter = iter(plt.cm.rainbow(np.linspace(0, 5, len(data['cluster'].unique()))))
    for clust in data['cluster'].unique():
        colors.append(next(color_iter))
    return colors

def clustering(data, k):
    categories = ['position', 'best_ranking', 'worst_ranking', 'ranking_std']
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
    data = data[:50]
    data = handle_categorical_features(data)
    data = handle_missing_values(data)
    data['cluster'] = clustering(data, 7)
    colors = get_colors(data)
    labels = data['cluster'].unique()
    plot_cluster(data, colors, labels)