def is_inside(r, c, mat):
    return 0 <= r < len(mat) and 0 <= c < len(mat)


def is_knight(r, c, mat):
    return mat[r][c] == "K"


def get_attack_counter(r, c, mat):
    result = 0
    if is_inside(r-2, c-1, mat) and is_knight(r-2, c-1, mat):
        result += 1
    if is_inside(r-2, c+1, mat) and is_knight(r-2, c+1, mat):
        result += 1
    if is_inside(r-1, c-2, mat) and is_knight(r-1, c-2, mat):
        result += 1
    if is_inside(r-1, c+2, mat) and is_knight(r-1, c+2, mat):
        result += 1
    if is_inside(r+2, c-1, mat) and is_knight(r+2, c-1, mat):
        result += 1
    if is_inside(r+2, c+1, mat) and is_knight(r+2, c+1, mat):
        result += 1
    if is_inside(r+1, c-2, mat) and is_knight(r+1, c-2, mat):
        result += 1
    if is_inside(r+1, c+2, mat) and is_knight(r+1, c+2, mat):
        result += 1
    return result


n = int(input())

matrix = [[i for i in input()]for row in range(n)]

removed_knights = 0

while True:
    table = {}

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "0":
                continue
            counter = get_attack_counter(row, col, matrix)
            if counter:
                table[(row, col)] = counter
    if not table:
        break
    best_counter = 0
    for loc, count in table.items():
        if count > best_counter:
            spec_row = loc[0]
            spec_col = loc[1]
            best_counter = count
    matrix[spec_row][spec_col] = "0"
    removed_knights += 1

print(removed_knights)
