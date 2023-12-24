
def fact(num) :
    if num == 1 :
        return num
    else :
        return num * fact(num - 1)
    
factorial = fact(8)
print(factorial)