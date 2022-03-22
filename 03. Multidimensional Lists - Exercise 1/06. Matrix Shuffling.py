def outside(old1, old2, rowers, colers):
    return old1 < 0 or old2 < 0 or old1 > rowers or old2 > colers


rows, cols = [int(s) for s in input().split()]

matrix = [[i for i in input().split()]for row in range(rows)]

while True:
    command = input()
    if command == "END":
        break
    command = command.split()

    if len(command) != 5 or command[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(i) for i in command[1:]]

    if outside(row1, col1, rows, cols) or outside(row2, col2, rows, cols):
        print("Invalid input!")
        continue
    else:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for line in matrix:
            print(*line)


