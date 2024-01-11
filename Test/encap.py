
# class Employee :
#     def __init__(self, name, salary, department) :
        # public attribute
        # self.name = name
        # self.salary = salary
        # self.department = department

        # protected attribute
        # self._name = name
        # self._salary = salary
        # self._department = department
        # self._showData()

        # private attribute
        # self._name = name # protected
        # self.__salary = salary
        # self.__department = department
        # self.__showData()

        # self.__name = name
        # self.__salary = salary
        # self.__department = department

    # public method
    # def showData(self) :
    #     print("Name : {}".format(self.name))
    #     print("Salary : {}".format(self.salary))
    #     print("Department : {}".format(self.department))
        
    # protected method
    # def _showData(self) :
        # print("Name : {}".format(self._name))
        # print("Salary : {}".format(self._salary))
        # print("Department : {}".format(self._department))

    # private method
    # def __showData(self) :
    #     print("Name : {}".format(self._name))
    #     print("Salary : {}".format(self.__salary))
    #     print("Department : {}".format(self.__department))
        
    # def _showData(self) :
        # print("Name : {}".format(self.__name))
        # print("Salary : {}".format(self.__salary))
        # print("Department : {}".format(self.__department))
        # print("Name : {}".format(self.getName()))
        # print("Salary : {}".format(self.getSalary()))
        # print("Department : {}".format(self.getDepartment()))

    # create setter to change the data in private
        # setter method
    # def setName(self, newname) :
    #     self.__name = newname

    # def setSarlary(self, newsalary) :
    #     self.__salary = newsalary
    
    # def setDeparment(self, newdepartment) :
    #     self.__department = newdepartment

    # # getter method
    # def getName(self) :
    #     return self.__name
    
    # def getSalary(self) :
    #     return self.__salary
    
    # def getDepartment(self) :
    #     return self.__department
    
# obj1 = Employee("Pink", 20000, "Accounting")
# obj2 = Employee("kiki", 35000, "Programmer")
# obj3 = Employee("kuku", 50000, "Manager")
# print(obj1.__class__)
# obj1._name = "booboo"
# print(obj1._name)
# obj1._showData()
# obj1.__salary = 60000 # private cannot change
# obj1.setName("bobo")
# obj1.setSarlary(75000)
# obj1.setDeparment("Boss")
# obj1._showData()
    
# obj1 = Employee("Pink", 20000, "Accounting")
# print(obj1.getName())
# print("Department = {}".format(obj1.getDepartment()))
# obj1._showData()
# print(obj1.__department)
        