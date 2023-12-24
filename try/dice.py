
# เกมทายลูกเต๋า

import random

random_number = random.randrange(1, 10)
print(random_number)

i = 1
while i <= 3 :
    number = int(input("Enter your answer : "))
    i += 1
    if number < 0 :
        break

    if number == random_number :
        break
    else :
        if number < random_number :
            print("Your number is lower than lucky number..")
        else :
            print("Your number is greater than lucky number..")

if number == random_number :
    print("Correct!")
else :
    print("Oh noooo...")
    print("==>")
    print("The lucky number is :", random_number)