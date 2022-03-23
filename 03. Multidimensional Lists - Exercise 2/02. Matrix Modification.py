n = int(input())

matrix = [[int(s) for s in input().split()]for row in range(n)]

while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    action = command[0]
    c_row = int(command[1])
    c_col = int(command[2])
    strength = int(command[3])

    if 0 <= c_row < n and 0 <= c_col < n:
        if action == "Add":
            matrix[c_row][c_col] += strength
        else:
            matrix[c_row][c_col] -= strength
    else:
        print("Invalid coordinates")

for line in matrix:
    print(*line)