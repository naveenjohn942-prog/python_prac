print("Savings Calculator")
rate=float(input("please enter the ineterest rate "))
years=int(input("PLease enter the number of years "))
init=float(input("Enter the initial sum of the money "))
final=init*(1.0+rate)**years
print("After %d years the savings will be Rs %.2f" %(years,final))
