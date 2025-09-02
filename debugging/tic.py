#!/usr/bin/python3

def print_board(board):
    """
    Display the current state of the tic-tac-toe board.
    
    Function Description:
    Prints the 3x3 board in a readable format with separators between cells and rows.
    
    Parameters:
    board (list): A 3x3 list representing the game board
    
    Returns:
    None: Prints the board to console
    """
    print("\nCurrent Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # Don't print separator after last row
            print("-" * 9)

def check_winner(board):
    """
    Check if there's a winner on the board.
    
    Function Description:
    Examines all possible winning combinations (rows, columns, diagonals)
    to determine if any player has achieved three in a row.
    
    Parameters:
    board (list): A 3x3 list representing the current game board
    
    Returns:
    str or None: Returns the winning player ('X' or 'O') if there's a winner,
                 None if no winner is found
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """
    Check if the board is completely filled (tie game).
    
    Function Description:
    Examines all positions on the board to determine if there are any
    empty spaces remaining.
    
    Parameters:
    board (list): A 3x3 list representing the current game board
    
    Returns:
    bool: True if board is full, False if there are empty spaces
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt, valid_range):
    """
    Get valid numeric input from user with error handling.
    
    Function Description:
    Continuously prompts user for input until a valid number within
    the specified range is entered. Handles non-numeric input gracefully.
    
    Parameters:
    prompt (str): Message to display when asking for input
    valid_range (list): List of valid integer values
    
    Returns:
    int: Valid integer input from user
    """
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Invalid input. Please enter {', '.join(map(str, valid_range))}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """
    Main game loop for tic-tac-toe.
    
    Function Description:
    Manages the complete tic-tac-toe game including board initialization,
    player turns, input validation, win checking, and game end conditions.
    Handles both win and tie scenarios.
    
    Parameters:
    None
    
    Returns:
    None: Runs complete game until win or tie
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Players will alternate turns. Enter row and column numbers (0, 1, or 2)")
    
    while True:
        print_board(board)
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
            
        # Check for tie
        if is_board_full(board):
            print("It's a tie! The board is full.")
            break
        
        print(f"\nPlayer {player}'s turn:")
        
        # Get valid input with error handling
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ", [0, 1, 2])
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ", [0, 1, 2])
        
        # Check if spot is available
        if board[row][col] == " ":
            board[row][col] = player
            # Switch players
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
