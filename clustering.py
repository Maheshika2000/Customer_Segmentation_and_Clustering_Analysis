# clustering.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt


# 1. Load engineered features
features = pd.read_csv("Customer_Features_Extended.csv")


# Drop CustomerID (it's an identifier, not a feature for clustering)
X = features.drop(columns=["CustomerID"])


# 2. Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



# 3. Find optimal number of clusters
inertia = []   # measure of compactness of clusters
silhouette_scores = []  # measure of how well-separated clusters are
K_range = range(2, 11)  # test cluster numbers from 2 to 10



for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))


# Plot Elbow Method
plt.plot(K_range, inertia, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal k")
plt.show()


# Plot Silhouette Scores
plt.plot(K_range, silhouette_scores, marker="o", color="orange")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Scores for k")
plt.show()


# 4. Choose final number of clusters
# (For example, let's assume k=4 after analyzing plots)
best_k = K_range[silhouette_scores.index(max(silhouette_scores))]
print(f"✅ Best k based on silhouette score: {best_k}")


#5. Final clustering
kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
features["Cluster"] = kmeans.fit_predict(X_scaled)


# 5. Save results
features.to_csv("customer_segments.csv", index=False)
print("✅ Clustering complete! Segments saved in 'customer_segments.csv'")
print(features.head())
