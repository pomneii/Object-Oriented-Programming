
# Return

def random_number(x) :
    if len(x) < 3 :
        return             # like you out of function
    if x == "100" :
        print("Lucky!")
        return 1000
    else :
        print("Noo..")
        return 0

money = random_number("10")
a = 300
# result = money - a
print("Money :", money)
# print("Result :", result)