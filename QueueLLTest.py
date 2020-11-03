import ds
from ds import QueueLL
if __name__ =="__main__":
    ob=Queue()
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
            print("Num removed from queue"+str(p))
        if t==3:
            break
        
         
    
        
