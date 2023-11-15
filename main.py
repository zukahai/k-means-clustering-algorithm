import csv
import json
import math
import random
import matplotlib.pyplot as plt

class HeartKNN:
    def __init__(self, k=3):
        self.k = k
        self.file_path = "./datasets/iris.csv"
        self.data = self.csv_to_json(self.file_path)

        for i in range(len(self.data)):
            self.data[i]["SepalLengthCm"] = float(self.data[i]["SepalLengthCm"])
            self.data[i]["SepalWidthCm"] = float(self.data[i]["SepalWidthCm"])
            self.data[i]["PetalLengthCm"] = float(self.data[i]["PetalLengthCm"])
            self.data[i]["PetalWidthCm"] = float(self.data[i]["PetalWidthCm"])


        random_centers = random.sample(self.data, self.k)

        self.clusters = []
        for i in range(self.k):
            elements = [random_centers[i]]
            self.clusters.append({
                "elements": elements,
                "center": {
                    "SepalLengthCm": self.data[i]["SepalLengthCm"],
                    "SepalWidthCm": self.data[i]["SepalWidthCm"],
                    "PetalLengthCm": self.data[i]["PetalLengthCm"],
                    "PetalWidthCm": self.data[i]["PetalWidthCm"]
                }
            })

    def calculate_distance(self, a, b):
        distance = 0
        for i in a.keys():
            distance += (float(a[i]) - float(b[i])) ** 2
        return math.sqrt(distance)
    
    def solve(self):
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

    def reset_center(self, index_cluster):
        elements = self.clusters[index_cluster]["elements"]
        new_center = {
            "SepalLengthCm": 0,
            "SepalWidthCm": 0,
            "PetalLengthCm": 0,
            "PetalWidthCm": 0
        }
        for element in elements:
            for key in new_center.keys():
                new_center[key] += element[key]
        
        for key in new_center.keys():
            new_center[key] /= len(elements)

        self.clusters[index_cluster]["center"] = new_center
            
    def print_clusters(self):
        for cluster in self.clusters:
            print(len(cluster["elements"]))

    def draw_clusters(self):
        list_color = ["green", "blue", "orange", "magenta", "black", "cyan", "purple", "yellow"]
        # vẽ K nhóm
        for index in range(len(self.clusters)):
            random_color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
            color = random_color if index >= len(list_color) else list_color[index]
            x = [x['SepalLengthCm'] for x in self.clusters[index]["elements"]]
            y = [y['SepalWidthCm'] for y in self.clusters[index]["elements"]]
            plt.scatter(x, y, color=color)

        # Vẽ K điểm center
        x = [x['center']['SepalLengthCm'] for x in self.clusters]
        y = [y['center']['SepalWidthCm'] for y in self.clusters]
        plt.scatter(x, y, color="red", marker='X', s=200)


        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Sepal Width (cm)')
        plt.title('K-Means Clustering of Iris Dataset')
        plt.show()


    def csv_to_json(self, csv_file_path):
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            json_data = [row for row in csv_reader]
        return json_data
    
if __name__ == "__main__":
    clusters = 3
    heart = HeartKNN(k=clusters)
    heart.solve()
    heart.print_clusters()
    heart.draw_clusters()