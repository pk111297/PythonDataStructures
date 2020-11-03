class Queue:
    def __init__(self):
        self.lst=SinglyLinkedList()
    def queue(self,num):
        self.lst.addAtEnd(num)
    def dequeue(self):
        if self.lst.getLength()==0:
            return "Queue Empty"
        z=self.lst.start.num
        self.lst.removeFromPosition(1)
        return z
    def isEmpty(self):
        if self.lst.getLength()==0: return True
        else : return False
    def isFull(self):
        return False
