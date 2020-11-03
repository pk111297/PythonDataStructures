class Stack:
    def __init__(self):
        self.lst=SinglyLinkedList.SinglyLinkedList()
    def push(self,num):
        self.lst.addAtEnd(num)
    def pop(self):
        if self.lst.getLength()==0:
               return "Stack is Empty"
        z=self.lst.start
        t=0
        while z!=None:
            t=z.num
            z=z.next
        self.lst.removeFromPosition(self.lst.getLength())
        return t
    def isEmpty(self):
        if self.lst.start==None:
               return True
        else: return False
    def isFull(self):
        return False
