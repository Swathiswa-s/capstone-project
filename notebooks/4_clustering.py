import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("../data/cleaned_jobs.csv")

X = df[['Lag1', 'Lag2']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

print(df.head())
