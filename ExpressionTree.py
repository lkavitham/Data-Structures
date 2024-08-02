class Node:
    def __init__(self, value):
        self.info=value
        self.lchild=None
        self.rchild=None

class ExpressionTree:
    def __init__(self):
        self.root=None

    def buildTree(self,postfix):
        stack=[]

        for char in postfix:
            if isOperator(char):
                t=Node(char)
                t.rchild=stack.pop()
                t.lchild=stack.pop()
                stack.append(t)
            else:
                t=Node(char)
                stack.append(t)
        self.root = stack.pop()

    def prefix(self):
        self._preorder(self.root)
        print()

    def _preorder(self,p):
        if p is None:
            return
        print(p.info, end=' ')
        self._preorder(p.lchild)
        self._preorder(p.rchild)

    def postfix(self):
        self._postorder(self.root)
        print()

    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info, end=' ')

    def infix(self):
        self._inorder(self.root)
        print()

    def _inorder(self, p):
        if p is None:
            return
        
        if isOperator(p.info):
            print('(', end='')

        self._inorder(p.lchild)
        print(p.info, end=' ')
        self._inorder(p.rchild)

        if isOperator(p.info):
            print(')', end='')

    def display(self):
        self._display(self.root, 0)
        print()

    def _display(self, p, level):
        if p is None:
            return
        self._display(p.rchild, level + 1)
        print('   ' * level, p.info)
        self._display(p.lchild, level + 1)

    def evaluate(self):
        return self._evaluate(self.root)

    def _evaluate(self, p):
        if not isOperator(p.info):
            return int(p.info)
        leftValue=self._evaluate(p.lchild)
        rightValue=self._evaluate(p.rchild)

        if p.info=='+':
            return leftValue + rightValue
        elif p.info=='-':
            return leftValue - rightValue
        elif p.info=='*':
            return leftValue * rightValue
        elif p.info=='/':
            return leftValue // rightValue

def isOperator(c):
    return c in ['+', '-', '*', '/']

if __name__=="__main__":
    tree = ExpressionTree()

    postfix = "35+18*83*-"

    tree.buildTree(postfix)
    print("Tree Structure: ")
    tree.display()
    
    print("Prefix: ")
    tree.prefix()

    print("Postfix: ")
    tree.postfix()

    print("Infix: ")
    tree.infix()

    print("Evaluated Value: ", tree.evaluate())