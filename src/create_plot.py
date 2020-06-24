import pandas as pd
import numpy as np
import matplotlib as plt

from sklearn.preprocessing import OrdinalEncoder

def handle_missing_values(data):
    data['bye_week'].fillna(method='ffill')
    data['vs ADP'].fillna(method='ffill')
    data['ADP'].fillna(method='ffill', inplace=True)

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
    y = data['average_ranking']
    X = data.drop(['average_ranking'], axis=1)
    X = handle_categorical_features(X)
    X = handle_missing_values(X)