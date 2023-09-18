def missing_feature_meta(data, feature, preprocessed):
    """
    Print information about missing values in a specified feature before or after preprocessing.

    Parameters:
        data (pd.DataFrame): The DataFrame containing the dataset.
        feature (str): The name of the feature for which you want to report missing values.
        preprocessed (bool): Indicates whether the data is preprocessed (True) or not (False).

    Returns:
        None: This function doesn't return any values but prints information about missing values.
        
    Example:
        >>> missing_feature_meta(data, 'Age', preprocessed=False)
        Filling Age feature
        ----------------------------------------------------------------------
        Missing values in Age before preprocessing: 25
    """

    stage = 'after' if preprocessed else 'before'
    print('Filling ' + feature + ' feature')
    print('-' * 70)
    miss_before = data[feature].isnull().sum()
    print('Missing values in ' + feature + ' ' + stage + ' preprocessing: ' + str(miss_before))

    return None