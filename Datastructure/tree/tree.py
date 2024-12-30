class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_node(self,data):
        if data==self.data:
            return
        elif data<self.data:
            if self.left==None:
                self.left=BST(data)
            else:
                self.left.add_node(data)
        else:
            if self.right==None:
                self.right=BST(data)
            else:
                self.right.add_node(data)
# '''Depth First Search'''
    def IOT(self,r):
        if r==None:
            return 
        self.IOT(r.left)
        print(r.data,end=' ')
        self.IOT(r.right)

    def PREOT(self,r):
        if r==None:
            return 
        print(r.data,end=' ')
        self.PREOT(r.left)
        self.PREOT(r.right)

    def POSTOT(self,r):
        if r==None:
            return 
        self.POSTOT(r.left)
        self.POSTOT(r.right)
        print(r.data,end=' ')


# Bredth First Search

    def BFS(self):
        Q=[self]
        while Q:
            var=Q.pop(0)
            print(var.data,end=' ')
            if var.left!=None:
                Q.append(var.left)
            if var.right!=None:
                Q.append(var.right)
    
    def BSearch(self,val):
        var=self
        if self==None:
            return False
        if self.data==val:
            return True
        elif val<self.data:
            return self.left.BSearch(val)
        else:
            return self.right.BSearch(val)
            
            

o1=BST(50)
o1.add_node(25)
o1.add_node(30)
o1.add_node(90)
o1.add_node(60)

o1.IOT(o1)
print()
o1.PREOT(o1)
print()
o1.POSTOT(o1)
print()
o1.BFS()
print()
print(o1.BSearch(40))
# print(o1.data)
# print(o1.left)
# print(o1.right)
# print()
# print(o1.left.data)
# print(o1.left.left)
# print(o1.left.right)
# print()
# print(o1.right.data)
# print(o1.right.left)
# print(o1.right.right)