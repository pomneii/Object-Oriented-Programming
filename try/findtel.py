
data = {"191" : "Police", "1669" : "Hospital", "1112" : "Pizza"}

def search_number(str) :
    for key, value in data.items() :
        if value == str :
            print(key)
        else :
            return

str = input()
search_number(str)