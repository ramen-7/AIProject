# Sudoku Solver
from types import NoneType
import sys

sys.setrecursionlimit(5000)


loop = 0

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


tester_board = [[1 for i in range(9)] for j in range(9)]


def boardconverter(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                board[i][j] = 0

            else:
                board[i][j] = int(board[i][j])


def print_rows(list):
    for i in list:
        print(i)


def copier(to_copy):

    return_copy = [[0 for i in range(9)] for j in range(9)]
    for i in range(0, 9):
        for j in range(0, 9):
            return_copy[i][j] = to_copy[i][j]
    return return_copy


def unit_finder(y, x):
    return 3 * (y // 3), 3 * (x // 3)


def next_zero(board):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                return [y, x]

    return False


def is_possible(board, y, x, to_fill):
    range_y, range_x = unit_finder(y, x)

    for i in range(9):
        if board[y][i] == to_fill:
            return 0

    for i in range(9):
        if board[i][x] == to_fill:
            return 0

    for i in range(range_y, range_y + 3):
        for j in range(range_x, range_x + 3):
            if board[i][j] == to_fill:
                return 0

    return 1


open = []
visited = []
visited_set = {}


def solver(board):
    loop = 1
    open.append(board)

    while open:

        print(loop)
        loop += 1

        this_board = open[0]
        open.pop(0)
        next_y, next_x = next_zero(this_board)
        for i in range(1, 10):
            if is_possible(this_board, next_y, next_x, i):
                # new_board = copier(this_board)
                # new_board[next_y][next_x] = i
                # if next_zero(new_board):
                #     return new_board
                # open.insert(0, new_board)

                this_board[next_y][next_x] = i
                if not next_zero(this_board):
                    return this_board
                open.insert(0, this_board)
                this_board[next_y][next_x] = 0


def recursive_solver(board):
    global loop
    print(loop)
    loop += 1

    if not next_zero(board):
        return board

    next_y, next_x = next_zero(board)

    for i in range(1, 10):
        if is_possible(board, next_y, next_x, i):

            # new_board = copier(board)
            board[next_y][next_x] = i

            if recursive_solver(board):
                return board

            board[next_y][next_x] = 0


# solution = recursive_solver(board)
# # solution = solver(board)

# print_rows(solution)


# def test(board, y, x):

#     range_y, range_x = unit_finder(y, x)

#     for i in range(range_y, range_y + 3):
#         for j in range(range_x, range_x + 3):
#             board[i][j] = 0


# test(tester_board, 7, 5)
# print_rows(tester_board)

boardconverter(board)


def isValidSudoku(board) -> bool:

    for i in range(9):
        for j in range(9):

            if board[i][j] != ".":
                if not is_possible(board, i, j, int(board[i][j])):
                    return False

    return True


print(isValidSudoku(board))
