
"""
    โดยใช้กลุ่มเดิม ใช้ระบบ Pair Programmer คือ คนที่ 1 บอก Code ให้คนที่ 2 เขียนตามคําบอก
    โดยหากไม่เห็นด้วย สามารถทักท้วงได้

    ให้เขียนโปรแกรม เพื่อสร้างคลาสต่อไปนี้
    - นักศึกษา (Student) โดยมี attribute : student_id, student_name
    - รายวิชา (Subject) โดยมี attribute : subject_id, subject_name, section, credit
    - ผู้สอน (Teacher) โดยมี attribute : teacher_id, teacher_name
    - สามารถเพิ่ม attribute อื่นๆ ได้

    ให้สร้าง Instance ของทุกคลาส และ สร้างความสัมพันธ์ (สามารถเพิ่ม attribute ได้)
    - ให้สร้าง instance ของนักศึกษา 5 คนขึ้นไป
    - ให้สร้าง instance ของอาจารย์ 2 คน
    - ให้สร้าง instance ของวิชา object oriented programming 2 instance 2 section โดยแต่ละ
      section มีผู้สอนคนละคน และแต่ละ section มีคนเรียนอย่างน้อย 2 คน
    - ข้อมูลใน Instance ให้เป็นข้อมูลที่จริงจังสักหน่อย

    ให้เขียนฟังก์ชัน #1 โดยเมื่อใส่ รหัสผู้สอน แล้วสามารถบอกได้ว่ามี นศ. คนไหนบ้างที่เรียนกับผู้สอนนี้
    โดยให้บอกเป็นชื่อนักศึกษา

    ให้เขียนฟังก์ชัน #2 โดยเมื่อใส่ รหัส นศ. แล้วบอกว่าเรียนวิชาอะไรบ้าง โดยให้บอกเป็นชื่อวิชา

    ข้อมูลทั้งหมดต้องอยู่ในคลาสเท่านั้น ยกเว้น List ที่เก็บ นศ. ทั้งหมด วิชาทั้งหมด อาจารย์ทั้งหมด ให้
    อยู่ข้างนอกได้ และห้ามใช้ dictionary ในการเก็บข้อมูล
"""

class Student :
    def __init__(self, student_id, student_name) :
        self.stu_id = student_id
        self.name = student_name

class Subject :
    def __init__(self, subject_id, subject_name, section, credit) :
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit
        self.teacher_in_class = []
        self.student_in_class = []

class Teacher :
    def __init__(self, teacher_id, teacher_name) :
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

student1 = Student('00000001', 'woranuch')
student2 = Student('00000002', 'manchai')
student3 = Student('00000011', 'pink')
student4 = Student('00000004', 'junior')
student5 = Student('00000005', 'worachai')
list_stu = [student1,student2,student3,student4,student5]

teacher1 = Teacher('001', 'Orachat')
teacher2 = Teacher('002', 'Thana')
list_tea = [teacher1,teacher2]

oop1 = Subject('111', 'oop1', 16, 3)
oop2 = Subject('112', 'oop2', 17, 3)
list_sub = [oop1,oop2]

oop1.teacher_in_class.append(teacher1)
oop2.teacher_in_class.append(teacher2)

oop1.student_in_class.append(student1)
oop1.student_in_class.append(student2)
oop1.student_in_class.append(student3)

oop2.student_in_class.append(student4)
oop2.student_in_class.append(student5)

def function1(teach_id) :
    lis = []
    for i in list_sub :
        for k in range(len(i.teacher_in_class)) :
            if teach_id == i.teacher_in_class[k].teacher_id :
                for j in range(len(i.student_in_class)) :
                    lis.append(i.student_in_class[j].name)     
    return lis

def function2(stu_id) :
    lis_sub = []
    for i in list_sub :
        for j in range(len(i.student_in_class)) : 
            if stu_id == i.student_in_class[j].stu_id :
                lis_sub.append(i.subject_name) 
    
        return lis_sub

x = input("[001/002] : ")
y = input("[00000001-00000005] : ")
print(function1(x))
print(function2(y))