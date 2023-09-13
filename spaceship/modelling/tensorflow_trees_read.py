# Script for gathering reading the results from tensorflow trees models
import pandas as pd
import numpy as np
import json


def tf_tree_based_models_read_result(model_name='random_forest'):
    path_results = 'C:/Users/juaan/Documents/GitHub/kaggle/kaggle_spaceship/y_forecast/'

    # Read result and predictions
    predictions = np.load(path_results + model_name + '_predictions.npy')
    result = json.load(open(path_results + model_name + '_stats.json', 'r'))
    result['predictions'] = predictions

    return result
