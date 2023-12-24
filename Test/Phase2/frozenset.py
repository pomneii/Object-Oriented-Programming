
# frozen set

# normal set
fruits = set(["mango", "apple", "grape"])
print(fruits)
fruits.add("pineapple")
print(fruits)
fruits.discard("mango")
print(fruits)

# frozen set
fruits = frozenset(["mango", "apple", "grape"])
# # cannot add or delete or change anythong in frozen set
# fruits.add("pineapple")
# fruits.discard("mango")

for i in fruits :
    print(i)
