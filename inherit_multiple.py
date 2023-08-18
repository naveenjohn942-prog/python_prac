class Department1:
    def __init__(self,departmentname):
        self.departmentname=departmentname
class Department2:
    def __init__(self,departmentname):
        self.departmentname=departmentname
class old(Department1,Department2):
    def __init__(self,departmentname1,departmentname2):
        self.departmentname1=departmentname1
        self.departmentname2=departmentname2
        Department1.__init__(self,departmentname1)
        Department2.__init__(self,departmentname2)

    def print(self):
        print("Department 1 is ",self.departmentname1)
        print("Department 2 is ",self.departmentname2)

obj=old("Computer Science Department","Sociology Department")
obj.print()
