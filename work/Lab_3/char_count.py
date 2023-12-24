
"""
    เขียนฟังก์ชัน char_count(str) โดยรับพารามิเตอร์ 1 ตัว เป็นข้อมูลชนิด string และให้ส่งคืนเป็น
    dictionary ที่มี key เป็นตัวอักษรแต่ละตัวของ string นั้น และ value คือ จํานวนครั้งที่ตัวอักษรนั้นปรากฏ
    ใน string เช่น
    Input : 'language'
    return : {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'e': 1}
"""

def char_count(str):
    return {chars : str.count(chars) for chars in str}
    # result = {}
    # for chars in str :
    #     result.update({chars : str.count(chars)})
    # return result 


str = input()
x = char_count(str)
print(x)