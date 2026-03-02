# to initialize the board state

board = {}

#using a list of tuples for all possible winning combinations

winning_combinations = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
]

player = "O"
computer = "X"

for x in range(1,10,1):
    board[x] = " "

def displayBoard(board):
    for x in range(1,10,1):
        print(f"|{board[x]}|",end="")
        if x % 3 == 0:
            print("\n")

#checks win condition
 
def checkWin():
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != " ":
            return True
    return False


def checkMarkWin(mark):
    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == mark:
            return True
    return False



def checkDraw(board):
    for key in board.keys():
        if board[key] == " ":
            return False
    return True

def spaceFree(position):
    if board[position] == " ":
        return True
    return False
    
#checks if moves made are legal

def moveMade(letter,position):
    if spaceFree(position):
        board[position] = letter
        displayBoard(board)
        if checkWin():
            if letter == "X":
                print("The Computer Wins!!!")
                exit()
            print("You Win!!!")
            exit()
        if checkDraw(board):
            print("DRAW!!!")
            exit()
        return
    else:
        print("Invalid Position")
        position = int(input("\nPlease choose a new position"))
        moveMade(letter,position)
        return

#moves being made

def playerMove():
    move = int(input("Please make a move for: O "))
    moveMade(player,move)
    return

def compMove():
    bestScore = -100
    bestMove = 0
    for key in board.keys():
        if board[key] == " ":
            board[key] = computer 
            score = minimax(board,False)
            board[key] = " " 
            if score > bestScore:
                bestScore = score
                bestMove = key
    moveMade(computer,bestMove)
    return
    
def minimax(board,maximising):
    if checkMarkWin(computer):
        return 1 
    elif checkMarkWin(player):
        return -1
    elif checkDraw(board):
        return 0
    
    if maximising:
        bestScore = -100
        for key in board.keys():
            if board[key] == " ":
                board[key] = computer
                score = minimax(board,False)
                board[key] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 100
        for key in board.keys():
            if board[key] == " ":
                board[key] = player
                score = minimax(board,True)
                board[key] = " "
                if score < bestScore:
                    bestScore = score
        return bestScore


#main loop

while not checkWin():
    compMove()
    playerMove()
