import ds
from ds import *
lst=[11,31,334,63,86,75,12,20,33]
lst.sort()
i=int(input("Enter number to search"))
b=BinarySearch.BinarySearch(lst)
t=b.search(i)
if t==-1:
    print("Number not found")
else :
    print("Number found at %d index"%t)
   
