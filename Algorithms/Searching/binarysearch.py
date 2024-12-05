def Binarysearch(coll,val):
    si=0
    ei=len(coll)-1
    while si<=ei:
        mid=(si+ei)//2
        
        if val>coll[mid]:
            si=mid+1
        elif val<coll[mid]:
            ei=mid-1
        else:
            return mid
    return -1


print(Binarysearch([10,20,30,40,50,60],60))