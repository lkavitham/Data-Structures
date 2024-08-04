class Vertex:
    def __init__(self,name):
        self.name=name

class DirectedGraph:
    def __init__(self,size=20):
        self.adj=[ [0 for column in range(size)]  for row in range(size)]    # Nested list comprehension
        self.n=0
        self.vertexList=[]

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.adj[i][j],end=' ')
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
    
    def vertices(self):
        return [vertex.name for vertex in self.vertexList]
    
    def edges(self):
        edges=[]
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j]!=0:
                    edges.append((self.vertexList[i].name ,self.vertexList[j].name))
        return edges
    
    def getindex(self,s):    
        index=0
        for name in (vertex.name for vertex in self.vertexList):
            if s==name:
                return index
            index+=1
        return None
    
    def insertVertex(self,name):
        if name in (vertex.name for vertex in self.vertexList):
            print("Vertex is already present")
            return
        self.vertexList.append(Vertex(name))
        self.n+=1

    def insertEdge(self,s1,s2):
        u=self.getindex(s1)
        v=self.getindex(s2)

        if u is None:
            print("start vertex is not present,first insert the start vertex ")
        elif v is None:
             print("end vertex is not present,first insert the end vertex ")
        elif u==v:
            print("not valid edge")
        elif self.adj[u][v]!=0:
            print("Edge is already present")
        else:
            self.adj[u][v]=1

    def removeEdge(self,s1,s2):
        u=self.getindex(s1)
        v=self.getindex(s2)

        if u is None:
            print("start vertex is not present")
        elif v is None:
            print("end vertex is not present")
        elif u==v:
            print("not valid edge")
        elif self.adj[u][v]==0:
            print("Edge not present")
        else:
            self.adj[u][v]=0

    def removeVertex(self,name):
        u=self.getindex(name)
        if u is None:
            print("vetex not present")
            return
        self.adj.pop(u)
        for i in range(self.n):
            self.adj[i].pop(u)
        self.vertexList.pop(u)
        self.n-=1

    def isAdjacnet(self,s1,s2):
        u=self.getindex(s1)
        v=self.getindex(s2)
        if u is None:
            print("start vertex is not present")
        elif v is None:
            print("start vertex is not present")
            return False
        return False if self.adj[u][v]==0 else True
    
    def outDegree(self,s):
        u=self.getindex(s)
        if u is None:
            print("vertex is not present")
            return
        outd=0
        for v in range(self.n):
            if self.adj[u][v]!=0:
                outd+=1
        return outd
    
    def inDegree(self,s):
        u=self.getindex(s)
        if u is None:
            print("vertex is not present")
            return
        ind=0
        for v in range(self.n):
            if self.adj[v][u]!=0:
                ind+=1
        return ind
    
if __name__=="__main__":
    g=DirectedGraph()

    g.insertVertex("AA")
    g.insertVertex("BB")
    g.insertVertex("CC")
    g.insertVertex("DD")
    g.insertVertex("EE")

    g.insertEdge("AA","BB")
    g.insertEdge("AA","CC")
    g.insertEdge("CC","DD")
    g.insertEdge("DD","AA")
    g.insertEdge("CC","AA")
    g.insertEdge("BB","EE")

    while True:
        print("1.Display Adjacency list,vertices and edges")
        print("2.Insert a vertex")
        print("3.Insert a edge")
        print("4.Remove a vertex")
        print("5.Remove a edge")
        print("6.Display indegree and out degree of a vertex")
        print("7.Check if there is an edge between a vertex")
        print("8.Quit")

        option=int(input("Enter your choice : "))
         
        if option==1:
            print("No. of vertices: ",g.numVertices())
            print("No. of edges: ",g.numEdges())
            print("List of vertices : ",g.vertices())
            print("List of edges : ",g.edges())
            g.display()
        
        elif option==2:
            s=input("Enter the name of the vertex to be inserted : ")
            g.insertVertex(s)
        
        elif option==3:
            s1=input("Enter the name of the start vertex :")
            s2=input("Enter the name of the end vertex :")
            g.insertEdge(s1,s2)

        elif option==4:
            s=input("Enter the name of the vertex to be removed : ")
            g.removeVertex(s)
        
        elif option==5:
            s1=input("Enter the name of the start vertex :")
            s2=input("Enter the name of the end vertex :")
            g.removeEdge(s1,s2)

        elif option==6:
            s=input("Enter the name of the edge : ")
            i=g.inDegree(s)
            if i is not None:
                print("Indgree of", s , "is", i)
            o=g.outDegree(s)
            if o is not None:
                print("Outdegree of", s ,"is", o)
            
        elif option==7:
            s1=input("Enter the name of the first vertex :")
            s2=input("Enter the name of the second vertex :")
            if g.isAdjacnet(s1,s2):
                print("There is an edge from", s1 , " to ", s2)
            else:
                print("There is no edge from", s1 , " to ", s2)
        
        elif option==8:
            break

        else:
            print("Wrong Option")

        print()





