while True:
    n = int(input("Nhập 1 số nguyên dương:"))
    dem=0
    for i in range(n,n+1):
        if n%i == 0:
            dem+=1
        if dem==2:
            print(n,"Là số nguyên tố")
        else:
            print(n,"Không là số nguyên tố")
    hoi = input("Tiếp tục ko?:")
    if hoi is "k":
        break
print("Bye")