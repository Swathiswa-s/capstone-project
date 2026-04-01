import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/Smarket.csv"
df = pd.read_csv(url)

print(df.head())

# Save raw data
df.to_csv("../data/raw_jobs.csv", index=False)
