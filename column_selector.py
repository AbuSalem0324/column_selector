import pandas as pd

def select_columns(df, columns):
    """
    Select specific columns from a DataFrame and check for NaNs, missing values,
    zeros, negative numbers, and potential outliers.

    Args:
    df (pandas.DataFrame): The original DataFrame.
    columns (list): List of column names to include in the new DataFrame.

    Returns:
    pandas.DataFrame: A new DataFrame with the specified columns.
    """
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"The following columns are not in the DataFrame: {missing_cols}")

    selected_df = df[columns]

    check_data_quality(selected_df)

    return selected_df

def check_data_quality(df):
    """
    Check for NaNs, missing values, zeros, negative numbers, and potential outliers
    in a DataFrame.
    """
    for col in df.columns:
        # Check for NaNs and missing values
        if df[col].isnull().any():
            print(f"Warning: Column '{col}' contains NaN or missing values.")

        # Check for zeros
        if (df[col] == 0).any():
            print(f"Warning: Column '{col}' contains zeros.")

        # Check for negative numbers
        if (df[col] < 0).any():
            print(f"Warning: Column '{col}' contains negative values.")

        # Check for potential outliers (using IQR)
        check_outliers(df, col)

def check_outliers(df, col):
    """
    Check for potential outliers in a DataFrame column using the IQR method.
    """
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    if ((df[col] < lower_bound) | (df[col] > upper_bound)).any():
        print(f"Warning: Column '{col}' may contain potential outliers.")




