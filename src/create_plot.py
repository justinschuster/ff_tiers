"""Provides methods for clustering and plotting consensus ranking data.

Provides methods for: handling missing values, encoding categorical features,
expliciting defining data types, sorting data by position, clustering data
into tiers and for creating a scatter plot fo these tiers.
"""

import sys
import itertools
from errno import EEXIST
from os import makedirs, path

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import style
from sklearn.preprocessing import OrdinalEncoder
from sklearn.cluster import KMeans

def mkdir_p(mypath):
    '''Creates a directory. Equivalent to using mkdir -p on the command line'''

    try:
        makedirs(mypath)
    except OSError as exc:
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else:
            raise


def get_position_data(data, pos):
    """Returns data only for the specified position"""

    try:
        return data.loc[data['position'] == pos].reset_index(drop=True)
    except KeyError:
        print('Could not find: ' + pos)
        sys.exit()


def plot_cluster(data, labels, pos, scoring_sys):
    """Creates a scatter plot of the clustered data. """

    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(25, 25))
    plt.ylabel('Consensus Rank')
    plt.xlabel('Average Rank')
    plt.title('Pre-Draft - {} - Tiers - {}'.format(pos, scoring_sys))
    plt.gca().invert_yaxis()
    ax.grid(b=True, which='major', color='white', linestyle='-')

    colors = itertools.cycle(['r', 'g', 'b', 'magenta', 'sienna', 'c', 'k'])
    data['tier'] = [0] * len(data['cluster'])
    tier = 1
    for cluster_num in range(len(labels)):
        curr_color = next(colors)
        curr_cluster = data.loc[data['cluster'] == labels[cluster_num]]
        data.loc[data['cluster'] == labels[cluster_num], 'tier'] = tier
        plt.errorbar(curr_cluster['average_ranking'],
                     curr_cluster.index.values,
                     xerr=curr_cluster['ranking_std'],
                     zorder=2,
                     linestyle='None',
                     ecolor=curr_color)
        plt.scatter(curr_cluster['average_ranking'],
                    curr_cluster.index.values,
                    color=curr_color,
                    zorder=2,
                    label='Tier {}'.format(tier))
        tier += 1

    for i, txt in enumerate(data['player_name']):
        ax.annotate(txt,
                    xy=(data['average_ranking'][i], data.index.values[i]),
                    xytext=(4, 6),
                    textcoords="offset points")

    plt.legend(facecolor='white', markerscale=1.5, fontsize='x-large')
    output_dir = '../plots'
    mkdir_p(output_dir)
    plt.savefig('{}/{}_{}.png'.format(output_dir, pos, scoring_sys))


def clustering(data, k):
    """Clusters data using KMeans algorithm then returns labels."""

    categories = [
        'best_ranking', 'worst_ranking', 'average_ranking', 'consensus_ranking'
    ]
    data = data[categories]
    kmeans = KMeans(n_clusters=k)
    y_pred = kmeans.fit_predict(data)
    return y_pred


def handle_missing_values(data):
    """Handles missing values found in bye_week, vs_ADP and ADP categories."""

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
    """Explicitly defines the data types for numerical categories."""

    numeric_categories = [
        'consensus_ranking', 'bye_week', 'best_ranking', 'worst_ranking',
        'average_ranking', 'ranking_std', 'ADP', 'vs_ADP'
    ]
    for cat in numeric_categories:
        data[cat] = pd.to_numeric(data[cat], errors='coerce')
    return data
