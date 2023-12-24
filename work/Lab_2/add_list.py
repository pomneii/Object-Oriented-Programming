
"""
    กําหนดให้ list x และ y เป็น list ของจํานวนเต็ม โดยมีขนาดเท่ากัน
    ให้ return list ที่เป็นผลบวกของ list x และ y โดยใช้ list comprehension
    ให้เขียนในฟังก์ชัน function ชื่อ add2list(lst1,lst2)
"""

def add2list(lst1, lst2) :
  if len(lst1) != len(lst2) :
    return -1
  else :
    lis = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return lis

num1 = [int(e) for e in input().split()]
num2 = [int(e) for e in input().split()]

if len(num1) != len(num2) :
    print("Error!")
else :
    x = add2list(num1, num2)
    print(x)