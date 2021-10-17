
#Definir la fonction qui contient le numero de disques et les 3 batonets

def hanoiTower(disk, beginning, end, middle):
    #On determine que si on n'a qu'un seule disque on le change directement du premier au dernier batonets
    if disk == 1:
        print("Disk number 1 ",beginning," --> " , end )
        return
    # Pour le reste des disques on applique la recursivité
    hanoiTower(disk -1, beginning, middle, end)
    print("Disk number", disk, beginning , " --> ", end )
    hanoiTower(disk-1, middle, end, beginning)

disk = int(input('Choose the number of the disks: '))
hanoiTower(disk, "Rod 1", "Rod 2", "Rod 3" )
