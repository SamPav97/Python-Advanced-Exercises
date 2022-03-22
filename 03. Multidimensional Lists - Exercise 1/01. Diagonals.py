size = int(input())

matrix = [[int(x) for x in input().split(", ")]for row in range(size)]

primary_diagonal = []
secondary_diagonal = []

for row in range(size):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][size-row-1])

print(f"Primary diagonal: {', '.join([str(s) for s in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(s) for s in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
