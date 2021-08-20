from random import randrange

somay=randrange(1,101)
solandoan = 0
win = False
while solandoan<7:
    solandoan+=1
    songuoi=int(input("Máy đoán [1...100], mời bạn đoán:"))
    print("Ban đã đoán lần thứ", solandoan)
    if somay == songuoi:
        print("Đã đoán đúng, số máy là=", somay)
        win = True
        break
    if somay>songuoi:
        print("Đoán sai, số máy > số ban")
    elif somay < songuoi:
        print("Đoán sai, số máy < số bạn")
if win == False:
    print("Game Over!")
hoi = input("Tiếp không?")
if hoi=="k":
    print("Thank for playing!!!")
