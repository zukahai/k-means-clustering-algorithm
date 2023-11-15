# Import các thư viện cần thiết
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

# Tải tập dữ liệu Iris
iris = datasets.load_iris()
X = iris.data  # Lấy các đặc trưng của mỗi mẫu

print(X)

# Sử dụng K-Means với số cụm (clusters) là 3 (do có 3 loài hoa Iris)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Lấy nhãn của từng điểm dữ liệu và tâm của các cụm
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Vẽ đồ thị phân cụm
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker='X', s=200, color='red')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('K-Means Clustering of Iris Dataset')
plt.show()
