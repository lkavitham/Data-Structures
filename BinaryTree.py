from collections import deque

class Node:
    def __init__(self,value):
        self.info = value
        self.lchild=None
        self.rchild=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def is_empty(self):
        return self.root==None

    def display(self):
        pass

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self,p):
        if p is None:
            return
        print(p.info," ",end='')
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def inorer(self):
        self._inorder(self.root)
        print()

    def _inorder(self,p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info," ",end='')
        self._inorder(p.rchild)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self,p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info," ",end='')

    def level_order(self):
        if self.root is None:
            print("Tree is empty")
            return
        qu=deque()
        qu.append(self.root)
        while len(qu)!=0:
            p=qu.popleft()
            if p.lchild is not None:
                qu.append(p.lchild)
            if p.rchild is not None:
                qu.append(p.rchild)

    def height(self):
        return self._height(self.root)

    def _height(self,p):
        if p is not None:
            return 0
        hL=self._height(p.lchild)
        hR=self._height(p.rchild)
        if hL>hR:
            return 1+hL
        if hR>hL:
            return 1+hR

    def create_tree(self):
        self.root=Node('P')
        self.root.lchild=Node('Q')
        self.root.rchild=Node('R')
        self.root.lchild.lchild=Node('S')
        self.root.lchild.rchild=Node('T')
        self.root.rchild.lchild=Node('U')


bt=BinaryTree()
bt.create_tree()


print("Inorder : ")
bt.inorer()
print("Preorder : ")
bt.preorder()
print("Postorder : ")
bt.postorder()
print("level order : ")
bt.level_order()
print("Height : ")
bt.height()