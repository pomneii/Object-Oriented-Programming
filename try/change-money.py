
# แลกเงินและหาจำนวนแบงค์

# 2000 ==> 1000 2 ใบ
# 1500 ==> 1000 1 ใบ , 500 1 ใบ

number = int(input("Enter your money : "))

if number >= 1000 :
    print("1000 = ", number // 1000, "ใบ")
    number = number % 1000

if number >= 500 :
    print("500 = ", number // 500, "ใบ")
    number = number % 500

if number >= 100 :
    print("100 = ", number // 100, "ใบ")
    number = number % 100

if number >= 50 :
    print("50 = ", number // 50, "ใบ")
    number = number % 50

if number >= 20 :
    print("20 = ", number // 20, "ใบ")
    number = number % 20

if number >= 10 :
    print("10 = ", number // 10, "เหรียญ")
    number = number % 10
    
if number >= 5 :
    print("5 = ", number // 5, "เหรียญ")
    number = number % 5

if number >= 2 :
    print("2 = ", number // 2, "เหรียญ")
    number = number % 2

if number >= 1 :
    print("1 = ", number // 1, "เหรียญ")
    number = number % 1


