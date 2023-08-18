f=lambda x,y,z=0,w=0:x+2*y+3*z+4*w
print(f(1,2))
print(f(1,2,3))
print(f(1,2,w=3))
ex=lambda x=2,y=3:x*x*x+y*y*y+5
print(ex())
