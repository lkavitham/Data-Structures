class Node(object):
    def __init__(self,value):
        self.info=value
        self.link=None

class CirclarLinkedList:
    def __init__(self):
        self.last=None
    
    def display(self):
        if self.last is None:
            print("list is empty")
            return
        p=self.last.link
        while True:
            print(p.info," ",end='')
            p=p.link
            if p==self.last.link:
                break
        print()
    def insert_beg(self,data):
        temp=Node(data)
        temp.link=self.last.link
        self.last.link=temp
    def insert_empty(self,data):
        temp=Node(data)
        self.last=temp
        self.last.link=self.last
    def insert_end(self,data):
        temp=Node(data)
        temp.link=self.last.link
        self.last.link=temp
        self.last=temp
    def insert_after(self,data,x):
        p=self.last.link
        while True:
            if p.info==x:
                break
            p=p.link
            if p==self.last.link:
                break
        if p==self.last.l and p.info!=x:
            print("Element is not found")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
            if p==self.last:
                self.last=temp
    def delete_first(self):
        if self.last is None:
            return "list is empty"
        if self.last.link==self.last:
            self.last=None
            return
        self.last.link=self.last.link.link
    def delete_last(self):
        if self.last is None:
            print("List is empty")
            return
        if self.last.link == self.last:
            self.last = None
            return
        p = self.last.link
        while p.link != self.last:
            p = p.link
        p.link = self.last.link
        self.last = p
    def delete_node(self,x):
        if self.last.link is None:
            return "list is empty"
        if self.last.link==self.last:
            self.last=None
            return
        p=self.last.link
        while p.link!=self.last.link:
            if p.info==x:
                break
            p=p.link
        if p.link == self.last.link:
            print(x,"element is not found")
        else:
            p.link=p.link.link
            if self.last.info==x:
                self.last=p
    def create_list(self):
        n=int(input("Enter the no. of elements"))
        if n==0:
            return
        data=int(input("Enter the element : "))
        self.insert_empty(data)
        for i in range(n-1):
            data=int(input("Enter the element : "))
            self.insert_end(data)

list=CirclarLinkedList()
list.create_list()

while True:
    print("1. Display list")
    print("2. Insert in empty list")
    print("3. Insert a node in the beginning of the list")
    print("4. Insert a node in the ending  of the list")
    print("5. Insert a node after a specfic node")
    print("6. Delete first node ")
    print("7. Delete last node")
    print("8. Delete any node")
    print("9. Quit")

    option=int(input("Enter your choice : "))

    if option==1:
        list.display()
    elif option==2:
        data=int(input("Enter the element : "))
        list.insert_empty(data)
    elif option==3:
        data=int(input("Enter the element : "))
        list.insert_beg(data)
    elif option==4:
        data=int(input("Enter the element : "))
        list.insert_end(data)
    elif option==5:
        x=int(input("Enter the element after which to insert"))
        data=int(input("Enter the element :"))
        list.insert_after(data)
    elif option==6:
        list.delete_first()
    elif option==7:
        list.delete_last
    elif option==8:
        data=int(input("Enter the element : "))
        list.delete_node(data)
    elif option==9:
        break
    else:
         print("Wrong option")
    print()