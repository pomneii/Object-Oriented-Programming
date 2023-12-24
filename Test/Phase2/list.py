 
# Non-Primitive

# List

number = [] # empty list
number = [1, 2, 3, 4, 5] # int
name = ["Pink", "kuku", "kiki"] # string
all = [10, "Pink", True, 2.3, -24]

# constructor
name = list(["Pink", "kuku", "kiki"])

print(type(name))

# list = ["A", "B", "C", "D"]
#          0    1    2    3     index
#         -4   -3   -2    -1    negative index
print(number[2])
print(number[2] + number[1])
print(name[2])
print(all[1:4])
print(all[-4:])

# How to edit data

# variable [index] = "new data"

number = [1, 2, 3, 4, 5]
print("Before :", number)
number[2] = 9
number[4] = 10
number[-4] = 7
number[3] = "kiki"
print("After :", number)

# loop
number = [1, 2, 3, 4, 5]
sum = 0
for i in number :
    print(i, end=' ')
print("")
for j in number :
    sum = sum + j
print(sum)

fruits = ["mango", "banana", "orange", "lemon"]

if "banana" in fruits :
    print("True")
else :
    print("False")

# length of list
number = [1, 2, 3, 4, 5]
fruits = ["mango", "banana", "orange", "lemon"]
print(len(number))
print(len(fruits))

for i in range(len(number)) :
    print(number[i])

# append()
# add member in list
print(fruits)
fruits.append("coconut")
print(fruits)

# insert(index, "new")
# add member in list
fruits.insert(1, "watermelon")
print(fruits)

# remove data

# remove()
fruits.remove("mango")
print(fruits)

# pop() remove last index
fruits.pop()
print(fruits)

# del() delete index
del fruits[2]
print(fruits)
# del fruits # delete fruits

# clear() remain empty list
fruits.clear()
print(fruits)

# copy()
number = [1, 2, 3, 4, 5]
fruits = ["mango", "banana", "orange", "lemon"]

x =[]
print(x)
x = fruits.copy()
print(x)

# merge list
mix = number + fruits
print(mix)

# count
number = [1, 2, 3, 5, 2, 3, 1, 1, 2, 1]
a = number.count(2)
print(a)

# merge list and use old list
number = [1, 2, 3, 4, 5]
fruits = ["mango", "banana", "orange", "lemon"]
number.extend(fruits)
print(number)
