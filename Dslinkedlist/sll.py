class Snode:
    def __init__(self,data):
        self.data=data
        self.add=None
    def get_data(self):
        return self.data
    def get_add(self):
        return self.add
    def set_data(self,new):
        self.data=new
    def set_add(self,new):
        self.add=new

class Sll:
    def __init__(self):
        self.head=None

    def Create_node(self):
        data=eval(input('Enter the value:'))
        node=Snode(data)
        return node

    def Add_first(self):
        node=self.Create_node()
        if self.head==None:
            self.head=node
        else:
            node.set_add(self.head)
            self.head=node

    def Add_last(self):
        node=self.Create_node()
        if self.head==None:
            self.head=node
        else:
            ptr=self.head
            while ptr.get_add()!=None:
                ptr=ptr.get_add()

            ptr.set_add(node)

    def display(self):
        ptr=self.head
        while ptr!=None:
            print(ptr.get_data(),end='')
            ptr=ptr.get_add()

    def __len__(self):
        count=0
        ptr=self.head
        while ptr!=None:
            count+=1
            ptr=ptr.get_add()
        return count

    def __getitem__(self,index):
        count=0
        ptr=self.head
        while ptr!=None:
            if count==index:
                return ptr
            else:
                count+=1
                ptr=ptr.get_add()
        raise IndexError

    def __setitem__(self,index,new):
        var=self[index]
        var.set_data(new)

    def insert(self,index):
        if index==0:
            self.Add_first()
        elif index>=len(self)-1:
            self.Add_last()
        else:
            node=self.Create_node()
            prv=self[index-1]
            nxt=self[index]
            prv.set_add(node)
            node.set_add(nxt)
    
    def del_first(self):
        if self.head==None:
            raise IndexError
        else:
            ptr=self.head
            self.head=ptr.get_add()
            del ptr

    def del_last(self):
        if self.head==None:
            raise IndexError
        else:
            ptr=self[len(self)-1]
            prv=self[len(self)-2]
            prv.set_add(None)
            del ptr

    def remove(self,index):
        if index==0:
            self.del_first()
        elif index==len(self)-1:
            self.del_last()
        elif index>len(self):
            raise IndexError
        else:
            prv=self[index-1]
            ptr=self[index]
            prv.set_add(ptr.get_add())
            del ptr

    def sort(self):
        for Pass in range(1,len(self)):
            for i in range(len(self)-Pass):
                if self[i].get_data()>self[i+1].get_data():
                    a=self[i].get_data()
                    self[i].set_data(self[i+1].get_data())
                    self[i+1].set_data(a)
    
    def __str__(self):
        result=''
        ptr=self.head
        while ptr!=None:
            result+=str(ptr.get_data()) + ', '
            ptr=ptr.get_add()
        result=result.strip(', ')
        return '['+result+']'


        
        

        
s1=Sll()
s1.Add_first()
s1.Add_first()
s1.Add_first()
s1.Add_first()
s1.Add_last()
s1.Add_last()
print()
s1.display()
# print()
# print(len(s1))
print()
# print(s1[2])
# s1.insert(2)
# s1.display()
# s1.del_first()
# s1.display()
# print()
# s1.del_last()
# s1.display()
# print()
# s1.remove(3)
# s1.display()
print(s1.sort())
s1.display()
print()
print(s1)