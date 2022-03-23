def cookie(dir_, good_k, pres, santa_r, santa_c, mat):
    mat[santa_r][santa_c] = "-"
    if dir_ == "up":
        santa_r -= 1
    if dir_ == "down":
        santa_r += 1
    if dir_ == "left":
        santa_c -= 1
    if dir_ == "right":
        santa_c += 1
    mat[santa_r][santa_c] = "S"
    if mat[santa_r + 1][santa_c] == "V" or mat[santa_r + 1][santa_c] == "X":
        if mat[santa_r + 1][santa_c] == "V":
            good_k -= 1
        mat[santa_r + 1][santa_c] = "-"
        pres -= 1
    if mat[santa_r - 1][santa_c] == "V" or mat[santa_r - 1][santa_c] == "X":
        if mat[santa_r - 1][santa_c] == "V":
            good_k -= 1
        mat[santa_r - 1][santa_c] = "-"
        pres -= 1
    if mat[santa_r][santa_c + 1] == "V" or mat[santa_r][santa_c + 1] == "X":
        if mat[santa_r][santa_c + 1] == "V":
            good_k -= 1
        mat[santa_r][santa_c + 1] = "-"
        pres -= 1
    if mat[santa_r][santa_c - 1] == "V" or mat[santa_r][santa_c - 1] == "X":
        if mat[santa_r][santa_c - 1] == "V":
            good_k -= 1
        mat[santa_r][santa_c - 1] = "-"
        pres -= 1
    return good_k, pres, santa_r, santa_c, mat


presents = int(input())
n = int(input())
matrix = []
good_kids = 0
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa_row = row
            santa_col = col
        elif matrix[row][col] == "V":
            good_kids += 1

constant_good = good_kids
while True:
    command = input()
    if command == "Christmas morning":
        break
    if command == "up":
        if matrix[santa_row-1][santa_col] == "V":
            presents -= 1
            good_kids -= 1
            matrix[santa_row][santa_col] = "-"
            matrix[santa_row - 1][santa_col] = "S"
            santa_row -= 1
            good_kids -= 1
        elif matrix[santa_row-1][santa_col] == "C":
            good_kids, presents, santa_row, santa_col, matrix = cookie(command, good_kids, presents, santa_row, santa_col, matrix)
        else:
            matrix[santa_row][santa_col] = "-"
            matrix[santa_row - 1][santa_col] = "S"
            santa_row -= 1
    elif command == "down":
        if matrix[santa_row + 1][santa_col] == "V":
            presents -= 1
            good_kids -= 1
            matrix[santa_row][santa_col] = "-"
            matrix[santa_row + 1][santa_col] = "S"
            santa_row += 1
        elif matrix[santa_row + 1][santa_col] == "C":
            good_kids, presents, santa_row, santa_col, matrix = cookie(command, good_kids, presents, santa_row, santa_col, matrix)
        else:
            matrix[santa_row][santa_col] = "-"
            matrix[santa_row + 1][santa_col] = "S"
            santa_row += 1
    elif command == "right":
        if matrix[santa_row][santa_col + 1] == "V":
            presents -= 1
            good_kids -= 1
            matrix[santa_row][santa_col] = "-"
            matrix[santa_row][santa_col + 1] = "S"
            santa_col += 1
        elif matrix[santa_row][santa_col + 1] == "C":
            good_kids, presents, santa_row, santa_col, matrix = cookie(command, good_kids, presents, santa_row, santa_col, matrix)
        else:
            matrix[santa_row][santa_col] = "-"
            matrix[santa_row][santa_col + 1] = "S"
            santa_col += 1
    elif command == "left":
        if matrix[santa_row][santa_col - 1] == "V":
            presents -= 1
            good_kids -= 1
            matrix[santa_row][santa_col] = "-"
            matrix[santa_row][santa_col - 1] = "S"
            santa_col -= 1
        elif matrix[santa_row][santa_col - 1] == "C":
            good_kids, presents, santa_row, santa_col, matrix = cookie(command, good_kids, presents, santa_row, santa_col, matrix)
        else:
            matrix[santa_row][santa_col] = "-"
            matrix[santa_row][santa_col - 1] = "S"
            santa_col -= 1
    if presents == 0 and good_kids > 0:
        print("Santa ran out of presents!")
        break
    elif good_kids == 0:
        break
for line in matrix:
    print(*line)

if good_kids > 0:
    print(f"No presents for {good_kids} nice kid/s.")
if good_kids == 0:
    print(f"Good job, Santa! {constant_good} happy nice kid/s.")