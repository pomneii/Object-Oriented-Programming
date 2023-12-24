
"""
    ให้เขียนโปรแกรมเพื่อรับ string 1 ตัว
    ให้ส่งคืนเฉพาะตัวอักษรที่เป็นภาษาอังกฤษ โดยใช้ List comprehension
    ให้เขียนในฟังก์ชัน only_english(string1) แล้ว return เป็นคําตอบเป็น string
"""

def only_english(string1) :
    lis = [i for i in string1 if i.isalpha()]
    b = ''.join([e for e in lis])
    return b

str = input()
x = only_english(str)
print(x)