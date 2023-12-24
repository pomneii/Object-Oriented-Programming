
# order number and find max min sum

list = []
while True :
    num = int(input("Enter numbers : "))
    if num < 0 :
        break
    list.append(num)

print("Before :", list)

# sort()
list.sort()
print("After :", list)

# reverse()
list.reverse()
print("After reverse :", list)

# max min sum
print("Max : ", max(list))
print("Min : ", min(list))
print("Sum : ", sum(list))

print("End of program!")