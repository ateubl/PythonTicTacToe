# Started on 12/20/22
# Created by Andrew Teubl: andrewteubl@gmail.com

from random import randint

# Definitions
board = []
moves = []
win = 0
valid = 1

# Create Board
for i in range(3):
    row = []
    for j in range(3):
        row.append('-')
    board.append(row)

# Create Move Matrix
for i in range(3):
    row = []
    for j in range(3):
        row.append([i,j])
    moves.append(row)

# Display Board
print("", board[0], "\n", board[1], "\n", board[2])
print("See index for move location reference (no comma)")
print("", moves[0], "\n", moves[1], "\n", moves[2])

# Check to see if game is over (win or tie)
def check_win(board):
    for i in range(3):
            # Horizontal Check
            if board[i][0] == board[i][1] == board[i][2] == 'x':
                print("Game over, x wins")
                return 1

            if board[i][0] == board[i][1] == board[i][2] == 'o':
                print("Game over, o wins")
                return 1
        
            # Vertical Check
            if board[0][i] == board[1][i] == board[2][i] == 'x':
                print("Game over, x wins")
                return 1
    
            if board[0][i] == board[1][i] == board[2][i] == 'o':
                print("Game over, o wins")
                return 1

    # Diagonal Check
    if board[0][0] == board[1][1] == board[2][2] == 'o':
        print("Game over, o wins")
        return 1

    if board[0][0] == board[1][1] == board[2][2] == 'x':
        print("Game over, x wins")
        return 1
    
    if board[0][2] == board[1][1] == board[2][0] == 'o':
        print("Game over, o wins")
        return 1
    
    if board[0][2] == board[1][1] == board[2][0] == 'x':
        print("Game over, x wins")
        return 1

    # Tie Check
    x_count = board[0].count('x') + board[1].count('x') + board[2].count('x')
    if x_count == 5:
        print("Tie Game!")
        return 1

# Check if input is valid
def check_valid(move):
    
    # Check to see if the move space is already occupied
    if board[move[0]][move[1]] == 'x' or board[move[0]][move[1]] == 'o':
        print("Invalid Move: Space must be empty")
        return 0
    # Check to see if the input is within range
    if move[0] > 2 or move [1] > 2 or move[0] < 0 or move[1] < 0:
        print("Invalid Input: Entry must be from 0 to 2")
        return 0
    else:
        return 1  

# Player input
while win != 1:
    # Player X move
    move = [int(x) for x in input("Player x: Enter move location:").split()]
    valid = check_valid(move)

    if valid == 1:
        board[move[0]][move[1]] = 'x'
        print("", board[0], "\n", board[1], "\n", board[2])
        print("", moves[0], "\n", moves[1], "\n", moves[2])
        win = check_win(board)


    # Player O move (Computer Opponent)
    if win != 1 and valid == 1:
        valid = 0
        while valid == 0:
            move = [randint(0,2), randint(0,2)]
            valid = check_valid(move)
            
            if valid == 1:
                board[move[0]][move[1]] = 'o'
                print("", board[0], "\n", board[1], "\n", board[2])
                print("", moves[0], "\n", moves[1], "\n", moves[2])
                win = check_win(board)

