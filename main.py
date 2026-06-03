from clean_data import run_cleaning_pipeline
from generate_report import generate_report
from visualize_data import create_visualizations


def main():
    raw_df, cleaned_df, cleaned_path = run_cleaning_pipeline()
    figure_paths = create_visualizations(cleaned_df)
    report_path = generate_report(cleaned_df, figure_paths)

    print("Data cleaning and visualization complete.")
    print(f"Raw rows: {len(raw_df)}")
    print(f"Cleaned rows: {len(cleaned_df)}")
    print(f"Cleaned data: {cleaned_path}")
    print(f"Report: {report_path}")
    print("Figures:")
    for figure_path in figure_paths:
        print(f"- {figure_path}")


if __name__ == "__main__":
    main()
