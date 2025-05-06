#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérifie lignes
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    # Vérifie colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Vérifie diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Entrée sécurisée
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Coordinates must be between 0 and 2. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Changer de joueur
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
