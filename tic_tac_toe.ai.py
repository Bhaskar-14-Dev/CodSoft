import math

def print_board(board):
    print('\n')
    for row in range(3):
        print(' | '.join(board[row]))
        if row < 2:
            print('--+---+--')
    print('\n')

def check_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_empty_cells(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            move = (i, j)
    if move:
        board[move[0]][move[1]] = 'O'

def human_move(board):
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid position. Choose from 1 to 9.")
                continue
            i, j = divmod(pos, 3)
            if board[i][j] != ' ':
                print("Cell already taken. Choose another one.")
                continue
            board[i][j] = 'X'
            break
        except ValueError:
            print("Please enter a valid number (1-9).")

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. The AI is 'O'.\n")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Board positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9\n")
    print("Let's start!\n")
    print_board(board)
    while True:
        human_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        print("AI's turn...")
        ai_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()