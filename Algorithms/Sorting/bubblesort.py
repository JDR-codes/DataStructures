def bubblesort(coll):
    for Pass in range(1,len(coll)):
        for i in range(len(coll)-Pass):
            if coll[i]>coll[i+1]:
                coll[i],coll[i+1]=coll[i+1],coll[i]

a=[3,1,15,11,9,2]
print(a)
bubblesort(a)
print(a)