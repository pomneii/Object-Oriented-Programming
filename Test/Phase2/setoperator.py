
# union
fruitsA = {"banana", "lemon", "grape"}
fruitsB = {"apple", "watermelon", "mangosteen"}

# new set
allfruits = fruitsA.union(fruitsB)

# old set
fruitsA.update(fruitsB)

print(allfruits)
print(fruitsA)

# copy set
fruitsc = fruitsA.copy()
print(fruitsc)

# difference
fruitsA = {"banana", "lemon", "grape", "watermelon"}
fruitsB = {"apple", "watermelon", "mangosteen"}

# new set
fruitsc = fruitsA.difference(fruitsB)
print(fruitsc)

# old set
fruitsA.difference_update(fruitsB)
print(fruitsA)

# insersection
fruitsd = fruitsA.intersection(fruitsB)
print(fruitsd)

# subset
animals = {"fish", "bear", "cat", "dog"} # superset

x = {"ant", "elephant"} # subset
y = {"fish", "cat"}

print(x.issubset(animals))
print(y.issubset(animals))

# superset
print(animals.issuperset(x))
print(animals.issuperset(y))

# min, max
number = {-100, 20, 54, 35, 42, 78, 100}
print(min(number))
print(max(number))


