class Account:
    def __init__(self,name,number,balance=0):#default constructor
        self.name=name
        self.number=number
        self.balance=balance
    def deposit(self,amount): #self is representing the object who is calling the function
        self.balance=self.balance+amount
    def __str__(self):# default display
        return ("Name ",self.name," Number ",self.number," Balance ",self.balance)
    def display(self):
        print("Name ",self.name," Number ",self.number," Balance ",self.balance)
a=Account("James",14501,56000)# arguements are present in class constrcutor thats why i have to write it here otherwise I can not write __init__ and Account() just that
a.balance=1000
a.deposit(1000)
print(a.balance)
#Account.deposit(a,100) explicit way to call the function
#Constructor
a1=Account("John",100014,250000)
a1.deposit(45000)
a1.display()
print(a1.__doc__)
print(a1.__dict__)
print(a1.__module__)
print(a1)# for default display