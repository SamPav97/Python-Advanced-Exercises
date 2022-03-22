n = int(input())

matrix = [[int(s) for s in input().split()]for row in range(n)]

primary_diagonal = []
secondary_diagonal = []

for index in range(n):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][n - index - 1])

sum1 = sum(primary_diagonal)
sum2 = sum(secondary_diagonal)

difference = abs(sum1 - sum2)

print(difference)