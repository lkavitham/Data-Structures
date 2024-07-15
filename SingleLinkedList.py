class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display(self):
        if self.start is None:
            print("List is empty")
        print("list is : ")
        p = self.start
        while p is not None:
            print(p.info, " ", end='')
            p = p.link
        print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("No. of nodes in the list is : ",n)

    #this is used to search the elements
    def search_nodes(self, x):
        p = self.start
        position=1
        while p is not None:
            if p.info == x:
                print("Element is found at position : ",position)
                return True
            position+=1
            p = p.link
        else:
            print("Element is not found")
            return False
    
    #This is used to insert the element
    def insert_beg(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def insert_position(self, data, k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
        p = self.start
        i = 1
        while i < k - 1 and p is not None:
            p = p.link
            i += 1
        if p is None:
            print("You can insert upto positon", i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
            if p is None:
                print(x, " is not present")
            else:
                temp = Node(data)
                temp.link = p.link
                p.link = temp

    def insert_before(self, data, x):
        if self.start is None:
            print("List is empty")
        if x==1:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
        temp=Node(data)
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
            if p.link is None:
                print("Element is not found")
            else:
                temp.link=p.link
                p.link=temp

    def create_list(self):
        n = int(input("No. of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter teh element to be inserted : "))
            self.insert_end(data)
            
     #This is used to delete a node
    def del_bef(self):
        if self.start is None:
            print("List is empty")
        self.start = self.start.link

    def del_end(self):
        if self.start is None:
            return
        p = self.start
        while p.link.link is None:
            p = p.link
        p.link = None

    def del_node(self):
        if self.start is None:
            print("List is empty")
            return
        if self.start.info == x:
            self.start = self.start.link
            return
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print("Element ", x, "not in list")
        else:
            p.link = p.link.link

    def reverse(self):
        p = self.start
        prev = None
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p=next
        self.start = prev


list = SingleLinkedList()
list.create_list()
while True:
    print("1.Display list")
    print("2.Count no. of nodes")
    print("3.Search for the element")
    print("4.Insert at the beginning")
    print("5.Insert at the ending")
    print("6.Insert at any position")
    print("7.Insert after a node")
    print("8.insert before a node")
    print("9.Delete at beginning")
    print("10.Delete at ending")
    print("11.Delete any node")
    print("12.Reverse the list")
    print("13.Quit")

    option = int(input("Enter your choice : "))
    if option == 1:
        list.display()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data =int(input("Enter the element to be searched : "))
        list.search_nodes(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_beg(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted : "))
        k = int(input("Enter the position at which the element to be insert : "))
        list.insert_position(data,k)
    elif option == 7:
        data = int(input("Enter the element to be inserted : "))
        x=int(input("Enter the position after which element to be inserted"))
        list.insert_after(data,x)
    elif option == 8:
        data = int(input("Enter the element to be inserted : "))
        x=int(input("Enter the position before which element to be inserted "))
        list.insert_before(data,x)
    elif option == 9:
        list.del_bef()
    elif option == 10:
        list.del_end()
    elif option == 11:
        list.del_node()
    elif option == 12:
        list.reverse()
    elif option == 13:
        break
    else:
        print("Wrong Option")
    print()
