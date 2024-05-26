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
        print("No. of nodes in the list is : ")

    def search_nodes(self, x):
        p = self.start
        while p is not None:
            if p.info == x:
                return True
            p = p.link
        else:
            print("Element is not found")
            return False

    def insert_beg(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_end(self, data):
        temp = Node(data)
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
        pass

    def create_list(self):
        n = int(input("No. of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter teh element to be inserted : "))
            self.insert_end(data)

    def del_beg(self):
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
        pass

    def reverse(self):
        p = self.start
        prev = None
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
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

    option = int(input("Enter your choice"))
    if option == 1:
        list.display()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = ("Enter the element to be searched : ")
        list.search_nodes(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_beg(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted : "))
        k = int(input("Enter the position at which toinsert : "))
        list.insert_position(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_after(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_before(data)
    elif option == 9:
        list.del_beg()
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



class Node:
    def __init__ (self,value) :
        self.info=value
        self.link=None
class SingleLinkedList:
    def __init__(self):
        self.start=None
    def display_list(self):
        if self.start is None:
            print("List is empty")
        else:
            print("List is : ")
            p=self.start
            while p is not None:
                print(p.info," ",end='')
                p=p.link
            print()
    def count_nodes(self):
        p=self.start
        n=0
        while p is not None:
            n+=1
            p=p.link
        print("No.of nodes in the list = ",n)
    def search(self,x):
        position=1
        p=self.start
        while p is not None:
            if p.info==x:
                print(x,"is at positon",position)
                return True
            position+=1
            p=p.link
        else:
            print(x,"is not found in the list")
            return False
    def insert_in_beginning(self, data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp
    def insert_at_end(self,data):
        temp=Node(data)
        if self.start is None:
            self.start=temp
            return

        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp
    def create_list(self):
        n=int(input("Enter no.of nodes : "))
        if n==0:
            return
        for i in range(n):
            data=int(input("Enter the elements to be inserted : "))
            self.insert_at_end(data)
    def insert_after(self,data,x):
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
            if p is None:
                print(x,"is not present")
            else:
                temp=Node(data)
                temp.link=p.link
                p.link=temp
    def insert_before(self,data,x):
        if self.start is None:
            print("List is empty")
            return
        if x==self.start.info:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return

        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
        if p.link is None:
            print(x," is not present in the list")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
    def insert_at_position(self,data,k):
        if k==1:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return
        p=self.start
        i=1
        while i<k-1 and p is not None:
            p=p.link
            i+=1
        if p is None:
            print("you can insert only upto position",i)
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
    def delete_node(self,x):
        if self.start is None:
            print("List is empty")
            return
        if self.start.info==x:
            self.start=self.start.link
            return
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
        if p.link is None:
            print("Element ",x,"not in list")
        else:
            p.link=p.link.link
    def delete_first_node(self):
        if self.start is None:
            return
        self.start=self.start.link
    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start = None
            return
        p=self.start
        while p.link.link is not None:
            p = p.link
        p.link = None
    def reverse_list(self):
        pass
    def bubble_sort_exdata(self):
        pass
    def bubble_sort_exlinks(self):
        pass
    def has_cycle(self):
        pass
    def find_cycle(self):
        pass
    def remove_cycle(self):
        pass
    def insert_cycle(self):
        pass
    def merge2(self,list2):
        pass
    def _merge2(self,p1,p2):
        pass
    def merge_sort(self):
        pass
    def _merge_sort_rec(self,listStart):
        pass
    def _divide_list(self,p):
        pass

list = SingleLinkedList()
list.create_list()
while True:
    print("1.Display list")
    print("2.Count the no.of nodes")
    print("3.Search for the element")
    print("4.Insert in empty list/Insert in beginning of the list")
    print("5.Insert a node at the end of the list")
    print("6.Insert a node after a specified node")
    print("7.Insert a node before a specified node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10.Delete last node")
    print("11.Delete any node")
    print("12.Reverse the list")
    print("13.Bubble sort by exchanging data")
    print("14.Bubble sort by exchanging links")
    print("15.MergeSort")
    print("16.Insert Cycle")
    print("17.Delete Cycle")
    print("18.Remove Cycle")
    print("19.Quite")

    option = int(input("Enter your choice : "))
    if option==1:
        list.display_list()
    elif option==2:
        list.count_nodes()
    elif option==3:
        data=int(input("Enter the element to be searched : "))
        list.search(data)
    elif option==4:
        data=int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option==6:
        data=int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element after which to insert : "))
        list.insert_after(data,x)
    elif option==7:
        data=int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element before which to insert : "))
        list.insert_before(data,x)
    elif option==8:
        data=int(input("Enter the element to be inserted : "))
        k = int(input("Enter the position at which to insert : "))
        list.insert_at_position(data, k)
    elif option==9:
        list.delete_first_node()
    elif option==10:
        list.delete_last_node()
    elif option==11:
        data=int(input("Enter the element to be deleted : "))
        list.delete_node(data)
    elif option==12:
        list.reverse_list()
    elif option==13:
        list.bubble_sort_exdata()
    elif option==14:
        list.bubble_sort_exlinks()
    elif option == 15:
        list.merge_sort()
    elif option==16:
        data = int(input("Enter the element at which the cycle has to be inserted : "))
        list.insert_cycle(data)
    elif option==17:
        if list.has_cycle():
            print("List has a cycle")
        else:
            print("List does not has a cycle")
    elif option == 18:
        list.remove_cycle()
    elif option == 19:
        break
    else:
        print("Wrong option")
    print()



