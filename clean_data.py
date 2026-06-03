from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "sales_data.csv"
CLEANED_DATA_DIR = PROJECT_ROOT / "data" / "cleaned"
CLEANED_DATA_PATH = CLEANED_DATA_DIR / "cleaned_sales_data.csv"


def load_raw_data(path=RAW_DATA_PATH):
    """Load the raw CSV dataset."""
    return pd.read_csv(path)


def fill_missing_values(df):
    """Fill missing numeric values with medians and text values with modes."""
    cleaned = df.copy()

    numeric_columns = cleaned.select_dtypes(include="number").columns
    text_columns = cleaned.select_dtypes(include="object").columns

    for column in numeric_columns:
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())

    for column in text_columns:
        mode_value = cleaned[column].mode(dropna=True)
        if not mode_value.empty:
            cleaned[column] = cleaned[column].fillna(mode_value.iloc[0])

    return cleaned


def cap_outliers_iqr(df, columns):
    """Cap numeric outliers using the interquartile range method."""
    cleaned = df.copy()

    for column in columns:
        q1 = cleaned[column].quantile(0.25)
        q3 = cleaned[column].quantile(0.75)
        iqr = q3 - q1
        lower_limit = q1 - 1.5 * iqr
        upper_limit = q3 + 1.5 * iqr
        cleaned[column] = cleaned[column].clip(lower=lower_limit, upper=upper_limit)

    return cleaned


def clean_sales_data(df):
    """Run all data-cleaning steps."""
    cleaned = df.copy()
    cleaned["order_date"] = pd.to_datetime(cleaned["order_date"], errors="coerce")
    cleaned = cleaned.drop_duplicates()
    cleaned = fill_missing_values(cleaned)
    cleaned = cap_outliers_iqr(cleaned, ["quantity", "unit_price", "customer_rating"])
    cleaned["total_sales"] = cleaned["quantity"] * cleaned["unit_price"]

    return cleaned


def save_cleaned_data(df, path=CLEANED_DATA_PATH):
    CLEANED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return path


def run_cleaning_pipeline():
    raw_df = load_raw_data()
    cleaned_df = clean_sales_data(raw_df)
    output_path = save_cleaned_data(cleaned_df)

    return raw_df, cleaned_df, output_path


if __name__ == "__main__":
    _, cleaned_data, saved_path = run_cleaning_pipeline()
    print(f"Cleaned {len(cleaned_data)} rows and saved file to {saved_path}")
