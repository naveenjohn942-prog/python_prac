#class is a uder defined data type class won't occupy any memory
class Account:
    pass# statement that does nothing
a1=Account()#class data type
a2=Account()
a1.name="John"
a1.balance=1000
a2.surname="Marina"
a2.value=100010
a2.balance=0
print(Account)
print(a1)
print(a2)
print(a1.name)
print(a1.balance)
print(a2.surname)
print(a2.value)
print(a2.balance)
print(id(a1))
print(id(a1.balance))
 #del a1.balance deleting the attribute balance of the object a1
