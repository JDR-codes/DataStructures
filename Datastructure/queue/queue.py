'''Dynamic length queue'''
class QueueUnderFlow(Exception):
    pass
class Queue:
    def __init__(self):
        self.queue=[]
        self.front=0
        self.rear=0
    def enqueue(self,data):
        self.queue.append(data)
        self.rear+=1

    def dequeue(self):
        if self.rear==0:
            raise QueueUnderFlow
        else:
            var=self.queue.pop(self.front)
            self.rear-=1
            return var
            
    def peek(self):
        return self.queue[self.top]
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
# print(q1.queue)
# print(q1.dequeue())
# print(q1.queue)


'''Fixed length queue'''
class QueueOverFlow(Exception):
    pass

class FQueue:
    size=3
    def __init__(self):
        self.queue=[]
        self.front=0
        self.rear=0
    def enqueue(self,data):
        if self.rear<self.size:
            self.queue.append(data)
            self.rear+=1
        else:
            raise QueueOverFlow

    def dequeue(self):
        if self.rear==0:
            raise QueueUnderFlow
        else:
            var=self.queue.pop(self.front)
            self.rear-=1
            return var
            
    def peek(self):
        return self.queue[self.top]
    

q2=FQueue()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
print(q2.queue)
q2.dequeue()
q2.dequeue()
q2.dequeue()
q2.dequeue()
