
"""
    ให้แก้ไขคลาส student โดยเพิ่มข้อมูล พี่รหัส (student_menter) หมายถึงนักศึกษาที่เป็นพี่รหัสขึ้นไป 1 ชั้นปีเท่านั้น

    ให้สร้าง instance ของ นศ. 4 คนขึ้นไป เช่น a เป็นปี 1, b เป็นปี 2 และเป็นพี่รหัสของ a
    c เป็นปี 3 และเป็นพี่รหัสของ b ส่วน d เป็นปี 4 และเป็นพี่รหัสของ c การสร้าง Instance ให้ใช้รหัส
    นักศึกษา 8 หลัก และเลข 2 ตัวแรกตามชั้นปีจริง
    - ให้เขียนฟังก์ชัน #3 โดยเมื่อป้อนรหัสนักศึกษา x แล้วตอบว่ามีพี่รหัส เป็นใครบ้าง โดยให้
    ตอบให้ครบ เช่น ถ้าป้อน a ให้ตอบ b, c, d ถ้าป้อน b ให้ตอบ c, d โดยให้แสดงทั้งรหัส
    นักศึกษาและชื่อ ในการแสดงให้แสดงกรณีไม่มีพี่รหัสด้วย
    - ให้เขียนฟังก์ชัน #4 โดยเมื่อป้อนรหัสนักศึกษา Student x และ student y ให้ตรวจสอบว่าเป็น
    สายรหัสกันหรือไม่ ให้ตอบเป็น True และ False

    โปรแกรมอาจแยกเขียนจากโปรแกรม 4.2 ก็ได้
"""


class Student:
    def __init__(self, student_id, student_name):
        self.stu_id = student_id
        self.name = student_name
        self.student_menter = None


# สายรหัส s1<s2<s3<s4 , s5 ไม่มีสายรหัส

student1 = Student('66000001', 'woranuch')
student2 = Student('65000002', 'manchai')
student3 = Student('64000003', 'worachai')
student4 = Student('63000004', 'junior')
student5 = Student('66000005', 'tin')
stu = [student1, student2, student3, student4, student5]

student1.student_menter = student2
student2.student_menter = student3
student3.student_menter = student4


def find_stu(id):
    for i in stu:
        if id == i.stu_id:
            return i


def have_menter_or_not(student_stu):
    if student_stu.student_menter != None:
        return True
    else:
        False


def function3(id):
    list_ = []
    student_stu = find_stu(id)
    while (1):
        if have_menter_or_not(student_stu):
            list_.append(student_stu.student_menter)
            student_stu = student_stu.student_menter
        else:
            break

    n = len(list_)
    list_result = []
    for i in range(n):
        list_result += [[list_[i].name, list_[i].stu_id]]

        
    return list_result

def function4(stu_id_1, stu_id_2) :
    list_result_1 = function3(stu_id_1)
    list_result_2 = function3(stu_id_2)
    # if len(list_result_2) > len(list_result_1)
    name = find_stu(stu_id_1).name
    print(name)
    for i in range(len(list_result_1) + 1) :
        for j in range(len(list_result_1)) :
            if list_result_1[i][j] == name :
                return True
    # return list_result
    # pass

print(function3('66000001'))
print(function4('66000001', '64000003'))
