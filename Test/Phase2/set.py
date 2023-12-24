
"""
    List : [] ข้อมูลชนิดต่างกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันได้ , ซ้าย ==> ขวา
    Tuple : () ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลไม่ได้ , ข้อมูลซ้ำกันได้ , ซ้าย ==> ขวา
    Set : {} ข้อมูลต่างชิดกัน , แก้ไขข้อมูลสมาชิกไม่ได้ , ข้อมูลซ้ำกันไม่ได้ , ลำดับไม่แน่นอน
"""

# normal
fruits = {"mango", "apple", "banana"}
# not same index
print(fruits)
print(type(fruits))

# constructor
animals = set(["fish", "bird", "bird"])
print(animals)
# no same member in set

kiki = {"kiki", 2, False, 5.0, "baba"}
print(kiki)

# add data
fruits.add("orange")
fruits.add("pineapple")
fruits.add(100)
print(fruits)

# add many data in one time
lis = ["chilli", "cucumber", "cabbage"]
fruits.update(lis)
print(fruits)

# loop
for i in fruits :
    print(i)

# length of set
print(len(fruits))

# check set
if "mango" in fruits :
    print("Yes")
else :
    print("No")

# delete data

# if there's not pineapple in set it will show error : suggestion ==> discard
fruits.remove("pineapple") 
print(fruits)

# even there's not grape it will not show error
fruits.discard("grape")
print(fruits)

# clear()
fruits.clear()
print(fruits)

# # del ; delete fruits
# del fruits
# print(fruits)

