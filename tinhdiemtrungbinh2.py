print("Tính điểm trung bình")
toan,ly,hoa = eval(input("Nhập diểm toán,lý,hóa:"))
print("ĐIểm toán:", toan)
print("Điểm hóa:", hoa)
print("Điểm lý:", ly)
if(toan<0 or ly<0 or hoa<0):
    print("Nhập sai điểm")
else:
    dtb=(toan+ly+hoa)/3
    print("Điểm trung bình=", round(dtb,2))