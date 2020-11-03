import sys
sys.setrecursionlimit(1000000)
class MergeSort:
    def __init__(self,lst):
        self.lst=lst
    def sort(self):
        ub=len(self.lst)-1
        lb=0
        self.mergeSort(lb,ub)
    def mergeSort(self,lb,ub):
        if lb<ub:
            mid=int((lb+ub)/2)
            self.mergeSort(lb,mid)
            self.mergeSort(mid+1,ub)
            self.merge(lb,ub,mid)
    def merge(self,lb,ub,mid):
        i=lb
        tmp=[]
        j=mid+1
        k=lb
        while i<=mid and j<=ub:
            if self.lst[i]<self.lst[j]:
                tmp.append(self.lst[i])
                i=i+1
            else:
                tmp.append(self.lst[j])
                j=j+1
        while i<=mid:
            tmp.append(self.lst[i])
            i=i+1
        while j<=ub:
            tmp.append(self.lst[j])
            j=j+1
        for a in tmp:
            self.lst[k]=a
            k=k+1