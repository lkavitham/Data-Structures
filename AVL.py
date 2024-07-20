class Node:
    def __init__(self,value):
        self.info=value
        self.lchild =None
        self.rchild=None
        self.balance=0

class AVLTree:
    taller=False
    shorter=False

    def __init__(self):
        self.root=None

    def isEmpty(self):
        return self.root==None

    def display(self):
        self._display(self.root,0)
        print()

    def _display(self,p,level):
        if p is None:
            return 
        self._display(p.rchild,level+1)
        print()

        for i in range(level):
            print("   ",end='')
        print(p.info)
        self._display(p.lchild,level+1)

    def search(self,key):
        return self._search(self.root,key)

    def _search(self,p,key):
        if p is None or p.info==key:
            return p
        if key<p.info:
            return self._search(p.lchild,key)
        return self._search(p.rchild,key)

    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self,p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info," ",end='')
        self._inorder(p.rchild)

    def insert(self,key,):
        self.root=self._insert(self.root,key)

    def _insert(self,p,key):
        if p is None:
            p=Node(key)
            AVLTree.taller=True
        elif key<p.info:
            p.lchild=self._insert(p.lchild,key)
            if AVLTree.taller==True:
                p=self._insertionLeftSubtreeCheck(p)
        elif key>p.info:
            p.rchild=self._insert(p.rchild,key)
            if AVLTree.taller==True:
                p=self._insertRightSubtreeCheck(p)
        else:
            print(key," is already present")
            AVLTree.taller=False
        return p

    def _insertionLeftSubtreeCheck(self,p):
        if p.balance==0:
            p.balance=1
        elif p.balance==-1:
            p.balance=0
            AVLTree.taller=False
        else:
            p=self._insertionLeftBalance(p)
            AVLTree.taller=False
        return p

    def _insertRightSubtreeCheck(self,p):
        if p.balance==0:
            p.balance=-1
        elif p.balance==1:
            p.balance=0
            AVLTree.taller=False
        else:
            p=self._insertionRightBalance(p)
            AVLTree.taller=False
        return p

    def _insertionLeftBalance(self,p):
        a=p.lchild
        if a.balance==1:
            p.balance=0
            a.balance=0
            p=self._rotateRight(p)
        else:                       
            b=a.rchild
            if b.balance==1:
                p.balance=-1
                a.balance=0
            elif b.balance==-1:
                p.balance=0
                a.balance=1
            else:
                p.balance=0
                a.balance=0
            b.balance=0
            p.lchild=self._rotateLeft(a)
            p=self._rotateRight(p)
        return p

    def _insertionRightBalance(self,p):
        a=p.rchild
        if a.balance==-1:
            p.balance=0
            a.balance=0
            p=self._rotateLeft(p)
        else:
            b=a.lchild
            if b.balance==-1:
                p.balance=1
                a.balance=0
            elif b.balance==1:
                p.balance=0
                a.balance=-1
            else:
                p.balance=0
                a.balance=0
            b.balance=0
            p.rchild=self._rotateRight(a)
            p=self._rotateLeft(p)
        return p

    def _rotateLeft(self,p):
        a=p.rchild
        p.rchild=a.lchild
        a.lchild=p
        return a
    
    def _rotateRight(self,p):
        a=p.lchild
        p.lchild=a.rchild
        a.rchild=p
        return a 

    def delete(self,key):
        self.root=self._delete(self.root,key)
    
    def _delete(self,p,key):
        if p is None:
            print(key," is not found")
            AVLTree.shorter=False
        if key<p.info:
            p.lchild=self._delete(p.lchild,key)
            if AVLTree.shorter==True:
                p=self._deletionLeftSubtreeCheck(p)
        elif key>p.info:
            p.rchild=self._delete(p.rchild,key)
            if AVLTree.shorter==True:
                p=self._deletionRightSubtreeCheck(p)
        else:
            if p.lchild is not None and p.rchild is not None:
                s=p.rchild
                while s.lchild is not None:
                    s=s.lchild
                p.info=s.info
                p.rchild=self._delete(p.rchild,s.info)
                if AVLTree.shorter==True:
                    p=self._deletionRightSubtreeCheck(p)
            else:
                if p.lchild is not None:
                    ch=p.lchild
                else:
                    ch=p.rchild
                p=ch
                AVLTree.shorter=True
        return p

    def _deletionLeftSubtreeCheck(self,p):
        if p.balance==0:
            p.balance=-1
            AVLTree.shorter=False
        elif p.balance==1:
            p.balance=0
        else:
            p=self._deletionLeftBalance(p)
        return p

    def _deletionRightSubtreeCheck(self,p):
        if p.balance==0:
            p.balance=1
            AVLTree.shorter=False
        elif p.balance==-1:
            p.balance=0
        else:
            p=self._deletionRightBalance(p)
        return p

    def _deletionLeftBalance(self,p):
        a=p.lchild
        if a.balance==0:
            a.balance=-1
            AVLTree.shorter=False
            p=self._rotateRight(p)
        elif a.balance==1:
            p.balance=0
            a.balance=0
            p=self._rotateRight(p)
        else:
            b=a.rchild
            if b.balance==0:
                p.balance=0
                a.balance=0
            elif b.balance==-1:
                p.balance=0
                a.balance=1
            else:
                p.balance=-1
                a.balance=0
            b.balance=0
            p.lchild=self._rotateLeft(a)
            p=self._rotateRight(p)
        return p 

    def _deletionRightBalance(self,p):
        a=p.rchild
        if a.balance==0:
            a.balance=1
            AVLTree.shorter=False
        elif a.balance==-1:
            p.balance=0
            a.balance=0
        else:
            b=a.lchild
            if b.balance==0:
                p.balance=0
                a.balance=0
            elif b.balance==1:
                p.balance=0
                a.balance=-1
            else:
                p.balance=1
                a.balance=0
            b.balance=0
            p.rchild=self._rotateRight(a)
            p=self._rotateLeft(p)
        return p           

    
if __name__=="__main__":
    tree=AVLTree()

    while True:
        print("1.Display : ")
        print("2.Insert a new node")
        print("3.Delete a node")
        print("4.Inorder Traversal")
        print("5.Quit")

        choice=int(input("Enter your choice : "))

        if choice ==1:
            tree.display()
        elif choice==2:
            key=int(input("Enter the key to be inserted : "))
            tree.insert(key)
        elif choice==3:
            key=int(input("Enter the key to be deleted : "))
            tree.delete(key)
        elif choice==4:
            tree.inorder()
        elif choice==5:
            break
        else:
            print("Wrong choice")
        print()