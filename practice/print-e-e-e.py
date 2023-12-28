
"""
    input : 5
            agml gaga gwpoga gapg;a gapgag
    output : eeee eeee eeeeee eeeeee eeeeee

    print 'e' * len of each word
"""

num = int(input())
str = input().split(' ')
lis = []
for i in range(len(str)) :
    lis.append('e' * len(str[i]))

print(' '.join([e for e in lis]))