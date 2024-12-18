class Dnode:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Dcll:
    def __init__(self):
        self.head=None
        self.tail=None

    def Create_node(self,data):
        node=Dnode(data)
        return node

    def Add_first(self,data):
        node=self.Create_node(data)
        if self.head==None:
            self.head=node
            self.tail=node
            node.next=node
        else:
            self.head.prev=node
            node.next=self.head
            self.tail.next=node
            self.head=node

    def Add_last(self,data):
        node=self.Create_node(data)
        if self.head==None:
            self.head=node
            self.tail=node
            self.head.next=node
        else:
            self.tail.next=node
            node.prev=self.tail
            node.next=self.head
            self.tail=node
        
    def __str__(self):
        res=''
        ptr=self.head
        while ptr!=None:
            res+=str(ptr.data)+','
            ptr=ptr.next
            if ptr==self.head:
                break
        res=res.strip(',')
        return '['+res+']'
    
    def __len__(self):
        count=0
        ptr=self.head
        while True:
            count+=1
            ptr=ptr.next
            if ptr==self.head:
                break
        return count
    
    def __getitem__(self,index):
        if index<0:
            index+=len(self)
        
        count=0
        ptr=self.head
        while True:
            if count==index:
                return ptr
            else:
                count+=1
                ptr=ptr.next
                if ptr==self.head:
                    break
    
    def __setitem__(self,index,val):
        self[index].data=val

    def insert(self,index,data):
        if index<0 and index>-len(self):
            index+=len(self)
        if index==0 or index <=-len(self):
            self.Add_first(data)
        elif index >len(self)-1:
            self.Add_last(data)
        else:
            node=self.Create_node(data)
            prev=self[index-1]
            next=self[index]
            prev.next=node
            node.prev=prev
            node.next=next
            next.prev=node

    def Del_first(self):
        if self.head==None:
            raise IndexError
        elif len(self)==1:
            ptr=self.head
            self.head=None
            self.tail=None
            print(ptr.data)
            del ptr
        else:
            ptr=self.head
            next=ptr.next
            next.prev=None
            self[-1].next=next
            self.head=next
            print(ptr.data)
            del ptr
    
    def Del_last(self):
        if self.head==None:
            raise IndexError
        elif len(self)==1:
            ptr=self.head
            self.head=None
            self.tail=None
            print(ptr.data)
            del ptr
        else:
            ptr=self.tail
            prev=ptr.prev
            prev.next=self.head
            self.tail=prev
            print(ptr.data)
            del ptr

    def Delete(self,index):
        if index<0:
            index+=len(self)
        if index==0:
            self.Del_first()
        elif index==len(self)-1:
            self.Del_last()
        elif index>len(self)-1:
            raise IndexError
        else:
            ptr=self[index]
            prev=ptr.prev
            next=ptr.next
            prev.next=next
            next.prev=prev
        
    def Search(self,low,high,val):
        si=low
        ei=high
        while si<=ei:
            mid=(si+ei)//2
            if self[mid].data==val:
                return True
            elif val<self[mid].data:
                ei=mid-1
            elif val>self[mid].data:
                si=mid+1
        return False






o1=Dcll()

o1.Add_first(70)
o1.Add_first(60)
o1.Add_first(50)
o1.Add_first(40)
o1.Add_first(30)
o1.Add_first(20)
o1.Add_first(10)



# print(o1)
# print()
# print(len(o1))
# print()
# o1[3]=80
# print(o1)
# o1.insert(6,90)
# print()
# print(o1)
# print(len(o1))
# o1.Del_first()
# print(o1)
# print()
# o1.Del_last()
# o1.Del_last()
# print(o1)
# o1.Delete(2)
# print(o1)
# o1.Delete(-3)
print(o1)
print(o1.Search(0,6,10))

