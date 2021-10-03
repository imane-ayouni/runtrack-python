class Personnes:
    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print(self.nom, self.prenom)
    def get_nom(self):
        return self.nom
    def set_nom(self,nouveau_nom):
        self.nom = nouveau_nom

P1 = Personnes("Parker","Anna")
P2= Personnes("Ayouni","Imane")
P3 = Personnes("McDonald","Sam")
P1.SePresenter()
P2.SePresenter()
P3.SePresenter()
print(Personnes.get_nom(P1))
P1.set_nom("James")
P2.set_nom("Rabie")
P3.set_nom("Smith")
print(P1.nom)
print(P2.nom)
print(P3.nom)