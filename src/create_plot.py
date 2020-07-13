import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import argparse
import itertools

from sklearn.preprocessing import OrdinalEncoder
from sklearn.cluster import KMeans
from matplotlib.colors import rgb2hex
from matplotlib import style 
from sys import exit
from sklearn.metrics import silhouette_score

def mkdir_p(mypath):
    '''Creates a directory. equivalent to using mkdir -p on the command line'''

    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise

def get_position_data(data, pos):
    try:
        return data.loc[data['position'] == pos].reset_index(drop=True)
    except KeyError:
        print('Could not find: ' + pos)
        exit()

def plot_cluster(data, labels, pos, scoring_sys):
    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(25,25))
    plt.ylabel('Consensus Rank')
    plt.xlabel('Average Rank')
    plt.title('Pre-Draft - {} - Tiers - {}'.format(pos, scoring_sys))
    plt.gca().invert_yaxis()
    ax.grid(b=True, which='major', color='white', linestyle='-')

    #colors = cm.rainbow(np.linspace(0,1, len(labels)))
    colors = itertools.cycle(['r','g','b', 'magenta', 'sienna', 'c', 'k'])
    for cluster_num in range(len(labels)):
        c = next(colors)
        curr_cluster = data.loc[data['cluster'] == labels[cluster_num]]
        plt.errorbar(curr_cluster['average_ranking'], curr_cluster.index.values, xerr=curr_cluster['ranking_std'], zorder=2,linestyle='None', ecolor=c)
        plt.scatter(curr_cluster['average_ranking'], curr_cluster.index.values, color='black', zorder=2)
    
    for i, txt in enumerate(data['player_name']):
        ax.annotate(txt, xy=(data['average_ranking'][i], data.index.values[i]), xytext=(4,6), textcoords="offset points")
    
    output_dir = '../plots'
    mkdir_p(output_dir)   
    plt.savefig('{}/{}_{}.png'.format(output_dir, pos, scoring_sys))

def clustering(data, k):
    categories = ['best_ranking', 'worst_ranking', 'average_ranking', 'consensus_ranking']
    data = data[categories]
    kmeans = KMeans(n_clusters=k)
    y_pred = kmeans.fit_predict(data)
    return y_pred

def handle_missing_values(data):
    missing_value_categories = ['bye_week', 'vs ADP', 'ADP']
    for cat in missing_value_categories:
        data[cat].fillna(method='ffill')
    return data

def handle_categorical_features(data):
    position_cat = data[['position']]
    ordinal_encoder = OrdinalEncoder()
    position_encode = ordinal_encoder.fit_transform(position_cat)
    data['position'] = position_encode
    return data

def get_data(scoring_sys):
    df = pd.read_csv('~/ff_tiers/data/{}-rankings.csv'.format(scoring_sys))
    return df

if __name__ == '__main__':
    positions = ['QB', 'RB', 'WR', 'TE', 'K']
    file_names = ["standard", "ppr", "half-ppr"]

    for scoring_sys in file_names:
        data = get_data(scoring_sys)
        for pos in positions:
            position_data = get_position_data(data, pos)
            position_data = position_data[:50]
            position_data = handle_categorical_features(position_data)
            position_data = handle_missing_values(position_data)
            position_data['cluster'] = clustering(position_data, 7)
            labels = position_data['cluster'].unique()
            plot_cluster(position_data, labels, pos, scoring_sys) 
