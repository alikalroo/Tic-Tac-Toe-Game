def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")


def check_winner(board, player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
                board[position[1]] == player and
                board[position[2]] == player):
            return True

    return False


def is_draw(board):
    return " " not in board


def play_game():
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Choose positions from 1 to 9.\n")

    print(" 1 | 2 | 3")
    print("---|---|---")
    print(" 4 | 5 | 6")
    print("---|---|---")
    print(" 7 | 8 | 9")

    while True:
        print_board(board)

        try:
            choice = int(input(f"Player {current_player}, enter position (1-9): "))

            if choice < 1 or choice > 9:
                print("Please enter a number between 1 and 9.")
                continue

            index = choice - 1

            if board[index] != " ":
                print("This position is already taken.")
                continue

            board[index] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter a number.")


play_game()
