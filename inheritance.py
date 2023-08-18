class Account:
    def __init__(self,name,number,balance=0):#default constructor
        self.name=name
        self.number=number
        self.balance=balance
    def deposit(self,amount): #self is representing the object who is calling the function
        if amount<=0:
            print("Error, negative amount")
        else:
            self.balance=self.balance+amount
    def withdraw(self,amount):
        if(amount<0):
            print("Error, negative amount")
            return
        if(amount>self.balance):
            print("Error, insuffecient fund")
            return
        self.balance-=amount
    def __str__(self):# default display
        return ("Name ",self.name," Number ",self.number," Balance ",self.balance)
    def display(self):
        print("Name ",self.name," Number ",self.number," Balance ",self.balance)
    
a=Account("Asher",100001,25000)
a.deposit(5000)
a.withdraw(100)
a.display()
#sub class
class CreditAccount(Account):
    pass
a1=Account("Naina",100002,35000)
a2=CreditAccount("Manav",100004,5000)
a2.display()
a1.display()
