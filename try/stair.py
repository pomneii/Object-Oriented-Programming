
# number stair

"""
n = 5
1
12
123
1234
12345
"""

num = int(input("Enter your number : "))

for row in range(1,num + 1) :
    for col in range(1,row + 1) :
        print(col, end="")
    print(" ")