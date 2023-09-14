from preprocessing.aux_feature_ages import assign_age_group

def feature_engineering_it_1(df):
    """
    Perform the first iteration of feature engineering on the Titanic dataset.

    This function adds several new features to the DataFrame based on age, billing, cabin, passenger ID, and group size.

    Args:
        df (DataFrame): The input DataFrame containing Titanic passenger data.

    Returns:
        DataFrame: The DataFrame with new features added.
    """

    # Create new features related to passenger ID and group size
    df['fe_group_id'] = df['PassengerId'].apply(lambda x: int(str(x)[:4]))
    df['fe_group_size'] = df.groupby('fe_group_id')['PassengerId'].transform('count')
    df['fe_is_alone'] = df['fe_group_size'].apply(lambda x: 'alone' if x == 1 else 'not_alone')

    # Fill missing values in the 'Name' column with 'Unknown Unknown'
    df['Name'].fillna('Unknown Unknown', inplace=True)

    # Create a 'Surname' column by extracting the last word from the 'Name' column
    df['Surname'] = df['Name'].str.split().str[-1]

    return df

def feature_engineering_it_2(df):
    """
    Perform the first iteration of feature engineering on the Titanic dataset.

    This function adds several new features to the DataFrame based on age, billing, cabin, passenger ID, and group size.

    Args:
        df (DataFrame): The input DataFrame containing Titanic passenger data.

    Returns:
        DataFrame: The DataFrame with new features added.
    """

    # Create a new feature 'fe_age_group' based on age
    df['fe_age_group'] = df['Age'].apply(assign_age_group)

    # Create new features related to billing
    cols_billing = ['FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck', 'RoomService']
    df['fe_billings'] = df[cols_billing].sum(axis=1)
    df['fe_has_spent'] = df['fe_billings'].apply(lambda x: 'has_spent' if x > 0 else 'has_not_spent')

    # Create new features related to cabin
    cols_cabin = ['fe_deck', 'fe_cabin_number', 'fe_cabin_letter']
    df[cols_cabin] = df['Cabin'].str.split('/', expand=True)
    for col in cols_cabin:
        df[col] = df[col].astype(str)

    return df