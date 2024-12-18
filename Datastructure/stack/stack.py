'''Dynamic length stack using list'''
class StackUnderflow(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack=[]
        self.top=0

    def push(self,data):
        self.stack.append(data)
        self.top+=1

    def pop(self):
        if self.top==0:
            raise StackUnderflow('Deleting from a empty stack')
        else:
            var=self.stack.pop()
            self.top-=1
            return var
        
    def peek(self):
        return self.stack[self.top-1]
    

    
s1=Stack()
s1.push(1)
s1.push(2)
s1.push(3)

# print(s1.stack)
# print(s1.pop())
# print(s1.peek())
# print(s1.pop())
# print(s1.pop())
# print(s1.pop())


'''Fixed length stack using list'''
class StackUnderflow(Exception):
    pass

class StackOverflow(Exception):
    pass

class Fstack:
    size=3
    def __init__(self):
        self.stack=[]
        self.top=0

    # def push(self,data):
    #     if  self.size==self.top:
    #         raise StackOverflow
    #     else:
    #         self.stack.append(data)
    #         self.top+=1

    def push(self,data):
        if self.size==self.top:
            self.stack.pop()
            self.stack.append(data)
        else:
            self.stack.append(data)
            self.top+=1

    def pop(self):
        if self.top==0:
            raise StackUnderflow('Deleting from a empty stack')
        else:
            var=self.stack.pop()
            self.top-=1
            return var
        
    def peek(self):
        return self.stack[self.top-1]
    

                
    



# s2=Fstack()
# s2.push(10)
# s2.push(20)
# s2.push(30)
# print(s2.stack)
# s2.push(40)

# print(s2.stack)


'''Questions'''
'''Pgm to check whether the brackets are matching'''
def ck_brac(string):
    l=Stack()
    d={'[':']','(':')','{':'}'}
    for i in string:
        if i in d.keys():
            l.push(i)
        elif i in d.values():
            if i!=d[l.pop()]:
                return False
    return True

print(ck_brac('[({{()}})]'))


'''Dynamic length stack using singly node'''
class snode:
    def __init__(self,data):
        self.data=data
        self.add=None

class DlStack:
    def __init__(self):
        self.stack=snode(None)
        self.top=0
        self.head=None

    # def push(self,data):
    #     if self.head==None:
    #         self.

