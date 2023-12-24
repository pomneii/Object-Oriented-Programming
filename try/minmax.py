
# เขียนโปรแกรมหาตัวเลขมาก / น้อย

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if a > b :
    print(str(a) + " is greater than " + str(b)) # convert to str so it can merge
    print(a, "is greater than", b)
else :
    print(str(b) + " is greater than " + str(a))
    print(b, "is greater than", a)