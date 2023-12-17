import random

# set global variables
board = ["_", "_", "_", 
         "_", "_", "_",
         "_", "_", "_"]

currentPlayer = "X"
winner = None
gameRun = True

# print game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("___________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("___________")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("___________")

# take player input
def playerInput(board):
    inpt = int(input("Enter a number 1-9: "))
    if inpt >= 1 and inpt <= 9 and board[inpt-1] == "_":
        board[inpt - 1] = currentPlayer
    else:
        print("Oops, spot is already occupied")

# check for win or tie
def checkRow(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

def checkCol(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True 

def checkDiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

# check for tie
def checkTie(board):
    global gameRun
    if "_" not in board:
        printBoard(board)
        print("This game is a tie")
        gameRun = False

# check for win
def checkWin():
    if checkCol(board) or checkRow(board) or checkDiag(board):
        print(f"The winner is {winner}")
        global gameRun
        gameRun = False

# switch players
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# computer player
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switchPlayer()

# check for win or tie again
while gameRun:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)