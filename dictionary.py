menu={"Biriyani":500,"Tandoori":400,"Pasta":120,"Tea":10,"program":[100,200,300]}
print(menu)
print(menu["Biriyani"])
print(menu.get("Tea"))
print(menu["program"][1])
print(menu.keys()) #the keys are displayed
print(id(menu)) # id of a variable
menu["coffee"]=20 # adding another element in dictionry
print(menu)
menu["Pasta"]=230
print(menu)
print(menu.values())# values are displayed
menu.update({"Tea":15})# updating a key value pair using update 
print(menu)
menu.pop("Pasta")
print(menu)
#menu.pop()# error needs atleast one arguement
#print(menu)
#del menu["Biriyani"] biriryani pair is deleted
#del menu delete the entire dictionary
for x in menu:
    print(x)
for x in menu.values():
    print(x)
for x in menu.items():
    print(x)
menu1=menu.copy()
print(menu1)# menu1=dict(menu) used for copying

def f(x,y):
    print( x+" "+y) 

d={"a":"Christ","b":"University"}
f(d["a"],d["b"])



