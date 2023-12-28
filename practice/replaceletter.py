
"""
    input = 2
            10
    output = X1XXXXXXXX

    input = 2, 4, 6
            10
    output = X1X1X1XXXX

    input = 0
            10
    output = XXXXXXXXXX

    first input = index
    second input = len of string
    you need to replace index with '1'

"""

num = [int(e) for e in input().split(',')]
len_of_str = int(input())
lis = []
for i in range(len_of_str) :
    lis.append('X')
for j in lis :
    for k in num :
        if k > 0 :
            lis[k - 1] = '1'
print(''.join([i for i in lis]))

# my code is so long, i'm trying to study how to code in python