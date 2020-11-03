import ds
from ds import *
if __name__=="__main__":
	sll=SinglyLinkedList.SinglyLinkedList()
	while True:
		print("1>Add a node at End")
		print("2>Insert a node at top")
		print("3>Insert a node at a position")
		print("4>Remove a node from a position")
		print("5>Traverse- Top To Bottom")
		print("6>Traverse- Bottom To Top")
		print("7>Exit")
		print("Enter your choice:",end="")
		ch=int(input())
		if(ch==1):
			print("Enter a Number to add at End:",end="")
			sll.addAtEnd(int(input()))
		if ch==2:
			print("Enter a Number to insert at Top:",end="")
			sll.insertAtTop(int(input()))
		if ch==3:
			print("Enter a Number to insert:",end="")
			num=int(input())
			print("Enter a Position To Enter:",end="")
			pos=int(input())
			sll.insertAtPosition(num,pos)
		if ch==4:
			print("Enter position of node to remove:",end="")
			sll.removeFromPosition(int(input()))
		if ch==5:
			sll.traverseTopToBottom()
		if ch==6:
			sll.traverseBottomToTop()
		if ch==7:
			break
