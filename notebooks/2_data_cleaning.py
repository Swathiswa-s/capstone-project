import pandas as pd

df = pd.read_csv("../data/raw_jobs.csv")

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Convert target column
df['Direction'] = df['Direction'].map({'Up': 1, 'Down': 0})

print(df.head())

# Save cleaned data
df.to_csv("../data/cleaned_jobs.csv", index=False)
