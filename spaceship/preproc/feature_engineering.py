# 
# Scrit for creating new features (feature engineering)

def pipe_feature_engineering(df, target):
    """
    Pipeline for feature engineering
    """

    # 1. Split Cabin into Deck, Cabin_number and Cabin_letter
    cols_cabin = ['deck', 'cabin_number', 'cabin_letter']
    df[cols_cabin] = df['Cabin'].str.split('/', expand=True)
    # 2. Transform all as string
    for col in cols_cabin:
        df[col] = df[col].astype(str)

    return df
