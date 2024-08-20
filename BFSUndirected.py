INITIAL=0
WAITING=1
VISITED=2

class vertex:
    def __init__(self,name):
        self.name=name

class BFSUndirected:
    def __init__(self,size=20):
        self.adj=[[ 0 for column in range(size)] for row in range(size)]
        self.n=0
        self.verticesList=[]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.adj[i][j],end='')
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
        return None
    
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
            print("Start vertex is not found")
        elif v is None:
            print("End vertex is not present")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]!=0:
            print("Vertex is already present")
        else:
            self.adj[u][v]=1

    def removeEdge(self,s1,s2):
        u=self.getIndex(s1)
        v=self.getIndex(s2)

        if u is None:
            print("Start vertex is not present")
        elif v is None:
            print("End vertex is not present")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]==0:
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
        self.verticesList.pop(u)
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

    def Degree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not found")
            return
        deg=0
        for v in range(self.n):
            if self.adj[u][v]!=0:
                deg+=1
        return deg

    def bfsC(self,v,cN):
        from queue import Queue
        qu=Queue()
        qu.put(v)
        self.verticesList[v].state=WAITING

        while qu.qsize()!=0:
            v=qu.get()
            self.verticesList[v].state=VISITED
            self.verticesList[v].componentNumber=cN

            for i in range(self.n):
                if self.adj[v][i]!=0 and self.verticesList[i].state==INITIAL:
                    qu.put(i)
                    self.verticesList[i].state=WAITING

    def isConnected(self):
        for v in range(self.n):
            self.verticesList[v].state=INITIAL
        cN=1
        self.bfsC(0,cN)
        
        for v in range(self.n):
            if self.verticesList[v].state==INITIAL:
                cN+=1
                self.bfsC(v,cN)
        if cN ==1:
            print("Graph is connected")
            return True
        else:
            print("Graph is not connected, it has",cN," connected components")
            for v in range(self.n):
                print(self.verticesList[v].name," ",self.verticesList[v].componentNumber)
            return False

if __name__=="__main__":
    g=BFSUndirected()

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
    g.insertVertex("Ten")
    g.insertVertex("Eleven")
    g.insertVertex("Twelve")
    g.insertVertex("Thirteen")
    g.insertVertex("Fourteen")
    g.insertVertex("Fifteen")
    g.insertVertex("Sixteen")

    g.insertEdge("Zero","One")
    g.insertEdge("Zero","Two")
    g.insertEdge("Zero","Three")
    g.insertEdge("One","Three")
    g.insertEdge("Two","Five")
    g.insertEdge("Three","Four")
    g.insertEdge("Four","Five")
    g.insertEdge("Six","Seven")
    g.insertEdge("Six","Eight")
    g.insertEdge("Seven","Ten")
    g.insertEdge("Eight","Nine")
    g.insertEdge("Nine","Ten")
    g.insertEdge("Eleven","Twelve")
    g.insertEdge("Eleven","Fourteen")
    g.insertEdge("Eleven","Fifteen")
    g.insertEdge("Twelve","Thirteen")
    g.insertEdge("Thirteen","Fourteen")
    g.insertEdge("Fourteen","Sixteen")

    g.isConnected()
