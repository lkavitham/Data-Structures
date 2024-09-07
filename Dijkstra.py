from sys import maxsize as INFINITY

TEMPORARY=1
PERMANENT=2

class vertex:
    def __init__(self,name):
        self.name=name

class DirectedWeightedGraph:
    def __init__(self,size=20):
        self.adj=[[ 0 for column in range(size)] for row in range(size)]
        self.n=0
        self.verticiesList=[]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print('self.adj[i][j]',end='')
        print()

    def numVertices(self):
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
            print("Start vertex is not present")
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
            print("Start vertex is not present")
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
            print("Vertex is not present")
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
            print("Start vertex is not present")
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

    def inDegree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not present")
            return
        ind=0
        for v in range(self.n):
            if self.adj[v][u]!=0:
                ind+=1
        return ind

    def dijkstra(self,s):
        for v in range(self.n):
            self.verticiesList[v].status=TEMPORARY
            self.verticiesList[v].pathLength=INFINITY
            self.verticiesList[v].predecessor=None
        self.verticiesList[s].pathLength=0
        while True:
            c=self.tempVertexMin()
            if c==None:
                return
            self.verticiesList[c].status=PERMANENT

            for v in range(self.n):
                if self.adj[c][v]!=0 and self.verticiesList[v].status==TEMPORARY:
                    if self.verticiesList[c].pathLength+self.adj[c][v]<self.verticiesList[v].pathLength:
                        self.verticiesList[v].predecessor=c
                        self.verticiesList[v].pathLength=self.verticiesList[c].pathLength+self.adj[c][v]
     
    def tempVertexMin(self):
        min=INFINITY
        x=None
        for v in range(self.n):
            if self.verticiesList[v].status==TEMPORARY and self.verticiesList[v].pathLength<min:
                min=self.verticiesList[v].pathLength
                x=v
        return x

    def findpath(self,source):
        s=self.getIndex(source)
        if s is None:
            print("Vertex is not present")
            return
        self.dijkstra(s)
        print("Source Vertex : ",source)
        for v in range(self.n):
            print("Destination vertex : ",self.verticiesList[v].name)
            if self.verticiesList[v].pathLength==INFINITY:
                print("There is no path from ",source,"to vertex ",self.verticiesList[v].name,"\n")
            else:
                self._findpath(s,v)

    def _findpath(self,s,v):
        path=[]
        sd=0
        count=0
        while v!=s:
            count+=1
            path.append(v)
            u=self.verticiesList[v].predecessor
            sd+=self.adj[u][v]
            v=u
        path.append(s)

        print("Shortest path : ",end=' ')
        for u in reversed(path):
            print(u,end=' ')
        print("\nShortest distance is : ",sd,"\n")

if __name__=="__main__":
    g=DirectedWeightedGraph()

    g.insertVertex("Zero")
    g.insertVertex("One")
    g.insertVertex("Two")
    g.insertVertex("Three")
    g.insertVertex("Four")
    g.insertVertex("Five")
    g.insertVertex("Six")
    g.insertVertex("Seven")
    g.insertVertex("Eight")

    g.insertEdge("Zero", "Three", 2)
    g.insertEdge("Zero", "One", 5)
    g.insertEdge("Zero", "Four", 8)
    g.insertEdge("One", "Four", 2)
    g.insertEdge("Two", "One", 3)
    g.insertEdge("Two", "Five", 4)
    g.insertEdge("Three", "Four", 7)
    g.insertEdge("Three", "Six", 8)
    g.insertEdge("Four", "Five", 9)
    g.insertEdge("Four", "Seven", 4)
    g.insertEdge("Five", "One", 6)
    g.insertEdge("Six", "Seven", 9)
    g.insertEdge("Seven", "Three", 5)
    g.insertEdge("Seven", "Five", 3)
    g.insertEdge("Seven", "Eight", 5)
    g.insertEdge("Eight", "Five", 3)

    g.findpath("Zero")