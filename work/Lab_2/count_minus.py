
"""
    ให้เขียนโปรแกรมเพื่อรับข้อมูล 1 บรรทัด ที่ประกอบด้วยจํานวนเต็มหลายจํานวน (คั่นด้วยช่องว่าง)
    ให้ส่งคืนว่ามีจํานวนที่เป็นลบกี่จํานวน โดยใช้ List comprehension
    ให้เขียนในฟังก์ชัน count_minus(str) แล้ว return เป็นคําตอบ
"""

def count_minus(str) :
    str = [int(e) for e in str.split()]
    count = 0
    for i in str :
        if i < 0 :
            count += 1
    return count

number = [int(e) for e in input().split()]
result = count_minus(number)
print(result)
