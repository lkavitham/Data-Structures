class Vertex:
    def __init__(self,name):
        self.name=name

class DirectedGraph:
    def __init__(self):
        self.graph={}
        self.vertexObjects=set()

    def display(self):
        for vertex in self.graph:
            print(vertex,"  --> ",self.graph[vertex])
        print()

    def numVertices(self):
        return len(self.graph)

    def numEdges(self):
        e=0
        # Iterate through each adjacency list in the graph
        for adjList in self.graph.values():
            e+=len(adjList)
        return e

    def vertices(self):
        return list(self.graph)

    def Edges(self):
        edgeList=[]
        for u in self.graph:
            for v in self.graph[u]:
                edgeList.append((u,v))
        return edgeList

    def insertVertex(self,name):
        if name in self.graph:
            print("Vertes is already present")
        else:
            self.graph[name]=set()
            self.vertexObjects.add(Vertex(name))

    def insertEdge(self,s1,s2):
        if s1 not in self.graph:
            print("Start vertex is not present")
        elif s2 not in self.graph:
            print("End vertex is not present")
        elif s1==s2:
            print("Not a valid edge")
        elif s2 in self.graph[s1]:
            print("Edge already present")
        else:
            self.graph[s1].add(s2)

    def removeEdge(self,s1,s2):
        if s2 not in self.graph[s1]:
            print("Edge is not found")
        else:
            self.graph[s1].remove(s2)

    def removeVertices(self,name):
        if name not in self.graph:
            print("Vertex is not present")
            return
        self.graph.pop(name)

        for u in self.graph:
            if name in self.graph[u]:
                self.graph[u].remove(name)

        for vertex in self.vertexObjects:
            if name==vertex.name:
                v=vertex
                break
        self.vertexObjects.remove(v)

    def isAdjacenct(self,s1,s2):
        if s1 not in self.graph:
            print("start vertex is not present")
            return
        if s2 not in self.graph:
            print("End vertex is not present")
            return False
        return s2 in self.graph[s1]

    def outDegree(self,s):
        if s not in self.graph:
            print("Vertex not present in the graph")
            return
        return len(self.graph[s])

    def inDegree(self,s):
        if s not in self.graph:
            print("Vertex is not present")
            return
        ind=0
        for u in self.graph:
            ind+=list(self.graph[u]).count(s)
        return ind

    def getVertex(self,s):
        for vertex in self.vertexObjects:
            if s==vertex.name:
                return vertex
        return None
    
if __name__=="__main__":
    l=DirectedGraph()

    l.insertVertex("AA")
    l.insertVertex("BB")
    l.insertVertex("CC")
    l.insertVertex("DD")
    l.insertVertex("EE")

    l.insertEdge("AA","BB")
    l.insertEdge("AA","CC")
    l.insertEdge("CC","DD")
    l.insertEdge("DD","AA")
    l.insertEdge("CC","AA")
    l.insertEdge("BB","EE")

    while True:
        print("1.Display Adj list,vertices and edges")
        print("2.Insert Vertex")
        print("3.Insert Edge")
        print("4.Delete Vertex")
        print("5.Delete Edge")
        print("6.Dispay Indegree , outdegree")
        print("7.Adjacent ")
        print("8.Quit")

        option=int(input("Enter your choice :"))

        if option==1:
            l.display()
            print("No. of vertices: ",l.numVertices())
            print("No. of edges: ",l.numEdges())
            print("List of vertices : ",l.vertices())
            print("List of edges : ",l.Edges())
        elif option==2:
            name=input("Enter the name of the vertex to be inserted: ")
            l.insertVertex(name)
        elif option==3:
            s1=input("Enter the name of first vertex : ")
            s2=input("Enter the name of end vertex :")
            l.insertEdge(s1,s2)
        elif option==4:
            s=input("Enter the name of the vertex to be deleted : ")
            l.removeVertices(s)
        elif option==5:
            s1=input("Start vertex :")
            s2=input("End vertex : ")
            l.removeEdge(s1,s2)
        elif option==6:
            s=input("Vertex name :")
            i=l.inDegree(s)
            if i is not None:
                print("Indegree of ",s," is ",i )
            o=l.outDegree(s)
            if o is not None:
                print("OutDegree of ",s, " is ",o)
        elif option==7:
            s1=input("Enter the name of first vertex : ")
            s2=input("Enter the name of end vertex :")
            if l.isAdjacenct(s1,s2):
                print("There is an edge from ",s1," to ",s2)
            else:
                print("There is an edge from ",s2," to ",s1)
        elif option==8:
            break
        else:
            print("Wrong Option")
        print()