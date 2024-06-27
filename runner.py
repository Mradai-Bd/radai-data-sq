# Tic-Tac-Toe with Minimax AI
import tictactoe as ttt

def print_board(board):
    for row in board:
        print(row)

def main():
    board = ttt.initial_state()

    while not ttt.terminal(board):
        print_board(board)
        if ttt.player(board) == ttt.X:
            print("Player X's turn")
            i, j = map(int, input("Enter row and column (0, 1, or 2): ").split())
            board = ttt.result(board, (i, j))
        else:
            print("Player O's turn (AI)")
            move = ttt.minimax(board)
            board = ttt.result(board, move)

    print_board(board)
    winner = ttt.winner(board)
    if winner:
        print(f"Winner: {winner}")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
