
wins = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


def show_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def show_positions():
    print()
    print("POSITION GUIDE")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()


def check_winner(board):
    for line in wins:
        a = line[0]
        b = line[1]
        c = line[2]

        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    return None


def minimax(board, computer_turn):
    result = check_winner(board)

    if result == "O":
        return 1

    if result == "X":
        return -1

    if " " not in board:
        return 0

    scores = []

    for i in range(9):
        if board[i] == " ":
            if computer_turn:
                board[i] = "O"
            else:
                board[i] = "X"

            score = minimax(board, not computer_turn)
            scores.append(score)

            board[i] = " "

    if computer_turn:
        return max(scores)
    else:
        return min(scores)


def computer_move(board):
    best_score = -2
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"


def human_move(board):
    while True:
        move = input("Enter position (1-9): ")

        if not move.isdigit():
            print("Please enter a number.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Choose a position from 1 to 9.")
            continue

        if board[move - 1] != " ":
            print("Position already occupied.")
            continue

        board[move - 1] = "X"
        break


def main():
    board = [" "] * 9
    turn = "human"

    print("=" * 25)
    print("   TIC TAC TOE GAME")
    print("=" * 25)
    print("Your Symbol     : X")
    print("Computer Symbol : O")
    print("First Turn      : You")
    print("=" * 25)

    show_positions()

    input("Press Any key to start the game...")

    while True:
        show_board(board)

        if turn == "human":
            human_move(board)
        else:
            print("Computer is thinking...")
            computer_move(board)

        result = check_winner(board)

        if result is not None:
            show_board(board)

            if result == "X":
                print("Congratulations! You win!")
            else:
                print("Computer wins!")

            break

        if " " not in board:
            show_board(board)
            print("Game draw!")
            break

        if turn == "human":
            turn = "computer"
        else:
            turn = "human"


main()
