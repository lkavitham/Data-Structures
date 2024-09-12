class vertex:
    def __init__(self,name):
        self.name=name

class UndirectedWeightedGraph:
    def __init__(self,size=20):
        self.adj=[[0 for column in range(size)] for row in range(size)]
        self.n=0
        self.verticesList=[]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.adj[i][j],end=' ')
        print

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
                    edges.append((self.verticesList[i].name,self.verticesList[j].name))
        return edges

    def getIndex(self,s):
        index=0
        for name in(vertex.name for vertex in self.verticesList):
            if s==name:
                return index
            index+=1
        return None

    def insertVertex(self,name):
        if name in(vertex.name for vertex in self.verticesList):
            print("Vertex is already present")
            return
        self.verticesList.append(vertex(name))
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
        elif self.adj[u][v]==1:
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
        elif self.adj[u][v]==0:
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

    def degree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vetex is not present")
            return
        deg=0
        for v in range(self.n):
            if self.adj[u][v]!=0:
                deg+=1
        return deg

    def kruskal(self):
        edgeList=[]

        for u in range(self.n):
            for v in range(self.n):
                if self.adj[u][v]!=0:
                    edgeList.append((u,v,self.adj[u][v]))

        edgeList=sorted(edgeList,key=lambda item: item[2],reverse=True)

        for v in range(self.n):
            self.verticesList[v].father=None

        r1=None
        re=None
        edgeInTree=0
        wtTree=0

        while len(edgeList)!=0 and edgeInTree<self.n-1:
            edge=edgeList.pop()
            v1=edge[0]
            v2=edge[1]
            v=v1
            while self.verticesList[v].father!=None:
                v=self.verticesList[v].father
            r1=v
            v=v2
            while self.verticesList[v].father!=None:
                v=self.verticesList[v].father
            r2=v

            if r1!=r2:
                edgeInTree+=1
                print(self.verticesList[v1].name,"->",self.verticesList[v2].name)
                wtTree+=edge[2]
                self.verticesList[r2].father=r1
        if edgeInTree<self.n-1:
            print("Graph is not connected, no spanning tree possible")
            return
        print("Weight okf Minimum Spanning Tree is : ",wtTree)

if __name__=="__main__":
    g=UndirectedWeightedGraph()

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

    g.kruskal()