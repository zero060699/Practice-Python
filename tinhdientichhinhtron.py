import math

try:
    r = float(input("Nhập vào hình tròn"))
    cv = 2*math.pi*r
    dt = r**2
    print("Chu vi:", cv)
    print("Diện tích", dt)
except:
    print("Lỗi")