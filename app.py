import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
from main import KMeans
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("K-Means Clustering Algorithm")
        self.root.geometry("300x350")
        self.root.resizable(False, False)
        self.root.config(bg="#343541")  # Set the background color to black
        self.file_path = None

        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - 300) // 2
        y_position = (screen_height - 350) // 2
        self.root.geometry(f"300x350+{x_position}+{y_position}")

        button_font = ("Arial", 12)
        button_bg_color = "#776B5D"
        button_fg_color = "#F3EEEA"

        select_icon = Image.open("./assets/images/csv_icon.png")
        select_icon = select_icon.resize((32, 32), Image.LANCZOS)
        select_icon = ImageTk.PhotoImage(select_icon)

        result_icon = Image.open("./assets/images/result.png")
        result_icon = result_icon.resize((32, 32), Image.LANCZOS)
        result_icon = ImageTk.PhotoImage(result_icon)

        # Tạo và thiết lập giao diện
        self.file_button = tk.Button(root, text="Chọn File CSV", command=self.load_csv, image=select_icon, compound="left", font=button_font, bg=button_bg_color, fg=button_fg_color)
        self.file_button.image = select_icon
        self.file_button.pack(pady=10)

        self.num_columns_label = tk.Label(root, text="Nhập số cụm:")
        self.num_columns_label.config(font=("Arial", 12), bg="#343541", fg="#FFFFFF")  # Set the background color to black and text color to white
        self.num_columns_label.pack()

        self.num_columns_entry = tk.Entry(root)
        num_columns_entry_font = ("Arial", 12)
        self.num_columns_entry.config(font=num_columns_entry_font)
        # giá trị mặc định là 3
        self.num_columns_entry.insert(0, "3")
        self.num_columns_entry.pack()

        self.column_frame = ttk.Frame(root)
        self.column_frame.pack()

        # Use a Label widget as a workaround for setting the background color
        frame_bg_label = tk.Label(self.column_frame, bg="#343541")
        frame_bg_label.pack(fill=tk.BOTH, expand=True)

        self.column_listbox = tk.Listbox(frame_bg_label, selectmode=tk.MULTIPLE, font=('Arial', 10), width=35, bg="#F3EEEA")  # Adjust the font size and width here, set the background color
        self.column_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(frame_bg_label, orient=tk.VERTICAL, command=self.column_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.column_listbox.config(yscrollcommand=self.scrollbar.set)

        self.show_result_button = tk.Button(root, text="Hiển thị kết quả", command=self.solve_kmeans, image=result_icon, compound="left", font=button_font, bg=button_bg_color, fg=button_fg_color)
        self.show_result_button.image = result_icon
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
    app = App(root)
    root.mainloop()
