size = 9
# On importe les fichiers qui contient les grides du jeux en differents niveaux
import easy
import medium
import hard

# On laisse l'utilisateur choisir le niveau

level_choice = input("Choose the level of complexity: easy, medium or hard : ")
if level_choice == "easy":
    board = easy.board
if level_choice == "medium":
    board = medium.board
if level_choice == "hard":
    board = hard.board


# Creer la fonction qui va verifier si les cases sont assigniées ou pas, et produit une liste avec les index des cases vides

def is_unassigned(row,col):
    unassigned_number = 0
    for i in range(0,size):
        for j in range(0,size):
            if board[i][j] == 0:
                row = i
                col = j
                unassigned_number = 1
                index = [row,col,unassigned_number]
                return index
    index = [-1,-1,unassigned_number]
    return index

# Creer une fonction qui determiner les possibilité de  mettre un nombre dans une case ou pas

def is_possible(number,row,col):
    for i in range(0,size):
        if board[row][i] == number:
            return  False
    for i in range(0,size):
        if board[i][col] == number:
            return False

# Pour savoir l'index du debut de la submatrix (3*3)

    row_start = (row//3)*3
    col_start = (col//3)*3
    for i in range(row_start,row_start+3):
        for j in range(col_start,col_start+3):
            if board[i][j] == number:
                return False

    return True

# Creer la fonction qui determine si on peu mettre un nombre dans une case ou pas

def solve_game():
    row = 0
    col = 0

# Si toues les cases sont pleines, le jeu est fini

    index = is_unassigned(row,col)
    if index[2] == 0 :
        return True

    row = index[0]
    col = index[1]

# S'il est possible de mettre un certain nombre dans la case, on le met. Sinon on revient à l'étape precedante et on choise un autre numero

    for i in range(0,10):
        if is_possible(i,row,col):
            board[row][col] = i
            if solve_game():
                return True
            board[row][col] = 0


    return False


# Fonction pour visialuser le tableau
if solve_game():
    for i in board:
        print(*i, sep=" ")























