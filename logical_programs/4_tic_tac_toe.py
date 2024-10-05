'''
4 Tic-Tac-Toe Game
    a. Desc -> Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1
    is the Computer and the Player 2 is the user. Player 1 take Random Cell that is
    the Column and Row.
    b. I/P -> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’
    c. Logic -> The User or the Computer can only take the unoccupied cell. The Game
    is played till either wins or till draw...
    d. O/P -> Print the Col and the Cell after every step.
    e. Hint -> The Hints is provided in the Logic. Use Functions for the Logic
'''
import random
# Prints the Tic-Tac-Toe board.
def print_board(board):
    for row in board:
        # The join() method takes all items in an iterable and joins them into one string.
        print(" | ".join(row))
        print("-" * 9)

# Checks if the specified player has won.
def check_winner(board, player):
    # Check rows, columns, and diagonals
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

# Checks if the game is a draw (i.e., the board is full and there’s no winner).
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Handles the user's move by taking input and updating the board.
def user_move(board):
    while True:
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell is already occupied. Choose another.")
        except (IndexError, ValueError):
            print("Invalid input. Enter row and column as integers between 0 and 2.")

# Handles the computer’s move by choosing a random unoccupied cell.
def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            break

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    # [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        user_move(board)
        print("User Move:")
        print_board(board)
        
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break
        
        computer_move(board)
        print("Computer Move:")
        print_board(board)
        
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Start the game
tic_tac_toe()