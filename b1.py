a = int(input("Nhập giá trị cần kiểm tra "))
if a > 10:
    print("Giá trị lớn hơn 10 và là số dương")
elif 0 < a <= 10:
    print("Giá trị nhỏ hơn hoặc bằng 10 và là số dương")
elif a < 0:
    print("Giá trị là số âm")
else:
    print("Giá trị bằng 0")