class Node:
	def __init__(self):
		self.num=None
		self.next=None
class SinglyLinkedList:
	def __init__(self):
		self.start=None
	def addAtEnd(self,num):
		t=Node()
		t.num=num
		if self.start==None:
			self.start=t
		else:
			i=self.start
			while i.next!=None:
				i=i.next
			i.next=t
	def insertAtTop(self,num):
		t=Node()
		t.num=num
		if self.start==None:
			self.start=t
		else:
			t.next=self.start
			self.start=t
	def insertAtPosition(self,num,pos):
		t=Node()
		t.num=num
		if self.start==None:
			self.start=t
		else:
			count=1
			i=self.start
			j=self.start
			while i.next!=None:
				if count>=pos: break	
				j=i
				i=i.next
				count+=1
			if i==None:
				j.next=t
			else:
				if i==self.start:
					t.next=self.start
					self.start=t
				else:
					j.next=t
					t.next=i
	def removeFromPosition(self,pos):
		if self.start==None:
			print("Invalid Position(List is Empty)")
			return
		x=1
		p2=None
		p1=self.start
		while x<pos and p1!=None:
			p2=p1
			p1=p1.next
			x=x+1
		if p1==None:
			print("Invalid Position")
			return 
		if p1==self.start:
			self.start=self.start.next
		else:
			p2.next=p1.next
	def traverseTopToBottom(self):
		i=self.start
		while i!=None:
			print(i.num)
			i=i.next
	def traverseBottomToTop(self):
		i=self.start
		l=[]
		while i!=None:
			l.append(i.num)
			i=i.next
		l.reverse()
		for i in l:
			print(i)
	def getLength(self):
		count=0
		t=self.start
		while t!=None:
			count=count+1
			t=t.next
		return count
