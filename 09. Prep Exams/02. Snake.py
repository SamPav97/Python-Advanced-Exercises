def check_snake(mat):
    for r in range(len(mat)):
        for c in range(len(mat)):
            if mat[r][c] == "S":
                return True


def go_up(r, c, yum, teleport, mat):
    if r == 0:
        mat[r][c] = "."
        return mat, yum, r, c
    mat[r][c] = "."
    r -= 1
    if mat[r][c] == "*":
        yum += 1
        mat[r][c] = "S"
    elif mat[r][c] == "-":
        mat[r][c] = "S"
    elif mat[r][c] == "B":
        teleport.remove([r, c])
        mat[r][c] = "."
        r, c = teleport[0]
        mat[r][c] = "S"
    return mat, yum, r, c


def go_down(r, c, yum, teleport, mat):
    if r == (len(mat)-1):
        mat[r][c] = "."
        return mat, yum, r, c
    mat[r][c] = "."
    r += 1
    if mat[r][c] == "*":
        yum += 1
        mat[r][c] = "S"
    elif mat[r][c] == "-":
        mat[r][c] = "S"
    elif mat[r][c] == "B":
        teleport.remove([r, c])
        mat[r][c] = "."
        r, c = teleport[0]
        mat[r][c] = "S"
    return mat, yum, r, c


def go_left(r, c, yum, teleport, mat):
    if c == 0:
        mat[r][c] = "."
        return mat, yum, r, c
    mat[r][c] = "."
    c -= 1
    if mat[r][c] == "*":
        yum += 1
        mat[r][c] = "S"
    elif mat[r][c] == "-":
        mat[r][c] = "S"
    elif mat[r][c] == "B":
        teleport.remove([r, c])
        mat[r][c] = "."
        r, c = teleport[0]
        mat[r][c] = "S"
    return mat, yum, r, c


def go_right(r, c, yum, teleport, mat):
    if c == (len(mat)-1):
        mat[r][c] = "."
        return mat, yum, r, c
    mat[r][c] = "."
    c += 1
    if mat[r][c] == "*":
        yum += 1
        mat[r][c] = "S"
    elif mat[r][c] == "-":
        mat[r][c] = "S"
    elif mat[r][c] == "B":
        teleport.remove([r, c])
        mat[r][c] = "."
        r, c = teleport[0]
        mat[r][c] = "S"
    return mat, yum, r, c


n = int(input())
matrix = [[i for i in input()] for row in range(n)]
portals = []
food = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "S":
            sneak_row = row
            sneak_col = col
        if matrix[row][col] == "B":
            portals.append([row, col])

while True:
    command = input()

    if command == "up":
        matrix, food, sneak_row, sneak_col = go_up(sneak_row, sneak_col, food, portals, matrix)
        if not check_snake(matrix):
            print("Game over!")
            break

    elif command == "down":
        matrix, food, sneak_row, sneak_col = go_down(sneak_row, sneak_col, food, portals, matrix)
        if not check_snake(matrix):
            print("Game over!")
            break

    elif command == "left":
        matrix, food, sneak_row, sneak_col = go_left(sneak_row, sneak_col, food, portals, matrix)
        if not check_snake(matrix):
            print("Game over!")
            break

    elif command == "right":
        matrix, food, sneak_row, sneak_col = go_right(sneak_row, sneak_col, food, portals, matrix)
        if not check_snake(matrix):
            print("Game over!")
            break
    if food >= 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food}")
for m in matrix:
    print("".join(m))
