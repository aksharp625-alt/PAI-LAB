import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_full(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, isMax):
    if check_win(board, 'O'):
        return 10 - depth
    if check_win(board, 'X'):
        return depth - 10
    if check_full(board):
        return 0
    
    if isMax:
        maxEval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    minEval = min(minEval, eval)
        return minEval

def best_move(board):
    bestVal = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                moveVal = minimax(board, 0, False)
                board[i][j] = ' '
                if moveVal > bestVal:
                    bestVal = moveVal
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        row, col = map(int, input("Player X, enter row and column (0-2): ").split())
        if board[row][col] != ' ':
            print("This spot is taken try again")
            continue
        board[row][col] = 'X'
        
        if check_win(board, 'X'):
            print_board(board)
            print("Player X wins")
            break
        if check_full(board):
            print_board(board)
            print("It's a draw")
            break
        
        print("Player O is making its move")
        row, col = best_move(board)
        board[row][col] = 'O'
        
        if check_win(board, 'O'):
            print_board(board)
            print("Player O wins")
            break
        if check_full(board):
            print_board(board)
            print("It's a draw")
            break

play_game()
