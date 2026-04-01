import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_jobs.csv")

# Summary statistics
print(df.describe())

# Plot volume over years
plt.plot(df['Year'], df['Volume'])
plt.title("Market Volume Over Years")
plt.xlabel("Year")
plt.ylabel("Volume")
plt.show()

# Direction count
df['Direction'].value_counts().plot(kind='bar')
plt.title("Market Direction Count")
plt.show()
