def check_movement(r, c, mat):
    if r < 0 or c < 0 or r >= n or c >= n:
        return False

    location = mat[r][c]

    if location == "R":
        return "R"
    elif location.isdigit():
        return "digit"
    elif location == "." or location == "*":
        return "."



def move_up(r, c):
    return r-1, c


def move_down(r, c):
    return r+1, c


def move_left(r, c):
    return r, c-1


def move_right(r, c):
    return r, c+1


n = int(input())
matrix = []
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            alice_row = row
            alice_col = col

teas = 0
while True:
    command = input()
    if command == "up":
        matrix[alice_row][alice_col] = "*"
        alice_row, alice_col = move_up(alice_row, alice_col)
    elif command == "down":
        matrix[alice_row][alice_col] = "*"
        alice_row, alice_col = move_down(alice_row, alice_col)
    elif command == "left":
        matrix[alice_row][alice_col] = "*"
        alice_row, alice_col = move_left(alice_row, alice_col)
    elif command == "right":
        matrix[alice_row][alice_col] = "*"
        alice_row, alice_col = move_right(alice_row, alice_col)
    if check_movement(alice_row, alice_col, matrix) == "digit":
        teas += int(matrix[alice_row][alice_col])
        if teas >= 10:
            matrix[alice_row][alice_col] = "*"
            break
    elif check_movement(alice_row, alice_col, matrix) == ".":
        matrix[alice_row][alice_col] = "*"
    elif check_movement(alice_row, alice_col, matrix) == "R":
        print("Alice didn't make it to the tea party.")
        matrix[alice_row][alice_col] = "*"
        for line in matrix:
            print(*line)
        quit()
    elif not check_movement(alice_row, alice_col, matrix):
        print("Alice didn't make it to the tea party.")
        for line in matrix:
            print(*line)
        quit()
print("She did it! She went to the party.")
for line in matrix:
    print(*line)