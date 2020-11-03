import ds
from ds import *
if __name__ =="__main__":
    ob=Queue.Queue()
    while True:
        print("1.Enter a number into Queue")
        print("2.Remove a number from Queue")
        print("3.Exit")
        t=int(input("Enter your choice"))
        if t==1:
            n=int(input("Enter the number"))
            ob.queue(n)
        if t==2:
            p=ob.dequeue()
            print("Num removed from Queue "+str(p))
        if t==3:
            break    
        
    
