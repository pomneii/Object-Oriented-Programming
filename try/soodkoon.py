
start = int(input("Enter first number : "))
end = int(input("Enter end number : "))

for i in range(start,end + 1) :
    print("<==", i, "==>")
    for j in range(1,13) :
        print(i, "x", j , "=", i * j)