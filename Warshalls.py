class vertex:
    def __init__(self,name):
        self.name=name

class Warshalls:
    def __init__(self,size=20):
        self.adj=[[0 for column in range(size)] for row in range(size)]
        self.n=0
        self.verticesList=[]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.adj[i][j],end='')
            print()

    def numvertices(self):
        return self.n

    def numEdges(self):
        e=0
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j]!=0:
                    e+=1
        return e

    def vertices(self):
        return [vertex.name for vertex in self.verticesList]

    def Edges(self):
        edges=[]
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j]!=0:
                    edges.append((self.vertices[i].name,self.vertices[j].name ))

    def getIndex(self,s):
        index=0
        for name in (vertex.name for vertex in self.verticesList):
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
            print("Start vertex is not present")
        elif v is None:
            print("End vertex is not present")
        elif u==v:
            print("Invalid")
        else:
            self.adj[u][v]=1

    def deleteEdge(self,s1,s2):
        u=self.getIndex(s1)
        v=self.getIndex(s2)

        if u is None:
            print("Start is not present")
        elif v is None:
            print("End vertex is not found")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]==0:
            print("Edge is not found")
        else:
            self.adj[u][v]=0

    def deleteVertex(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not found")
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
            print("Start vertex is not present")
        elif v is None:
            print("End vertex is not present")
        return False if self.adj[u][v]==0 else True
    def outDegree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex is not found")
            return
        outd=0
        for v in range(self.n):
            if self.adj[u][v]!=0:
                outd+=1

    def indegree(self,s):
        u=self.getIndex(s)
        if u is None:
            print("Vertex not found")
            return
        ind=0
        for v in range(self.n):
            if self.adj[v][u]!=0:
                ind+=1
            
    def warshall(self):
        p=[[ 1 for column in range(self.n)] for row in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                p[i][j]=self.adj[i][j]

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    p[i][j]=p[i][j] or ( p[i][k] and p[k][j])

        for i in range(self.n):
            for j in range(self.n):
                if p[i][j]!=0:
                    print("1",end='')
                else:
                    print("0",end='')
            print()
        print()

if __name__=="__main__":
    w=Warshalls()

    w.insertVertex("Zero")
    w.insertVertex("One")
    w.insertVertex("Two")
    w.insertVertex("Three")

    w.insertEdge("Zero","One")
    w.insertEdge("Zero","Three")
    w.insertEdge("One","Two")
    w.insertEdge("Two","One")
    w.insertEdge("Three","Zero")
    w.insertEdge("Three","Two")

    w.warshall()