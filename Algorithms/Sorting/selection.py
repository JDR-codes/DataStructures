def sortred_ele(coll,low,high):
    pivot=coll[low]
    i=low+1
    j=high
    while i<=j:
        while i<=j and coll[i]<pivot:
            i+=1
        while i<=j and coll[j]>pivot:
            j-=1
    
        # if i<=j:
        #     l[i],l[j]=l[j],l[i]
        #     i+=1
        #     j-=1 
    
    
    coll[j],coll[low]=coll[low],coll[j]
    return j

def Selectionsort(coll,low,high):
    if low>=high:
        return
    j=sortred_ele(coll,low,high)
    Selectionsort(coll,low,j-1)
    Selectionsort(coll,j+1,high)

l=[65,-2,-15,100,81,72,67]
print(l)
Selectionsort(l,0,len(l)-1)
print(l)