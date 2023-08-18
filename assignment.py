import math
import cmath
print(1+3*2-5+4)
print(1+3*(2-5)+4)
print(5**2**2*3+1)
print(5**(2**2)*3+1)
print(1+3/2)


print("Right side")
#10^5
print(10**5)
#root over 10
print(math.sqrt(10))
#lg(2+root 5)
print(math.log10(2+math.sqrt(5)))
#area of the circle r=5.5
print(math.pi*5.5*5.5)
#sin 2.5
print(math.sin(2.5))
#x2-7x+10=0 roots
a=1
b=-7
c=10
num1=-b+math.sqrt(b*b-4*a*c)
num2=-b-math.sqrt(b*b-4*a*c)
den=2*a
root1=num1/den
root2=num2/den
print("The roots are ",root1," ",root2)

#the complex roots fr x2-2x+10=0
a=1
b=-2
c=10
num1=-b+cmath.sqrt(b*b-4*a*c)
num2=-b-cmath.sqrt(b*b-4*a*c)
den=2*a
root1=num1/den
root2=num2/den
print("The roots are ",root1," ",root2)

#4!
print(math.factorial(4))
#sum of k from 32 to 128
s=0
for i in range(32,128):
    s=s+i
print(s)
s=0
#product of k from 3 to 17
for i in range(3,17):
    s=s*i
print(s)

