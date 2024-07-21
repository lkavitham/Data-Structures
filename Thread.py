class Node:
    def __init__(self,value):
        self.info=value
        self.left=None
        self.right=None
        self.leftThread=True
        self.rightThread=True

class ThreadedBinaryTree:
    def __init__(self):
        self.root=None
    
    def _inorderPredecessor(self,p):
        if p.leftThread==True:
            return p.left
        else:
            p=p.left
            while p.rightThread==False:
                p=p.right
            return p
    
    def _inorderSuccesor(self,p):
        if p.rightThread==True:
            return p.right
        else:
            p=p.right
            while p.leftThread==False:
                p=p.left
            return p

    def inorder(self):
        if self.root==None:
            print("Tree is empty")
            return
        p=self.root
        while p.leftThread==False:
            p=p.left

        while p is not None:
            print(p.info," ",end='')
            if p.rightThread==True:
                p=p.right
            else:
                p=p.left
                while p.leftThread==False:
                    p=p.left
        print()

    def insert(self,x):
        p=self.root
        par=None
        while p is not None:
            if x<p.info:
                if p.leftThread==False:
                    p=p.left
                else:
                    break
            elif x>p.info:
                if p.rightThread==False:
                    p=p.right
                else:
                    break
            else:
                print(x," already present in the tree")
                return

        temp=Node(x)
        if par==None:
            self.root=temp
        elif x<par.info:
            temp.left=par.left
            temp.right=par
            par.leftThread=False
            par.left=temp
        else:
            temp.left=par
            temp.right=par.right
            par.rightThread=False
            par.right=temp

    def delete(self,x):
        p=self.root
        par=None
        while p is not None:
            if x==p.info:
                break
            par=p
            if x<p.info:
                if p.leftThread==False:
                    p=p.left
                else:
                    break
            else:
                if p.rightThread==False:
                    p=p.right
                else:
                    break
        if p==None or p.info!=x:
            print(x," not found")
            return

        if p.leftThread==False and p.rightThread ==False:
            ps=p
            s=p.right

            while s.leftThread==False:
                ps=s
                s=s.left
            p.info=s.info
            p=s
            par=ps
            
        if p.leftThread==True and p.rightThread==True:
            if par==None:
                self.root=None
            elif p==par.left:
                par.leftThread=True
                par.left=p.left
            else:
                par.rightThread=True
                par.right=p.right
            return

        if p.leftThread==False:
            ch=p.left
        else:
            ch=p.right
            
        if par==None:
            self.root=ch
        elif p==par.left:
            par.left=ch
        else:
            par.right=ch

        pred=self._inorderPredecessor(p)
        succ=self._inorderSuccesor(p)

        if p.leftThread==False:
            pred.right=succ
        else:
            succ.left.pred

if __name__=="__main__":
    tree=ThreadedBinaryTree()

    while True:
        print("1.Insert a new node")
        print("2.Delete a node")
        print("3.Inorder Traversal")
        print("4.Quit")

        choice=int(input("Enter your choice"))

        if choice==1:
            key=int(input("Enter the key to be inserted : "))
            tree.insert(key)
        elif choice==2:
            key=int(input("Enter the key to be deleted : "))
            tree.delete(key)
        elif choice==3:
            tree.inorder()
        elif choice==4:
            break
        else:
            print("Wrong choice")
        print()