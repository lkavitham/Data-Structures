from sys import maxsize as INFINITY

TEMPERORY=1
PERMANENT=2

class vertex:
    def __init__(self,name):
        self.name=name

class UndirectedWeighted:
    def __init__(self,size=20):
        self.adj=[[0 for column in range(size)] for row in range(size)]
        self.n=0
        self.verticiesList=[]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.adj[i][j],end=' ')
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
    
    def Verticies(self):
        return [vertex.name for vertex in self.verticiesList]

    def Edges(self):
        edges=[]
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j]!=0:
                    edges.append((self.verticiesList[i].name,self.verticiesList[j].name))
        return edges

    def getIndex(self,s):
        index=0
        for name in(vertex.name for vertex in self.verticiesList):
            if s==name:
                return index
            index+=1
        return None

    def insertVertex(self,name):
        if name in(vertex.name for vertex in self.verticiesList):
            print("Vertex is already present")
            return None
        self.verticiesList.append(vertex(name))
        self.n+=1

    def insertEdge(self,s1,s2,weight):
        u=self.getIndex(s1)
        v=self.getIndex(s2)
        if u is None:
            print("start vertex is not present")
        elif v is None:
            print("End vertex is not present")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]!=0:
            print("Edge is already present")
        else:
            self.adj[u][v]=weight

    def removeEdge(self,s1,s2):
        u=self.getIndex(s1)
        v=self.getIndex(s2)
        if u is None:
            print("start vertex is not present")
        elif v is None:
            print("End vertex is not present")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]!=1:
            print("Edge is not present")
        else:
            self.adj[u][v]=0

    def removeVertex(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vetex is not present")
            return
        self.adj.pop(u)
        for v in range(self.n):
            self.adj[v].pop(u)
        self.verticiesList.pop(u)
        self.n-=1

    def isAdjacent(self,s1,s2):
        u=self.getIndex(s1)
        v=self.getIndex(s2)
        if u is None:
            print("start vertex is not present")
        elif v is None:
            print("End vertex is not present")
        elif u==v:
            print("Invalid")
        else:
            return False if self.adj[u][v]==0 else True

    def outDegree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not present")
            return
        outd=0
        for v in range(self.n):
            if self.adj[u][v]!=0:
                outd+=1
        return outd

    def inDgeree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not present")
            return
        ind=0
        for v in range(self.n):
            if self.adj[v][u]!=0:
                ind+=1
        return ind

    def prims(self):
        edgesInTree=0
        wtTree=0

        for i in range(self.n):
            self.verticiesList[i].status=TEMPERORY
            self.verticiesList[i].predecessor=None
            self.verticiesList[i].length=INFINITY
        root=0
        self.verticiesList[root].length=0

        while True:
            c=self.temperoryMin()
            if c==None:
                if edgesInTree==self.n-1:
                    print("Weights of min spanning tree is : ",wtTree)
                else:
                    print("Graph is not connected,Spanning tree is not possible")
                return
            self.verticiesList[c].status=PERMANENT
            if c!=root:
                edgesInTree+=1
                print("(",self.verticiesList[c].predecessor,",",c,")")
                wtTree=wtTree+self.adj[self.verticiesList[c].predecessor] [c]
            for v in range(self.n):
                if self.adj[c][v] and self.verticiesList[v].status==TEMPERORY:
                    if self.adj[c][v]<self.verticiesList[v].length:
                        self.verticiesList[v].length=self.adj[c][v]
                        self.verticiesList[v].predecessor=c

    def temperoryMin(self):
        min=INFINITY
        x=None

        for v in range(self.n):
            if self.verticiesList[v].status==TEMPERORY and self.verticiesList[v].length<min:
                min=self.verticiesList[v].length
                x=v
        return x
    
if __name__=="__main__":
    g=UndirectedWeighted()

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

    
    g.insertEdge("Zero", "One", 19)
    g.insertEdge("Zero", "Three", 14)
    g.insertEdge("Zero", "Four", 12)
    g.insertEdge("One", "Two", 20)
    g.insertEdge("One", "Four", 18)
    g.insertEdge("Two", "Four", 17)
    g.insertEdge("Two", "Five", 15)
    g.insertEdge("Two", "Nine", 29)
    g.insertEdge("Three", "Four", 13)
    g.insertEdge("Three", "Six", 28)
    g.insertEdge("Four", "Five", 16)
    g.insertEdge("Four", "Six", 21)
    g.insertEdge("Four", "Seven", 22)
    g.insertEdge("Four", "Eight", 24)
    g.insertEdge("Five", "Eight", 26)
    g.insertEdge("Five", "Nine", 27)
    g.insertEdge("Six", "Seven", 23)
    g.insertEdge("Seven", "Eight", 30)
    g.insertEdge("Eight", "Nine", 35)

    g.prims()
