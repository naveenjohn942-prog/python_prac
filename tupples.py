food_items=("Biriyani","TAndoori","Burger","Pizza","Pasta")
prices=(200,400,210,120,500)
todays_special=("Alfredo Pasta","Makhani Chicken Burger","Aloo Paratha")
type(food_items)
type(prices)
print(food_items)
print(prices[2:5])
print(todays_special[:2])
print(food_items[1:])
if "Biriyani" in food_items:
    print("Yes it is avaiable")
else:
    print("It is not here")
print(id(prices))
print(id(food_items))
print(id(todays_special))
food_items=prices+food_items
print(prices*3) #repeating 3 times
print(len(food_items))
print(prices[-2])
print(sum(prices))
print(max(prices))
print(min(prices))
s=0
for i in prices:
    s=s+i
print(s)
x=range(3,10,2)
for i in x:
    print(i)

del prices
print(prices)
