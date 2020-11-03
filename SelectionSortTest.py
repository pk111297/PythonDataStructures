import ds
from ds import *
if __name__=="__main__":
	lst=[]
	while True:
		z=input("Enter a Number To append:")
		if z=="q":
			break
		lst.append(int(z))
	print(lst)
	l=SelectionSort.SelectionSort(lst)
	l.sort()
	print(lst)
            
        
