rows, cols = [int(s) for s in input().split()]

word = input()
ind = 0

for row in range(rows):
    temp_row = []
    for col in range(cols):
        temp_row.append(word[ind % len(word)])
        ind += 1
    if row % 2 == 0:
        print(*temp_row, sep="")
    else:
        print(*reversed(temp_row), sep="")