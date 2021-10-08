class Personnes:
    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print(self.nom, self.prenom)

P1 = Personnes("Parker","Sarah")
P2 = Personnes("Smith","Sam")

class Auteur(Personnes):
    def __init__(self,nom,prenom):
        Personnes.__init__(self,nom,prenom)
        self.ouevres = []
    def listeroeuvres(self):
        for oeuvre in self.ouevres:
            print(oeuvre)
    def ecrireunlivre(self,livre):
        return self.ouevres.append(livre)
class Livre:
    def __init__(self,titre):
        self.titre = titre
        print(self.titre)
A1 = Auteur(P1.nom,P1.prenom)
A1.ecrireunlivre("Under the rain, Lost in the dessert")
A1.listeroeuvres()


A2 = Auteur(P2.nom,P2.prenom)
A2.ecrireunlivre("She won ! , Happy holidays")
A2.listeroeuvres()














