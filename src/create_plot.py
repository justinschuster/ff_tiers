import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
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
    except OSError as exc:
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

    colors = itertools.cycle(['r','g','b', 'magenta', 'sienna', 'c', 'k'])
    data['tier'] = [0]*len(data['cluster'])
    tier = 1
    for cluster_num in range(len(labels)):
        c = next(colors)
        curr_cluster = data.loc[data['cluster'] == labels[cluster_num]]
        data.loc[data['cluster'] == labels[cluster_num], 'tier'] = tier
        plt.errorbar(curr_cluster['average_ranking'], curr_cluster.index.values, xerr=curr_cluster['ranking_std'], zorder=2,linestyle='None', ecolor=c)
        plt.scatter(curr_cluster['average_ranking'], curr_cluster.index.values, color=c, zorder=2, label='Tier {}'.format(tier))
        tier += 1
    
    for i, txt in enumerate(data['player_name']):
        ax.annotate(txt, xy=(data['average_ranking'][i], data.index.values[i]), xytext=(4,6), textcoords="offset points")

    plt.legend(facecolor='white', markerscale=1.5, fontsize='x-large')
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
    missing_value_categories = ['bye_week', 'vs_ADP', 'ADP']
    for cat in missing_value_categories:
        data[cat].fillna(method='ffill')
    return data

def handle_categorical_features(data):
    position_cat = data[['position']]
    ordinal_encoder = OrdinalEncoder()
    position_encode = ordinal_encoder.fit_transform(position_cat)
    data['position'] = position_encode
    return data

def handle_wrong_dtypes(data):
    numeric_categories = ['consensus_ranking', 'bye_week', 'best_ranking', 
            'worst_ranking', 'average_ranking', 'ranking_std', 'ADP', 'vs_ADP']
    for cat in numeric_categories:
        data[cat] = pd.to_numeric(data[cat], errors='coerce')
    return data 

