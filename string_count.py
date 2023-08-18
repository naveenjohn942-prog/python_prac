def countbase(seq):
    
    a=seq.count("A")
    c=seq.count("C")
    g=seq.count("G")
    t=seq.count("T")
    dict={"A":a,"C":c,"G":g,"T":t}
    print(dict)

seq=input("Enter your DNA sequence ")
countbase(seq)



