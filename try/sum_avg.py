
def sum(num) :
    total, avg = 0, 0
    for i in num :
        total += i
    avg = total / len(num)
    return total, avg

x = [1, 2, 3, 4, 5, 6]
m, n = sum(x)
print("Sum ", m)
print("Avg :", n)



