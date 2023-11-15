import matplotlib.pyplot as plt
import numpy as np

def ve_diem(x, y, color, label):
    plt.scatter(x, y, color=color)

# Thay đổi giá trị của N tùy thuộc vào số điểm bạn muốn vẽ
N = 10

# Tạo dữ liệu ngẫu nhiên cho tọa độ x, y cho điểm đỏ và xanh
x_do = np.random.rand(N)
y_do = np.random.rand(N)

x_xanh = np.random.rand(N)
y_xanh = np.random.rand(N)

# Vẽ N điểm màu đỏ và N điểm màu xanh trên cùng một đồ thị
ve_diem(x_do, y_do, 'red', 'Diem Do')
ve_diem(x_xanh, y_xanh, 'blue', 'Diem Xanh')

# Cài đặt các nhãn và tiêu đề
plt.title('N Diem Mau Do va N Diem Mau Xanh')
plt.xlabel('Truc X')
plt.ylabel('Truc Y')

# Hiển thị chú thích
plt.legend()

# Hiển thị đồ thị
plt.show()
