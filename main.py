import csv
import json

class HeartKNN:
    def __init__(self, k=3):
        self.k = k
        self.file_path = "./datasets/heart_attack_prediction_dataset.csv"
        self.data = self.csv_to_json(self.file_path)
        print(len(self.data))

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def csv_to_json(self, csv_file_path):
        # Mở file CSV để đọc
        with open(csv_file_path, mode='r') as csv_file:
            # Sử dụng DictReader để đọc dữ liệu từ file CSV
            csv_reader = csv.DictReader(csv_file)
            # Chuyển đổi dữ liệu thành mảng JSON
            json_data = [row for row in csv_reader]
        return json_data
    
if __name__ == "__main__":
    heart = HeartKNN(3)