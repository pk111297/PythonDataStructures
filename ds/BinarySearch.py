class BinarySearch:
    def __init__(self,lst):
         self.lst=lst
    def search(self,num):
         low=0
         high=len(self.lst)-1
         mid=0
         while low<=high:
            mid=(low+high)//2
            if self.lst[mid]==num:return mid
            if self.lst[mid]<num:
                 low=mid+1
            if self.lst[mid]>num:
                 high=mid-1
         return -1   
