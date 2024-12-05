class Dnode:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
    def get_prev(self):
        return self.prev
    def set_prev(self,new):
        self.prev=new
    def get_next(self):
        return self.next
    def set_next(self,new):
        self.next=new
    def get_data(self):
        return self.data
    def set_data(self,new):
        self.data=new

class Dll:
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
        else:
            self.head.set_prev(node)
            node.set_next(self.head)
            self.head=node

    def __str__(self):
        res=''
        a=self.head
        while a!=None:
            res+=str(a.get_data())+','
            a=a.get_next()
        res=res.strip(',')
        return '['+res+']'
    

    def Add_last(self,data):
        node=self.Create_node(data)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail)
            self.tail=node
    
    def __len__(self):
        count=0
        ptr=self.head
        while ptr!=None:
            count+=1
            ptr=ptr.get_next()
        return count
    
    def __getitem__(self,index):
        count=0
        if index<0:
            index=len(self)+index
        ptr=self.head
        while ptr!=None:
            if count==index:
                return ptr
                break
            else:
                count+=1
                ptr=ptr.get_next()

    def __setitem__(self,index,new):
        self[index].set_data(new) 

    def insert(self,index):
        if index==0:
            self.Add_first(eval(input('Enter data:')))
            self.head=node
        elif index>=len(self)-1:
            self.Add_last(eval(input('Enter data:')))
            self.tail=node
        else:
            node=self.Create_node(eval(input('Enter data:')))
            prev=self[index-1]
            next=self[index]
            prev.set_next(node)
            node.set_prev(prev)
            node.set_next(next)
            next.set_prev(node)

    def Del_first(self):
        if self.head==None:
            raise IndexError
        else:
            ptr=self.head
            self.head=ptr.get_next()
            del ptr

    def Del_last(self):
        if self.head==None:
            raise IndexError
        else:
            ptr=self.tail
            prev=self[len(self)-2]
            prev.set_next(None)
            self.tail=prev
            del ptr

    def remove(self,index):
        if index>len(self):
            raise IndexError
        elif index==0:
            self.Del_first()
        elif index==len(self)-1:
            self.Del_last()
        else:
            ptr=self[index]
            prev=self[index-1]
            next=self[index+1]
            prev.set_next(next)
            next.set_prev(next)
            del ptr


    def sort(self):
        for Pass in range(1,len(self)):
            for i in range(len(self)-Pass):
                if self[i].get_data()>self[i+1].get_data():
                    a=self[i].get_data()
                    b=self[i+1].get_data()

                    self[i].set_data(b)
                    self[i+1].set_data(a)


o1=Dll()
o1.Add_first(10)
o1.Add_first(20)
o1.Add_first(30)
o1.Add_first(40)
o1.Add_last(50)
o1.Add_last(60)
o1.Add_last(70)
print(o1)
print(len(o1))
# print(o1[-1])
o1[2]=90
print(o1)
# o1.insert(3)
# print(o1)
# o1.Del_first()
# print(o1)
# o1.Del_last()
# print(o1)
# o1.remove(3)
# print(o1)
o1.sort()
print(o1)