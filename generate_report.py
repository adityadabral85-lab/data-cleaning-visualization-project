from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORT_PATH = REPORTS_DIR / "summary_report.md"


def build_summary(df):
    total_sales = df["total_sales"].sum()
    average_rating = df["customer_rating"].mean()
    best_category = df.groupby("category")["total_sales"].sum().idxmax()
    best_region = df.groupby("region")["total_sales"].sum().idxmax()

    return {
        "rows": len(df),
        "total_sales": total_sales,
        "average_rating": average_rating,
        "best_category": best_category,
        "best_region": best_region,
    }


def generate_report(df, figure_paths):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    summary = build_summary(df)

    figure_lines = "\n".join(
        f"- `{path.relative_to(PROJECT_ROOT)}`" for path in figure_paths
    )

    report = f"""# Sales Data Cleaning and Visualization Report

## Dataset Summary

- Rows after cleaning: {summary["rows"]}
- Total sales: {summary["total_sales"]:.2f}
- Average customer rating: {summary["average_rating"]:.2f}
- Best performing category: {summary["best_category"]}
- Best performing region: {summary["best_region"]}

## Cleaning Steps

- Converted order dates into datetime format
- Removed duplicate rows
- Filled missing numeric values with median values
- Filled missing text values with mode values
- Capped outliers using the IQR method
- Added a `total_sales` column

## Visualizations

{figure_lines}

## Key Finding

The cleaned dataset is ready for analysis, and the generated charts make it easier
to compare sales performance across categories and regions.
"""

    REPORT_PATH.write_text(report, encoding="utf-8")
    return REPORT_PATH


if __name__ == "__main__":
    cleaned_path = PROJECT_ROOT / "data" / "cleaned" / "cleaned_sales_data.csv"
    cleaned_df = pd.read_csv(cleaned_path)
    path = generate_report(cleaned_df, [])
    print(f"Report saved to {path}")
