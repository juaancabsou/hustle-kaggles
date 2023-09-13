import pandas as pd

def basic_eda_dataset(df, name):
    """
    Perform basic exploratory data analysis (EDA) on a DataFrame and display summary information.

    Args:
        df (DataFrame): The DataFrame to analyze.
        name (str): A name or label for the DataFrame.

    Returns:
        None
    """
    # Display the shape of the DataFrame
    print(f'{name} shape: {df.shape}')
    print('-' * 50)
    
    # Display information about the DataFrame
    print(f'{name} info:')
    df_info = df.info()
    print('-' * 50)
    
    # Count missing values per column as a percentage alongside the total number of missing values
    print(f'{name} missing values:')
    
    missing_values_percentage = (df.isnull().mean() * 100).round(1)
    missing_values = df.isnull().sum()
    
    # Create a summary DataFrame for missing values
    missing_values_summary = pd.DataFrame({
        'missing_values_percentage': missing_values_percentage,
        'missing_values_count': missing_values
    })
    display(missing_values_summary)
    
    print(f'{name} describe:')
    df_description = df.describe()
    print(df_description)
    print('-' * 50)
    
    # Display the first few rows of the DataFrame
    display(df.head(2))

    return None
