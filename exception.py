def f(x):
    try:
        print(1/x)
    except ZeroDivisionError:
        print("Division by Zero")
    except (TypeError,ValueError):
        print("Type or Value Error")

f(0)
f(1)
l=[1,2,3,4]
try:
    print(l[5])#IndexError
except IndexError:
    print("Wrong index provided Please write the correct Index Value")
finally:
    print("happy programming!")
    
