
def get_name(name) :
    print(name)


"""
    lambda function ==> dont want to name the function

    lambda arguments : expression
"""

x = lambda name : name
sum = lambda x, y : x + y
multi = lambda a, b : a * b

print(x("kiki"))
print(sum(5, 7))
print(multi(4, 5))

def my_data(m) :
    return lambda n : m ** n

y = my_data(5)
result = y(2)
print(result)