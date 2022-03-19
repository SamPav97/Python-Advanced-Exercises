import math
from collections import deque

cups = deque([int(s) for s in input().split()])
bottles = deque([int(s) for s in input().split()])
wasted_water = 0
while cups:
    if not bottles:
        break
    cup = cups.popleft()
    bottle = bottles.pop()
    if 0 < cup < bottle:
        wasted_water += bottle - cup
    if cup > bottle and bottles:
        while cup > 0:
            if cup > bottle and bottles:
                cup -= bottle
                bottle = bottles.pop()
            else:
                cup -= bottle
                wasted_water += abs(cup)

if bottles:
    print(f"Bottles: {' '.join([str(s) for s in bottles])}")
    print(f"Wasted litters of water: {wasted_water}")
else:
    print(f"Cups: {' '.join([str(s) for s in cups])}")
    print(f"Wasted litters of water: {wasted_water}")
