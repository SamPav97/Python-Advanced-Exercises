def check_up(r, c, mat):
    if r == 0:
        return mat
    else:
        if mat[r-1][c] != "*":
            mat[r-1][c] += 1
        return mat


def check_down(r, c, mat):
    if r == (len(mat)-1):
        return mat
    else:
        if mat[r+1][c] != "*":
            mat[r+1][c] += 1
        return mat


def check_left(r, c, mat):
    if c == 0:
        return mat
    else:
        if mat[r][c-1] != "*":
            mat[r][c-1] += 1
        return mat


def check_right(r, c, mat):
    if c == (len(mat)-1):
        return mat
    else:
        if mat[r][c+1] != "*":
            mat[r][c+1] += 1
        return mat


def check_right_up(r, c, mat):
    if r == 0 or c == (len(mat)-1):
        return mat
    else:
        if mat[r-1][c+1] != "*":
            mat[r-1][c+1] += 1
        return mat


def check_left_up(r, c, mat):
    if r == 0 or c == 0:
        return mat
    else:
        if mat[r-1][c-1] != "*":
            mat[r-1][c-1] += 1
        return mat


def check_right_down(r, c, mat):
    if r == (len(mat)-1) or c == (len(mat)-1):
        return mat
    else:
        if mat[r+1][c+1] != "*":
            mat[r+1][c+1] += 1
        return mat


def check_left_down(r, c, mat):
    if r == (len(mat)-1) or c == 0:
        return mat
    else:
        if mat[r+1][c-1] != "*":
            mat[r+1][c-1] += 1
        return mat


n = int(input())
bombs = int(input())
matrix = [[int(0) for i in range(n)]for row in range(n)]

for _ in range(bombs):
    bomb = input().replace("(", "").replace(")", "").split(", ")
    bomb_row = int(bomb[0])
    bomb_col = int(bomb[1])
    matrix[bomb_row][bomb_col] = "*"
    matrix = check_up(bomb_row, bomb_col, matrix)
    matrix = check_down(bomb_row, bomb_col, matrix)
    matrix = check_left(bomb_row, bomb_col, matrix)
    matrix = check_right(bomb_row, bomb_col, matrix)
    matrix = check_right_up(bomb_row, bomb_col, matrix)
    matrix = check_left_up(bomb_row, bomb_col, matrix)
    matrix = check_right_down(bomb_row, bomb_col, matrix)
    matrix = check_left_down(bomb_row, bomb_col, matrix)

for row in matrix:
    print(*row)




