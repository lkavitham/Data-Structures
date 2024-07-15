class Node:
    def __init__(self,value):
        self.info=value
        self.lchild=None
        self.rchild=None

class BinarysearchTree:
    def __init__(self):
        self.root=None
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, p, key):
        if key < p.info:
            if p.lchild is None:
                p.lchild = Node(key)
            else:
                self._insert(p.lchild, key)
        elif key > p.info:
            if p.rchild is None:
                p.rchild = Node(key)
            else:
                self._insert(p.rchild, key)
    def preorder(self):
        self._preorder(self.root)
        print()
    def _preorder(self,p):
        if p is None:
            return
        print(p.info," ",end='')
        self._preorder(p.lchild)
        self._preorder(p.rchild)
    def inorder(self):
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
    def search(self, key):
        return self._search(self.root, key)
    def _search(self, p, key):
        if p is None or p.info == key:
            return p
        if key < p.info:
            return self._search(p.lchild, key)
        return self._search(p.rchild, key)
    def isempty(self):
        return self.root==None
    def display(self):
        self._display(self.root,0)
        print()

    def _display(self, p, level):
        if p is None:
            return
        self._display(p.rchild, level + 1)
        print()
        for i in range(level):
            print("   ", end='')
        print(p.info)
        self._display(p.lchild, level + 1)

    def height(self):
        return self._height(self.root)
    
    def _height(self, p):
        if p is None:
            return 0
        hL = self._height(p.lchild)
        hR = self._height(p.rchild)
        return 1 + max(hL, hR)
        
    
    def delete(self, x):
        self.root = self._delete(self.root, x)
    
    def _delete(self, p, x):
        if p is None:
            return None
        if x < p.info:
            p.lchild = self._delete(p.lchild, x)
        elif x > p.info:
            p.rchild = self._delete(p.rchild, x)
        else:
            if p.lchild is not None and p.rchild is not None:
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild, s.info)
            else:
                if p.lchild is not None:
                    p = p.lchild
                else:
                    p = p.rchild
        return p      
    
if __name__=="__main__":
    bt=BinarysearchTree()
    elements=[5,3,7,4,9,1,6]

    for ele in elements:
        bt.insert(ele)

        print("Preorder : ")
        bt.preorder()
        print("Inorder : ")
        bt.inorder()
        print("Postorder :")
        bt.postorder()
        print("Display : ")
        bt.display()
        print("Height")
        bt.height()
        print("Delete")
        bt.delete(4)