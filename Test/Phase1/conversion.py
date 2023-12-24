
# Type Conversion

x = 10
y = 3.14
z = "20"

# string => int
result1 = x + y
result2 = x + int(z) # make it to int 
result3 = int(z) + y # make it to int
print(type(x))
print(type(y))
print(type(z))

print(result1)
print(result2)
print(result3)

# string + string
a = "Hello"
b = "World"
c = "20"
print(a + " " + b)
print("result : " + c)