
rows, columns = [int(s) for s in input().split()]

for row in range(rows):
    for col in range(columns):
        print(f"{chr(97+row)}{chr(97+row+col)}{chr(97+row)}", end=" ")
    print()