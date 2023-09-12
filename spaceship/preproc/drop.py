# 
# Simple script for dropping columns not needed for the model

def pipeline_drop_cols(df, drop_cols):
    """
    Pipeline for dropping columns
    """

    for col in drop_cols:
        if col in df.columns:
            print('Dropping column: {}'.format(col))
            df = df.drop(col, axis=1)
        else:
            print('Column {} not found'.format(col))

    return df
