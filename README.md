# Data Cleaning and Visualization Project

A beginner-friendly Python project for cleaning a raw dataset, handling missing values and outliers, and creating visual reports with Pandas, Matplotlib, and Seaborn.

## Features

- Load a raw CSV dataset
- Detect and handle missing values
- Remove duplicate rows
- Treat outliers using the IQR method
- Create cleaned CSV output
- Generate visualizations
- Build a simple summary report

## Project Structure

```text
data-cleaning-visualization-project/
  data/
    raw/
      sales_data.csv
    cleaned/
  reports/
    figures/
  src/
    clean_data.py
    visualize_data.py
    generate_report.py
    main.py
  requirements.txt
  README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS/Linux, activate the virtual environment with:

```bash
source .venv/bin/activate
```

## Run the Project

```bash
python src/main.py
```

After running, check:

- `data/cleaned/cleaned_sales_data.csv`
- `reports/summary_report.md`
- `reports/figures/`

## Dataset

The included sample dataset represents sales records with missing values, duplicate rows, and outliers. You can replace `data/raw/sales_data.csv` with your own dataset and update the column names in the scripts if needed.

## How to Push to GitHub

```bash
git init
git add .
git commit -m "Add data cleaning and visualization project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub details.
