import pandas as pd
def clean_csv(
    input_path: str,
    output_path: str,
    drop_duplicates: bool = True,
    fill_missing: bool = True):
    """
    Cleans a CSV file by removing duplicates, handling missing values,
    normalizing column names, and trimming text fields.
    """
    df = pd.read_csv(input_path)
    # Normalize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True))
    # Remove duplicate rows
    if drop_duplicates:
        df = df.drop_duplicates()
    # Handle missing values
    if fill_missing:
        for col in df.select_dtypes(include=["object"]):
            df[col] = df[col].fillna("")
        for col in df.select_dtypes(exclude=["object"]):
            df[col] = df[col].fillna(0)

    # Trim text fields
    for col in df.select_dtypes(include=["object"]):
        df[col] = df[col].str.strip()

    df.to_csv(output_path, index=False)
