# Tic-Tac-Toe with Minimax AI
import math
import random

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X

def actions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY]

def result(board, action):
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action")
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None

def terminal(board):
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        value, move = max_value(board)
    else:
        value, move = min_value(board)
    return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    value = -math.inf
    best_action = None
    for action in actions(board):
        action_value, _ = min_value(result(board, action))
        if action_value > value:
            value = action_value
            best_action = action
    return value, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None
    value = math.inf
    best_action = None
    for action in actions(board):
        action_value, _ = max_value(result(board, action))
        if action_value < value:
            value = action_value
            best_action = action
    return value, best_action
