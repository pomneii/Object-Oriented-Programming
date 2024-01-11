
"""
    Activity #1 จาก Activity #2 ของครั้งที่แล้ว
    - ให้เขียนโปรแกรม เพื่อสร้างคลาสต่อไปนี้
        • นักศึกษา (Student) โดยมี attribute : stu_id, stu_name
        • รายวิชา (Subject) โดยมี attribute : subject_id, subject_name, section, credit
        • ผู้สอน (Teacher) โดยมี attribute : teacher_id, teacher_name

    • ให้ปรับปรุง Code โดยเพิ่ม access modifier กําหนดให้ attribute ทุกตัวในคลาสเป็น
    แบบ private
    • ให้เขียน setter และ getter ของทุก attribute ที่จําเป็น โดยให้ validate ข้อมูลใน
    ส่วน setter ด้วย เช่น ชื่อ ต้องเป็นภาษาอังกฤษเท่านั้น
"""

class Student :
    def __init__(self, stu_id, stu_name) :
        self.__stu_id = stu_id
        self.__stu_name = stu_name
        
    # getter stu_name
    def get_stu_name(self) :
        return self.__stu_name
        
    # getter stu_id
    def get_stu_id(self) :
        return self.__stu_id

class Subject :
    def __init__(self, subject_id, subject_name, section, credit) :
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__section = section
        self.__credit = credit

    # getter subject id
    def get_subject_id(self) :
        return self.__subject_id
    
    # getter subject name
    def get_subject_name(self) :
        return self.__subject_name
    
    # getter section
    def get_section(self) :
        return self.__section
    
    # getter credit
    def get_credit(self) :
        return self.__credit

class Teacher :
    def __init__(self, teacher_id, teacher_name) :
        self.__teacher_id = teacher_id
        self.__teacher_name = teacher_name

    # getter teacher id
    def get_teacher_id(self) :
        return self.__teacher_id
    
    # getter teacher name 
    def get_teacher_name(self) :
        return self.__teacher_name
    
# def make_pretty(func) :
#     def inner() :
#         print("I got decorated")
#         func()

#     return inner

# def ordinary() : 
#     print("I am ordinary")

# decorated_func = make_pretty(ordinary)

# decorated_func()