from abc import ABC, abstractmethod
class Shape():
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def area(self):
        return self.l*self.b

class Triangle(Shape):
    def __init__(self,x,y):
        self.b=x
        self.h=y
    def area(self):
        return 0.5*self.b*self.h
ob=Rectangle(10,5)
print(ob.area())

ob1=Triangle(8,9)
print(ob1.area())