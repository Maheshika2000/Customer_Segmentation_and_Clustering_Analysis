# cluster_profiling.py

import pandas as pd

# ===============================
# 1. Load clustered data
# ===============================
segments = pd.read_csv("customer_segments.csv")

# ===============================
# 2. Basic overview
# ===============================
print("\nNumber of customers per cluster:")
print(segments["Cluster"].value_counts())

# ===============================
# 3. Cluster statistics
# ===============================
cluster_summary = segments.groupby("Cluster").agg({
    "Recency": ["mean", "median"],
    "Frequency": ["mean", "median"],
    "Monetary": ["mean", "median"],
    "AvgBasketSize": ["mean", "median"],
    "AvgOrderValue": ["mean", "median"]
}).round(2)

print("\nCluster summary statistics:")
print(cluster_summary)

# ===============================
# 4. Country distribution per cluster
# ===============================
# Find country columns (one-hot encoded)
country_cols = [col for col in segments.columns if col.startswith("Country_")]

# Count top 3 countries per cluster
for cluster in segments["Cluster"].unique():
    print(f"\nTop countries in Cluster {cluster}:")
    cluster_data = segments[segments["Cluster"] == cluster]
    country_means = cluster_data[country_cols].mean().sort_values(ascending=False).head(3)
    print(country_means)

# ===============================
# 5. Save profiling results
# ===============================
cluster_summary.to_csv("cluster_profile_summary.csv")
print("\n✅ Cluster profiling complete! Summary saved in 'cluster_profile_summary.csv'")
