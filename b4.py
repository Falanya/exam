a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = input("Nhập phép tính: ")

if c == "+" :
    result = a + b
    print("Kết quả của phép tính là: %f" %(result))
elif c == "-" :
    result = a - b
    print("Kết quả của phép tính là: %f" %(result))
elif c == "*" :
    result = a * b
    print("Kết quả của phép tính là: %f" %(result))
elif c == "/" :
    if a != 0:
        result = a / b
        print("Kết quả của phép tính là: %f" %(result))
    else:
        print("Nhập giá trị ngu thế dcm")
elif c == "%" :
    if a != 0:
        result = a % b
        print("Kết quả của phép tính là: %f" %(result))
    else:
        print("Nhập giá trị ngu thế dcm")
else:
    print("Nhập phép tính ngu thế dcm")