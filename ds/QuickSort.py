import sys
sys.setrecursionlimit(1000000)
class QuickSort:
	def __init__(self,lst):
		self.lst=lst
	def sort(self):
		lb=0
		ub=len(self.lst)-1
		self.quickSort(lb,ub)
	def quickSort(self,lb,ub):
		if ub<=lb: return
		part=self.partitionPoint(lb,ub)
		self.quickSort(0,part-1)
		self.quickSort(part+1,ub)
	def partitionPoint(self,lb,ub):
		num=self.lst[lb]
		e=lb
		f=ub
		while(True):
			while(True):
				if e==ub or num<self.lst[e]:break
				e+=1
			while(True):
				if f==lb or num>=self.lst[f]:break
				f-=1
			if e<f:
				self.lst[e],self.lst[f]=self.lst[f],self.lst[e]
			else:
				self.lst[lb],self.lst[f]=self.lst[f],self.lst[lb]
				break
		return f