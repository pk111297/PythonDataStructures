class BubbleSort:
	def __init__(self,lst):
		self.lst=lst
	def sort(self):
		l=len(self.lst)
		m=0
		while m<l-1:
			i=0
			j=i+1
			while j<l:
				if self.lst[i]>self.lst[j]:
					temp=self.lst[i]
					self.lst[i]=self.lst[j]
					self.lst[j]=temp
				i=i+1
				j=j+1
			l=l-1