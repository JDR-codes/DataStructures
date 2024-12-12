class Snode:
    def __init__(self,data):
        self.data=data
        self.add=None

class SCLL:
    def __init__(self):
        self.head=None

    def Create_node(self,data):
        node=Snode(data)
        return node
    
    def Add_first(self,data):
        node=self.Create_node(data)
        if self.head==None:
            self.head=node
            node.add=self.head
        else:
            node.add=self.head
            ptr=self.head
            while ptr.add!=self.head:
                ptr=ptr.add
            ptr.add=node
            self.head=node

    def __str__(self):
        res=''
        ptr=self.head
        while ptr!=None:
            res+=str(ptr.data) + ','
            ptr=ptr.add
            if ptr==self.head:
                break
        res=res.strip(',')
        return '['+res+']'
    
    def Add_last(self,data):
        node=self.Create_node(data)
        if self.head==None:
            self.head=node
            node.add=self.head
        else:
            ptr=self[-1]
            ptr.add=node
            node.add=self.head    
    def __getitem__(self,index):
        if index<0:
            index=index+len(self)
        count=0
        ptr=self.head
        while True:
            if index==count:
                return ptr
            ptr=ptr.add
            count+=1
            if ptr==self.head:
                break
        raise IndexError

    def __setitem__(self,index,new):
        self[index].data=new

    def __len__(self):
        if self.head==None:
            return 0
        count=0
        ptr=self.head
        while True:
            ptr=ptr.add
            count+=1
            if ptr==self.head:
                break
        return count


    def insert(self,index,val):
        if index==0:
            self.Add_first(val)
        elif index>len(self)-1:
            self.Add_last(val)
        else:
            node=self.Create_node(val)
            prev=self[index-1]
            next=self[index]
            prev.add=node
            node.add=next

    def Del_first(self):
        if self.head==None:
            raise IndexError
        elif len(self)==1:
            ptr=self.head
            self.head=None
            print(ptr.data)
            del ptr
        
        else:
            ptr=self.head
            last=self[-1]
            last.add=self.head.add
            self.head=self.head.add
            print(ptr.data)
            del ptr
    
    def Del_last(self):
        if self.head==None:
            raise IndexError
        elif len(self)==1:
            ptr=self.head
            self.head=None
            print(ptr.data)
            del ptr
        else:
            ptr=self[-1]
            last=self[-2]
            last.add=self.head
            print(ptr.data)
            del ptr

o1=SCLL()
o1.Add_first(10)
# o1.Add_first(20)
# o1.Add_first(30)
# o1.Add_first(40)
# o1.Add_last(60)
# o1.Add_last(70)
# print(o1)
# # print(o1[0])
# o1[2]=50
# print(o1)
# print(len(o1))
# o1.insert(2,90)
# print(o1)
# o1.Del_first()
# print(o1)
# # o1.Del_first()
# # print(o1)
# o1.Del_last()
# print(len(o1))
# print(o1)

o1.Del_last()
print(o1)