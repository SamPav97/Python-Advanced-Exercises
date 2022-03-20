n = int(input())
compounds = set()

for _ in range(n):
    given = input().split()
    for s in given:
        compounds.add(s)

for comp in compounds:
    print(comp)