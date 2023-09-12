# Simple script for analyzing the dataset and fetching some basic information about it

import pandas as pd


def basic_eda_dataset(df, name):
    print('{} shape is: {}'.format(name, df.shape))
    print('-' * 50)
    print('{} info:'.format(name))
    print(df.info())
    print('-' * 50)
    # Count missing values per column as a percentage alongside the total number of missing values
    print('{} missing values:'.format(name))

    cols_analysed = []
    missing_values = []
    missing_values_percentage = []

    for col in df.columns:
        cols_analysed.append(col)
        missing_values.append(df[col].isnull().sum())
        missing_values_percentage.append((str(round(df[col].isnull().sum() / len(df[col]) * 100, 1)) + "%"))

    # Create a dataframe with 3 rows where:
    # Dataframe columns are the values inside cols_analysed
    # First row: missing_values, indicate in the index the meaning of the values
    # Second row: missing_values_percentage, indicate in the index the meaning of the values

    df_missing_values = pd.DataFrame([missing_values_percentage, missing_values], columns=cols_analysed,
                                     index=['missing_values_percentage', 'missing_values'])
    display(df_missing_values)

    print('{} describe:'.format(name))
    print(df.describe())
    print('-' * 50)
    display(df.head(2))

    return None
