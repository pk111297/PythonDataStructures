class SelectionSort:
    def __init__(self,lst):
        self.lst=lst
    def sort(self):
        l=len(self.lst)
        e=0
        while e<=l-2:
            m=e
            f=e+1
            while f<=l-1:
                if self.lst[f]<self.lst[m]:
                    m=f
                f=f+1
            g=self.lst[e]
            self.lst[e]=self.lst[m]
            self.lst[m]=g
            e=e+1        