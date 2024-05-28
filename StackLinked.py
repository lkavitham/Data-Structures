class EmptyStackError(Exception):
    pass
class Node:
    def __init__(self,value):
        self.info=value
        self.link =None
class Stack:
    def __init__(self):
        self.top=None
    def is_empty(self):
        return self.top==None
    def size(self):
        if self.is_empty():
            return 0
        count=0
        p=self.top
        while p is not None:
            count+=1
            p=p.link
        return count
    def push(self,data):
        temp=Node(data)
        temp.link=self.top
        self.top=temp
    def pop(self,data):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        popped=self.top.info
        self.top=self.top.link
        return popped
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.top.info
    def display(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        print("Stack is : ")
        p=self.top
        while p is not None:
            print(p.info," ",end='')
            p=p.link


if __name__=="__main__":
    st=Stack()
    while True:
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Size")
        print("5.Display")
        print("6.Quit")

        choice=int(input("Enter your choice"))

        if choice==1:
            x=int(input("Enter the element to be pushed : "))
            st.push(x)
        elif choice==2:
            st.pop()
            print("Popped element is : ")
        elif choice==3:
            print("Element in the top is : ",st.peek())
        elif choice==4:
            print("Size of the list is : ",st.size())
        elif choice==5:
            st.display()
        elif choice==6:
            break
        else:
            print("Wrong choice : ")
        print()