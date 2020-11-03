class Stack:
    def __init__(self):
        self.lst=[]
    def push(self,num):
        self.lst.insert(0,num)
    def pop(self):
        if len(self.lst)==0:
               return "Stack is Empty"
        z=self.lst[0]
        del self.lst[0]
        return z
    def isEmpty(self):
        if len(self.lst)==0:
            return True 
        else: return False
    def isFull(self):
        return False