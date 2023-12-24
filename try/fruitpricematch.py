
fruits = ["mango", "apple", "banana", "grape", "watermelon"]
price = [20, 25, 30]

for x, y in zip(fruits, price) :
    print(x, y, "THB")

for x, y in zip(fruits, price[::-1]) :
    print(x, y, "THB")