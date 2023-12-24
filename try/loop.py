
start, stop = 1, 5
sum = 0

while start <= stop :
    number = int(input("Enter your number : "))
    sum += number
    start += 1

print("Sum :", sum)
print("Average :", sum / stop)