#wrong code
class Department1:
    def __init__(self,departmentname1):
        self.departmentname1=departmentname1
class Department2(Department1):
    def __init__(self,departmentname1,departmentname2):
        self.departmentname2=departmentname2
        Department1.__init__(departmentname1)
class old(Department2):
    def __init__(self,departmentname1,departmentname2,old):
        self.old=old
        Department2.__init__(self,departmentname1,departmentname2)

    def print(self):
        print("Department 1 is ",self.departmentname1)
        print("Department 2 is ",self.departmentname2)
        print("Number of years old ",old)

obj=old("Computer Science Department","Sociology Department",52)
obj.print()
