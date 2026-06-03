from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEANED_DATA_PATH = PROJECT_ROOT / "data" / "cleaned" / "cleaned_sales_data.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"


def load_cleaned_data(path=CLEANED_DATA_PATH):
    return pd.read_csv(path, parse_dates=["order_date"])


def save_bar_chart(df):
    sales_by_category = df.groupby("category", as_index=False)["total_sales"].sum()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=sales_by_category, x="category", y="total_sales", hue="category", legend=False)
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.tight_layout()

    path = FIGURES_DIR / "sales_by_category.png"
    plt.savefig(path)
    plt.close()
    return path


def save_region_chart(df):
    sales_by_region = df.groupby("region", as_index=False)["total_sales"].sum()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=sales_by_region, x="region", y="total_sales", hue="region", legend=False)
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.tight_layout()

    path = FIGURES_DIR / "sales_by_region.png"
    plt.savefig(path)
    plt.close()
    return path


def save_price_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["unit_price"], bins=10, kde=True)
    plt.title("Unit Price Distribution")
    plt.xlabel("Unit Price")
    plt.ylabel("Count")
    plt.tight_layout()

    path = FIGURES_DIR / "unit_price_distribution.png"
    plt.savefig(path)
    plt.close()
    return path


def save_rating_chart(df):
    rating_by_category = df.groupby("category", as_index=False)["customer_rating"].mean()

    plt.figure(figsize=(8, 5))
    sns.lineplot(data=rating_by_category, x="category", y="customer_rating", marker="o")
    plt.title("Average Customer Rating by Category")
    plt.xlabel("Category")
    plt.ylabel("Average Rating")
    plt.ylim(0, 5)
    plt.tight_layout()

    path = FIGURES_DIR / "average_rating_by_category.png"
    plt.savefig(path)
    plt.close()
    return path


def create_visualizations(df):
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    return [
        save_bar_chart(df),
        save_region_chart(df),
        save_price_distribution(df),
        save_rating_chart(df),
    ]


if __name__ == "__main__":
    cleaned_df = load_cleaned_data()
    figure_paths = create_visualizations(cleaned_df)
    for figure_path in figure_paths:
        print(f"Saved {figure_path}")
