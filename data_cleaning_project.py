import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("titanic.csv")

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill Age column
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Embarked column
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)

# Remove Cabin column
df.drop("Cabin", axis=1, inplace=True)

# -----------------------------
# Remove Duplicates
# -----------------------------
duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df.drop_duplicates(inplace=True)

# -----------------------------
# Outlier Removal
# -----------------------------
Q1 = df["Fare"].quantile(0.25)
Q3 = df["Fare"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - (1.5 * IQR)
upper = Q3 + (1.5 * IQR)

df = df[
    (df["Fare"] >= lower)
    & (df["Fare"] <= upper)
]

print("\nShape After Cleaning:")
print(df.shape)

# -----------------------------
# Visualization 1
# -----------------------------
plt.figure(figsize=(8,5))

sns.countplot(
    x="Survived",
    data=df
)

plt.title("Passenger Survival Count")

plt.savefig(
    "outputs/survival_count.png"
)

plt.close()

# -----------------------------
# Visualization 2
# -----------------------------
plt.figure(figsize=(8,5))

sns.histplot(
    df["Age"],
    bins=30,
    kde=True
)

plt.title("Age Distribution")

plt.savefig(
    "outputs/age_distribution.png"
)

plt.close()

# -----------------------------
# Visualization 3
# -----------------------------
plt.figure(figsize=(8,5))

sns.countplot(
    x="Sex",
    hue="Survived",
    data=df
)

plt.title("Gender vs Survival")

plt.savefig(
    "outputs/gender_survival.png"
)

plt.close()

# -----------------------------
# Visualization 4
# -----------------------------
plt.figure(figsize=(8,5))

sns.boxplot(
    y=df["Fare"]
)

plt.title("Fare Boxplot")

plt.savefig(
    "outputs/fare_boxplot.png"
)

plt.close()

# -----------------------------
# Visualization 5
# -----------------------------
numeric_df = df.select_dtypes(
    include=np.number
)

plt.figure(figsize=(10,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig(
    "outputs/heatmap.png"
)

plt.close()

# -----------------------------
# Insights
# -----------------------------
print("\nProject Completed Successfully")

print("\nInsights:")
print("1. Missing values handled")
print("2. Duplicate records removed")
print("3. Fare outliers removed")
print("4. Graphs generated")
print("5. Dataset ready for analysis")
