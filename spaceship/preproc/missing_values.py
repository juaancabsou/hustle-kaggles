# 
# Simple script for dealing and imputing missing values


def pipe_missing_values(df, target, cols_num_impute, cols_cat_impute):
    """
    Pipeline for dealing with missing values in numerical features
    """
    list_imputers = ['zero']

    # Numerical features: impute with zero
    if 'zero' in list_imputers:
        df[cols_num_impute] = df[cols_num_impute].fillna(0)

    return df
