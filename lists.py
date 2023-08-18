li=["Biriyani","TAndoori","Burger","Pizza","Pasta"]
print(li[1])
print(li[1:5])
print(li[:4])
print(li[1:])
if "Pasta" in li:
    print("Pasta is here")
for x in li:
    print(x)
print(li)

li.append("Tea")
print(li)
li.insert(2,"Coffee")
print(li)
li.remove("Burger")
print(li)
a=[1,2,3,4,5,5]
a.extend(li)
print(a)

prices=(200,400,210,120,500)
li.extend(prices) # we cant assign a new variblal here it will show error 
print(li)
list=["Biriyani","TAndoori","Burger","Pizza","Pasta"]
newlist=[print(x) for x in list]
print(newlist)
newlst=[x for x in list]
print(newlst)
#newlst is a new list
newlist=[x for x in list if 'a' in x]
print(newlist)
newlist=[x  if x!="Burger" else "orange" for x in list]
print(newlist)
