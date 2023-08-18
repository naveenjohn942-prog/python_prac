class School:
    def __init__(self, schoolname):
        self.schoolname=schoolname
    def print_name(self):
        print("School name:- ",self.schoolname)
        print("Department name:- ",self.dep)


class Department1(School):
    def __init__(self, dep,schoolname):
        self.dep=dep
        School.__init__(self, schoolname)


obj=Department1("Department of Computer Science","School Of Sciences")
print(obj.schoolname)
obj.print_name()
obj1=School("School of Sciences")
#obj1.print_name() #will throw error

