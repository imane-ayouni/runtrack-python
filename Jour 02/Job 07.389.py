
class Personnes:
    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print(self.nom, self.prenom)

P1 = Personnes("Parker","Sarah")
P2 = Personnes("Smith","Sam")
P3 = Personnes("James","Hanna")
P4 = Personnes("Kim","Yang")


class Biblioteque :
    def __init__(self, nom, catalogue):
        self.nom = nom
        self.catalogue = catalogue
    def acheterLivre(self,nom,livre,quantite):
        catalogue: []
        self.nom = nom
        self.livre = livre
        self.quantite = quantite
        print(self.nom,self.livre)

    def inventaire (self,livre,quantite):
        self.livre = livre
        self.quantite = quantite
        inv = {"titre" : self.livre,
               "quantité" : self.quantite}
        print(inv)

    def louer(self,client,titre, quantite):
        self.client = client
        self.titre = titre
        self.quantite = quantite
        livre_du_client = []

        if self.titre in self.catalogue :
            livre_du_client.append(self.titre)
            x = self.catalogue.index(self.titre)
            quantité = self.quantite[x]
            quantité-=1
        print("vous avez prêté", livre_du_client)
        print("il en reste en stock: ", quantité)


# à rectifier
            #########
    def rendreLivre(self,client):
        self.client = client
        returned = []
        x = Biblioteque.louer(self.client,self.livre)
        for i in  x :
            returned.append(i)
        add = self.catalogue + returned
        return add
class Client(Personnes):
    def __init__(self, nom,prenom, collection):
        Personnes.__init__(self,nom,prenom)
        self.collection = collection
    def inventaire(self):
        print(Biblioteque.louer(self.client, self.livre))
            ##########
list_livre1 = {"Titres" : ["Happy to see you", "What a wonderful world", " always a pleasure"],
               "quantité" : [20,18,9]
               }
list_livre2 ={"titres" : ["night and day","between two waters","infinity now"],
              "quantité": [30,14, 21]
              }
list_livre3 = [["Good morning America","Mother's day","Happy memories"], [47,12,30]]



#Generer la liste des livres par auteur
catalogue_1= Biblioteque(P1.nom,"Catalogue 1")
catalogue_1.acheterLivre( P1.nom, str(list_livre1["Titres"]), str(list_livre1["quantité"]))

catalogue_2 = Biblioteque(P2.nom,"catalogue 2")
catalogue_2.acheterLivre(P2.nom, str(list_livre2["titres"]), str(list_livre2["quantité"]))


#Generer l'inventaire
inventaire_1 = Biblioteque(P1.nom,"inventaire 1")
inventaire_1.inventaire(list_livre1["Titres"],list_livre1["quantité"])

inventaire_2 = Biblioteque(P2.nom , "inventaire 2")
inventaire_2.inventaire(list_livre2["titres"],list_livre2["quantité"])

#Prêter un livre
pret = Biblioteque(P3.nom, list_livre3[0])
pret.louer(P3.nom,"Happy memories",list_livre3[1])













