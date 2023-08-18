import random as ran
a=True
b=ran.randint(1,5)
while a:
    c=int(input("Try to guess the random number enter here "))
    if(c==b):
        print("Correct guess")
        break
    elif(c<b):
        print("The number chosen is less than the random number ")
    else:
        print("The number chosen is more than the random number")
