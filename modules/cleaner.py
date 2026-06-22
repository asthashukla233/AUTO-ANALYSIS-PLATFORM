import pandas as pd

def clean_data(df):

    cleaned_df = df.copy()

    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates()

    # Numeric columns
    numeric_cols = cleaned_df.select_dtypes(
        include=["number"]
    ).columns

    for col in numeric_cols:

        median_value = cleaned_df[col].median()

        cleaned_df[col] = cleaned_df[col].fillna(
            median_value
        )

    # Categorical columns
    categorical_cols = cleaned_df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_cols:

        if cleaned_df[col].mode().shape[0] > 0:

            mode_value = cleaned_df[col].mode()[0]

            cleaned_df[col] = cleaned_df[col].fillna(
                mode_value
            )

    return cleaned_df