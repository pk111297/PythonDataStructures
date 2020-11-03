import ds
from ds import *
lst=[]
while True:
	z=input("Enter a Number To append:")
	if z=="q":
		break
	lst.append(float(z))
print(lst)
q=QuickSort.QuickSort(lst)
q.sort()
print(lst)
