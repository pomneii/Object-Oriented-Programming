
num = int(input("Enter the size : "))

for i in range(1, num + 1) :
    for j in range(1, num + 1) :
        if (i + j) % 2 == 0 :
            print("x", end='')
        else :
            print("o", end='')
    print("")