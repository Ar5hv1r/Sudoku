import pprint

pp = pprint.PrettyPrinter()
board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

# outputs the row and column of each blank square
def find_blank(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                # print(f"Blank at row: {row} and column: {col}")
                return row, col


# outputs current state of the board
def print_board(board):
    pp.pprint(board)


def solve_puzzle(board):
    blank = find_blank(board)
    if not blank:
        return True
    else:
        row, col = blank

    for i in range(1, 10):
        if check_valid(board, i, (row, col)):
            board[row][col] = i

            if solve_puzzle(board):
                return True

            board[row][col] = 0

    return False


def check_valid(board, num, pos):
    # check if number can fit in column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check if number can fit in row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check if number can fit in box
    xBox = pos[1] // 3
    yBox = pos[0] // 3

    for i in range(yBox * 3, yBox * 3 + 3):
        for j in range(xBox * 3, xBox * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


print_board(board)

solve_puzzle(board)

print_board(board)
