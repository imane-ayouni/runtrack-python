
n = int(input("Choose a number "))

board = [[0]*n for i in range(n)]



def is_attacked(row, col):
    for c in range(0,n):
        if board[row][c]==1 or board[c][col] == 1:
            return True
    for upD in range(0,n):
        for dwD in range(0,n):
            if (upD+dwD == row+col) or (upD-dwD == row-col):
                if board[upD][dwD] == 1:
                    return True
    return False

def placeQueen(q):
    if q == 0:
        return True
    for row in range(0,n):
        for col in range(0,n):
            if (not (is_attacked(row,col))) and (board[row][col] != 1 ):
                board[row][col] = 1
                if placeQueen(q - 1) ==True:
                    return True
                board[row][col] = 0

    return False

placeQueen(n)
for i in board:
    print(i)




