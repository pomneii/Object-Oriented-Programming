
# find min/ max

max, min = 0, 999

while True :
    number = int(input("Enter your number : "))
    if number < 0 :
        break
    if number > max :
        max = number
    if number < min :
        min = number

print("Max :", max)
print("Min :", min)