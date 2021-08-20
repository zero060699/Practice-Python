# def LocSoDienThoai(dauso):
#     dsArr=["093454356", "0978689709", "0953455664", "0987687645"]
#     for phone in dsArr:
#         if(phone.startswith(dauso)):
#             return phone;
#         return "<empty>";
# print("Nhập đầu số:")
# dauso=input()
# phone = LocSoDienThoai(dauso)
# print(phone)

def LocSoDienThoai(dauso):
    dsArr=["093454356", "0978689709", "0953455664", "0987687645"]
    dsFound=[]
    for phone in dsArr:
        if(phone.startswith(dauso)):
            dsFound.append(phone)
        return dsFound
dauso=input("Nhap dau so:")
dsFound = LocSoDienThoai(dauso)
print(dsFound)
