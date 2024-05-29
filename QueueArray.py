class EmptyQueueError(Exception):
    pass
class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[0]
    def display(self):
        print(self.items)

if __name__=="__main__":
    qu=Queue()

    while True:
        print("1.Enqueue")
        print("2.Dequeue")
        print("3.Peek")
        print("4.Size")
        print("5.Display")
        print("6.Quit")

        choice=int(input("Enter your choice : "))

        if choice==1:
            x=int(input("Enter the element to be enqueue : "))
            qu.enqueue(x)
        elif choice==2:
            qu.dequeue()
            print("Popped element is : ")
        elif choice==3:
            print("Element in the top is : ",qu.peek())
        elif choice==4:
            print("Size of the list is : ",qu.size())
        elif choice==5:
            qu.display()
        elif choice==6:
            break
        else:
            print("Wrong choice : ")
        print()



