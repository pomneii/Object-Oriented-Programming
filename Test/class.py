
# class Student :
#     id = ' '
#     name = ' '

# stu1 = Student()
# stu1.id = '001'
# stu1.name = 'Pink'

# stu2 = Student()
# stu2.id = '002'
# stu2.name = 'kiki'

# print(stu1.id)
# print(stu2.id)

# Constructor
'''
                           parameters
    def __init__(self, number, client, balance) :
        self.number = number
        self.client = client
        self.balace = balance
-- Instance Attributes -- Values
'''

# class Student :
#     def __init__(self, id, name) :
#         self.id = id
#         self.name = name

# stu1 = Student('001', 'koko')
# stu2 = Student('002', 'booboo')
# print(stu1.id)
# print(stu2.id)

# Instance
#   <variable> = <ClassName>(<arguments>)

# Class Relation
# class Student :
#     def __init__(self, id, name) :
#         self.id = id
#         self.name = name

# class Subject :
#     def __init__(self, sub_id, sub_name) :
#         self.sub_id = sub_id
#         self.sub_name = sub_name
#         self.student_list = []

# stu1 = Student('001', 'Pink')
# stu2 = Student('004', 'kiki')
# sub1 = Subject('90xxxx', 'Sports')

# sub1.student_list.append(stu1)
# sub1.student_list.append(stu2)

# print(sub1.student_list)

# How to create class
# class Employee :

#     # How to create method
#     def detail(self, name, salary) :
#         self.name = name
#         self.salary = salary
#         self.team = "Accounting"
#         print("Name : {}".format(self.name))
#         print("Salary : {}".format(self.salary))
#         print("Team : {}".format(self.team))
# # How to create object
# obj1 = Employee()
# obj1.detail("Pink", 24000)

# obj2 = Employee()
# obj2.detail("kiki", 50000)

# obj3 = Employee()
# obj3.detail("booboo", 75000)

# How to create constructor
# class Employee :

#     # def detail(self, name, salary) :
#     #     self.name = name
#     #     self.salary = salary
#     #     self.team = "Accounting"
#     #     print("Name : {}".format(self.name))
#     #     print("Salary : {}".format(self.salary))
#     #     print("Team : {}".format(self.team))
    
#     def __init__(self, name, salary) :
#         self.name = name
#         self.salary = salary
#         self.team = "Accounting"
        
#     def show_data(self) :
#         print("Name : {}".format(self.name))
#         print("Salary : {}".format(self.salary))
#         print("Team : {}".format(self.team))

# obj1 = Employee()
# obj1.detail("Pink", 24000)

# obj2 = Employee()
# obj2.detail("kiki", 50000)

# obj3 = Employee()
# obj3.detail("booboo", 75000)
        
# obj1 = Employee("Pink", 24000)
# # change data
# obj1.salary = 100000
# obj1.show_data()
# obj2 = Employee("kiki", 50000)
# obj2.show_data()
# obj3 = Employee("booboo", 75000)
# obj3.show_data()

# More function

# class Employee :
    
#     def __init__(self, name, salary) :
#         self.name = name
#         self.salary = salary
#         self.team = "Accounting"
        
#     def show_data(self) :
#         print("Name : {}".format(self.name))
#         print("Salary : {}".format(self.salary))
#         print("Team : {}".format(self.team))

# obj1 = Employee("Pink", 24000)
# # change data
# obj1.salary = 100000
# obj1.show_data()
# obj2 = Employee("kiki", 50000)
# obj2.show_data()
# obj3 = Employee("booboo", 75000)
# obj3.show_data()

# # check is the instance in <class> ?
# print(isinstance(obj1, Employee))
# print(isinstance(obj1, int))

# # dir
# print(dir(obj1))

# # check obj1 is from what class
# print(obj1.__class__)