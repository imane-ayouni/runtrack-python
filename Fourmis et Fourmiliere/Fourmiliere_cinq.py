import networkx as nx
import matplotlib.pyplot as plt

class Vestibule:
    def __init__(self,name, size):
        self.name = name
        self.size = size

class Salles:
    def __init__(self,name,size):
        self.name = name
        self.size = size

class Dorm:
    def __init__(self,name,size):
        self.name = name
        self.size = size
size = 50

Sv = Vestibule("Sv",size)
salles = Salles(("S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13","S14"),(0,0,0,0,0,0,0,0,0,0,0,0,0,0))
dorm = Dorm("Sd",0)
print("There are ", size, " ants")



class Anthill:
    def __init__(self):
        self.nodes = []
        self.edges = []
    def addNodes(self,a,b,c,d):
        nodes = [a,b,c,d]
        self.nodes.append(nodes)
    def addEdges(self,a,b):
        edges = [a,b]
        self.edges.append(edges)
    def visualizeGraph(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.nodes)
        graph.add_edges_from(self.edges)
        nx.draw_networkx(graph)
        plt.show()

graph = Anthill()
graph.addEdges(salles.name[0],salles.name[1])
graph.addEdges(salles.name[1],salles.name[2])
graph.addEdges(salles.name[2],salles.name[3])
graph.addEdges(salles.name[3],dorm.name)
graph.addEdges(Sv.name,salles.name[0])
graph.addEdges(salles.name[1],salles.name[4])
graph.addEdges(salles.name[4],salles.name[3])
graph.addEdges(salles.name[12],dorm.name)
graph.addEdges(salles.name[7],salles.name[11])
graph.addEdges(salles.name[11],salles.name[12])
graph.addEdges(salles.name[5],salles.name[6])
graph.addEdges(salles.name[6],salles.name[8])
graph.addEdges(salles.name[8],salles.name[13])
graph.addEdges(salles.name[13],dorm.name)
graph.addEdges(salles.name[6],salles.name[9])
graph.addEdges(salles.name[9],salles.name[13])
graph.addEdges(salles.name[0],salles.name[5])
graph.addEdges(salles.name[5],salles.name[7])
graph.addEdges(salles.name[7],salles.name[10])
graph.addEdges(salles.name[10],salles.name[12])

graph.visualizeGraph()























