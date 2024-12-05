def Linearserch(data,coll):
    for i in range(len(coll)):
        if coll[i]==data:
            return i
        
    return -1
        
print(Linearserch(40,[10,20,30]))
