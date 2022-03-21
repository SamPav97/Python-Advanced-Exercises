from collections import deque

bees = deque([int(s) for s in input().split()])
nectar = [int(s) for s in input().split()]
symbols = deque(input().split())
honey = 0
while bees and nectar:

    bee = bees[0]
    nect = nectar.pop()
    if bee > nect:
        continue
    bees.popleft()
    symbol = symbols.popleft()
    if symbol == "+":
        honey += abs(bee + nect)
    elif symbol == "-":
        honey += abs(bee - nect)
    elif symbol == "*":
        honey += abs(bee * nect)
    elif symbol == "/" and nect != 0:
        honey += abs(bee / nect)


print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(i) for i in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(i) for i in nectar])}")