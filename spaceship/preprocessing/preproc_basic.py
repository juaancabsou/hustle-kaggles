def clean_categorical_columns(df, columns):
    """Standardize categorical columns:
     1. Remove additional spaces, special characters, and accents
     2. Replace spaces, dots, and hyphens with underscores
     3. Transform all categories to lowercase

    Args:
        df (DataFrame): Dataframe to transform
        columns (list): Columns to clean
    """
    for col in columns:
        df[col] = df[col].str.normalize('NFKD') \
            .str.encode('ascii', errors='ignore') \
            .str.decode('utf-8') \
            .str.replace('[\s\.\-]', '_', regex=True) \
            .str.lower()


def preprocess_dataset(dataset):
    """Preprocess a dataset:
     1. Remove useless columns (insights from the previous EDA)
     2. Standardize categorical columns
     3. Transform boolean values to int

    Args:
        dataset (DataFrame): Input dataset

    Returns:
        DataFrame: Preprocessed dataset
    """
    # Remove useless columns (insights from the previous EDA)
    cols_to_remove = ['VIP']
    dataset.drop(cols_to_remove, inplace=True, axis=1)
            
    # Standardize categorical columns
    categorical_columns = ['HomePlanet', 'Destination']
    clean_categorical_columns(dataset, categorical_columns)

    # Transform boolean values to int
    bool_columns = dataset.select_dtypes(include='bool').columns.tolist()
    dataset[bool_columns] = dataset[bool_columns].astype(int)

    return dataset

