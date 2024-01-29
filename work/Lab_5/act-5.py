
"""
    1. สร้างคลาสต่อไปนี้ โดยใช้หลัก Encapsulation ซึ่งจะไม่ยอมให้มีการเข้าถึงข้อมูลโดยตรง โดยให้กําหนด attribute ทุกตัวเป็นแบบ private
        - Student โดยมี attribute : student_id, student_name
        - Subject โดยมี attribute : subject_id, subject_name, credit
        - Teacher โดยมี attribute : teacher_id, teacher_name
        - ให้สร้าง setter, getter เท่าที่จําเป็น คือ สร้างเฉพาะเมื่อมีการร้องขอ หรือ กําหนดค่าจาก ภายนอกเท่านั้น ถ้าพบ setter, getter ที่ไม่จําเป็น จะหักคะแนน
        - สามารถสร้าง class อื่นๆ หรือเพิ่ม attribute ได้ตามความเหมาะสม
    2. กําหนดให้แต่ละรายวิชา มีผู้สอน 1 คน และ นักเรียนสามารถลงเรียนในรายวิชาใดๆ ก็ได้ จํานวนกี่วิชาก็ได้ และนักเรียน สามารถถอนวิชาได้ หากไม่ต้องการเรียนอีกต่อไป
    3. หลังจากการเรียน จะมีการสอบและให้เกรด โดยจะต้องเก็บข้อมูลว่านักเรียนแต่ละคนได้เกรดในวิชาใดเป็นเกรดใด กําหนดให้ A=4, B=3, C=2, D=1, F=0
    4. ให้สร้าง method ที่ทํางานดังนี้
        - method สําหรับลงทะเบียน (enroll_to_subject) โดยส่ง argument เป็น instance ของ Student และ
          Subject หากนักศึกษายังไม่ลงทะเบียนวิชานั้น ให้เพิ่ม object การลงทะเบียนและ return “Done”
          หากลงแล้วให้ return “Already Enrolled” แต่ถ้า argument ไม่ถูกต้องให้ return “Error”
        - method สําหรับถอนรายวิชา (drop_from_subject) โดยส่ง argument เป็น instance ของ Student
          และ Subject หากพบการลงทะเบียนให้ ดําเนินการถอน (ลบข้อมูลการลงทะเบียน) และ return
          “Done” หากยังไม่ได้ลงให้คืนค่า “Not Found” แต่ถ้า argument ไม่ถูกต้องให้ return “Error”
        - method สําหรับค้นหาการลงทะเบียนในรายวิชา (search_student_enrolled_in_subject) โดยส่ง
          argument เป็น instance ของ Subject และ ส่งคืนมาเป็น List ของ instance ของ การลงทะเบียน
          ที่ลงในวิชานั้น ถ้าไม่มีให้คืนเป็น List ว่าง แต่ถ้า argument ไม่ถูกต้องให้ return “Error”
        - method สําหรับบอกจํานวนนักศึกษาที่ลงในวิชา (get_no_student_enrolled) โดยส่ง argument เป็น
          instance ของ Subject และคืนค่าเป็นจํานวน หากไม่เจอ ให้คืนค่า “Not Found”
        - method สําหรับค้นหาการลงทะเบียนที่ นศ. ลงทะเบียน (search_subject_that_student_enrolled)
          โดยส่ง argument เป็น instance ของ Student และส่งคืนเป็น List ของ instance ของ การ
          ลงทะเบียน หากไม่เจอ ให้คืนค่า “Not Found”
        - method สําหรับค้นหาอาจารยที่สอนในวิชานั้น (get_teacher_teach) โดยส่ง argument เป็น
          instance ของ Subject และ ส่งคืนเป็น Instance ของอาจารยที่สอนวิชานั้น หากไม่เจอ ให้คืนค่า
          “Not Found”
        - method สําหรับค้นหาการลงทะเบียนที่ นศ. ลงทะเบียนในรายวิชานั้น
          (search_enrollment_subject_student) argument เป็น instance ของ Subject และ Student และ
          ส่งคืนเป็น instance การลงทะเบียน (สําหรับเรียกใช้โดย assign_grade)
        - method สําหรับกําหนดเกรดให้กับนักศึกษาในรายวิชา (assign_grade) โดยส่ง argument เป็น
          instance ของ Student และ Subject และ เกรด (เป็น string) หากยังไม่มีเกรดให้ เพิ่ม เกรด ลงใน
          การลงทะเบียน และ return “Done” หากมีเกรดแล้วให้ return “Error” หากไม่พบให้คืนค่า “Not Found”
        - method สําหรับค้นหาผลการเรียนของนักศึกษา (get_student_record) โดยส่ง argument เป็น
          instance ของ Student และส่งคืนเป็น dictionary { 'subject_id' : ['subject_name', 'grade' } หาก
          ไม่เจอ ให้คืนเป็น dictionary ว่าง
        - method สําหรับคํานวณเกรดเฉลี่ยของนักศึกษา (get_student_GPS) โดยส่ง argument เป็น
            instance ของ Student และคืนเป็นเกรดเฉลี่ย ให้เรียกใช้ get_student_record
    5. โปรแกรมจะต้องเป็นไปตามข้อกําหนดดังนี้
        - ห้ามใช้ dictionary ในการเก็บข้อมูล
        - ห้ามเก็บข้อมูลนอกคลาส ยกเว้นกรณีที่เป็น list ของ object
        - ในการสร้างคลาสให้กําหนดว่าจะเก็บข้อมูลใด และ ห้ามมิให้เก็บข้อมูลที่ไม่ใช่ข้อมูลที่เกี่ยวข้องกับ
          คลาสนั้น หากไม่สามารถเก็บลงในคลาสใดได้เลย ให้พิจารณาสร้างคลาสใหม่
        - ในคลาสไม่ให้มีการ Input ค่าหรือ print ค่าโดยตรง ให้ส่งข้อมูล parameter เข้าไปและได้ข้อมูล
          กลับมาเท่านั้น (ให้มอง class เป็น service)
        - ข้อมูลที่เก็บในคลาสที่ไม่ใช่คลาสพื้นฐาน เช่น คลาสนักศึกษา จะต้องเก็บข้อมูลเป็น Instance ของคลาสพื้นฐานเท่านั้น
    6. Test Case จะมีการทํางานดังนี้
        - สร้าง instance Student 10 คน
        - สร้าง instance Subject 3 วิชา
        - สร้าง instance Teacher 3 คน โดย add ชื่อผู้สอนเข้าไปในแต่ละวิชาที่สร้าง โดยใช้ method
          assign_teacher ของ instance วิชา
        - จะมีการเรียกใช้ function enroll_to_subject เพื่อลงทะเบียนนักศึกษาในแต่ละรายวิชา
    
    o Test Case #1 : กรณีที่ นศกับวิชานั้น ยังไม่เคยมีการลงทะเบียน การลงทะเบียนสําเร็จ ให้ return
                     “Done” จากนั้นจะมีการเรียกใช้ function search_subject_that_student_enrolled(student_id) เพื่อ
                     ตรวจสอบว่าคืนเป็น List ของวิชาที่ลงทะเบียนหรือไม่
    o Test Case #2 : ทดสอบ enroll_to_subject ในกรณีที่ argument ไม่เป็น instance
    o Test Case #3 : ทดสอบ enroll_to_subject ในกรณีที่มีการลงทะเบียนซ้ํา
    o Test Case #4 : ทดสอบ drop_from_subject ในกรณีที่ argument ไม่เป็น instance
    o Test Case #5 : ทดสอบ drop_from_subject ในกรณีไม่พบการลงทะเบียน
    o Test Case #6 : ทดสอบ drop_from_subject กรณี drop สําเร็จ
    o Test Case #7 : ทดสอบ search_student_enroll_in_subject โดยกําหนดให้ instance ของ การ
                     ลงทะเบียน ให้ทํา getter สําหรับ instance Subject และ instance Student และทํา getter สําหรับ
                     student id สําหรับ class Student และ subject_id สําหรับ class Subject
    o Test case #8 ทดสอบ get_no_of_student_enrolled โดยคืนค่าจํานวนนักศึกษา
    o Test Case #9 ทดสอบ search_subject_that_student_enrolled ค้นหาวิชาที่นักศึกษาลงทะเบียน
    o Test Case #10 ทดสอบ get_teacher_teach ค้นหา instance ของอาจารยที่สอนในวิชา
    o Test Case #11 ทดสอบ search_enrollment_subject_student ค้นหา instance ของ การลงทะเบียนของ นักศึกษา กับ รายวิชา
    o Test Case #12 ทดสอบ assign_grade
    o Test Case #13 ทดสอบ get_student_record
    o Test Case #14 ทดสอบ get_student_GPS
"""

class Student :
    def __init__(self, student_id, student_name) :
        self.__student_id = student_id
        self.__student_name = student_name
        
    # getter student_name
    def get_student_name(self) :
        return self.__student_name
        
    # getter student_id
    def get_student_id(self) :
        return self.__student_id
    
class Subject :
    def __init__(self, subject_id, subject_name, credit) :
        self.__subject_id = subject_id
        self.__subject_name = subject_name
        self.__credit = credit
        self.__assign_teacher = []

    # add teacher
    def assign_teacher(self, teacher) :
        self.__add_teacher = teacher

    # getter assign teacher
    def get_assign_teacher(self) :
        return self.__add_teacher

    # getter subject id
    def get_subject_id(self) :
        return self.__subject_id
    
    # getter subject name
    def get_subject_name(self) :
        return self.__subject_name
    
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
    
class Enrollment :
    def __init__(self, student, subject) :
        self.__student = student
        self.__subject = subject
        self.__grade = None

    def get_student(self) :
        return self.__student
    
    def get_subject(self) :
        return self.__subject
    
    def get_grade(self) :
        return self.__grade

    def set_grade(self, grade) :
        self.__grade = grade

student_list = []
subject_list = []
teacher_list = []
enrollment_list = []

# TODO 1 : function สำหรับค้นหา instance ของวิชาใน subject_list
def search_subject_by_id(subject_id) :
    for subject in subject_list :
        if subject.get_subject_id() == subject_id :
            return subject
    return None

# TODO 2 : function สำหรับค้นหา instance ของนักศึกษาใน student_list
def search_student_by_id(student_id):
    for student in student_list :
        if student.get_stu_id() == student_id :
            return student
    return None

# TODO 3 : function สำหรับสร้างการลงทะเบียน โดยรับ instance ของ student และ subject
def enroll_to_subject(student, subject) :
    if not isinstance(student, Student) or not isinstance(subject, Subject) :
        return "Error"
    for enroll in enrollment_list :
        if enroll.get_student() == student and enroll.get_subject() == subject :
            return "Already Enrolled"
    enrollment_list.append(Enrollment(student, subject))
    return "Done"
        
# TODO 4 : function สำหรับลบการลงทะเบียน โดยรับ instance ของ student และ subject
def drop_from_subject(student, subject) :
    if not isinstance(student, Student) or not isinstance(subject, Subject) :
        return "Error"
    for enroll in enrollment_list :
        if enroll.get_student() == student and enroll.get_subject() == subject :
            enrollment_list.remove(enroll)
            return "Done"
    return "Not Found"
        
# TODO 5 : function สำหรับค้นหาการลงทะเบียน โดยรับ instance ของ student และ subject
def search_enrollment_subject_student(subject, student) :
    if not isinstance(student, Student) or not isinstance(subject, Subject) :
        return "Error"       
    for enroll in enrollment_list :
        if enroll.get_subject() == subject and enroll.get_student() == student :
            return enroll 
    return "Not Found"    

# TODO 6 : function สำหรับค้นหาการลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def search_student_enroll_in_subject(subject) :
    student_in_subject_list = []
    if not isinstance(subject, Subject) :
        return "Error"
    for enroll in enrollment_list :
        if enroll.get_subject() == subject :
            student_in_subject_list.append(enroll.get_student())
    return student_in_subject_list

# TODO 7 : function สำหรับค้นหาการลงทะเบียนของนักศึกษาว่ามีวิชาอะไรบ้าง โดยรับ instance ของ student
def search_subject_that_student_enrolled(student) :
    subject_that_student_enroll_list = []
    if not isinstance(student, Student) :
        return "Error"
    for enroll in enrollment_list :
        if enroll.get_student() == student :
            subject_that_student_enroll_list.append(enroll.get_subject())
    return subject_that_student_enroll_list

# TODO 8 : function สำหรับใส่เกรดลงในการลงทะเบียน โดยรับ instance ของ student และ subject
def assign_grade(student, subject, grade) :
    for enroll in enrollment_list :
        if enroll.get_subject() == subject and enroll.get_student() == student :
            if enroll.get_grade() :
                return "Error"
            enroll.set_grade(grade)
        # my bug cuz I put it out of condition so in tesscase 13 every subjects have None grade
        # print(enroll.get_student().get_student_name())
        # enroll.get_grade()
            return "Done"
    return "Not Found"
            
# TODO 9 : function สำหรับคืน instance ของอาจารย์ที่สอนในวิชา
def get_teacher_teach(subject_search) :
    for teacher in teacher_list :
        if subject_search.get_assign_teacher() == teacher :
            return teacher
    return "Not Found"

# TODO 10 : function สำหรับค้นหาจำนวนของนักศึกษาที่ลงทะเบียนในรายวิชา โดยรับ instance ของ subject
def get_no_of_student_enrolled(subject) :
    lis = []
    for enroll in enrollment_list :
        if enroll.get_subject() == subject :
            lis.append(enroll.get_student())
    return len(lis)

# TODO 11 : function สำหรับค้นหาข้อมูลการลงทะเบียนและผลการเรียนโดยรับ instance ของ student
#           และ คืนค่าเป็น dictionary { ‘subject_id’ : [‘subject_name’, ‘grade’ }
def get_student_record(student) :
    record_dict = {}
    for enroll in enrollment_list :
        if enroll.get_student() == student :
            record_dict[enroll.get_subject().get_subject_id()] = [enroll.get_subject().get_subject_name(), enroll.get_grade()]
    return record_dict
    # one line code by my friend
    # return {enroll.get_subject().get_subject_id() : [enroll.get_subject().get_subject_name(),enroll.get_grade()] for enroll in enrollment_list if isinstance(student, Student) and enroll.get_student() == student}

# แปลงจาก เกรด เป็นตัวเลข
def grade_to_count(grade) :
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return grade_mapping.get(grade, 0)

# TODO 12 : function สำหรับคำนวณเกรดเฉลี่ยของนักศึกษา โดยรับ instance ของ student
def get_student_GPS(student) :
    divide = 0
    sum_credit = 0
    student_record_id_dict = get_student_record(student)
    subject_record_id = list(get_student_record(student).keys())
    for id in subject_record_id :
        sum_credit += (search_subject_by_id(id).get_credit()) * grade_to_count(student_record_id_dict[id][1]) 
        divide += (search_subject_by_id(id).get_credit())
    return sum_credit / divide

# ค้นหานักศึกษาลงทะเบียน โดยรับเป็น รหัสวิชา และคืนค่าเป็น dictionary {รหัส นศ. : ชื่อ นศ.}
def list_student_enrolled_in_subject(subject_id) :
    subject = search_subject_by_id(subject_id)
    if subject is None :
        return "Subject not found"
    filter_student_list = search_student_enroll_in_subject(subject)
    student_dict = {}
    for enrollment in filter_student_list :
        student_dict[enrollment.get_student_id()] = enrollment.get_student_name()
    return student_dict

# ค้นหาวิชาที่นักศึกษาลงทะเบียน โดยรับเป็น รหัสนักศึกษา และคืนค่าเป็น dictionary {รหัสวิชา : ชื่อวิชา }
def list_subject_enrolled_by_student(student_id) :
    student = search_student_by_id(student_id)
    if student is None :
        return "Student not found"
    filter_subject_list = search_subject_that_student_enrolled(student) # self.search_subject_that_student_enrolled(student)
    subject_dict = {}
    for enrollment in filter_subject_list :
        subject_dict[enrollment.subject.subject_id] = enrollment.subject.subject_name
    return subject_dict

def create_instance() :
    student_list.append(Student('66010001', "Keanu Welsh"))
    student_list.append(Student('66010002', "Khadijah Burton"))
    student_list.append(Student('66010003', "Jean Caldwell"))
    student_list.append(Student('66010004', "Jayden Mccall"))
    student_list.append(Student('66010005', "Owain Johnston"))
    student_list.append(Student('66010006', "Isra Cabrera"))
    student_list.append(Student('66010007', "Frances Haynes"))
    student_list.append(Student('66010008', "Steven Moore"))
    student_list.append(Student('66010009', "Zoe Juarez"))
    student_list.append(Student('66010010', "Sebastien Golden"))

    subject_list.append(Subject('CS101', "Computer Programming 1", 3))
    subject_list.append(Subject('CS102', "Computer Programming 2", 3))
    subject_list.append(Subject('CS103', "Data Structure", 3))

    teacher_list.append(Teacher('T001', "Mr. Welsh"))
    teacher_list.append(Teacher('T002', "Mr. Burton"))
    teacher_list.append(Teacher('T003', "Mr. Smith"))

    subject_list[0].assign_teacher(teacher_list[0])
    subject_list[1].assign_teacher(teacher_list[1])
    subject_list[2].assign_teacher(teacher_list[2])

# ลงทะเบียน
def register():
    enroll_to_subject(student_list[0], subject_list[0])  # 001 -> CS101
    enroll_to_subject(student_list[0], subject_list[1])  # 001 -> CS102
    enroll_to_subject(student_list[0], subject_list[2])  # 001 -> CS103
    enroll_to_subject(student_list[1], subject_list[0])  # 002 -> CS101
    enroll_to_subject(student_list[1], subject_list[1])  # 002 -> CS102
    enroll_to_subject(student_list[1], subject_list[2])  # 002 -> CS103
    enroll_to_subject(student_list[2], subject_list[0])  # 003 -> CS101
    enroll_to_subject(student_list[2], subject_list[1])  # 003 -> CS102
    enroll_to_subject(student_list[2], subject_list[2])  # 003 -> CS103
    enroll_to_subject(student_list[3], subject_list[0])  # 004 -> CS101
    enroll_to_subject(student_list[3], subject_list[1])  # 004 -> CS102
    enroll_to_subject(student_list[4], subject_list[0])  # 005 -> CS101
    enroll_to_subject(student_list[4], subject_list[2])  # 005 -> CS103
    enroll_to_subject(student_list[5], subject_list[1])  # 006 -> CS102
    enroll_to_subject(student_list[5], subject_list[2])  # 006 -> CS103
    enroll_to_subject(student_list[6], subject_list[0])  # 007 -> CS101
    enroll_to_subject(student_list[7], subject_list[1])  # 008 -> CS102
    enroll_to_subject(student_list[8], subject_list[2])  # 009 -> CS103

create_instance()
register()

### Test Case #1 : test enroll_to_subject complete ###
student_enroll = list_student_enrolled_in_subject('CS101')
print("Test Case #1 : test enroll_to_subject complete")
print(student_enroll)
print("Answer : {'66010001': 'Keanu Welsh', '66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall','66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
print("")

# ### Test case #2 : test enroll_to_subject in case of invalid argument
print("Test case #2 : test enroll_to_subject in case of invalid argument")
print("Answer : Error")
print(enroll_to_subject('66010001','CS101'))
print("")

# ### Test case #3 : test enroll_to_subject in case of duplicate enrolled
print("Test case #3 : test enroll_to_subject in case of duplicate enrolled")
print("Answer : Already Enrolled")
print(enroll_to_subject(student_list[0], subject_list[0]))
print("")

# ### Test case #4 : test drop_from_subject in case of invalid argument 
print("Test case #4 : test drop_from_subject in case of invalid argument")
print("Answer : Error")
print(drop_from_subject('66010001', 'CS101'))
print("")

# ### Test case #5 : test drop_from_subject in case of not found 
print("Test case #5 : test drop_from_subject in case of not found")
print("Answer : Not Found")
print(drop_from_subject(student_list[8], subject_list[0]))
print("")

# ### Test case #6 : test drop_from_subject in case of drop successful
print("Test case #6 : test drop_from_subject in case of drop successful")
print("Answer : {'66010002': 'Khadijah Burton', '66010003': 'Jean Caldwell', '66010004': 'Jayden Mccall', '66010005': 'Owain Johnston', '66010007': 'Frances Haynes'}")
drop_from_subject(student_list[0], subject_list[0])
print(list_student_enrolled_in_subject(subject_list[0].get_subject_id()))
print("")

# ### Test case #7 : test search_student_enrolled_in_subject
print("Test case #7 : test search_student_enrolled_in_subject")
print("Answer : ['66010002','66010003','66010004','66010005','66010007']")
lst = search_student_enroll_in_subject(subject_list[0])
print([i.get_student_id() for i in lst])
print("")

# ### Test case #8 : get_no_of_student_enrolled
print("Test case #8 get_no_of_student_enrolled")
print("Answer : 5")
print(get_no_of_student_enrolled(subject_list[0]))
print("")

# ### Test case #9 : search_subject_that_student_enrolled
print("Test case #9 search_subject_that_student_enrolled")
print("Answer : ['CS102','CS103']")
lst = search_subject_that_student_enrolled(student_list[0])
print([i.get_subject_id() for i in lst])
print("")

# ### Test case #10 : get_teacher_teach
print("Test case #10 get_teacher_teach")
print("Answer : Mr. Welsh")
print(get_teacher_teach(subject_list[0]).get_teacher_name())
print("")

# ### Test case #11 : search_enrollment_subject_student
print("Test case #11 search_enrollment_subject_student")
print("Answer : CS101 66010002")
enroll = search_enrollment_subject_student(subject_list[0],student_list[1])
print(enroll.get_subject().get_subject_id(), enroll.get_student().get_student_id())
print("")

# ### Test case #12 : assign_grade
print("Test case #12 assign_grade")
print("Answer : Done")
assign_grade(student_list[1],subject_list[0],'A')
assign_grade(student_list[1],subject_list[1],'B')
print(assign_grade(student_list[1],subject_list[2],'C'))
print("")

# ### Test case #13 : get_student_record
print("Test case #13 get_student_record")
print("Answer : {'CS101': ['Computer Programming 1', 'A'], 'CS102': ['Computer Programming 2', 'B'], 'CS103': ['Data Structure', 'C']}")
print(get_student_record(student_list[1]))
print("")

# ### Test case #14 : get_student_GPS
print("Test case #14 get_student_GPS")
print("Answer : 3.0")
print(get_student_GPS(student_list[1]))
