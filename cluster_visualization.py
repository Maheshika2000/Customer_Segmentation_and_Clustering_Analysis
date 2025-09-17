# simple_customer_segmentation_viz_colored.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===============================
# 1. Load clustered data
# ===============================
segments = pd.read_csv("customer_segments.csv")

# ===============================
# 2. Number of customers per cluster
# ===============================
plt.figure(figsize=(6,4))
sns.countplot(x='Cluster', data=segments, palette=['skyblue', 'orange', 'green', 'purple', 'red'])
plt.title("Number of Customers per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Number of Customers")
plt.show()

# ===============================
# 3. Average Recency, Frequency, Monetary per cluster
# ===============================
cluster_avg = segments.groupby('Cluster')[['Recency','Frequency','Monetary']].mean().reset_index()
cluster_avg_melted = cluster_avg.melt(id_vars='Cluster', var_name='Metric', value_name='Average')

plt.figure(figsize=(8,5))
sns.barplot(x='Cluster', y='Average', hue='Metric', data=cluster_avg_melted,
            palette=['#FFA07A','#20B2AA','#9370DB'])  # visible pastel colors
plt.title("Average Customer Metrics per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Average Value")
plt.legend(title='Metric')
plt.show()

# ===============================
# 4. Average Basket Size & Order Value per cluster
# ===============================
if 'AvgBasketSize' in segments.columns and 'AvgOrderValue' in segments.columns:
    cluster_avg_extra = segments.groupby('Cluster')[['AvgBasketSize','AvgOrderValue']].mean().reset_index()
    cluster_avg_extra_melted = cluster_avg_extra.melt(id_vars='Cluster', var_name='Metric', value_name='Average')

    plt.figure(figsize=(8,5))
    sns.barplot(x='Cluster', y='Average', hue='Metric', data=cluster_avg_extra_melted,
                palette=['#FF6347','#3CB371'])  # visible colors
    plt.title("Average Basket Size & Order Value per Cluster")
    plt.xlabel("Cluster")
    plt.ylabel("Average Value")
    plt.legend(title='Metric')
    plt.show()

