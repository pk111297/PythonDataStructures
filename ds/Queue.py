class Queue:
    def __init__(self):
            self.lst=[]
    def queue(self,num):
        self.lst.append(num)
    def dequeue(self):
        if len(self.lst)==0:
            return "Empty Queue"
        z=self.lst[0]
        del self.lst[0]
        return z
    def isEmpty(self):
        if len(self.lst)==0: True
        else : False
    def isFull(self):
        return False