import csv
import json
import math
import random
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=3, columns=4, file_path="./datasets/iris.csv"):
        self.k = k
        self.columns = columns
        self.file_path = file_path
        self.data = self.csv_to_json(self.file_path)
        self.columns = columns
        self.k = k
        self.file_path = "./datasets/iris.csv"
        self.data = self.csv_to_json(self.file_path)

        for i in range(len(self.data)):
            for col in self.columns:
                self.data[i][col] = float(self.data[i][col])

    def init_centers(self):
        random_centers = random.sample(self.data, self.k)
        self.clusters = []
        for i in range(self.k):
            elements = [random_centers[i]]
            cluster = {
                "elements": elements,
                "center": elements[0]
            }
            self.clusters.append(cluster)

    def solve(self):
        self.init_centers()

        for i in range(self.k, len(self.data)):
            index_cluster = 0
            min_distance = 10**10
            for index in range(len(self.clusters)):
                cluster = self.clusters[index]
                center = cluster["center"]
                distance = self.calculate_distance(center, self.data[i])
                if distance < min_distance:
                    min_distance = distance
                    index_cluster = index
            self.clusters[index_cluster]["elements"].append(self.data[i])
            self.reset_center(index_cluster)

    def calculate_distance(self, a, b):
        distance = 0
        for i in self.columns:
            distance += (float(a[i]) - float(b[i])) ** 2
        return math.sqrt(distance)
    
    def reset_center(self, index_cluster):
        elements = self.clusters[index_cluster]["elements"]
        new_center = {}
        for col in self.columns:
            new_center[col] = 0
        for element in elements:
            for key in new_center.keys():
                new_center[key] += element[key]
        
        for key in new_center.keys():
            new_center[key] /= len(elements)

        self.clusters[index_cluster]["center"] = new_center
            
    def print_clusters(self):
        len_clusters = [len(cluster["elements"]) for cluster in self.clusters]
        for index, cluster in enumerate(self.clusters):
            print(f"Cluster {index + 1}: {len(cluster['elements'])} elements")
        return len_clusters

    def draw_clusters(self):
        list_color = ["green", "blue", "orange", "magenta", "black", "cyan", "purple", "yellow"]
        # vẽ K nhóm
        for index in range(len(self.clusters)):
            random_color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
            color = random_color if index >= len(list_color) else list_color[index]
            x = [x[self.columns[0]] for x in self.clusters[index]["elements"]]
            y = [y[self.columns[1]] for y in self.clusters[index]["elements"]]
            plt.scatter(x, y, color=color)

        # Vẽ K điểm center
        x = [x['center'][self.columns[0]] for x in self.clusters]
        y = [y['center'][self.columns[1]] for y in self.clusters]
        plt.scatter(x, y, color="red", marker='X', s=200)


        plt.xlabel(self.columns[0])
        plt.ylabel(self.columns[1])
        plt.title('K-Means Clustering')
        plt.show()


    def csv_to_json(self, csv_file_path):
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            json_data = [row for row in csv_reader]
        return json_data
    
if __name__ == "__main__":
    clusters = 3
    cloumns = ["SepalLengthCm", 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    iris_kmeans = KMeans(k=clusters, columns=cloumns)
    iris_kmeans.solve()
    iris_kmeans.print_clusters()
    iris_kmeans.draw_clusters()