INITIAL=0
VISITED=1

class vertex:
    def __init__(self,name):
        self.name=name
    
class DFS:
    def __init__(self,size=20):
        self.adj=[[0 for column in range(size)] for row in range(size)]
        self.n=0
        self.verticesList=[]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.adj[i][j],end=' ')
        print()
    
    def numVertex(self):
        return self.n

    def numEdges(self):
        e=0
        for  i in range(self.n):
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

    def get_Index(self,s):
        index=0
        for name in (vertex.name for vertex in self.verticesList):
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

    def insertEdge(self,s1,s2):
        u=self.get_Index(s1)
        v=self.get_Index(s2)

        if u is None:
            print("Start vertex is not present")
        elif v is None:
            print("Edge vertex is not present")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]!=0:
            print("Edge is already present")
        else:
            self.adj[u][v]=1

    def removeEdge(self,s1,s2):
        u=self.get_Index(s1)
        v=self.get_Index(s2)

        if u is None:
            print("Start vertex is not present")
        elif v is None:
            print("Edge vertex is not present")
        elif u==v:
            print("Invalid")
        elif self.adj[u][v]!=1:
            print("Edge is not present")
        else:
            self.adj[u][v]=0

    def removeVertex(self,s):
        u=self.get_Index(s)
        if u is None:
            print("Vertex is not present")
            return
        self.adj.pop(u)
        for v in range(self.n):
            self.adj[v].pop(u)
        self.verticesList.pop(u)
        self.n-=1

    def isAdjacent(self,s1,s2):
        u=self.get_Index(s1)
        v=self.get_Index(s2)

        if u is None:
            print("Start vertex is not present")
        elif v is None:
            print("Edge vertex is not present")
        elif u==v:
            print("Invalid")
        else:
            return False if self.adj[u][v]==0 else True

    def outDegree(self,s):
        u=self.get_Index(s)
        if u is None:
            print("Vertex is not present")
            return
        outd=0
        for v in range(self.n):
            if self.adj[u][v]!=0:
                outd+=1
        return outd

    def inDegree(self,s):
        u=self.get_Index(s)
        if u is None:
            print("Vertex is not present")
            return
        ind=0
        for v in range(self.n):
            if self.adj[v][u]!=0:
                ind+=1
        return ind

    def dfsTreeEdge(self):
        s=input("Enter the start vertex : ")
        u=self.get_Index(s)
        if u is None:
            print("Vertex is not present")
            return
        for v in range(self.n):
            self.verticesList[v].state=INITIAL
            self.verticesList[v].predecessor=None
        self.dfs1(u)

        for v in range(self.n):
            if self.verticesList[v]==INITIAL:
                self.dfs1(v)
        print("Tree Edges : ")
        for v in range(self.n):
            u=self.verticesList[v].predecessor
            if u!=None:
                print("(",self.verticesList[u].name,", ",self.verticesList[v].name,")")

    def dfs1(self,v):
        from queue import LifoQueue
        st=LifoQueue()
        st.put(v)

        while st.qsize()!=0:
            v=st.get()
            if self.verticesList[v].state==INITIAL:
                print(self.verticesList[v].name,end=' ')
                self.verticesList[v].state=VISITED
            for i in range(self.n-1,-1,-1):
                if self.adj[v][i]!=0 and self.verticesList[i].state==INITIAL:
                    st.put(i)
                    self.verticesList[i].predecessor=v
        print()

    def dfsTraversal(self):
        s=input("Enter starting vertex : ")
        u=self.get_Index(s)
        if u is None:
            print("Vertex is not present")
            return
        for v in range(self.n):
            self.verticesList[v].state=INITIAL
        self.dfs(u)
        
    def dfs(self,v):
        from queue import LifoQueue
        st=LifoQueue()
        st.put(v)

        while st.qsize()!=0:
            v=st.get()
            if self.verticesList[v].state==INITIAL:
                print(self.verticesList[v].name,end=' ')
                self.verticesList[v].state=VISITED
            for i in range(self.n-1,-1,-1):
                if self.adj[v][i]!=0 and self.verticesList[i].state==INITIAL:
                    st.put(i)
        print()

    def dfsAll(self):
        s=input("Enter starting vertex : ")
        u=self.get_Index(s)
        if u is None:
            print("Vertex is not present")
            return
        
        for v in range(self.n):
            self.verticesList[v].state=INITIAL
        self.dfs(u)

        for v in range(self.n):
            self.verticesList[v].state=INITIAL
            self.dfs(v)
        
if __name__=="__main__":
    g=DFS()

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

    
    g.insertEdge("Zero","One")
    g.insertEdge("Zero","Three")
    g.insertEdge("One","Two")
    g.insertEdge("One","Four")
    g.insertEdge("One","Five")
    g.insertEdge("Two","Five")
    g.insertEdge("Two","Seven")
    g.insertEdge("Three","Six")
    g.insertEdge("Four","Three")
    g.insertEdge("Five","Three")
    g.insertEdge("Five","Seven")
    g.insertEdge("Five","Six")
    g.insertEdge("Five","Eight")
    g.insertEdge("Seven","Eight")
    g.insertEdge("Seven","Ten")
    g.insertEdge("Eight","Eleven")
    g.insertEdge("Nine","Six")
    g.insertEdge("Eleven","Nine")

    g.dfsTreeEdge()
