import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
from main import KMeans

class CSVColumnSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Column Selector")

        # Tạo và thiết lập giao diện
        self.file_button = tk.Button(root, text="Chọn File CSV", command=self.load_csv)
        self.file_button.pack(pady=10)

        self.num_columns_label = tk.Label(root, text="Nhập số cụm:")
        self.num_columns_label.pack()

        self.num_columns_entry = tk.Entry(root)
        self.num_columns_entry.pack()

        self.column_frame = ttk.Frame(root)
        self.column_frame.pack()

        self.column_listbox = tk.Listbox(self.column_frame, selectmode=tk.MULTIPLE)
        self.column_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.column_frame, orient=tk.VERTICAL, command=self.column_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.column_listbox.config(yscrollcommand=self.scrollbar.set)

        self.show_result_button = tk.Button(root, text="Hiển thị kết quả", command=self.solve_kmeans)
        self.show_result_button.pack(pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.file_path = file_path
        if file_path:
            self.column_listbox.delete(0, tk.END)
            columns = self.get_csv_columns(file_path)
            for column in columns:
                self.column_listbox.insert(tk.END, column)

    def get_csv_columns(self, file_path):
        df = pd.read_csv(file_path)
        return df.columns.tolist()

    def solve_kmeans(self):
        selected_columns = [self.column_listbox.get(i) for i in self.column_listbox.curselection()]
        num_columns = self.get_num_columns()

        if not num_columns.isdigit() or int(num_columns) <= 0:
            messagebox.showwarning("Lưu Ý", "Nhập một số nguyên dương cho số cột.")
            return

        if selected_columns and len(selected_columns) > 1:
            kmeans = KMeans(k=int(num_columns), columns=selected_columns, file_path=self.file_path)
            kmeans.solve()
            kmeans.draw_clusters()
        else:
            messagebox.showwarning("Lưu Ý", "Chọn ít nhất 2 cột để có thể vẽ biểu đồ")

        

    def get_num_columns(self):
        # Lấy giá trị nhập vào từ ô văn bản số cột
        return self.num_columns_entry.get()

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVColumnSelector(root)
    root.mainloop()
