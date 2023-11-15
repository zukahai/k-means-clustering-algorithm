import csv
import random
import numpy as np

class HeartKNN:
    def __init__(self, k=3):
        self.k = k
        self.file_path = "./datasets/iris.csv"
        self.data = self.csv_to_json(self.file_path)

        self.initialize_clusters()

    def initialize_clusters(self):
        # Chọn ngẫu nhiên k điểm từ dữ liệu
        random_centers = random.sample(self.data, self.k)

        self.clusters = []
        for center in random_centers:
            self.clusters.append({
                "elements": [center],
                "center": {key: float(center[key]) for key in center.keys()}
            })

    def calculate_distance(self, a, b):
        a_values = np.array(list(a.values()), dtype=float)
        b_values = np.array(list(b.values()), dtype=float)
        return np.linalg.norm(a_values - b_values)

    def solve(self):
        while True:
            old_centers = [cluster["center"].copy() for cluster in self.clusters]

            for point in self.data:
                distances = [self.calculate_distance(point, cluster["center"]) for cluster in self.clusters]
                index_cluster = np.argmin(distances)
                self.clusters[index_cluster]["elements"].append(point)

            for index, cluster in enumerate(self.clusters):
                elements = np.array(cluster["elements"])
                new_center = np.mean(elements, axis=0)
                self.clusters[index]["center"] = {key: float(value) for key, value in zip(point.keys(), new_center)}

            if np.all([np.allclose(old_center.values(), cluster["center"].values(), atol=1e-4) for old_center, cluster in zip(old_centers, self.clusters)]):
                break

    def print_clusters(self):
        for index, cluster in enumerate(self.clusters):
            print(f"Cluster {index + 1}: {len(cluster['elements'])} elements")

    def csv_to_json(self, csv_file_path):
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            json_data = [row for row in csv_reader]
        return json_data
    
if __name__ == "__main__":
    heart = HeartKNN(3)
    heart.solve()
    heart.print_clusters()
