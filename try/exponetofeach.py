
# exponent in each members

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)

# normal
for i in range(len(number)) :
    number[i] = number[i] * number[i]
print(number)

# easy way to write
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = [x * x for x in number]
print(number)