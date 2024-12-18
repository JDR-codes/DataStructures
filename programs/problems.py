'''-------Linked List------'''
class Snode:
    def __init__(self,data):
        self.data=data
        self.add=None

head1=Snode(10)
head1.add=Snode(50)
head1.add.add=Snode(30)
head1.add.add.add=Snode(40)
head1.add.add.add.add=Snode(20)

head2=Snode(100)
head2.add=Snode(200)
head2.add.add=Snode(500)
head2.add.add.add=Snode(300)
head2.add.add.add.add=Snode(400)


'''1.caf to  print the data in linkedlist'''
def traverse(head):
    while head!=None:
        print(head.data,end=' ')
        head=head.add

# traverse(head)

'''2.caf to reverse the gn linked list'''
def Reverse(ptr):
    prev=None
    curr=ptr
    while curr!=None:
        next=curr.add
        curr.add=prev
        prev=curr
        curr=next
    return ptr

# Reverse(head)
# print()
# traverse(head)

'''Caf to return the length of the given linked list'''
def length(ptr):
    count=0
    while ptr!=None:
        count+=1
        ptr=ptr.add
    return count
'''Caf to print the middle value in the gn linked list'''

def mid_val(ptr):
    count=len(ptr)
    mid=count//2
    index=0
    while ptr!=None:
        if index==mid:
            return (ptr.data)
        else:
            index+=1
            ptr=ptr.add


# print(mid_val(head1))

'''Caf to merge multiple singly linked list in a sorted order'''

def Merge(*a):
    l=[]
    for i in a:
        while i!=None:
            l.append(i.data)
            i=i.add
    l.sort()
    
    head=Snode(None)
    temp=head
    j=0
    while j<len(l):
        temp.add=Snode(l[j])
        temp=temp.add
        j+=1
    
    head=head.add
    return head


# traverse(Merge(head1,head2))

'''Caf to remove the mentioned value from the given linked list'''
def remove(ptr,val):
    prev=None
    curr=ptr
    while curr!=None:
        if val==curr.data:
            if prev==None:
                del curr
                return ptr.add
            else:
                prev=curr.add
                print(curr.data)
                del curr
                return 
        else:
            prev=curr
            curr=curr.add
    raise ValueError

# remove(head1,20)

'''Caf to remove the last occurance of the given linked list'''

def remove_last(ptr,val):
    curr=ptr
    count=0
    while curr!=None:
        if curr.data==val:
            count+=1
        curr=curr.add

    if count==0:
        raise ValueError

    prev=None
    temp=ptr
    while temp!=None:
        if temp.data==val and count==1:
            if prev==None:
                del temp
                return ptr.add
            else:
                prev=temp.add
                print(temp.data)
                del temp
                return ptr
        elif temp.data==val:
            count-=1
        else:
            prev=temp
            temp=temp.add

head3=Snode(1)
head3.add=Snode(2)
head3.add.add=Snode(1)
head3.add.add.add=Snode(1)

remove_last(head3,1)
traverse(head3)

