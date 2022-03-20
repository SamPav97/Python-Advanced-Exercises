n = int(input())
even = set()
odd = set()
row = 0
for _ in range(n):
    row += 1
    summ = 0
    name = input()
    for letter in name:
        summ += ord(letter)
    summ //= row
    if summ % 2 == 0:
        even.add(summ)
    else:
        odd.add(summ)

if sum(even) == sum(odd):
    print(", ". join([str(s) for s in odd.union(even)]))
elif sum(even) < sum(odd):
    print(", ".join([str(s) for s in odd.difference(even)]))
else:
    print(", ".join([str(s) for s in odd.symmetric_difference(even)]))