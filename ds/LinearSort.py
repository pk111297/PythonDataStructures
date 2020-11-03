class LinearSort:
	def __init__(self,lst):
		self.lst=lst
	def sort(self):
		l=len(self.lst)
		i=0
		j=0
		while i<l-1:
			j=i+1
			while j<l:
				if self.lst[i]>=self.lst[j]:
					temp=self.lst[i]
					self.lst[i]=self.lst[j]
					self.lst[j]=temp
				j=j+1
			i=i+1
