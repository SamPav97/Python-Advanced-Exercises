rows, columns = [int(s) for s in input().split()]

matrix = [[s for s in input().split()]for row in range(rows)]
count = 0
symbols = []
for row in range(0, rows-1):
    for column in range(0, columns-1):
        symbols.extend([matrix[row][column], matrix[row][column+1],
                        matrix[row+1][column], matrix[row+1][column+1]])
        result = all(element == symbols[0] for element in symbols)
        if result:
            count += 1
        symbols = []
        result = False

print(count)