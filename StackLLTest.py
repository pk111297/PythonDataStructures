import ds
from ds import *
if __name__ =="__main__":
    ob=StackLL.Stack()
    while True:
        print("1.Push a number into stack")
        print("2.POP a number from Stack")
        print("3.Exit")
        t=int(input("Enter your choice"))
        if t==1:
            n=int(input("Enter the number"))
            ob.push(n)
        if t==2:
            p=ob.pop()
            print("Num removed from stack"+str(p))
        if t==3:
            break
