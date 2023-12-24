
# สร้างขอบตาราง

num = int(input("Enter number : "))

for i in range(1, num + 1) :
    for j in range(1, num + 1) :
        if j == 1 or j == num or i == 1 or i == num :
            print("*", end='')
        else :
            print(" ", end='')
    print(" ")