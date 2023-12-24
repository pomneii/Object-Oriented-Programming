
# Even / Odd group

number = []
even = []
odd = []

while True :
    x = int(input("Enter numbers : "))
    if x < 0 :
        break
    if x % 2 == 0 :
        even.append(x)
    else :
        odd.append(x)
    number.append(x)

print("All :", number)
print("Even :", even)
print("Odd :", odd)