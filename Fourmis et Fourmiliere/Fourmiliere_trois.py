# Importer les librairie necessaires pour visualiser le graph
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Créer la class du vestibule qui contient son nom, taille et une fonction pour commencer le jeu

class Vestibule:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getSize(self):
        return size

    def getName(self):
        return self.name

    def start(self, ants):
        self.ants = ants
        ants = self.size
        print("There are ", ants, " ants in the vestibule")
        print("----------------------")
        return ants


# Créer la class des salles sui contient les nom, tailles et une fonction qui obtient les couloirs ou les fourmilles pouvent se déplacer

class Salles:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getRooms(self):
        x = dict(zip(self.name, self.size))
        return x

    def hallways(self, vestibule, salles, dorm):
        self.vestibule = vestibule
        self.salles = salles
        self.dorm = dorm
        salles = self.name
        self.hallways = []
        self.hallways.append((vestibule, salles[0]))
        self.hallways.append((salles[0], salles[1]))
        self.hallways.append((salles[1], salles[2]))
        self.hallways.append((salles[0], salles[3]))
        self.hallways.append((salles[3], dorm))
        return self.hallways




# La class qui contient le nom et la taille du dortoire

class Dorm:
    def __init__(self, name, size):
        self.name = name
        self.size = size


# Définir les paramêtres

size = 5

Sv = Vestibule("Sv", size)
Sv.start(size)
salles = Salles(("S1", "S2", "S3", "S4"), (0, 0, 0, 0))
dorm = Dorm("Sd", 0)
d = dorm.name
s = Salles(salles.name, salles.size)
hallways = Salles.hallways(salles, Sv.name, salles, dorm.name)




#Créer la fonction qui va établir toutes les connections entre chaques salle et toutes les autre


def buildGraph():
    edges = [
        [Sv.name, salles.name[0]],
        [salles.name[0], salles.name[1]],
        [salles.name[1], salles.name[2]],
        [salles.name[0], salles.name[3]],
        [salles.name[3], d]
    ]
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]

        graph[a].append(b)
        graph[b].append(a)
    return graph

if __name__ == "__main__":
    g = buildGraph()

# Créer la fonction qui détermine le chemin le plus court en commençant par le vestibule et arrivant au dortoir

def shortestPath(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                newPath = list(path)
                newPath.append(neighbour)
                queue.append(newPath)
                if neighbour == goal:
                    return list(newPath)
            explored.append(node)

if __name__ == "__main__":
    Sp = shortestPath(g, "Sv", "Sd")





# Créer la classe des fourmilles qui a comme attribut toutes les salles et qui contient la fonction qui déplace les fourmilles

class Ant:
    def __init__(self, ant, vestibule, rooms, dorm, hallways):
        self.ant = ant
        self.vestibule = vestibule
        self.rooms = rooms
        self.dorm = dorm
        self.hallways = hallways
        v = Vestibule("Sv", self.ant)
        vestibule = v.name
        self.ves_size = v.size
        self.ves_size = self.ant
        a = Vestibule.getSize(self.vestibule)  # ant = how many ants in the entrance
        ant = a
        s = Salles.getRooms(self.rooms)
        rooms = s
        d = Dorm("Sd", 0)
        dorm = d.name
        self.dormSize = d.size
        h = Salles.hallways(self.rooms, self.vestibule, self.rooms, self.dorm)
        hallways = h
        self.newHallways = []
        self.newHallways.append((Sp[0],Sp[1]))
        self.newHallways.append((Sp[1],Sp[2]))
        self.newHallways.append((Sp[2],Sp[3]))

# Définir la fonction qui itérer à travers tous les tunnels, et quand un des tunnels existe dans la liste des tunels 
# courts obtenus par la fonction shortPath, elle déplace les fourmis du vestibule et compte les étapes

    def go(self, a, x, steps):
        self.steps = steps
        self.x = x
        self.a = a
        for i in self.hallways:
            if i in self.newHallways:
                steps += 1
                y = (self.ant-self.ant) + x
                print("Ant: ",y, i[0], " -----> ", i[1])
                if self.newHallways.index(i) == len(self.newHallways) - 1:
                    print("Step: ",steps-2)
                    print("Remains in vestibule: ", a-1, " ants")
                    print("   -------------")
                    a -= 1
                    if self.a == 1:
                        break
                    self.go(a,x+1,steps-2)



go = Ant(size,Sv.name,salles,dorm.name,hallways)
go.go(size,1,0)



# Créer la classe qui visualise la fourmillière en graph

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
graph.addEdges(Sv.name,salles.name[0])
graph.addEdges(salles.name[0],salles.name[1])
graph.addEdges(salles.name[3],dorm.name)
graph.addEdges(salles.name[0],salles.name[3])
graph.addEdges(salles.name[1],salles.name[2])


graph.visualizeGraph()









