
# draw square

"""
n = 3
***
***
***
"""

num = int(input("Enter your nummber : "))

for i in range(1,num + 1) :
    for j in range(1, num + 1) :
        print("*", end='')
    print("")