
# member in tuple ==> variable

tup = (10, 20, 30)
a, b, c = tup
print(a)
print(b)
print(c)
 
# switch tuple
x = (50, 60)
y = (89, 88)
print("Before :", x)
print("Before :", y)
x, y = y, x
print("After :", x)
print("After :", y)

# tuple ==> string
character = ('P', 'i', 'n', 'k')
name = "".join(character)
print(name)

# reverse tuple
x = (20, 10, 87, 64, 23)
y = reversed(x)
print(x)
print(tuple(y))

# string ==> tuple
x = "Pink"
y = tuple(x)
print(y)