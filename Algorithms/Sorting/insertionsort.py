def insertionsort(coll):
    for Pass in range(1,len(coll)):
        key=coll[Pass]
        i=Pass-1
        while i>=0 and key<coll[i]:
            coll[i+1]=coll[i]
            i-=1
        coll[i+1]=key

a=[15,58,-1,60,20]
print(a)
insertionsort(a)
print(a)