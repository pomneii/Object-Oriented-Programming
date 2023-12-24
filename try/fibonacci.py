
"""
    0 1 1 2 3 5 ...
"""

def fibo(num) :
    if num <= 1 :
        return num
    else :
        return fibo(num - 1) + fibo(num - 2)


for i in range(10) :
    print(fibo(i))

"""
i = 0 ; i = 0
i = 1 ; i = 1
i = 2 ; 1 + 0 = 1
i = 3 ; 1 + 1 = 2
i = 4 ; 2 + 1 = 3
"""