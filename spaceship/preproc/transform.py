# 
# Simple script for transforming the dataset


def pipe_transform_values(df, target):
    """
    Pipeline for transforming target values
    """
    # From boolean to int
    cols_bools2int = ['VIP', 'CryoSleep']
    if target != None:
        cols_bools2int.append(target)

    df[cols_bools2int] = df[cols_bools2int].astype(int)

    return df
