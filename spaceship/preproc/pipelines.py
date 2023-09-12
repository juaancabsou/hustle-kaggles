# 
# Script that gathers all the preprocessing steps

from preproc.drop import pipeline_drop_cols
from preproc.feature_engineering import pipe_feature_engineering
from preproc.missing_values import pipe_missing_values
# Import libraries
from preproc.transform import pipe_transform_values


def main_pipelines(df, target, dataset_name):
    print('Preprocessing pipeline for dataset: ', dataset_name)
    print('-' * 50)
    cols_numerical_impute = ['VIP', 'CryoSleep', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']
    # First: Fill missing values
    df_missing = pipe_missing_values(df, target, cols_numerical_impute, [])
    # Second: Transform target and other values
    df_transform = pipe_transform_values(df_missing, target)
    # Third: Feature engineering
    df_engineered = pipe_feature_engineering(df_missing, target)
    # Fourth: Drop columns
    drop_cols = ['PassengerId', 'Name', 'Cabin']
    df_drop = pipeline_drop_cols(df_engineered, drop_cols)

    # Insert new line
    print('\n')
    return df_drop
