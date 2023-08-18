dic={"Ethernet()":["1.1.1.1","up"],"Ethernet1":["2.2.2.2","down"],"Serial()":["3.3.3.3","up"],"Serial1":["4.4.4.4","up"]}
interface=input("Enter the interface ")
for x in dic:
    if(x==interface):
        print(dic[interface][1])
    else:
        print("Wrong Interface")
for x in dic:#keys are navigated here
    if(dic[x][1]=="up"):
        print(x,dic[x][0])
count=0
for x in dic:
    if(x=="Ethernet()"):
        count=count+1

print(count)

#for key,val in dic.items():