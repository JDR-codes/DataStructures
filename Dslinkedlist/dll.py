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

s1=Dnode(10)
s2=Dnode(20)
s3=Dnode(30)
s4=Dnode(40)
s1.set_next(s2)