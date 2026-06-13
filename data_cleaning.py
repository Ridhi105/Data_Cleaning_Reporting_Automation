import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("netflix_titles.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Missing Value Handling
# -----------------------------
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['date_added'] = df['date_added'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')

# Fill any remaining missing values
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna("Unknown")

# -----------------------------
# Remove Duplicates
# -----------------------------
duplicates = df.duplicated().sum()
print("Duplicate Records Found:", duplicates)

df = df.drop_duplicates()

# -----------------------------
# Standardize Text Columns
# -----------------------------
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()

# -----------------------------
# Save Cleaned Dataset
# -----------------------------
df.to_csv("cleaned_data.csv", index=False)

print("Cleaned Shape:", df.shape)

# -----------------------------
# Generate Summary Report
# -----------------------------
summary = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isnull().sum().values,
    "Unique Values": [df[col].nunique() for col in df.columns]
})

summary.to_excel("report.xlsx", index=False)

# -----------------------------
# Visualization 1:
# Content Type Distribution
# -----------------------------
plt.figure(figsize=(6, 4))
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("content_distribution.png")
plt.close()

# -----------------------------
# Visualization 2:
# Top 10 Countries
# -----------------------------
country_counts = df['country'].value_counts().head(10)

plt.figure(figsize=(8, 5))
country_counts.plot(kind='bar')
plt.title("Top 10 Countries by Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_countries.png")
plt.close()

# -----------------------------
# Visualization 3:
# Release Year Trend
# -----------------------------
plt.figure(figsize=(10, 5))
df['release_year'].value_counts().sort_index().plot()
plt.title("Netflix Content Release Trend")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("release_year_trend.png")
plt.close()

# -----------------------------
# Project Statistics
# -----------------------------
print("\n----- REPORT SUMMARY -----")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
print("Missing Values Remaining:", df.isnull().sum().sum())
print("Report Saved: report.xlsx")
print("Cleaned Data Saved: cleaned_data.csv")
print("Charts Generated Successfully!")

print("\nProject Completed Successfully!")