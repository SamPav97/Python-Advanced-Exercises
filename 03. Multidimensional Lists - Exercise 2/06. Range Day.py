def make_steps(direct, step, r, c, mat):
    if direct == "down" and (r + step) < len(mat) and mat[r+step][c] == ".":
        mat[r][c] = "."
        mat[r+step][c] = "A"
    elif direct == "up" and (r - step) >= 0 and mat[r-step][c] == ".":
        mat[r][c] = "."
        mat[r-step][c] = "A"
    elif direct == "right" and (c + step) < len(mat) and mat[r][c+step] == ".":
        mat[r][c] = "."
        mat[r][c + step] = "A"
    elif direct == "left" and (c - step) >= 0 and mat[r][c-step] == ".":
        mat[r][c] = "."
        mat[r][c-step] = "A"
    return mat


def shoot(dire, r, c, mat):
    length = len(mat)
    hit = []
    #might be the issue that if they shoot down its out of range coz they are at lowest
    if dire == "down" and 0 <= r < length and 0 <= c < length:
        for target in range(r+1, length):
            if mat[target][c] == ".":
                pass
            else:
                mat[target][c] = "."
                hit.append([target, c])
                break
    elif dire == "up" and 0 <= r < length and 0 <= c < length:
        for target in range(r-1, -1, -1):
            if mat[target][c] == ".":
                pass
            else:
                mat[target][c] = "."
                hit.append([target, c])
                break
    elif dire == "right" and 0 <= r < length and 0 <= c < length:
        for target in range(c+1, length):
            if mat[r][target] == ".":
                pass
            else:
                mat[r][target] = "."
                hit.append([r, target])
                break
    elif dire == "left" and 0 <= r < length and 0 <= c < length:
        for target in range(c-1, -1, -1):
            if mat[r][target] == ".":
                pass
            else:
                mat[r][target] = "."
                hit.append([r, target])
                break
    return hit, mat



n = 5
matrix = []
targets = 0
for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            shooter_row = row
            shooter_cow = col
        elif matrix[row][col] == "x":
            targets += 1

coms = int(input())
shot = []
shot_1 = []
for com in range(coms):
    command = input().split()
    if command[0] == "shoot":
        direction = command[1]
        shot_1, matrix = shoot(direction,shooter_row, shooter_cow, matrix)
        shot += shot_1
    elif command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        matrix = make_steps(direction, steps, shooter_row, shooter_cow, matrix)
        for row in range(n):
            for col in range(n):
                if matrix[row][col] == "A":
                    shooter_row = row
                    shooter_cow = col

targets_fin = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == "x":
            targets_fin += 1

if not targets_fin:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets_fin} targets left.")
for one in shot:
    if one:
        print(one)
#
# for line in matrix:
#     print(line)