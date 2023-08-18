li=[1,2,3,4,45,12,0,54,75]
n=int(input("Enter the number "))
if(n in li):
    for x in range(1,11):
        print(n," * ",x," = ",n*x)
else:
    if(n>=len(li)):
        print("Enter value between 0 and ",len(li))
    else:
        print(li[n])
