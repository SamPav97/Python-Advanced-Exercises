def movement(command, r, c):
    if command == 'up':
        return r - 1, c
    if command == 'left':
        return r, c - 1
    if command == 'right':
        return r, c + 1
    if command == 'down':
        return r + 1, c


size = int(input())

commands = input().split()

start_row = 0
start_col = 0
coal = 0

matrix = []

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for column in range(size):
        element = row_elements[column]
        if element == "s":
            start_row = row
            start_col = column
        elif element == "c":
            coal += 1

for comm in commands:

    ro, co = movement(comm, start_row, start_col)
    if ro < 0 or ro >= size or co < 0 or co >= size:
        continue
    elif matrix[ro][co] == "c":
        matrix[ro][co] = "*"
        coal -= 1
        if coal == 0:
            print(f"You collected all coal! ({ro}, {co})")
            quit()

    elif matrix[ro][co] == "e":
        print(f"Game over! ({ro}, {co})")
        quit()

    start_row = ro
    start_col = co

print(f"{coal} pieces of coal left. ({start_row}, {start_col})")


# def get_next_pos(command, row, col):
#     if command == 'up':
#         return row - 1, col
#     if command == 'left':
#         return row, col - 1
#     if command == 'right':
#         return row, col + 1
#     if command == 'down':
#         return row + 1, col
#
#
# n = int(input())
# commands = input().split()
#
# matrix = []
#
# miner_row = 0
# miner_col = 0
# total_coal = 0
#
# for row in range(n):
#     row_elements = input().split()
#     matrix.append(row_elements)
#
#     for col in range(n):
#         element = row_elements[col]
#         if element == 's':
#             miner_row = row
#             miner_col = col
#         elif element == 'c':
#             total_coal += 1
#
# game_over = False
# for command in commands:
#     next_row, next_col = get_next_pos(command, miner_row, miner_col)
#
#     if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
#         continue
#
#     miner_row, miner_col = next_row, next_col
#     if matrix[miner_row][miner_col] == 'c':
#         matrix[miner_row][miner_col] = '*'
#         total_coal -= 1
#
#         if total_coal == 0:
#             break
#     elif matrix[miner_row][miner_col] == 'e':
#         game_over = True
#         break
#
# if total_coal == 0:
#     print(f'You collected all coal! ({miner_row}, {miner_col})')
# elif game_over:
#     print(f'Game over! ({miner_row}, {miner_col})')
# else:
#     print(f'{total_coal} pieces of coal left. ({miner_row}, {miner_col})')