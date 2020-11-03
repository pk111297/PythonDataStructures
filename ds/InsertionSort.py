class InsertionSort:
    def __init__(self,lst):
        self.lst=lst
    def sort(self):
        ub=len(self.lst)-1
        lb=0
        y=lb+1
        while y<=ub:
            p=y
            num=self.lst[p]
            j=p-1
            while j>=lb:
                if num>=self.lst[j]:
                    break
                self.lst[j+1]=self.lst[j]
                j=j-1
                p=p-1
            self.lst[p]=num
            y=y+1    