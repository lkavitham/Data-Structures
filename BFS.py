INITIAL=0
WAITING=1
VISITED=2

class vertex:
    def __init__(self,name):
        self.name=name

class BFS:
    def __init__(self,size=20):
        self.adj=[[ 0 for column in range(size)] for row in range(size)]
        self.n=0
        self.verticesList=[]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.adj[i][j],end='')
            print()
        print()

    def numVerticies(self):
        return self.n

    def numEdges(self):
        e=0
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j]!=0:
                    e+=1
        return e

    def Vertices(self):
        return [vertex.name for vertex in self.verticesList]

    def Edges(self):
        edges=[]
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j]!=0:
                    edges.append((self.verticesList[i].name, self.verticesList[j].name))
        return edges
    
    def getIndex(self,s):
        index=0
        for name in(vertex.name for vertex in self.verticesList):
            if s==name:
                return index
            index+=1
        return index
    
    def insertVertex(self,name):
        if name in (vertex.name for vertex in self.verticesList):
            print("Vertex is already present")
            return
        self.verticesList.append(vertex(name))
        self.n+=1

    def insertEdge(self,s1,s2):
        u=self.getIndex(s1)
        v=self.getIndex(s2)

        if u is None:
            print("Start vertex is not present")
        elif v is None:
            print("End vertex is not present")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]!=0:
            print("Edge is already present")
        else:
            self.adj[u][v]=1

    def deleteEdge(self,s1,s2):
        u=self.getIndex(s1)
        v=self.getIndex(s2)

        if u is None:
            print("Start vertex is not present")
        elif v is None:
            print("End vertex is not present")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]==0:
            print("Edge is not already present")
        else:
            self.adj[u][v]=0

    def deleteVertex(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not present")
            return
        self.adj.pop(u)
        for i in range(self.n):
            self.adj[i].pop(u)
        self.verticesList.pop(u)
        self.n-=1

    def isAdjacent(self,s1,s2):
        u=self.getIndex(s1)
        v=self.getIndex(s2)
        if u is None:
            print("Vertex is not present")
        elif v is None:
            print("Vetex is not present")
        elif u==v:
            print("Invaild")
        else:
            return False if self.adj[u][v]==0 else True

    def outDegree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vetex is not present")
            return
        outd=0
        for v in range(self.n):
            if self.adj[u][v]!=0:
                outd+=1            
        
    def inDegree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not present")
            return
        ind=0
        for v in range(self.n):
            if self.adj[v][u]!=0:
                ind+=1

    def bfsTraversal(self):
        s=input("Enter starting vertex")
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not present")
            return
        for v in range(self.n):
            self.verticesList[v].state=INITIAL
        
        self.bfs(u)

    def bfs(self,v):
        from queue import Queue
        qu=Queue()
        qu.put(v)
        self.verticesList[v].state=WAITING

        while qu.qsize()!=0:
            v=qu.get()
            print(self.verticesList[v].name," ")
            self.verticesList[v].state=VISITED

            for i in range(self.n):
                if self.adj[v][i]!=0 and self.verticesList[i].state==INITIAL:
                    qu.put(i)
                    self.verticesList[i].state=WAITING
        print()

    def bfsAll(self):
        s=input("Enter starting Vertex: ")
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not present")
            return
        
        for v in range(self.n):
            self.verticesList[v].state=INITIAL
        self.bfs(u)

        for v in range(self.n):
            if self.verticesList[v].state==INITIAL:
                self.bfs(v)

if __name__=="__main__":
    g=BFS()

    g.insertVertex("Zero")
    g.insertVertex("One")
    g.insertVertex("Two")
    g.insertVertex("Three")
    g.insertVertex("Four")
    g.insertVertex("Five")
    g.insertVertex("Six")
    g.insertVertex("Seven")
    g.insertVertex("Eight")
    g.insertVertex("Nine")

    g.insertEdge("Zero","One")
    g.insertEdge("Zero","Three")
    g.insertEdge("One","Two")
    g.insertEdge("One","Four")
    g.insertEdge("Zero","Five")
    g.insertEdge("Two","Three")
    g.insertEdge("Two","Five")
    g.insertEdge("Three","Six")
    g.insertEdge("Four","Five")
    g.insertEdge("Four","Seven")
    g.insertEdge("Five","Six")
    g.insertEdge("Five","Eight")
    g.insertEdge("Six","Eight")
    g.insertEdge("Six","Nine")
    g.insertEdge("Seven","Eight")
    g.insertEdge("Eight","Nine")

    print("Adjacency Matix - ")
    g.display()
    print("List of vertices - ")
    print(g.Vertices())
    print("List of edges - ")
    print(g.Edges())

    g.bfsTraversal()
    g.bfsAll()