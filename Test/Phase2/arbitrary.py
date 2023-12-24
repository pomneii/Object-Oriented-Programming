
# args ==> tuple

def sum_num(*args) :
    print(args[0])
    print(args[0] + args[1])
    sum = 0
    for i in range(len(args)) :
        sum += i
    print(sum)

x = int(input())
y = int(input())

sum_num(x, y)


