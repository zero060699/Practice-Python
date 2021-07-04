from math import sqrt

print("Tính diện tích tam giác")
a = float(input("Nhập a>0:"))
b = float(input("Nhập b>0:"))
c = float(input("Nhập c>0:"))
if (a<=0 or b<=0 or c<=0) and (a+b)<c or (a+c)<b or (b+c)<a:
    print("Tam giác không hợp lệ")
else:
    cv=a+b+c
    p=cv/2
    dt=sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích:",dt)