def go_up(r, c, mat):
    if c != 0:
        if mat[r-1][c-1] == "b":
            r -= 1
            c -= 1
            return r, c, mat
    if c != (len(mat)-1):
        if mat[r-1][c+1] == "b":
            r -= 1
            c += 1
            return r, c, mat
    r -= 1
    mat[r][c] = "w"
    return r, c, mat


def go_down(r, c, mat):
    if c != 0:
        if mat[r+1][c-1] == "w":
            r += 1
            c -= 1
            return r, c, mat
    if c != (len(mat)-1):
        if mat[r+1][c+1] == "w":
            r += 1
            c += 1
            return r, c, mat
    r += 1
    mat[r][c] = "b"
    return r, c, mat


board_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}
board_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}



n = 8
matrix = [[i for i in input().split()] for row in range(n)]
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "w":
            white_row = row
            white_col = col
        elif matrix[row][col] == "b":
            black_row = row
            black_col = col

while True:
    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {''.join([board_col[white_col], board_row[white_row]])}.")
        break
    if black_row == (len(matrix)-1):
        print(f"Game over! Black pawn is promoted to a queen at {''.join([board_col[black_col], board_row[black_row]])}.")
        break
    white_row, white_col, matrix = go_up(white_row, white_col, matrix)
    if white_row == black_row and white_col == black_col:
        print(f"Game over! White win, capture on {''.join([board_col[white_col], board_row[white_row]])}.")
        break
    black_row, black_col, matrix = go_down(black_row, black_col, matrix)
    if white_row == black_row and white_col == black_col:
        print(f"Game over! Black win, capture on {''.join([board_col[black_col], board_row[black_row]])}.")
        break
