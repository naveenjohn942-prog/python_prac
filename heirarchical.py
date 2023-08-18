class School:
    def __init__(self,schoolname):
        self.schoolname=schoolname
    def display(self):
        print("School Name ",self.schoolname)
        print("Department Name ",self.departmentname)
class Department1(School):
    def __init__(self,schoolname,departmentname):
        self.departmentname=departmentname
        School.__init__(self,schoolname)
class Department2(School):
    def __init__(self,schoolname,departmentname):
        self.departmentname=departmentname
        School.__init__(self,schoolname)
class Department3(School):
    def __init__(self,schoolname,departmentname):
        self.departmentname=departmentname
        School.__init__(self,schoolname)
ob1=Department1("School of Sciences","Computer Science")
ob1.display()
ob2=Department2("School of Sciences","Physics")
ob2.display()
ob3=Department3("School of Sciences","Mathematics")
ob3.display()
