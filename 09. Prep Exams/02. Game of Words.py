def go_up(r, c, mat, coin):
    if r == 0:
        coin = coin[:-1]
    else:
        mat[r][c] = "-"
        r -= 1
        if mat[r][c].isalpha():
            coin += mat[r][c]
        mat[r][c] = "P"
    return r, c, mat, coin


def go_down(r, c, mat, coin):
    if r == (len(mat)-1):
        coin = coin[:-1]
    else:
        mat[r][c] = "-"
        r += 1
        if mat[r][c].isalpha():
            coin += mat[r][c]
        mat[r][c] = "P"
    return r, c, mat, coin


def go_left(r, c, mat, coin):
    if c == 0:
        coin = coin[:-1]
    else:
        mat[r][c] = "-"
        c -= 1
        if mat[r][c].isalpha():
            coin += mat[r][c]
        mat[r][c] = "P"
    return r, c, mat, coin


def go_right(r, c, mat, coin):
    if c == (len(mat)-1):
        coin = coin[:-1]
    else:
        mat[r][c] = "-"
        c += 1
        if mat[r][c].isalpha():
            coin += mat[r][c]
        mat[r][c] = "P"
    return r, c, mat, coin


string_ = input()
n = int(input())
matrix = [[i for i in input()] for row in range(n)]

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col

commands = int(input())

for _ in range(commands):
    command = input()
    if command == "up":
        player_row, player_col, matrix, string_ = go_up(player_row, player_col, matrix, string_)
    elif command == "down":
        player_row, player_col, matrix, string_ = go_down(player_row, player_col, matrix, string_)
    elif command == "left":
        player_row, player_col, matrix, string_ = go_left(player_row, player_col, matrix, string_)
    elif command == "right":
        player_row, player_col, matrix, string_ = go_right(player_row, player_col, matrix, string_)

print(string_)
for r in matrix:
    print("".join(r))