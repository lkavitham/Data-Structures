class StudentRecord:
    def __init__(self,i,Name):
        self.studentId= i
        self.studentName=Name
    def get_student_id(self):
        return self.studentId
    def set_student_id(self,i):
        self.studentId=i
    def __str__(self):
        return str(self.studentId)+" "+(self.studentName)

class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class SingleLinkedList:
    def __init__(self):
        self.start=None
    def display(self):
        if self.start is None:
            print("List is empty")
        p=self.start
        while p is not None:
            print(p.info," ",end='')
            p=p.link
        print()
    def search(self,x):
        p=self.start
        position=1
        while p is not None:
            if p.info==x:
                print("Element is found at position ",position)
                return True
            position+=1
            p=p.link
        else:
            return False
    def insert_beg(self,data):
        temp=Node(data)
        temp.link=self.start
        self.start=temp
    def delete(self,x):
        if self.start is None:
            print("List is empty")
            return
        if self.start.info.get_student_id()==x:
            self.start=self.start.link
            return
        p=self.start
        while p.link is not None:
            if p.link.info.get_student_id()==x:
                break
            p=p.link
            if p.link is None:
                print("Element ",x,"is not present")
            else:
                p.link=p.link.link

class HashTable:
    def __init__(self,tablesize):
        self.m=tablesize
        self.array=[None]*self.m
        self.n=0
    def hash(self,key):
        return key%self.m
    def display(self):
        for i in range(self.m):
            print("[",i,"]    ---->  ",end='')
            if self.array[i]!=None:
                self.array[i].display()
            else:
                print("_____")
    def search(self,key):
        h=self.hash(key)
        if self.array[h]!=None:
            return self.array[h].search(key)
        return None
    def insert(self,newRecord):
        key=newRecord.get_student_id()
        h=self.hash(key)
        if self.array[h]==None:
            self.array[h]=SingleLinkedList()
        self.array[h].insert_beg(newRecord)
        self.n+=1
    def delete(self,key):
        h=self.hash(key)
        if self.array[h]!=None:
            self.array[h].delete(key)
            self.n-=1
        else:
            print("Value ",key," not present")


size=int(input("Enter the size of table: "))
table=HashTable(size)

while True:
    print("1.Insert a record")
    print("2.Search a record")
    print("3.Delete a record")
    print("4.Display table")
    print("5.Exit")

    option = int(input("Enter your option  : "))

    if option==1:
        id=int(input("Enter the student id : "))
        name=input("Enter the student name : ")
        aRecord=StudentRecord(id,name)
        table.insert(aRecord)
    elif option==2:
        id=int(input("Enter a key to be searched : "))
        aRecord=StudentRecord(id)
        if aRecord is None:
            print("key is not present")
        else:
            print(aRecord)
    elif  option==3:
        id=int(input("Enter the element to be deleted : "))
        table.delete(id)
    elif option==4:
        table.display()
    elif option==5:
        break
    else:
        print("Wrong option")
    print()