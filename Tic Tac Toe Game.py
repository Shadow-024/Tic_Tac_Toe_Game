def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt, lower, upper):
    while True:
        try:
            value = int(input(prompt))
            if value not in range(lower, upper):
                print("Invalid input! Please enter a valid number (0, 1, or 2).")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number (0, 1, or 2).")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = get_valid_input("Enter row (0, 1, or 2): ", 0, 3)
        col = get_valid_input("Enter column (0, 1, or 2): ", 0, 3)

        if board[row][col] == " ":
            board[row][col] = players[current_player]

            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = 1 - current_player
        else:
            print("Cell is already taken. Try again!")

tic_tac_toe()