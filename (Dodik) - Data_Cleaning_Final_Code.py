import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Datasets
# -------------------------------
df1 = pd.read_csv("dataset1.csv")
df2 = pd.read_csv("dataset2.csv")

# -------------------------------
# 2. Dataset1 Exploration
# -------------------------------
print("Dataset1 Info:")
print(df1.info())
print("\nDataset1 Description:")
print(df1.describe(include='all'))
print("\nDataset1 Missing Values:")
print(df1.isnull().sum())
print("\nDataset1 Duplicated Rows:")
print(df1.duplicated().sum())

# -------------------------------
# 3. Dataset2 Exploration
# -------------------------------
print("\nDataset2 Info:")
print(df2.info())
print("\nDataset2 Description:")
print(df2.describe(include='all'))
print("\nDataset2 Missing Values:")
print(df2.isnull().sum())
print("\nDataset2 Duplicated Rows:")
print(df2.duplicated().sum())

# -------------------------------
# 4. Dataset1 Cleaning
# -------------------------------
# Find duplicate rows
duplicates = df1[df1.duplicated(keep=False)]
print("\nDuplicate row indices in dataset1:", duplicates.index.tolist())

# Drop duplicates
df1_cleaned = df1.drop_duplicates()

# Drop rows with missing values
df1_cleaned = df1_cleaned.dropna()

# Save cleaned dataset1
df1_cleaned.to_csv("dataset1_cleaned.csv", index=False)

# -------------------------------
# 5. Dataset2 Cleaning
# -------------------------------
# Dataset2 is already clean
df2_cleaned = df2.copy()

# Save cleaned dataset2
df2_cleaned.to_csv("dataset2_cleaned.csv", index=False)

# -------------------------------
# 6. Visualizations
# -------------------------------
sns.set(style="whitegrid")

# 1. Distribution of bat_landing_to_food
plt.figure(figsize=(8, 5))
sns.histplot(df1["bat_landing_to_food"], bins=50, kde=True)
plt.title("Distribution of bat_landing_to_food")
plt.xlabel("Seconds")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visual_bat_landing_to_food.png")
plt.close()

# 2. Missing values per column in dataset1
missing_counts = df1.isnull().sum()
missing_counts[missing_counts > 0].plot(kind="bar", color="salmon")
plt.title("Missing Values per Column in dataset1")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("visual_missing_values.png")
plt.close()

# 3. Distribution of rat_minutes in dataset2
plt.figure(figsize=(8, 5))
sns.histplot(df2["rat_minutes"], bins=50, kde=True)
plt.title("Distribution of rat_minutes")
plt.xlabel("Minutes")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visual_rat_minutes.png")
plt.close()

# 4. Correlation between rat_arrival_number and bat_landing_number
plt.figure(figsize=(8, 5))
sns.scatterplot(x="rat_arrival_number", y="bat_landing_number", data=df2)
plt.title("Correlation: Rat Arrivals vs Bat Landings")
plt.xlabel("Rat Arrival Number")
plt.ylabel("Bat Landing Number")
plt.tight_layout()
plt.savefig("visual_rat_vs_bat.png")
plt.close()
