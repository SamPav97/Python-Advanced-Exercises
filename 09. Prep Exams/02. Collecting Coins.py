import math


def check_player(mat):
    for row in range(len(mat)):
        for col in range(len(mat)):
            if mat[row][col] == "P":
                return [row, col]


def go_up(r, c, mat, coin):
    if mat[r-1][c] == "X":
        return False
    else:
        mat[r][c] = 0
        r -= 1
        coin += int(mat[r][c])
        mat[r][c] = "P"
    return r, c, mat, coin


def go_down(r, c, mat, coin):
    if r == (len(mat)-1):
        r = -1
    if mat[r+1][c] == "X":
        return False
    else:
        mat[r][c] = 0
        r += 1
        coin += int(mat[r][c])
        mat[r][c] = "P"
    return r, c, mat, coin


def go_left(r, c, mat, coin):
    if mat[r][c-1] == "X":
        return False
    else:
        mat[r][c] = 0
        c -= 1
        coin += int(mat[r][c])
        mat[r][c] = "P"
    return r, c, mat, coin


def go_right(r, c, mat, coin):
    if c == (len(mat)-1):
        c = -1
    if mat[r][c+1] == "X":
        return False
    else:
        mat[r][c] = 0
        c += 1
        coin += int(mat[r][c])
        mat[r][c] = "P"
    return r, c, mat, coin


n = int(input())

matrix = [[i for i in input().split()]for row in range(n)]
player_row, player_col = check_player(matrix)


positions = [[player_row, player_col]]
coins = 0
while True:
    command = input()

    if command == "up":
        try:
            player_row, player_col, matrix, coins = go_up(player_row, player_col, matrix, coins)
            positions.append(check_player(matrix))
        except TypeError:
            if player_row == 0:
                positions.append([(n-1), player_col])
            else:
                positions.append([player_row-1, player_col])
            positions.append([player_row-1, player_col])
            print(f"Game over! You've collected {math.floor(coins/2)} coins.")
            print("Your path:")
            for path in positions:
                print(path)
            quit()

    elif command == "down":
        try:
            player_row, player_col, matrix, coins = go_down(player_row, player_col, matrix, coins)
            positions.append(check_player(matrix))
        except TypeError:
            if player_row == (n-1):
                positions.append([0, player_col])
            else:
                positions.append([player_row+1, player_col])
                print(f"Game over! You've collected {math.floor(coins / 2)} coins.")
                print("Your path:")
                for path in positions:
                    print(path)
                quit()

    elif command == "left":
        try:
            player_row, player_col, matrix, coins = go_left(player_row, player_col, matrix, coins)
            positions.append(check_player(matrix))
        except TypeError:
            if player_col == 0:
                positions.append([player_row, (n-1)])
            else:
                positions.append([player_row, player_col-1])
            print(f"Game over! You've collected {math.floor(coins / 2)} coins.")
            print("Your path:")
            for path in positions:
                print(path)
            quit()

    elif command == "right":
        try:
            player_row, player_col, matrix, coins = go_right(player_row, player_col, matrix, coins)
            positions.append(check_player(matrix))
        except TypeError:
            if player_col == (n - 1):
                positions.append([player_row, 0])
            else:
                positions.append([player_row, player_col+1])
            print(f"Game over! You've collected {math.floor(coins / 2)} coins.")
            print("Your path:")
            for path in positions:
                print(path)
            quit()

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        print("Your path:")
        for path in positions:
            print(path)
        quit()
