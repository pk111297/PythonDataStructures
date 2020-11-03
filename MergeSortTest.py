import ds
from ds import *
if __name__=="__main__":
	lst=[]
	while True:
		z=input("Enter a Number To append:")
		if z=="q":
			break
		lst.append(float(z))
	print(lst)
	l=MergeSort.MergeSort(lst)
	l.sort()
	print(lst)
