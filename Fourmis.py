from random import sample
import networkx as nx
import matplotlib.pyplot as plt

class AntHill:
    def __init__(self,F,Sv,S,Sd):
        self.F = F
        self.Sv = Sv
        self.S = S
        self.Sd = Sd


        self.Bhallways = dict()
        self.Ehallways = dict()
        for salle in sample(S, len((S))):
            self.Bhallways[(Sv, salle)] = True
            self.Ehallways[(salle, Sd)] = True



        def start():
            if Sv == F:
                return True

        def end():
            if Sd == F:
                return True

        def is_possible_to_go():
            for salle in S:
                if salle == 0:
                    return True
                else:
                    return False
        def movement():
            for salle in self.S:                                                  # F1
                if start():                                                   # start is valid (all ants there)
                    if is_possible_to_go():
                        beginning_hallways = list(self.Bhallways.keys())
                        for n in range(len(beginning_hallways)):
                            if beginning_hallways[n][1] == salle:
                                Bhallway = beginning_hallways[n]
                                self.Bhallways[Bhallway] = False
                                salle = 1
                                self.Sv -= 1
                                self.Bhallways[Bhallway] = True

                        end_hallways = list(self.Ehallways.keys())
                        for n in range(len(end_hallways)):
                            if end_hallways[n][0] == salle:
                                Ehallway = end_hallways[n]
                                self.Ehallways[Ehallway] = False
                                salle = 0
                                self.Sd += 1
                                self.Ehallways[Ehallway] = True


class Graph(AntHill):
    def __init__(self,F,Sv,S,Sd):
        AntHill.__init__(self,F,Sv,S,Sd)
        self.edges = []
        self.nodes = []


    def addEdge(self,a,b):
        edge = [a, b]
        self.edges.append(edge)

    def addNodes(self,Sv,S,Sd):
        nodes = [Sv,S,Sd]
        self.nodes.append(nodes)

    def visualize(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.nodes)
        graph.add_edges_from(self.edges)
        nx.draw_networkx(graph)
        plt.show()

F = 5
Sv = F
S = ["S1","S2","S3"]
Sd = 0

graph = Graph(F,Sv,S,Sd)

graph.addEdge(Sv,S[0])
graph.addEdge(Sv,S[1])
graph.addEdge(Sv,S[2])
graph.addEdge(S[0],Sd)
graph.addEdge(S[1],Sd)
graph.addEdge(S[2],Sd)

graph.visualize()





















































