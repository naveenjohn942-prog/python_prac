salary={1000,2000,45000,20000,10000,1000}
for x in salary:
    print(x)
print(len(salary))
salary.update("IJK")
print(salary)
pg=[1,1,2,1,3,4,5,6]
salary.update(pg)
print(salary)
salary.add("JOKER")
print(salary)
salary.add(1000)
print(salary)
#salary.add(pg)
#print(salary) wont work list cant be done like this tuple can be
tup=(1,2,3,4,5,6)
salary.add(tup)
print(salary)
salary.pop()
print(salary)
salary.remove(1000)
print(salary)
salary.discard("IJK")
#salary.remove("IJK") will throw error
print(salary)
salary.discard("IJK")
print(salary)
salary={10,20,40,79,-58,0}
print(max(salary))
print(min(salary))
print(sum(salary))
print(sorted(salary))
s={45,74,0}
print(all(s))
print(any(s))
print(id(s))
s.add(2)
print(id(s))
salary=frozenset({10,20,30,40,50})
print(id(salary))
#salary.add(78) error 
print(id(salary))
salary=frozenset({10,20,30,40,50})
course=frozenset({40,50,60,100})
uni=salary.union(course)
inter=salary.intersection(salary)
diff=salary.difference(salary)
diff01=salary.symmetric_difference(salary)
print(uni)
print(inter)
print(diff)
print(diff01)
