
# dictionary ==> key(การเข้าถึงข้อมูล), value(ค่าของข้อมูล)

# how to create dict
# variable = {key:value, key:value, key:value}

# colors = {"Red":"red", "Yellow":"yellow", "Green":"green", "Home":98}
# print(colors["Red"])
# print(colors["Yellow"])
# print(colors["Green"])
# print(colors["Home"])

# # constructor
# animals = dict(Cat = "cat", Bird = "bird", Dog = "dog")
# print(animals)

# print(colors.get("Red"))

# # change data
# colors["Home"] = 100
# print(colors)

# # update
# colors.update({"Blue":"blue"})
# print(colors)
# colors.update({"Orange":"orange"})
# colors.update({"Black":"black", "White":"white"})
# print(colors)

# # loop
# for i in colors :
#     print(i)  # key

# for i in colors.values() :
#     print(i)  # value

# for i in colors.keys() :
#     print(i)  # key

# for i in colors.items() :
#     print(i)  # both

# for i, j in colors.items() :
#     print("Key :", i, "Value :", j)  # both

# delete

# colors = {"Red":"red", "Yellow":"yellow", "Green":"green", "Home":98}

# print(colors)
# colors.pop("Red")
# print(colors)

# # popitem() ==> delete last data
# colors.popitem()
# print(colors)

# # clear()
# colors.clear()
# print(colors)

# # del
# del colors
# print(colors)

# # copy()
# colors = {"Red":"red", "Yellow":"yellow", "Green":"green", "Home":98}

# x = colors.copy()
# print(x)

# nested dict

market = {"kiki shop":{
            "name":"kiki",
            "menu":["Pepsi", "Fanta"],
            "zone":"A"
          }, 
          "kuku shop":{
              "name":"kuku",
              "menu":["mango", "banana"],
              "zone":"B"
          }, 
          "Pink":{
              "name":"Pink",
              "menu":["fried rice", "noodle"],
              "zone":"C"
          }}

print(market)
print(market["kiki shop"]["menu"])

if "noodle" in market["kiki shop"]["menu"] :
    print("Yess")
else :
    print("Nooo")











