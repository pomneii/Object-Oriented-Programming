
"""
    1.ไม่มีการรับค่าและส่งค่า
    def name() :
    
    2.มีการรับค่าเข้าไปทำงาน
    def name(a, b) :
    
    3.รับค่าเข้าไปทำงาน และส่งออกมา
    def name(a, b) :
    return a + b

    4. ไม่มีการรับค่าเข้ามา แต่ส่งค่าออกไป
"""


def sum(a, b) :
    return a + b

def display_number() :
    return 200

print(sum(10, 20))
x = sum(10, 20)
print(x)
y = display_number()
print(y)



def random_number(x) :
    if x == "100" :
        print("Lucky!")
        return 1000
    else :
        print("Noo..")
        return 0

money = random_number("100")
a = 300
result = money - a
print("Money :", money)
print("Result :", result)