rows, columns = [int(s) for s in input().split()]

matrix = [[int(s) for s in input().split()]for row in range(rows)]

total = []
biggest = -9999999999999
for row in range(0, rows-2):
    for column in range(0, columns-2):
        total.extend([matrix[row][column], matrix[row][column+1], matrix[row][column+2],
                      matrix[row+1][column], matrix[row+1][column+1], matrix[row+1][column+2],
                      matrix[row+2][column], matrix[row+2][column+1], matrix[row+2][column+2]])
        compare = sum(total)
        if compare > biggest:
            biggest = compare
            final = total
        total = []

print(f"Sum = {biggest}")
matt = []
while not final == []:
    matt.append(final[:3])
    final = final[3:]

for line in matt:
    print(*line)