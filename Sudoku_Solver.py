import numpy as np


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i, j], end=" ")
        print()

def is_valid(ans, row, column, num):
    m = row//3
    n = column//3
    brl, brh = m * 3, (m+1) * 3
    bcl, bch = n*3, (n+1) * 3
    if not(np.any(ans[row, :] == num)) and not(np.any(ans[:, column] == num)) and not(np.any(ans[brl:brh, bcl:bch] == num)):
        return True
    else:
        return False


def find_empty(board):
    indices = np.argwhere(board == 0)
    if indices.size > 0:
        return indices[0]
    else:
        return False
    

def sudoku_solver(board):
    result = find_empty(board)
    if result is False:
        print_board(board)
        return True
    row, column = result
    for num in range(1, 10):
        if is_valid(board, row, column, num):
            board[row, column] = num
            outcome = sudoku_solver(board)
            if outcome:
                return True
            else:
                board[row, column] = 0
    return False


def input_board():
    print("Enter each row as 9 numbers separated by spaces (0 for empty):")
    board = []
    for i in range(9):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        board.append(row)
    return np.array(board)


if __name__ == "__main__":
    board = input_board()
    print("\nUnsolved:")
    print_board(board)
    print("\nSolving...")
    sudoku_solver(board)