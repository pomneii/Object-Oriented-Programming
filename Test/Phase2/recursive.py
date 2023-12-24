
# Recursive Function

"""
    หาจุดวนซ้ำ
    หาจุดออกจาก function (return)
    มี parameter
"""

def add_number(number) :
    if number == 5 :
        return
    print(number + 1)
    number += 1
    add_number(number)

def sum(num) :
    if num == 1 :
        return num
    else :
        return num + sum(num - 1)
    

add_number(0)
x = sum(5)
print(x)


