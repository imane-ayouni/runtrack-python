# Importer les librairie necessaires pour visualiser le graph

import networkx as nx
import matplotlib.pyplot as plt

#Créer la class du vestibule qui contient son nom, taille et une fonction pour commencer le jeu

class Vestibule:
    def __init__(self,name, size):
        self.name = name
        self.size = size
    def getSize(self):
        return size
    def getName(self):
        return self.name

    def start(self,ants):
        self.ants = ants
        ants = self.size
        print("There are ",ants, " ants in the vestibule")
        print("----------------------")
        return ants

#Créer la class des salles sui contient les nom, tailles et une fonction qui obtient les couloirs ou les fourmilles pouvent se déplacer

class Salles:
    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.rooms = dict(zip(self.name, self.size))

    def getRooms(self):
        x = dict(zip(self.name,self.size))
        return x

    def hallways(self,vestibule,salles,dorm):
        self.vestibule = vestibule
        self.salles = salles
        self.dorm = dorm
        salles = self.name
        self.hallways = []
        self.hallways.append((vestibule,salles[0]))
        self.hallways.append((salles[0],salles[1]))
        self.hallways.append((salles[1],dorm))
        self.hallways.append((dorm,vestibule))
        return self.hallways

# Créer la classe des fourmilles qui a comme attribut toutes les salles et qui contient la fonction qui déplace les fourmilles

class Ant:
    def __init__(self,ant,vestibule,rooms,dorm,hallways):
        self.ant = ant
        self.vestibule = vestibule
        self.rooms = rooms
        self.dorm = dorm
        self.hallways = hallways
        v = Vestibule("Sv",self.ant)
        vestibule = v.name
        self.ves_size = v.size
        self.ves_size = self.ant
        a = Vestibule.getSize(self.vestibule)   # ant = how many ants in the entrance
        ant = a
        s = Salles.getRooms(self.rooms)
        rooms = s
        name = rooms.keys()
        size = rooms.values()
        d = Dorm("Sd",0)
        dorm = d.name
        self.dormSize = d.size
        h = Salles.hallways(self.rooms,self.vestibule,self.rooms,self.dorm)
        hallways = h

    # Pour chaqu'une des salles s'il y a un couloir entre elle et le vestibule, la fourmille peut se déplacer
    # Puis s'il y a un couloir entre le salle courante et la suivante, la fourmille se déplace
    # Et s'il y a un couloir entre la salle suivante (maintenant courante), la fourmille peut se déplacer
    # Enfin la fourmille retourne au vestibule
    
    def go(self, a,x,steps):
        self.steps = steps
        self.x = x
        self.a = a
        a = self.ant
        for i in range(len(self.rooms.name)):
            if (self.vestibule, self.rooms.name[i]) in self.hallways:
                self.ant -= 1
                self.rooms.size[i] == 1
                steps += 1
                y = (self.ant - self.ant) + x
                print("Step ", steps)
                print("Ant: ", y, " ", self.vestibule, " ---> ", self.rooms.name[i])
                print("------------")

                if (self.rooms.name[i], self.rooms.name[i + 1]) in self.hallways:
                    self.rooms.size[i] == 0
                    steps += 1
                    self.rooms.size[i + 1] == 1
                    print("Step ", steps)
                    print("Ant: ", y, " ", self.rooms.name[i], " ---> ", self.rooms.name[i + 1])
                    print("------------")

                    if (self.rooms.name[i + 1], self.dorm) in self.hallways:
                        self.rooms.size[i + 1] == 0
                        steps += 1
                        self.dormSize += 1
                        print("Step ", steps)
                        print("Ant: ", y, " ", self.rooms.name[i + 1], " ---> ", self.dorm)
                        print("------------")

                        if (self.dorm,self.vestibule) in self.hallways:
                            steps+= 1
                            print("Step ", steps)
                            print("Ant: ", y, " ", self.dorm, " ---> ", self.vestibule)
                            print("Remains in vestibule: ", self.ves_size, " ants")
                            print("------------")
                            if self.ant == 0:
                                break


                self.go(self.ant,x+1,steps)

# La class qui contient le nom et la taille du dortoire 

class Dorm:
    def __init__(self,name,size):
        self.name = name
        self.size = size


# Définir les paramêtres
size = 5

Sv = Vestibule("Sv",size)
Sv.start(size)
salles = Salles(("S1","S2"),(0,0))
dorm = Dorm("Sd",0)
d = dorm.name
s = Salles(salles.name,salles.size)
hallways = Salles.hallways(salles,Sv.name,salles,dorm.name)
go = Ant(size,Sv.name,salles,dorm.name,hallways)

# Executer la fonction qui jour le jeu

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
graph.addEdges(salles.name[1],dorm.name)
graph.addEdges(dorm.name,Sv.name)


graph.visualizeGraph()
