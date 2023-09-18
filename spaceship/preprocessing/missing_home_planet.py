import pandas as pd
from lib_eda.preproc_missing_values import missing_feature_meta

def missing_values_homeplanet(data):
    """
    Perform missing value analysis and filling for the 'HomePlanet' column in the input DataFrame.

    Args:
        data (pd.DataFrame): The input DataFrame containing 'HomePlanet' column.

    Returns:
        pd.DataFrame: A DataFrame with the missing values in the 'HomePlanet' column filled.
    """
    missing_feature_meta(data, 'HomePlanet', preprocessed=False)
    eda_joint_homeplanet_groupid(data) 
    eda_joint_homeplanet_cabindeck(data)

    data = fill_joint_homeplanet_groupid(data)
    data = fill_joint_homeplanet_cabindeck(data)

    missing_feature_meta(data, 'HomePlanet', preprocessed=True)

    return data

# EDA - Joints
# --------------------------
def eda_joint_homeplanet_groupid(data):
    """
    Perform exploratory data analysis on the relationship between 'HomePlanet' and 'GroupID'.

    Args:
        data (pd.DataFrame): The input DataFrame containing 'HomePlanet' and 'fe_group_id' columns.

    Returns:
        None
    """
    print('++EDA JOINT: HomePlanet <> GroupID')
    group_home_counts = data.groupby(['fe_group_id', 'HomePlanet'])['HomePlanet'].nunique().unstack(fill_value=0)
    min_count, max_count = group_home_counts.sum(axis=1).agg(['min', 'max'])
    
    print('Min planets per group:', min_count)
    print('Max planets per group:', max_count)
    print('Conclusion: Everyone in the same group has the same HomePlanet!')
    print('\n')
    return None

def eda_joint_homeplanet_cabindeck(data):
    """
    Perform exploratory data analysis on the relationship between 'HomePlanet' and 'fe_cabin_deck'.

    Args:
        data (pd.DataFrame): The input DataFrame containing 'HomePlanet' and 'fe_cabin_deck' columns.

    Returns:
        None
    """
    print('++EDA JOINT: HomePlanet <> GroupID')
    rel_deck_home = data.groupby(['fe_cabin_deck', 'HomePlanet'])['HomePlanet'].nunique().unstack().fillna(0)
    
    display(rel_deck_home)
    print('Conclusions: ')
    print('-All passengers from Deck A-B-C-T have as HomePlanet Europa')
    print('-All passengers from G have as a HomePlanet Earth')
    print('-All passengers from Deck D-E-F came from multiple planets')
    print('\n')
    return None

# Filling data
# --------------------------
    
def fill_joint_homeplanet_groupid(data):
    """
    Fill missing values in the 'HomePlanet' column of a DataFrame by matching 'fe_group_id' values.

    Parameters:
        data (pd.DataFrame): The input DataFrame containing 'fe_group_id' and 'HomePlanet' columns.

    Returns:
        pd.DataFrame: A DataFrame with missing values in the 'HomePlanet' column filled using
        non-null values from the same 'fe_group_id' and 'HomePlanet' pairs, if available.
        'HomePlanet' values are updated accordingly, and any intermediate columns are removed.
    """
    df_filtered = data.dropna(subset=['fe_group_id', 'HomePlanet'], how='any')[['fe_group_id', 'HomePlanet']].copy()
    data = data.merge(df_filtered, on='fe_group_id', how='left', suffixes=('', '_y'))
    data['HomePlanet'] = data['HomePlanet'].combine_first(data['HomePlanet_y'])
    data.drop(['HomePlanet_y'], axis=1, inplace=True)
    return data

def fill_joint_homeplanet_cabindeck(data):
    """
    Fill missing values in the 'HomePlanet' column based on the 'fe_cabin_deck' column.

    Args:
        data (pd.DataFrame): The DataFrame containing the data with 'HomePlanet' and 'fe_cabin_deck' columns.

    Returns:
        pd.DataFrame: The input DataFrame with missing values in the 'HomePlanet' column filled.
    """
    def missing_fill_homeplanet_cabindeck(row):
        home_planet = row['HomePlanet']
        cabin_deck = row['fe_cabin_deck']
        if pd.isnull(home_planet):
            if cabin_deck in ['A', 'B', 'C', 'T']:
                return 'europa'
            elif cabin_deck == 'G':
                return 'earth'
        return home_planet

    data['HomePlanet'] = data.apply(missing_fill_homeplanet_cabindeck, axis=1)

    return data
