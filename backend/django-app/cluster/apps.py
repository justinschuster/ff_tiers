import os
import pandas as pd
from django.apps import AppConfig
from joblib import load



class ClusterConfig(AppConfig):
    name = 'cluster'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
