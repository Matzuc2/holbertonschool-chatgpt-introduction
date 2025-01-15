#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if (
            board[0][col] == board[1][col] == board[2][col]
            and board[0][col] != " "
        ):
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def check_draw(board):
    for row in board:
        if " " in row:  # If there is any empty space, it is not a draw yet
            return False
    return True


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    last_player = None  # Track the last player who made a valid move
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(
                    f"Enter column (0, 1, or 2) for player {player}: "
            ))
        except ValueError:
            print("Invalid input! Please enter integers between 0 and 2.")
            continue

        # Check if the entered row/column is valid
        if row not in range(3) or col not in range(3):
            print(
                "Invalid input! Please enter numbers between 0 and 2 "
                "for both row and column."
            )
            continue

        # Check if the cell is already occupied
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player
        last_player = player  # Track the last player who made the move

        # Check if there is a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {last_player} wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
