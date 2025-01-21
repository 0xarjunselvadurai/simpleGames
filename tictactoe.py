def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
            
# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Main game function
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn")
        
        # Get valid move input
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if row not in range(3) or col not in range(3):
                    print("Row and column must be between 0 and 2.")
                    continue
                if board[row][col] != " ":
                    print("This cell is already taken. Choose another one.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter two integers between 0 and 2.")
        
        # Place the current player's mark on the board
        board[row][col] = current_player
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (draw)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the other player
        turn += 1

# Start the game
if __name__ == "__main__":
    play_game()

