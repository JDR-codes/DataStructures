def selectionsort(coll):
    for Pass in range(1,len(coll)):
        min=Pass-1
        for i in range(Pass,len(coll)):
            if coll[i]<coll[min]:
                min = i
        coll[min],coll[Pass-1]=coll[Pass-1],coll[min]

a=[65,13,90,34,21,45]
print(a)
selectionsort(a)
print(a)