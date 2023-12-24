
# Function call Function

def compare_max(a, b) :
    if a > b :
        return a
    else :
        return b
    
def compare_three(x, y, z) :
    # a = compare_max(x, y)
    # b = compare_max(a, z)
    # return b
    return compare_max(compare_max(x, y), z)
    
x = compare_max(10, 6)
print("Max :", x)
y = compare_three(20, 45, 89)
print("Max_Three :", y)


