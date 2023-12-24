
"""
    ให้เขียนฟังก์ชัน is_plusone_dictionary(d) โดยรับพารามิเตอร์ 1 ตัว เป็นข้อมูลชนิด dictionary และให้
    ทดสอบว่า dictionary ที่รับเข้ามาเป็น plusone dictionary หรือไม่ ผลลัพธ์ให้return เป็น True หรือ
    False โดย plusone dictionary คือ dictionary ที่ key และ value จะบวก 1 ต่อกันไปเรื่อยๆ

    Input : {1:2, 3:4, 5:6, 7:8}
    return : True
    อธิบาย : เพราะ key : value ต่างกันเป็น +1 ต่อกันไป
    Input : {1:2, 3:10, 5:6, 7:8}
    return : False
    อธิบาย : เพราะ key, value ไม่เป็นไปตามลําดับ
"""

def is_plusone_dictionary(d) :
    flag = 0 # 0 = not , 1 = yes
    dict_keys = [i for i in d.keys()]
    dict_values = [i for i in d.values()]
    for i in range(1, len(dict_keys)) :
        if dict_keys[i] - dict_keys[i - 1] != 2 :
            break
        else :
            if dict_values[i] - dict_values[i - 1] != 2 :
                break
            else :
                flag = 1

    if flag == 1 :
        for i in range(1, len(dict_keys)) :
            if dict_keys[i] - dict_values[i - 1] != 1 :
                flag = 0
                break

    if flag == 0 :
        return False
    else :
        return True

dic = input()
dic = eval(dic)
print(is_plusone_dictionary(dic))

# import unittest
# from main import *


# class UnitTests(unittest.TestCase):

#   def test_is_plusone_dictionary(self):
#       self.assertEquals(is_plusone_dictionary({1:2, 3:4, 5:6, 7:8}),True)
#       self.assertEquals(is_plusone_dictionary({1:2, 3:4, 5:6, 8:9}),False)
#       self.assertEquals(is_plusone_dictionary({1:2, 3:10, 5:6, 7:8}),False)
      
    

