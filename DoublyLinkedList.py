class Node:
    def __init__(self,value):
        self.info=value
        self.link=None
        self.next=None
class DoubleLinkedLise:
    def __init__(self):
        self.start=None

    def display(self):
        if self.start is None:
            print("List is empty")
            return
        print("List is ")
        p=self.start
        while p is not None:
            print(p.info," ",end='')
            p=p.next
        print()

    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print("The element is at position ",position)
                return True
            position+=1
            p=p.next
        else:
            print("element is not found")
            return False

    def count_nodes(self):
        p=self.start
        n=0
        while p is not None:
            n+=1
            p=p.next
        print("No. of nodes in the list : ",n)

    def insert_beg(self,data):
        temp=Node(data)
        temp.next=self.start
        self.start.prev=temp
        self.start=temp

    def insert_empty(self,data):
        temp=Node(data)
        self.start=temp

    def insert_end(self,data):
        temp=Node(data)
        p=self.start
        while p.next is not None:
            p=p.next
        p.next=temp
        temp.prev=p

    def insert_after(self,data,x):
        temp=Node(data)
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.next
            if p is None:
                print("Element is not present")
            else:
                temp.prev=p
                temp.next=p.next
                if p.next is not None:
                    p.next.prev=temp
                p.next=temp

    def insert_before(self,data):
        pass

    def del_end(self):
        if self.start is None:
            print("list is empty")
        p=self.start
        while p.next is not None:
            p=p.next
        p.prev.next=None

    def del_beg(self):
        if self.start is None:
            print("list is empty")
        self.start=self.start.next
        self.start.prev=None

    def del_node(self):
        pass

    def create_list(self):
        n=int(input("Enter the no. of elements : "))
        if n==0:
            return
        data=int(input("Enter the element to be inserted : "))
        self.insert_empty(data)
        for i in range(n-1):
            data=int(input("Enter the element : "))
            self.insert_end(data)

    def reverse(self):
        p1=self.start
        p2=p1.next
        p1.next=None
        p1.prev=p2
        while p2 is not None:
            p2.prev=p2.next
            p2.next=p1
            p1=p2
            p2=p2.prev
        self.start=p1


list=DoubleLinkedLise()
list.create_list()

while True:
    print("1.Display ")
    print("2.search no. of nodes ")
    print("3.count no. of nodes ")
    print("4.Insert an element at the beginning ")
    print("5.Insert an element at the end ")
    print("6.Insert an element after a node ")
    print("7.Insert an element before a node ")
    print("8.Insert an element at any position ")
    print("9.Delete at beginning ")
    print("10.Delete at ending ")
    print("11.Delete a node ")
    print("12.Quit ")

    option=int(input("Enter your choice"))

    if option==1:
        list.display()
    elif option==2:
        data=int(input("Enter the element to be searched"))
        list.search(data)
    elif option==3:
        list.count_nodes()
    elif option==4:
        data=int(input("Enter an element to be inserted"))
        list.insert_beg(data)
    elif option==5:
        data=int(input("Enter an element to be inserted "))
        list.insert_end(data)
    elif option==6:
        data=int(input("Enter an element to be inserted "))
        x=int(input("Enter the position at which element to be inserted"))
        list.insert_after(data,x)
    elif option==7:
        data=int(input("Enter an element to be inserted "))
        x=int(input("Enter the position at which element to be inserted"))
        list.insert_before(data,x)
    elif option==8:
        data=int(input("Enter an element to be inserted "))
        k=int(input("Enter the position at which element to be inserted"))
        list.insert_position(data,k)
    elif option==9:
        list.del_beg()
    elif option==10:
        list.del_end()
    elif option==11:
        list.del_node()
    elif option==12:
        break
    else:
        print("Wrong choice")
    print()
